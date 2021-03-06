import java.lang.annotation
import typing



class EverythingIsNonNull(java.lang.annotation.Annotation):
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("retrofit2.internal")``.

    EverythingIsNonNull: typing.Type[EverythingIsNonNull]
