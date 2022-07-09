import java.lang
import scala.annotation.meta
import scala.annotation.unchecked
import scala.collection.immutable
import typing



class Annotation:
    def __init__(self): ...

class StaticAnnotation: ...

class TypeConstraint: ...

class ClassfileAnnotation(StaticAnnotation): ...

class bridge(Annotation, StaticAnnotation):
    def __init__(self): ...

class compileTimeOnly(Annotation, StaticAnnotation):
    def __init__(self, message: typing.Union[java.lang.String, str]): ...

class elidable(Annotation, StaticAnnotation):
    def __init__(self, level: int): ...
    @staticmethod
    def ALL() -> int: ...
    @staticmethod
    def ASSERTION() -> int: ...
    @staticmethod
    def CONFIG() -> int: ...
    @staticmethod
    def FINE() -> int: ...
    @staticmethod
    def FINER() -> int: ...
    @staticmethod
    def FINEST() -> int: ...
    @staticmethod
    def INFO() -> int: ...
    @staticmethod
    def MAXIMUM() -> int: ...
    @staticmethod
    def MINIMUM() -> int: ...
    @staticmethod
    def OFF() -> int: ...
    @staticmethod
    def SEVERE() -> int: ...
    @staticmethod
    def WARNING() -> int: ...
    @staticmethod
    def byName() -> scala.collection.immutable.Map[java.lang.String, typing.Any]: ...
    def level(self) -> int: ...

class implicitAmbiguous(Annotation, StaticAnnotation):
    def __init__(self, msg: typing.Union[java.lang.String, str]): ...

class implicitNotFound(Annotation, StaticAnnotation):
    def __init__(self, msg: typing.Union[java.lang.String, str]): ...

class migration(Annotation, StaticAnnotation):
    def __init__(self, message: typing.Union[java.lang.String, str], changedIn: typing.Union[java.lang.String, str]): ...

class showAsInfix(Annotation, StaticAnnotation):
    def __init__(self, enabled: bool): ...
    @staticmethod
    def $lessinit$greater$default$1() -> bool: ...

class strictfp(Annotation, StaticAnnotation):
    def __init__(self): ...

class switch(Annotation, StaticAnnotation):
    def __init__(self): ...

class tailrec(Annotation, StaticAnnotation):
    def __init__(self): ...

class unspecialized(Annotation, StaticAnnotation):
    def __init__(self): ...

class varargs(Annotation, StaticAnnotation):
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scala.annotation")``.

    Annotation: typing.Type[Annotation]
    ClassfileAnnotation: typing.Type[ClassfileAnnotation]
    StaticAnnotation: typing.Type[StaticAnnotation]
    TypeConstraint: typing.Type[TypeConstraint]
    bridge: typing.Type[bridge]
    compileTimeOnly: typing.Type[compileTimeOnly]
    elidable: typing.Type[elidable]
    implicitAmbiguous: typing.Type[implicitAmbiguous]
    implicitNotFound: typing.Type[implicitNotFound]
    migration: typing.Type[migration]
    showAsInfix: typing.Type[showAsInfix]
    strictfp: typing.Type[strictfp]
    switch: typing.Type[switch]
    tailrec: typing.Type[tailrec]
    unspecialized: typing.Type[unspecialized]
    varargs: typing.Type[varargs]
    meta: scala.annotation.meta.__module_protocol__
    unchecked: scala.annotation.unchecked.__module_protocol__
