import java.io
import jpype.protocol
import typing



class FileUtils:
    @staticmethod
    def $init$($this: 'FileUtils') -> None: ...
    def createTempDir(self) -> java.io.File: ...
    def createTempFile(self) -> java.io.File: ...
    def deleteRecursive(self, root: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None: ...
    def org$ergoplatform$wallet$utils$FileUtils$_setter_$randomPrefixLength_$eq(self, x$1: int) -> None: ...
    def randomPrefixLength(self) -> int: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.ergoplatform.wallet.utils")``.

    FileUtils: typing.Type[FileUtils]
