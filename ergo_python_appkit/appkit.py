import json
import typing

from config import Config, Network
import jpype
import jpype.imports
from jpype.types import *
from jpype import JImplements, JOverride
from enum import Enum
from typing import Dict, List, TypeVar

try:
    jpype.addClassPath('../jars/*')
    jpype.addClassPath('./jars/*')
    jpype.startJVM(None, convertStrings=True)
except OSError:
    print("JVM already running")


from org.ergoplatform import DataInput, ErgoAddress, ErgoAddressEncoder
from org.ergoplatform.appkit import Address, BlockchainContext, BoxOperations, ConstantsBuilder, Eip4Token, ErgoClient, ErgoClientException, ErgoContract, ErgoToken, ErgoType, ErgoValue, InputBox, Iso, JavaHelpers, NetworkType, OutBox, PreHeader, ReducedTransaction, RestApiErgoClient, SignedTransaction, UnsignedTransaction
from org.ergoplatform.restapi.client import ApiClient, Asset, ErgoTransactionDataInput, ErgoTransactionOutput, ErgoTransactionUnsignedInput, Registers, TransactionSigningRequest, UnsignedErgoTransaction, WalletApi
from org.ergoplatform.explorer.client import ExplorerApiClient
from org.ergoplatform.settings import ErgoAlgos
from org.ergoplatform.appkit.impl import BlockchainContextBuilderImpl, BlockchainContextImpl, Eip4TokenBuilder, ErgoNodeFacade, ErgoTreeContract, ExplorerFacade, InputBoxImpl, ScalaBridge, SignedTransactionImpl, UnsignedTransactionImpl
from special.collection import Coll
from sigmastate.Values import ErgoTree
from sigmastate.serialization import ErgoTreeSerializer
from scala import Byte as SByte, Long as SLong
import java
import scala
from java.math import BigInteger
from java.lang import NullPointerException
import base64

DEBUG = True # CFG.DEBUG

#region LOGGING
import logging
levelname = (logging.WARN, logging.DEBUG)[DEBUG]
logging.basicConfig(format='{asctime}:{name:>8s}:{levelname:<8s}::{message}', style='{', levelname=levelname)

import inspect
myself = lambda: inspect.stack()[1][3]
#endregion LOGGING

CFG = Config[Network]

class ErgoException(Exception):
    pass

class ErgoValueT(Enum):
    Long = 0,
    ByteArray = 1,
    LongArray = 2,
    ByteArrayFromHex = 4

