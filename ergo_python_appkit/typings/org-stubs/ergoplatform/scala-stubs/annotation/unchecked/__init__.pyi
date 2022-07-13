import scala.annotation
import typing



class uncheckedStable(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class uncheckedVariance(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scala.annotation.unchecked")``.

    uncheckedStable: typing.Type[uncheckedStable]
    uncheckedVariance: typing.Type[uncheckedVariance]
