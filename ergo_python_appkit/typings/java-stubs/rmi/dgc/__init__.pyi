import java.io
import java.rmi
import java.rmi.server
import typing



class DGC(java.rmi.Remote):
    def clean(self, objIDArray: typing.List[java.rmi.server.ObjID], long: int, vMID: 'VMID', boolean: bool) -> None: ...
    def dirty(self, objIDArray: typing.List[java.rmi.server.ObjID], long: int, lease: 'Lease') -> 'Lease': ...

class Lease(java.io.Serializable):
    def __init__(self, vMID: 'VMID', long: int): ...
    def getVMID(self) -> 'VMID': ...
    def getValue(self) -> int: ...

class VMID(java.io.Serializable):
    def __init__(self): ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    @staticmethod
    def isUnique() -> bool: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.rmi.dgc")``.

    DGC: typing.Type[DGC]
    Lease: typing.Type[Lease]
    VMID: typing.Type[VMID]
