import java.lang
import typing



class Platform:
    @staticmethod
    def EOL() -> java.lang.String: ...
    @staticmethod
    def arrayclear(arr: typing.List[int]) -> None: ...
    @staticmethod
    def arraycopy(src: typing.Any, srcPos: int, dest: typing.Any, destPos: int, length: int) -> None: ...
    @staticmethod
    def collectGarbage() -> None: ...
    @staticmethod
    def createArray(elemClass: typing.Type[typing.Any], length: int) -> typing.Any: ...
    @staticmethod
    def currentTime() -> int: ...
    @staticmethod
    def defaultCharsetName() -> java.lang.String: ...
    @staticmethod
    def getClassForName(name: typing.Union[java.lang.String, str]) -> typing.Type[typing.Any]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scala.compat")``.

    Platform: typing.Type[Platform]
