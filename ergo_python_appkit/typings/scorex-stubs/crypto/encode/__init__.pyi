import scorex.util.encode
import typing



class package:
    @staticmethod
    def Base16() -> scorex.util.encode.Base16.: ...
    @staticmethod
    def Base58() -> scorex.util.encode.Base58.: ...
    @staticmethod
    def Base64() -> scorex.util.encode.Base64.: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scorex.crypto.encode")``.

    package: typing.Type[package]
