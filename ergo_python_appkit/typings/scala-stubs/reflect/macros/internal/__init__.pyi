import scala.annotation
import typing



class macroImpl(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self, referenceToMacroImpl: typing.Any): ...
    def referenceToMacroImpl(self) -> typing.Any: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scala.reflect.macros.internal")``.

    macroImpl: typing.Type[macroImpl]
