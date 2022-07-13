import scala.collection
import typing



class Booleans:
    @staticmethod
    def fromByteArray(b: typing.List[int]) -> bool: ...
    @staticmethod
    def toByteArray(v: bool) -> typing.List[int]: ...

class ByteArray:
    @staticmethod
    def compare(buffer1: typing.List[int], buffer2: typing.List[int]) -> int: ...
    @staticmethod
    def concat(seq: scala.collection.Traversable[typing.List[int]]) -> typing.List[int]: ...

class Random:
    @staticmethod
    def randomBytes(howMany: int) -> typing.List[int]: ...
    @staticmethod
    def randomBytes$default$1() -> int: ...

class package: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scorex.utils")``.

    Booleans: typing.Type[Booleans]
    ByteArray: typing.Type[ByteArray]
    Random: typing.Type[Random]
    package: typing.Type[package]
