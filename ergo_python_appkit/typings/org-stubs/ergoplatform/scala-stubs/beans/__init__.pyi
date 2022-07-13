import java.beans
import java.lang
import scala.annotation
import typing



class BeanDescription(scala.annotation.Annotation):
    def __init__(self, description: typing.Union[java.lang.String, str]): ...
    def description(self) -> java.lang.String: ...

class BeanDisplayName(scala.annotation.Annotation):
    def __init__(self, name: typing.Union[java.lang.String, str]): ...
    def name(self) -> java.lang.String: ...

class BeanInfo(scala.annotation.Annotation):
    def __init__(self): ...

class BeanInfoSkip(scala.annotation.Annotation):
    def __init__(self): ...

class BeanProperty(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class BooleanBeanProperty(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class ScalaBeanInfo(java.beans.SimpleBeanInfo):
    def __init__(self, clazz: typing.Type[typing.Any], props: typing.List[java.lang.String], methods: typing.List[java.lang.String]): ...
    def getMethodDescriptors(self) -> typing.List[java.beans.MethodDescriptor]: ...
    def getPropertyDescriptors(self) -> typing.List[java.beans.PropertyDescriptor]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scala.beans")``.

    BeanDescription: typing.Type[BeanDescription]
    BeanDisplayName: typing.Type[BeanDisplayName]
    BeanInfo: typing.Type[BeanInfo]
    BeanInfoSkip: typing.Type[BeanInfoSkip]
    BeanProperty: typing.Type[BeanProperty]
    BooleanBeanProperty: typing.Type[BooleanBeanProperty]
    ScalaBeanInfo: typing.Type[ScalaBeanInfo]
