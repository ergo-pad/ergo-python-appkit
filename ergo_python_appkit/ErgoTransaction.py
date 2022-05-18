from typing import Dict, List

from ergo_python_appkit.appkit import ErgoAppKit

from org.ergoplatform.appkit import Address, InputBox, OutBox, PreHeader, UnsignedTransaction
from org.ergoplatform import ErgoAddress

class ErgoTransaction:
    def __init__(self, appKit: ErgoAppKit) -> None:
        self.appKit = appKit
        self.preHeader = self.appKit.preHeader()
        self.tokensToBurn = None
        self.dataInputs = None

    @property
    def unsignedTx(self) -> UnsignedTransaction:
        return self.appKit.buildUnsignedTransaction(self.inputs,self.outputs,self.fee,self.changeAddress,self.tokensToBurn,self.dataInputs,self.preHeader)

    @property
    def eip12(self) -> str:
        return ErgoAppKit.unsignedTxToJson(self.unsignedTx)

    @property
    def ergoPaySigningRequest(self) -> str:
        return ErgoAppKit.formErgoPaySigningRequest(self.appKit.reducedTx(self.unsignedTx),self._changeAddress_str)

    @property
    def inputs(self) -> List[InputBox]:
        return self._inputs
    @inputs.setter
    def inputs(self, inputs: List[InputBox]) -> None:
        self._inputs = inputs

    @property
    def dataInputs(self) -> List[InputBox]:
        return self._dataInputs
    @dataInputs.setter
    def dataInputs(self, dataInputs: List[InputBox]) -> None:
        self._dataInputs = dataInputs

    @property
    def outputs(self) -> List[OutBox]:
        return self._outputs
    @outputs.setter
    def outputs(self, outputs: List[OutBox]) -> None:
        self._outputs = outputs

    @property
    def fee(self) -> int:
        return self._fee
    @fee.setter
    def fee(self, fee: int) -> None:
        self._fee = fee

    @property
    def tokensToBurn(self) -> Dict[str, int]:
        return self._tokensToBurn
    @tokensToBurn.setter
    def tokensToBurn(self, tokensToBurn: Dict[str, int]) -> None:
        self._tokensToBurn = tokensToBurn

    @property
    def preHeader(self) -> PreHeader:
        return self._preHeader
    @preHeader.setter
    def preHeader(self, preHeader: PreHeader) -> None:
        self._preHeader = preHeader

    @property
    def changeAddress(self) -> ErgoAddress:
        return self._changeAddress
    @changeAddress.setter
    def changeAddress(self, changeAddress: str) -> None:
        self._changeAddress = Address.create(changeAddress).getErgoAddress()
        self._changeAddress_str = changeAddress

    @property
    def appKit(self) -> ErgoAppKit:
        return self._appKit
    @appKit.setter
    def appKit(self, appKit: ErgoAppKit) -> None:
        self._appKit = appKit