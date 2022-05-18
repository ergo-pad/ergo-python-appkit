from typing import Dict, List
from ergo_python_appkit.appkit import ErgoAppKit
from org.ergoplatform.appkit import ErgoContract, ErgoValue, InputBox
from sigmastate.Values import ErgoTree

class ErgoContractBase:
    def __init__(self, appKit: ErgoAppKit, script: str = None, mapping: Dict[str,ErgoValue] = {}, ergoTree: ErgoTree = None) -> None:
        self.appKit = appKit
        if script is not None:
            with open(script) as f:
                self._ergoScript = f.read()
            self._ergoTree = self._appKit.compileErgoScript(self._ergoScript, mapping)
        if ergoTree is not None:
            self._ergoTree = ergoTree
        self.contract = self._appKit.contractFromTree(self._ergoTree)

    def validateInputBox(self, inBox: InputBox) -> bool:
        return inBox.getErgoTree() == self._ergoTree

    @property
    def contract(self) -> ErgoContract:
        return self._contract
    @contract.setter
    def contract(self, contract: ErgoContract) -> None:
        self._contract = contract

    @property
    def appKit(self) -> ErgoAppKit:
        return self._appKit
    @appKit.setter
    def appKit(self, appKit: ErgoAppKit) -> None:
        self._appKit = appKit

