import scala.collection
import typing



class ArithUtils:
    @typing.overload
    @staticmethod
    def addExact(a: int, b: int) -> int: ...
    @typing.overload
    @staticmethod
    def addExact(a: int, b: int, c: scala.collection.Seq[typing.Any]) -> int: ...
    @staticmethod
    def multiplyExact(e1: int, e2: int) -> int: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.ergoplatform.utils")``.

    ArithUtils: typing.Type[ArithUtils]
