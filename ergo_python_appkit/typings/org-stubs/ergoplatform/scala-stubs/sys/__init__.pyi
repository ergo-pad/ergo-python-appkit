import java.io
import java.lang
import scala
import scala.collection
import scala.collection.generic
import scala.collection.immutable
import scala.collection.mutable
import scala.runtime
import scala.sys.process
import typing



class ShutdownHookThread(java.lang.Thread):
    def __init__(self, name: typing.Union[java.lang.String, str]): ...
    @staticmethod
    def apply(body: scala.Function0[scala.runtime.BoxedUnit]) -> 'ShutdownHookThread': ...
    def remove(self) -> bool: ...

class SystemProperties(scala.collection.mutable.AbstractMap[java.lang.String, java.lang.String]):
    def __init__(self): ...
    @typing.overload
    def $minus$eq(self, elem1: typing.Any, elem2: typing.Any, elems: scala.collection.Seq[typing.Any]) -> scala.collection.generic.Shrinkable[typing.Any]: ...
    @typing.overload
    def $minus$eq(self, key: typing.Union[java.lang.String, str]) -> 'SystemProperties': ...
    @typing.overload
    def $plus$eq(self, elem1: typing.Any, elem2: typing.Any, elems: scala.collection.Seq) -> scala.collection.generic.Growable: ...
    @typing.overload
    def $plus$eq(self, kv: scala.Tuple2[typing.Union[java.lang.String, str], typing.Union[java.lang.String, str]]) -> 'SystemProperties': ...
    def contains(self, key: typing.Union[java.lang.String, str]) -> bool: ...
    def default(self, key: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    def empty(self) -> scala.collection.mutable.Map[java.lang.String, java.lang.String]: ...
    _exclusively__T = typing.TypeVar('_exclusively__T')  # <T>
    @staticmethod
    def exclusively(body: scala.Function0[_exclusively__T]) -> _exclusively__T: ...
    def get(self, key: typing.Union[java.lang.String, str]) -> scala.Option[java.lang.String]: ...
    @staticmethod
    def headless() -> 'BooleanProp': ...
    @staticmethod
    def help(key: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    def iterator(self) -> scala.collection.Iterator[scala.Tuple2[java.lang.String, java.lang.String]]: ...
    def names(self) -> scala.collection.Iterator[java.lang.String]: ...
    @staticmethod
    def noTraceSuppression() -> 'BooleanProp': ...
    @staticmethod
    def noTraceSupression() -> 'BooleanProp': ...
    @staticmethod
    def preferIPv4Stack() -> 'BooleanProp': ...
    @staticmethod
    def preferIPv6Addresses() -> 'BooleanProp': ...
    @staticmethod
    def systemPropertiesToCompanion(p: 'SystemProperties') -> 'SystemProperties.': ...
    _wrapAccess__T = typing.TypeVar('_wrapAccess__T')  # <T>
    def wrapAccess(self, body: scala.Function0[_wrapAccess__T]) -> scala.Option[_wrapAccess__T]: ...
    class : ...

class package:
    @staticmethod
    def addShutdownHook(body: scala.Function0[scala.runtime.BoxedUnit]) -> ShutdownHookThread: ...
    @staticmethod
    def allThreads() -> scala.collection.IndexedSeq[java.lang.Thread]: ...
    @staticmethod
    def env() -> scala.collection.immutable.Map[java.lang.String, java.lang.String]: ...
    @staticmethod
    def error(message: typing.Union[java.lang.String, str]) -> scala.runtime.Nothing.: ...
    @typing.overload
    @staticmethod
    def exit() -> scala.runtime.Nothing.: ...
    @typing.overload
    @staticmethod
    def exit(status: int) -> scala.runtime.Nothing.: ...
    @staticmethod
    def props() -> SystemProperties: ...
    @staticmethod
    def runtime() -> java.lang.Runtime: ...

class BooleanProp(scala.sys.Prop[typing.Any]):
    @staticmethod
    def booleanPropAsBoolean(b: 'BooleanProp') -> bool: ...
    @staticmethod
    def constant(key: typing.Union[java.lang.String, str], isOn: bool) -> 'BooleanProp': ...
    def disable(self) -> None: ...
    def enable(self) -> None: ...
    _keyExists__T = typing.TypeVar('_keyExists__T')  # <T>
    @staticmethod
    def keyExists(key: typing.Union[java.lang.String, str]) -> 'BooleanProp': ...
    def toggle(self) -> None: ...
    @typing.overload
    def value(self) -> bool: ...
    @typing.overload
    def value(self) -> typing.Any: ...
    _valueIsTrue__T = typing.TypeVar('_valueIsTrue__T')  # <T>
    @staticmethod
    def valueIsTrue(key: typing.Union[java.lang.String, str]) -> 'BooleanProp': ...
    class BooleanPropImpl(scala.sys.PropImpl[typing.Any], scala.sys.BooleanProp):
        def __init__(self, key: typing.Union[java.lang.String, str], valueFn: scala.Function1[typing.Union[java.lang.String, str], typing.Any]): ...
        def disable(self) -> None: ...
        def enable(self) -> None: ...
        _setValue__T1 = typing.TypeVar('_setValue__T1')  # <T1>
        def setValue(self, newValue: _setValue__T1) -> bool: ...
        def toggle(self) -> None: ...
        def value(self) -> typing.Any: ...
    class ConstantImpl(scala.sys.BooleanProp):
        def __init__(self, key: typing.Union[java.lang.String, str], value: bool): ...
        def clear(self) -> None: ...
        def disable(self) -> None: ...
        def enable(self) -> None: ...
        def get(self) -> java.lang.String: ...
        def isSet(self) -> bool: ...
        def key(self) -> java.lang.String: ...
        def option(self) -> scala.Option[typing.Any]: ...
        def set(self, newValue: typing.Union[java.lang.String, str]) -> java.lang.String: ...
        _setValue__T1 = typing.TypeVar('_setValue__T1')  # <T1>
        def setValue(self, newValue: _setValue__T1) -> bool: ...
        def toggle(self) -> None: ...
        def value(self) -> bool: ...
        def zero(self) -> bool: ...

_CreatorImpl__T = typing.TypeVar('_CreatorImpl__T')  # <T>
class CreatorImpl(scala.sys.Prop.Creator[_CreatorImpl__T], typing.Generic[_CreatorImpl__T]):
    def __init__(self, f: scala.Function1[typing.Union[java.lang.String, str], _CreatorImpl__T]): ...
    def apply(self, key: typing.Union[java.lang.String, str]) -> 'Prop'[_CreatorImpl__T]: ...

_Prop__Creator__T = typing.TypeVar('_Prop__Creator__T')  # <T>
_Prop__T = typing.TypeVar('_Prop__T')  # <T>
class Prop(typing.Generic[_Prop__T]):
    _apply__T = typing.TypeVar('_apply__T')  # <T>
    @staticmethod
    def apply(key: typing.Union[java.lang.String, str], evidence$1: 'Prop.Creator'[_apply__T]) -> 'Prop'[_apply__T]: ...
    def clear(self) -> None: ...
    def get(self) -> java.lang.String: ...
    def isSet(self) -> bool: ...
    def key(self) -> java.lang.String: ...
    def option(self) -> scala.Option[_Prop__T]: ...
    def set(self, newValue: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    _setValue__T1 = typing.TypeVar('_setValue__T1')  # <T1>
    def setValue(self, value: _setValue__T1) -> _Prop__T: ...
    def value(self) -> _Prop__T: ...
    def zero(self) -> _Prop__T: ...
    class Creator(typing.Generic[_Prop__Creator__T]):
        def apply(self, key: typing.Union[java.lang.String, str]) -> 'Prop'[_Prop__Creator__T]: ...
    class DoubleProp$(CreatorImpl[typing.Any]):
        MODULE$: typing.ClassVar['Prop.DoubleProp.'] = ...
        def __init__(self): ...
    class FileProp$(CreatorImpl[java.io.File]):
        MODULE$: typing.ClassVar['Prop.FileProp.'] = ...
        def __init__(self): ...
    class IntProp$(CreatorImpl[typing.Any]):
        MODULE$: typing.ClassVar['Prop.IntProp.'] = ...
        def __init__(self): ...
    class StringProp$(CreatorImpl[java.lang.String]):
        MODULE$: typing.ClassVar['Prop.StringProp.'] = ...
        def __init__(self): ...

_PropImpl__T = typing.TypeVar('_PropImpl__T')  # <T>
class PropImpl(Prop[_PropImpl__T], typing.Generic[_PropImpl__T]):
    def __init__(self, key: typing.Union[java.lang.String, str], valueFn: scala.Function1[typing.Union[java.lang.String, str], _PropImpl__T]): ...
    def clear(self) -> None: ...
    def get(self) -> java.lang.String: ...
    def isSet(self) -> bool: ...
    def key(self) -> java.lang.String: ...
    def option(self) -> scala.Option[_PropImpl__T]: ...
    def set(self, newValue: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    _setValue__T1 = typing.TypeVar('_setValue__T1')  # <T1>
    def setValue(self, newValue: _setValue__T1) -> _PropImpl__T: ...
    def toString(self) -> java.lang.String: ...
    def underlying(self) -> scala.collection.mutable.Map[java.lang.String, java.lang.String]: ...
    def value(self) -> _PropImpl__T: ...
    def zero(self) -> _PropImpl__T: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scala.sys")``.

    BooleanProp: typing.Type[BooleanProp]
    CreatorImpl: typing.Type[CreatorImpl]
    Prop: typing.Type[Prop]
    PropImpl: typing.Type[PropImpl]
    ShutdownHookThread: typing.Type[ShutdownHookThread]
    SystemProperties: typing.Type[SystemProperties]
    package: typing.Type[package]
    process: scala.sys.process.__module_protocol__
