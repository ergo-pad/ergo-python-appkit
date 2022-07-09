import java.lang
import scala.annotation
import typing



class beanGetter(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class beanSetter(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class companionClass(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class companionMethod(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class companionObject(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class field(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class getter(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class languageFeature(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self, feature: typing.Union[java.lang.String, str], enableRequired: bool): ...

class package: ...

class param(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class setter(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scala.annotation.meta")``.

    beanGetter: typing.Type[beanGetter]
    beanSetter: typing.Type[beanSetter]
    companionClass: typing.Type[companionClass]
    companionMethod: typing.Type[companionMethod]
    companionObject: typing.Type[companionObject]
    field: typing.Type[field]
    getter: typing.Type[getter]
    languageFeature: typing.Type[languageFeature]
    package: typing.Type[package]
    param: typing.Type[param]
    setter: typing.Type[setter]
