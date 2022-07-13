import json
from os import times
import typing

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


from org.ergoplatform import ErgoAddress, ErgoAddressEncoder
from org.ergoplatform.appkit import Address, BoxOperations, Eip4Token, ErgoClientException, ErgoContract, ErgoToken, ErgoType, ErgoValue, ExplorerAndPoolUnspentBoxesLoader, InputBox, Iso, JavaHelpers, NetworkType, OutBox, PreHeader, ReducedTransaction, RestApiErgoClient, SignedTransaction, UnsignedTransaction, SigmaProp, ErgoAuthUtils
from org.ergoplatform.restapi.client import ApiClient, ErgoTransactionOutput, ErgoTransactionUnsignedInput, TransactionSigningRequest, UnsignedErgoTransaction, UtxoApi, WalletApi
from org.ergoplatform.explorer.client import ExplorerApiClient
from org.ergoplatform.appkit.impl import BlockchainContextBuilderImpl, BlockchainContextImpl, ErgoTreeContract, InputBoxImpl, ScalaBridge, SignedTransactionImpl, UnsignedTransactionImpl
from sigmastate.Values import ErgoTree
from java.lang.reflect import UndeclaredThrowableException
from sigmastate.serialization import ErgoTreeSerializer
from sigmastate.lang.exceptions import InterpreterException
from retrofit2 import Response
from java.util import ArrayList
import scala
from java.lang import NullPointerException
from java.util.function import Function
import base64


#region LOGGING
import logging

import inspect
myself = lambda: inspect.stack()[1][3]
#endregion LOGGING


class ErgoException(Exception):
    pass

class ErgoValueT(Enum):
    Long = 0,
    ByteArray = 1,
    LongArray = 2,
    ByteArrayFromHex = 4

