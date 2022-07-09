import java.lang
import scala.util
import typing



class Base16:
    @staticmethod
    def Alphabet() -> java.lang.String: ...
    @staticmethod
    def decode(input: typing.Union[java.lang.String, str]) -> scala.util.Try[typing.List[int]]: ...
    @staticmethod
    def encode(input: typing.List[int]) -> java.lang.String: ...

class Base58:
    @staticmethod
    def Alphabet() -> java.lang.String: ...
    @staticmethod
    def decode(input: typing.Union[java.lang.String, str]) -> scala.util.Try[typing.List[int]]: ...
    @staticmethod
    def encode(input: typing.List[int]) -> java.lang.String: ...

class Base64:
    @staticmethod
    def Alphabet() -> java.lang.String: ...
    @staticmethod
    def decode(input: typing.Union[java.lang.String, str]) -> scala.util.Try[typing.List[int]]: ...
    @staticmethod
    def encode(input: typing.List[int]) -> java.lang.String: ...

class BytesEncoder:
    def Alphabet(self) -> java.lang.String: ...
    def decode(self, input: typing.Union[java.lang.String, str]) -> scala.util.Try[typing.List[int]]: ...
    def encode(self, input: typing.List[int]) -> java.lang.String: ...

class ZigZagEncoder:
    @staticmethod
    def decodeZigZagInt(n: int) -> int: ...
    @staticmethod
    def decodeZigZagLong(n: int) -> int: ...
    @staticmethod
    def encodeZigZagInt(n: int) -> int: ...
    @staticmethod
    def encodeZigZagLong(n: int) -> int: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scorex.util.encode")``.

    Base16: typing.Type[Base16]
    Base58: typing.Type[Base58]
    Base64: typing.Type[Base64]
    BytesEncoder: typing.Type[BytesEncoder]
    ZigZagEncoder: typing.Type[ZigZagEncoder]
