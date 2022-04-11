import java.beans
import scala.annotation
import typing



class BeanDescription(scala.annotation.Annotation):
    def __init__(self, description: str): ...
    def description(self) -> str: ...

class BeanDisplayName(scala.annotation.Annotation):
    def __init__(self, name: str): ...
    def name(self) -> str: ...

class BeanInfo(scala.annotation.Annotation):
    def __init__(self): ...

class BeanInfoSkip(scala.annotation.Annotation):
    def __init__(self): ...

class BeanProperty(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class BooleanBeanProperty(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class ScalaBeanInfo(java.beans.SimpleBeanInfo):
    def __init__(self, clazz: typing.Type[typing.Any], props: typing.List[str], methods: typing.List[str]): ...
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