class ErgoAppKit:
    
    def __init__(self,nodeUrl: str, networkType: str, explorerUrl: str):
        self._nodeUrl = nodeUrl
        self._networkType = ErgoAppKit.NetworkType(networkType)
        self._client = ApiClient(self._nodeUrl, "ApiKeyAuth", CFG.ergopadApiKey)
        self._explorerUrl = explorerUrl.replace("/api/v1","")
        if self._explorerUrl!="":
            self._explorer = ExplorerApiClient(self._explorerUrl)
        else:
            self._explorer = None
        self._addrEnc = ErgoAddressEncoder(self._networkType.networkPrefix)

    def compileErgoScript(self, ergoScript: str, constants: Dict[str,typing.Any] = {}) -> ErgoTree:
        return JavaHelpers.compile(constants,ergoScript,self._networkType.networkPrefix)

    def getBlockChainContext(self) -> BlockchainContextImpl:
        return BlockchainContextBuilderImpl(self._client, self._explorer, self._networkType).build()

    def tree2Address(self, ergoTree):
        return self._addrEnc.fromProposition(ergoTree).get().toString()

    def NetworkType(networkType: str):
        if networkType.lower()=="testnet":
            return NetworkType.TESTNET
        else:
            return NetworkType.MAINNET

    def buildOutBox(self,value: int, tokens: Dict[str,int], registers, contract) -> OutBox:
        ctx = self.getBlockChainContext()
        tb = ctx.newTxBuilder()
        ergoTokens = []
        tb = tb.outBoxBuilder().contract(contract).value(value)
        if tokens is not None:
            for token in tokens.keys():
                ergoTokens.append(ErgoToken(token,tokens[token]))
            tb = tb.tokens(ergoTokens)

        if registers is not None:
            tb = tb.registers(registers)

        return tb.build()

    def getBoxesById(self, boxIds: List[str]) -> List[InputBox]:
        ctx = self.getBlockChainContext()
        _ok = self._client.getOkBuilder().build()
        _retrofit = self._client.getAdapterBuilder().client(_ok).build()
        res = []
        for id in boxIds:
            boxData = ErgoNodeFacade.getBoxWithPoolById(_retrofit, id)
            if boxData is None:
                raise ErgoClientException("Cannot load UTXO box " + id, None)
            res.append(InputBoxImpl(ctx, boxData))
        return res
    
    def mintToken(self, value: int, tokenId: str, tokenName: str, tokenDesc: str, mintAmount: int, decimals: int, contract: ErgoContract) -> OutBox:
        ctx = self.getBlockChainContext()
        tb = ctx.newTxBuilder()
        return tb.outBoxBuilder().contract(contract).value(value).mintToken(Eip4Token(tokenId,mintAmount,tokenName,tokenDesc,decimals)).build()

    def buildInputBox(self,value: int, tokens: Dict[str,int], registers, contract) -> InputBox:
        return self.buildOutBox(value, tokens, registers, contract).convertToInputWith("ce552663312afc2379a91f803c93e2b10b424f176fbc930055c10def2fd88a5d", 0)

    def mapToErgoTokenList(self, map: Dict[str,int]) -> List[ErgoToken]:
        tts = []
        for entry in map:
            tts.append(ErgoToken(entry,map[entry]))
        return tts

    def boxesToSpend(self, address: str, nergToSpend: int, tokensToSpend: Dict[str,int] = {}) -> List[InputBox]:
        ctx = self.getBlockChainContext()
        tts = self.mapToErgoTokenList(tokensToSpend)
        try:
            coveringBoxes = ctx.getCoveringBoxesFor(Address.create(address),nergToSpend,java.util.ArrayList(tts))
        except NullPointerException as e:
            err = ""
            for stackTraceElement in e.getStackTrace():
                err = '\n'.join([err,stackTraceElement.toString()])
            err = '\n'.join([err,str(e.getMessage())])
            logging.info(err)
        if coveringBoxes.isCovered():
            return coveringBoxes.getBoxes()
        else:
            return None

    def ergoValue(self, value, t: ErgoValueT):
        if t == ErgoValueT.Long:
            res = ErgoValue.of(JLong(value))
            return res
        if t == ErgoValueT.ByteArrayFromHex:
            return ErgoValue.of(bytes.fromhex(value))
        if t == ErgoValueT.LongArray:
            collVal = []
            for l in value:
                collVal.append(JLong(l))
            res = ErgoValue.of(collVal,ErgoType.longType())
            return res
        if t == ErgoValueT.ByteArray:
            res = ErgoValue.of(value)
            return res

    def dummyContract(self) -> ErgoContract:
        return ErgoTreeContract(Address.create("4MQyML64GnzMxZgm").getErgoAddress().script(),self._networkType)

    def contractFromTree(self,tree: ErgoTree) -> ErgoContract:
        return ErgoTreeContract(tree,self._networkType)

    def contractFromAddress(self,addr: str) -> ErgoContract:
        return ErgoTreeContract(Address.create(addr).getErgoAddress().script(),self._networkType)

    def treeFromBytes(self,bytes: bytes) -> ErgoTree:
        treeSerializer = ErgoTreeSerializer()
        return self._addrEnc.fromProposition(treeSerializer.deserializeErgoTree(bytes)).get().script()

    def preHeader(self, timestamp: int = None) -> PreHeader:
        ctx = self.getBlockChainContext()
        phb = ctx.createPreHeader()
        if timestamp is not None:
            phb = phb.timestamp(JLong(timestamp))
        return phb.build()

    def buildUnsignedTransaction(self, inputs: List[InputBox], outputs: List[OutBox], fee: int, sendChangeTo: ErgoAddress, tokensToBurn: Dict[str,int] = None, dataInputs: List[InputBox] = None, preHeader: PreHeader = None) -> UnsignedTransaction:
        ctx = self.getBlockChainContext()
        tb = ctx.newTxBuilder()
        if preHeader is not None:
            tb = tb.preHeader(preHeader)
        if dataInputs is not None:
            tb = tb.withDataInputs(java.util.ArrayList(dataInputs))
        if tokensToBurn is not None:
            tb = tb.tokensToBurn(self.mapToErgoTokenList(tokensToBurn))
        tb = tb.boxesToSpend(java.util.ArrayList(inputs)).fee(fee).outputs(outputs).sendChangeTo(sendChangeTo)
        return tb.build()

    def signTransaction(self, unsignedTx: UnsignedTransaction) -> SignedTransaction:
        ctx = self.getBlockChainContext()
        prover = ctx.newProverBuilder().build()
        return prover.sign(unsignedTx)

    def sendTransaction(self, signedTx: SignedTransaction) -> str:
        ctx = self.getBlockChainContext()
        return ctx.sendTransaction(signedTx)

    def signTransactionWithNode(self, unsignedTx: UnsignedTransactionImpl) -> SignedTransaction:
        signRequest = TransactionSigningRequest()
        unsignedErgoTx = UnsignedErgoTransaction()
        unsignedErgoLikeTx = unsignedTx.getTx()
        for i in range(int(unsignedErgoLikeTx.inputs().length())):
            input = unsignedErgoLikeTx.inputs().apply(JInt(i))
            unsignedInput = ErgoTransactionUnsignedInput()
            unsignedInput.setBoxId(unsignedTx.getInputs()[i].getId().toString())
            unsignedInput.setExtension(scala.collection.JavaConversions.mapAsJavaMap(input.extension().values()))
            unsignedErgoTx = unsignedErgoTx.addInputsItem(unsignedInput)
        if unsignedErgoLikeTx.dataInputs().length() > 0:
            unsignedErgoTx.setDataInputs(Iso.inverseIso(Iso.JListToIndexedSeq(ScalaBridge.isoErgoTransactionDataInput())).to(unsignedErgoLikeTx.dataInputs()))
        unsignedErgoTx.setOutputs(Iso.inverseIso(Iso.JListToIndexedSeq(ScalaBridge.isoErgoTransactionOutput())).to(unsignedErgoLikeTx.outputs()))
        signRequest.setTx(unsignedErgoTx)
        api = self._client.createService(WalletApi)
        response = api.walletTransactionSign(signRequest).execute()
        if response.isSuccessful():
            ergoTx = response.body()
            tx = ScalaBridge.isoErgoTransaction().to(ergoTx)
            signedTx = SignedTransactionImpl(self.getBlockChainContext(),tx,0)
            return signedTx
        else:
            error = json.loads(response.errorBody().string())
            raise ErgoException(f'{error["reason"]}: {error["detail"]}')

    def getUnspentBoxes(self, address: str) -> List[InputBox]:
        ctx = self.getBlockChainContext()
        addr = Address.create(address)
        offset = 0
        limit = 100
        result = []
        pageResult = ctx.getUnspentBoxesFor(addr,offset,limit)
        while len(pageResult) > 0:
            result = result + list(pageResult)
            offset += limit
            pageResult = ctx.getUnspentBoxesFor(addr,offset,limit)
        return result

    def deserializeLongArray(self,hex: str) -> List[int]:
        ergoValue = ErgoValue.fromHex(hex)
        res = []
        for val in ergoValue.getValue().toArray():
            res.append(val)
        return res

    def getBalance(self, boxes: List[InputBox]) -> Dict[str,int]:
        res = {"erg":0}
        for box in boxes:
            res["erg"] += box.getValue()
            for token in box.getTokens():
                if token.getId().toString() not in res.keys():
                    res[token.getId().toString()] = token.getValue()
                else:
                    res[token.getId().toString()] += token.getValue()      
        return res

    def boxesCovered(self, inputs: List[InputBox], nErgRequired: int, tokensToSpend: Dict[str,int]) -> bool:
        balance = self.getBalance(inputs)
        if balance["erg"] < nErgRequired:
            return False
        for token in list(tokensToSpend.keys()):
            if balance.get(token,0) < tokensToSpend[token]:
                return False
        return True

    def cutOffExcessUTXOs(self, utxos: List[InputBox], nErgRequired: int, tokensToSpend: Dict[str,int]) -> List[InputBox]:
        result = []
        for utxo in utxos:
            result.append(utxo)
            if self.boxesCovered(result,nErgRequired,tokensToSpend):
                return result
        return result

    def unsignedTxToJson(self, unsignedTx: UnsignedTransactionImpl) -> str:
        inputs = []
        for i in unsignedTx.getInputs():
            j = json.loads(i.toJson(False))
            j["extension"] = {}
            j["value"] = str(j["value"])
            for ass in j["assets"]:
                ass["amount"] = str(ass["amount"])
            inputs.append(j)
        dataInputs = []
        for di in unsignedTx.getDataInputs():
            j = json.loads(di.toJson(False))
            j["extension"] = {}
            j["value"] = str(j["value"])
            for ass in j["assets"]:
                ass["amount"] = str(ass["amount"])
            dataInputs.append(j)
        outputs = []
        for o in unsignedTx.getOutputs():
            assets = []
            for t in o.getTokens():
                assets.append({'tokenId': str(t.getId().toString()), 'amount': str(t.getValue())})  
            additionalRegisters = {}
            r = 4
            for additionalRegister in o.getRegisters():
                additionalRegisters[f'R{r}']=additionalRegister.toHex()
                r+=1
            outputs.append({
                'value': str(o.getValue()),
                'ergoTree': o.getErgoTree().bytesHex(),
                'assets': assets,
                'additionalRegisters': additionalRegisters,
                'creationHeight': o.getCreationHeight()
            })

        return {
            'inputs': inputs,
            'dataInputs': dataInputs,
            'outputs': outputs
        }

    def reducedTx(self, unsignedTx: UnsignedTransactionImpl) -> ReducedTransaction:
        ctx = self.getBlockChainContext()
        return ctx.newProverBuilder().build().reduce(unsignedTx,0)

    def formErgoPaySigningRequest(
        self,
        reducedTx: ReducedTransaction, 
        address: str = None, 
        message: str = None,
        messageSeverity: str = None,
        replyTo: str = None) -> str:
        result = {}
        result['reducedTx'] = base64.urlsafe_b64encode(reducedTx.toBytes()).decode()
        if address is not None: result['address'] = address
        if message is not None: result['message'] = message
        if messageSeverity is not None: result['messageSeverity'] = messageSeverity
        if replyTo is not None: result['replyTo'] = replyTo
        return result


        

    