class ErgoAppKit:
    
    def __init__(self, nodeUrl: str, networkType: str, explorerUrl: str, nodeApiKey: str = ""):
        self._nodeUrl = nodeUrl
        self._networkType = ErgoAppKit.NetworkType(networkType)
        self._client: ApiClient = ApiClient(self._nodeUrl, "ApiKeyAuth", nodeApiKey)
        self._explorerUrl = explorerUrl.replace("/api/v1","")
        self._ergoClient = RestApiErgoClient.create(nodeUrl,self._networkType,nodeApiKey,self._explorerUrl)
        if self._explorerUrl!="":
            self._explorer = ExplorerApiClient(self._explorerUrl)
        else:
            self._explorer = None
        self._addrEnc = ErgoAddressEncoder(self._networkType.networkPrefix)

    def compileErgoScript(self, ergoScript: str, constants: Dict[str,typing.Any] = {}) -> ErgoTree:
        return JavaHelpers.compile(constants,ergoScript,self._networkType.networkPrefix)

    def tree2Address(self, ergoTree):
        return self._addrEnc.fromProposition(ergoTree).get().toString()

    @JImplements(Function)
    class BuildOutBoxExecutor(object):

        def __init__(self, value: int, tokens: Dict[str,int], registers, contract):
            self._value = value
            self._tokens = tokens
            self._registers = registers
            self._contract = contract

        @JOverride
        def apply(self, ctx: BlockchainContextImpl) -> OutBox:
            tb = ctx.newTxBuilder()
            ergoTokens = []
            tb = tb.outBoxBuilder().contract(self._contract).value(self._value)
            if self._tokens is not None:
                for token in self._tokens.keys():
                    ergoTokens.append(ErgoToken(token,self._tokens[token]))
                tb = tb.tokens(ergoTokens)

            if self._registers is not None:
                tb = tb.registers(self._registers)

            return tb.build()

    def buildOutBox(self,value: int, tokens: Dict[str,int], registers, contract) -> OutBox:
        return self._ergoClient.execute(ErgoAppKit.BuildOutBoxExecutor(value,tokens,registers,contract))

    @JImplements(Function)
    class GetBoxesByIdExecutor(object):

        def __init__(self, boxIds: List[str], api: UtxoApi):
            self._boxIds = boxIds
            self._api = api

        @JOverride
        def apply(self, ctx: BlockchainContextImpl) -> List[InputBox]:
            boxData: ErgoTransactionOutput = None
            res = []
            for id in self._boxIds:
                response: Response = self._api.getBoxWithPoolById(id).execute()
                if response.isSuccessful():
                    boxData = response.body()
                if boxData is None:
                    raise ErgoClientException("Cannot load UTXO box " + id, None)
                res.append(InputBoxImpl(boxData))
            return ArrayList(res)

    def getBoxesById(self, boxIds: List[str]) -> List[InputBox]:
        api = self._client.createService(UtxoApi)
        return list(self._ergoClient.execute(ErgoAppKit.GetBoxesByIdExecutor(boxIds,api)))
    
    @JImplements(Function)
    class MintTokenExecutor(object):

        def __init__(self, value: int, tokenId: str, tokenName: str, tokenDesc: str, mintAmount: int, decimals: int, contract: ErgoContract):
            self._value = value
            self._tokenId = tokenId
            self._tokenName = tokenName
            self._tokenDesc = tokenDesc
            self._mintAmount = mintAmount
            self._decimals = decimals
            self._contract = contract

        @JOverride
        def apply(self, ctx: BlockchainContextImpl) -> OutBox:
            tb = ctx.newTxBuilder()
            return tb.outBoxBuilder().contract(self._contract).value(self._value).mintToken(Eip4Token(self._tokenId,self._mintAmount,self._tokenName,self._tokenDesc,self._decimals)).build()

    def mintToken(self, value: int, tokenId: str, tokenName: str, tokenDesc: str, mintAmount: int, decimals: int, contract: ErgoContract) -> OutBox:
        return self._ergoClient.execute(ErgoAppKit.MintTokenExecutor(value,tokenId,tokenName,tokenDesc,mintAmount,decimals,contract))

    def buildInputBox(self,value: int, tokens: Dict[str,int], registers, contract, withTxId: str = "ce552663312afc2379a91f803c93e2b10b424f176fbc930055c10def2fd88a5d") -> InputBox:
        return self.buildOutBox(value, tokens, registers, contract).convertToInputWith(withTxId, 0)

    @JImplements(Function)
    class BoxesToSpendFromListExecutor(object):

        def __init__(self,   addresses: list[str], nergToSpend: int, tokensToSpend: Dict[str,int] = {}, includeMempool: bool = True):
            self._addresses = addresses
            self._nergToSpend = nergToSpend
            self._tokensToSpend = tokensToSpend
            self._includeMempool = includeMempool

        @JOverride
        def apply(self, ctx: BlockchainContextImpl) -> List[InputBox]:
            tts = ArrayList(ErgoAppKit.mapToErgoTokenList(self._tokensToSpend))
            nergLeft = self._nergToSpend
            addresses = []
            for addr in self._addresses:
                addresses.append(Address.create(addr))
            result = BoxOperations.createForSenders(ArrayList(addresses),ctx).withTokensToSpend(tts).withAmountToSpend(nergLeft).withInputBoxesLoader(ExplorerAndPoolUnspentBoxesLoader().withAllowChainedTx(self._includeMempool)).loadTop()
            if ErgoAppKit.boxesCovered(result,self._nergToSpend,self._tokensToSpend):
                return ArrayList(result)
            else:
                return None

    def boxesToSpendFromList(self, addresses: list[str], nergToSpend: int, tokensToSpend: Dict[str,int] = {}, includeMempool: bool = True) -> List[InputBox]:
        return list(self._ergoClient.execute(ErgoAppKit.BoxesToSpendFromListExecutor(addresses,nergToSpend,tokensToSpend,includeMempool)))

    def boxesToSpend(self, address: str, nergToSpend: int, tokensToSpend: Dict[str,int] = {}, includeMempool: bool = True) -> List[InputBox]:
        return list(self._ergoClient.execute(ErgoAppKit.BoxesToSpendFromListExecutor([address],nergToSpend,tokensToSpend,includeMempool)))

    def ergoValue(value, t: ErgoValueT):
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

    @JImplements(Function)
    class PreHeaderExecutor(object):

        def __init__(self,  timestamp: int = None):
            self._timestamp = timestamp

        @JOverride
        def apply(self, ctx: BlockchainContextImpl) -> PreHeader:
            phb = ctx.createPreHeader()
            if self._timestamp is not None:
                phb = phb.timestamp(JLong(self._timestamp))
            return phb.build()

    def preHeader(self, timestamp: int = None) -> PreHeader:
        return self._ergoClient.execute(ErgoAppKit.PreHeaderExecutor(timestamp))

    @JImplements(Function)
    class BuildUnsignedTransactionExecutor(object):

        def __init__(self,  inputs: List[InputBox], outputs: List[OutBox], fee: int, sendChangeTo: ErgoAddress, tokensToBurn: Dict[str,int] = None, dataInputs: List[InputBox] = None, preHeader: PreHeader = None):
            self._inputs = inputs
            self._outputs = outputs
            self._fee = fee
            self._sendChangeTo = sendChangeTo
            self._tokensToBurn = tokensToBurn
            self._dataInputs = dataInputs
            self._preHeader = preHeader

        @JOverride
        def apply(self, ctx: BlockchainContextImpl) -> UnsignedTransaction:
            tb = ctx.newTxBuilder()
            if self._preHeader is not None:
                tb = tb.preHeader(self._preHeader)
            if self._dataInputs is not None:
                tb = tb.withDataInputs(ArrayList(self._dataInputs))
            if self._tokensToBurn is not None:
                tb = tb.tokensToBurn(ErgoAppKit.mapToErgoTokenList(self._tokensToBurn))
            tb = tb.boxesToSpend(ArrayList(self._inputs)).fee(self._fee).outputs(self._outputs).sendChangeTo(self._sendChangeTo)
            return tb.build()

    def buildUnsignedTransaction(self, inputs: List[InputBox], outputs: List[OutBox], fee: int, sendChangeTo: ErgoAddress, tokensToBurn: Dict[str,int] = None, dataInputs: List[InputBox] = None, preHeader: PreHeader = None) -> UnsignedTransaction:
        return self._ergoClient.execute(ErgoAppKit.BuildUnsignedTransactionExecutor(inputs,outputs,fee,sendChangeTo,tokensToBurn,dataInputs,preHeader))

    @JImplements(Function)
    class SignTransactionExecutor(object):

        def __init__(self, unsignedTx: UnsignedTransaction):
            self._unsignedTx = unsignedTx

        @JOverride
        def apply(self, ctx: BlockchainContextImpl) -> SignedTransaction:
            prover = ctx.newProverBuilder().build()
            return prover.sign(self._unsignedTx)

    def signTransaction(self, unsignedTx: UnsignedTransaction) -> SignedTransaction:
        try:
            return self._ergoClient.execute(ErgoAppKit.SignTransactionExecutor(unsignedTx))
        except UndeclaredThrowableException as e:
            raise e.getCause()

    @JImplements(Function)
    class SendTransactionExecutor(object):

        def __init__(self, signedTx: SignedTransaction):
            self._signedTx = signedTx

        @JOverride
        def apply(self, ctx: BlockchainContextImpl) -> str:
            return ctx.sendTransaction(self._signedTx)

    def sendTransaction(self, signedTx: SignedTransaction) -> str:
        return self._ergoClient.execute(ErgoAppKit.SendTransactionExecutor(signedTx))

    @JImplements(Function)
    class SignTransactionWithNodeExecutor(object):

        def __init__(self, unsignedTx: UnsignedTransactionImpl, api: WalletApi):
            self._unsignedTx = unsignedTx
            self._api = api

        @JOverride
        def apply(self, ctx: BlockchainContextImpl) -> SignedTransaction:
            signRequest = TransactionSigningRequest()
            unsignedErgoTx = UnsignedErgoTransaction()
            unsignedErgoLikeTx = self._unsignedTx.getTx()
            for i in range(int(unsignedErgoLikeTx.inputs().length())):
                input = unsignedErgoLikeTx.inputs().apply(JInt(i))
                unsignedInput = ErgoTransactionUnsignedInput()
                unsignedInput.setBoxId(self._unsignedTx.getInputs()[i].getId().toString())
                unsignedInput.setExtension(scala.collection.JavaConversions.mapAsJavaMap(input.extension().values()))
                unsignedErgoTx = unsignedErgoTx.addInputsItem(unsignedInput)
            if unsignedErgoLikeTx.dataInputs().length() > 0:
                unsignedErgoTx.setDataInputs(Iso.inverseIso(Iso.JListToIndexedSeq(ScalaBridge.isoErgoTransactionDataInput())).to(unsignedErgoLikeTx.dataInputs()))
            unsignedErgoTx.setOutputs(Iso.inverseIso(Iso.JListToIndexedSeq(ScalaBridge.isoErgoTransactionOutput())).to(unsignedErgoLikeTx.outputs()))
            signRequest.setTx(unsignedErgoTx)
            response = self._api.walletTransactionSign(signRequest).execute()
            if response.isSuccessful():
                ergoTx = response.body()
                tx = ScalaBridge.isoErgoTransaction().to(ergoTx)
                signedTx = SignedTransactionImpl(ctx,tx,0)
                return signedTx
            else:
                error = json.loads(response.errorBody().string())
                raise ErgoException(f'{error["reason"]}: {error["detail"]}')

    def signTransactionWithNode(self, unsignedTx: UnsignedTransactionImpl) -> SignedTransaction:
        api = self._client.createService(WalletApi)
        return self._ergoClient.execute(ErgoAppKit.SignTransactionWithNodeExecutor(unsignedTx,api))

    @JImplements(Function)
    class GetUnspentBoxesExecutor(object):

        def __init__(self, address: str):
            self._address = address

        @JOverride
        def apply(self, ctx: BlockchainContextImpl) -> List[InputBox]:
            addr = Address.create(self._address)
            offset = 0
            limit = 100
            result = []
            pageResult = ctx.getUnspentBoxesFor(addr,offset,limit)
            while len(pageResult) > 0:
                result = result + list(pageResult)
                offset += limit
                pageResult = ctx.getUnspentBoxesFor(addr,offset,limit)
            return ArrayList(result)

    def getUnspentBoxes(self, address: str) -> List[InputBox]:
        return list(self._ergoClient.execute(ErgoAppKit.GetUnspentBoxesExecutor(address)))

    @JImplements(Function)
    class ReducedTxExecutor(object):

        def __init__(self, unsignedTx: UnsignedTransactionImpl):
            self._unsignedTx = unsignedTx

        @JOverride
        def apply(self, ctx: BlockchainContextImpl) -> ReducedTransaction:
            return ctx.newProverBuilder().build().reduce(self._unsignedTx,0)

    def reducedTx(self, unsignedTx: UnsignedTransactionImpl) -> ReducedTransaction:
        return self._ergoClient.execute(ErgoAppKit.ReducedTxExecutor(unsignedTx))

    #static functions
    def NetworkType(networkType: str):
        if networkType.lower()=="testnet":
            return NetworkType.TESTNET
        else:
            return NetworkType.MAINNET

    def formErgoPaySigningRequest(
            reducedTx: ReducedTransaction, 
            address: str = None, 
            message: str = None,
            messageSeverity: str = None,
            replyTo: str = None
        ) -> str:

        result = {}
        result['reducedTx'] = base64.urlsafe_b64encode(reducedTx.toBytes()).decode()
        if address is not None: result['address'] = address
        if message is not None: result['message'] = message
        if messageSeverity is not None: result['messageSeverity'] = messageSeverity
        if replyTo is not None: result['replyTo'] = replyTo
        return result

    def unsignedTxToJson(unsignedTx: UnsignedTransactionImpl) -> str:
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

    def cutOffExcessUTXOs(utxos: List[InputBox], nErgRequired: int, tokensToSpend: Dict[str,int]) -> List[InputBox]:
        result = []
        for utxo in utxos:
            result.append(utxo)
            if ErgoAppKit.boxesCovered(result,nErgRequired,tokensToSpend):
                return result
        return result

    def boxesCovered(inputs: List[InputBox], nErgRequired: int, tokensToSpend: Dict[str,int]) -> bool:
        balance = ErgoAppKit.getBalance(inputs)
        changeRequired = False
        if balance["erg"] < nErgRequired:
            return False
        if balance["erg"] - nErgRequired > 0 and balance["erg"] - nErgRequired < int(1e6):
            return False
        for token in list(tokensToSpend.keys()):
            if balance.get(token,0) < tokensToSpend[token]:
                return False
            if balance.get(token,0) > tokensToSpend[token]:
                changeRequired = True
        if len(tokensToSpend.keys()) < len(balance.keys()) - 1:
            changeRequired = True
        if changeRequired:
            return balance["erg"] > nErgRequired + int(1e6)
        return True

    def deserializeLongArray(hex: str) -> List[int]:
        ergoValue = ErgoValue.fromHex(hex)
        res = []
        for val in ergoValue.getValue().toArray():
            res.append(val)
        return res

    def getBalance(boxes: List[InputBox]) -> Dict[str,int]:
        res = {"erg":0}
        for box in boxes:
            res["erg"] += box.getValue()
            for token in box.getTokens():
                if token.getId().toString() not in res.keys():
                    res[token.getId().toString()] = token.getValue()
                else:
                    res[token.getId().toString()] += token.getValue()      
        return res

    def mapToErgoTokenList(map: Dict[str,int]) -> List[ErgoToken]:
        tts = []
        for entry in map:
            tts.append(ErgoToken(entry,map[entry]))
        return tts

    def getSigmaBooleanFromAddress(address: str) -> str:
        # we need a SigmaProp for ErgoAuth. Every address is a sigmaprop, so convert
        addressSigmaProp = SigmaProp.createFromAddress(Address.create(address))
        sigmaBoolean = base64.b64encode(addressSigmaProp.toBytes()).decode()
        return sigmaBoolean

    def verifyErgoAuthSignedMessage(address: str, message: str, signedMessage: str, proof: str) -> bool:
        addressSigmaProp = SigmaProp.createFromAddress(Address.create(address))
        proofBytes = base64.b64decode(proof)
        return ErgoAuthUtils.verifyResponse(addressSigmaProp, message, signedMessage, proofBytes)
