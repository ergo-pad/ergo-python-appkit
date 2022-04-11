import java.io
import java.lang
import java.util.stream
import scala
import scala.annotation
import scala.beans
import scala.collection
import scala.collection.generic
import scala.collection.immutable
import scala.collection.mutable
import scala.collection.parallel
import scala.collection.parallel.immutable
import scala.compat
import scala.concurrent
import scala.io
import scala.math
import scala.ref
import scala.reflect
import scala.runtime
import scala.sys
import scala.text
import scala.util
import typing



class AnyVal:
    def __init__(self): ...

_Array__T = typing.TypeVar('_Array__T')  # <T>
class Array(java.io.Serializable, java.lang.Cloneable, typing.Generic[_Array__T]):
    def __init__(self, _length: int): ...
    def apply(self, i: int) -> _Array__T: ...
    _canBuildFrom__T = typing.TypeVar('_canBuildFrom__T')  # <T>
    @staticmethod
    def canBuildFrom(t: scala.reflect.ClassTag[_canBuildFrom__T]) -> scala.collection.generic.CanBuildFrom[typing.Any, _canBuildFrom__T, typing.Any]: ...
    def clone(self) -> typing.Any: ...
    @staticmethod
    def concat(xss: scala.collection.Seq, evidence$8: scala.reflect.ClassTag) -> typing.Any: ...
    @staticmethod
    def copy(src: typing.Any, srcPos: int, dest: typing.Any, destPos: int, length: int) -> None: ...
    @staticmethod
    def empty(evidence$1: scala.reflect.ClassTag) -> typing.Any: ...
    @staticmethod
    def emptyBooleanArray() -> typing.List[bool]: ...
    @staticmethod
    def emptyByteArray() -> typing.List[int]: ...
    @staticmethod
    def emptyCharArray() -> typing.List[str]: ...
    @staticmethod
    def emptyDoubleArray() -> typing.List[float]: ...
    @staticmethod
    def emptyFloatArray() -> typing.List[float]: ...
    @staticmethod
    def emptyIntArray() -> typing.List[int]: ...
    @staticmethod
    def emptyLongArray() -> typing.List[int]: ...
    @staticmethod
    def emptyObjectArray() -> typing.List[typing.Any]: ...
    @staticmethod
    def emptyShortArray() -> typing.List[int]: ...
    _fallbackCanBuildFrom__T = typing.TypeVar('_fallbackCanBuildFrom__T')  # <T>
    @staticmethod
    def fallbackCanBuildFrom(m: 'Predef.DummyImplicit') -> scala.collection.generic.CanBuildFrom[typing.Any, _fallbackCanBuildFrom__T, scala.collection.mutable.ArraySeq[_fallbackCanBuildFrom__T]]: ...
    @typing.overload
    @staticmethod
    def fill(n: int, elem: 'Function0', evidence$9: scala.reflect.ClassTag) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def fill(n1: int, n2: int, elem: 'Function0', evidence$10: scala.reflect.ClassTag) -> typing.List[typing.Any]: ...
    @typing.overload
    @staticmethod
    def fill(n1: int, n2: int, n3: int, elem: 'Function0', evidence$11: scala.reflect.ClassTag) -> typing.List[typing.List[typing.Any]]: ...
    @typing.overload
    @staticmethod
    def fill(n1: int, n2: int, n3: int, n4: int, elem: 'Function0', evidence$12: scala.reflect.ClassTag) -> typing.List[typing.List[typing.List[typing.Any]]]: ...
    @typing.overload
    @staticmethod
    def fill(n1: int, n2: int, n3: int, n4: int, n5: int, elem: 'Function0', evidence$13: scala.reflect.ClassTag) -> typing.List[typing.List[typing.List[typing.List[typing.Any]]]]: ...
    @staticmethod
    def iterate(start: typing.Any, len: int, f: 'Function1', evidence$19: scala.reflect.ClassTag) -> typing.Any: ...
    def length(self) -> int: ...
    _newBuilder__T = typing.TypeVar('_newBuilder__T')  # <T>
    @staticmethod
    def newBuilder(t: scala.reflect.ClassTag[_newBuilder__T]) -> scala.collection.mutable.ArrayBuilder[_newBuilder__T]: ...
    @typing.overload
    @staticmethod
    def ofDim(n1: int, evidence$3: scala.reflect.ClassTag) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def ofDim(n1: int, n2: int, evidence$4: scala.reflect.ClassTag) -> typing.List[typing.Any]: ...
    @typing.overload
    @staticmethod
    def ofDim(n1: int, n2: int, n3: int, evidence$5: scala.reflect.ClassTag) -> typing.List[typing.List[typing.Any]]: ...
    @typing.overload
    @staticmethod
    def ofDim(n1: int, n2: int, n3: int, n4: int, evidence$6: scala.reflect.ClassTag) -> typing.List[typing.List[typing.List[typing.Any]]]: ...
    @typing.overload
    @staticmethod
    def ofDim(n1: int, n2: int, n3: int, n4: int, n5: int, evidence$7: scala.reflect.ClassTag) -> typing.List[typing.List[typing.List[typing.List[typing.Any]]]]: ...
    @typing.overload
    @staticmethod
    def range(start: int, end: int) -> typing.List[int]: ...
    @typing.overload
    @staticmethod
    def range(start: int, end: int, step: int) -> typing.List[int]: ...
    @typing.overload
    @staticmethod
    def tabulate(n: int, f: 'Function1', evidence$14: scala.reflect.ClassTag) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def tabulate(n1: int, n2: int, f: 'Function2', evidence$15: scala.reflect.ClassTag) -> typing.List[typing.Any]: ...
    @typing.overload
    @staticmethod
    def tabulate(n1: int, n2: int, n3: int, f: 'Function3', evidence$16: scala.reflect.ClassTag) -> typing.List[typing.List[typing.Any]]: ...
    @typing.overload
    @staticmethod
    def tabulate(n1: int, n2: int, n3: int, n4: int, f: 'Function4', evidence$17: scala.reflect.ClassTag) -> typing.List[typing.List[typing.List[typing.Any]]]: ...
    @typing.overload
    @staticmethod
    def tabulate(n1: int, n2: int, n3: int, n4: int, n5: int, f: 'Function5', evidence$18: scala.reflect.ClassTag) -> typing.List[typing.List[typing.List[typing.List[typing.Any]]]]: ...
    _unapplySeq__T = typing.TypeVar('_unapplySeq__T')  # <T>
    @staticmethod
    def unapplySeq(x: typing.Any) -> 'Option'[scala.collection.IndexedSeq[_unapplySeq__T]]: ...
    def update(self, i: int, x: _Array__T) -> None: ...

class Boolean:
    def __init__(self): ...
    def $amp(self, x: bool) -> bool: ...
    def $amp$amp(self, x: bool) -> bool: ...
    def $bang$eq(self, x: bool) -> bool: ...
    def $bar(self, x: bool) -> bool: ...
    def $bar$bar(self, x: bool) -> bool: ...
    def $eq$eq(self, x: bool) -> bool: ...
    def $up(self, x: bool) -> bool: ...
    @staticmethod
    def box(x: bool) -> bool: ...
    @staticmethod
    def toString() -> str: ...
    def unary_$bang(self) -> bool: ...
    @staticmethod
    def unbox(x: typing.Any) -> bool: ...

class Byte:
    def __init__(self): ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: str) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: str) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: float) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: float) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: str) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: float) -> float: ...
    @typing.overload
    def $div(self, x: float) -> float: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: str) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: str) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: float) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: float) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: str) -> bool: ...
    @typing.overload
    def $greater(self, x: float) -> bool: ...
    @typing.overload
    def $greater(self, x: float) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: str) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: float) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: float) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: str) -> bool: ...
    @typing.overload
    def $less(self, x: float) -> bool: ...
    @typing.overload
    def $less(self, x: float) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: str) -> bool: ...
    @typing.overload
    def $less$eq(self, x: float) -> bool: ...
    @typing.overload
    def $less$eq(self, x: float) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$less(self, x: int) -> int: ...
    @typing.overload
    def $less$less(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: float) -> float: ...
    @typing.overload
    def $minus(self, x: float) -> float: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: str) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: float) -> float: ...
    @typing.overload
    def $percent(self, x: float) -> float: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: str) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: float) -> float: ...
    @typing.overload
    def $plus(self, x: float) -> float: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: str) -> int: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: str) -> str: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: float) -> float: ...
    @typing.overload
    def $times(self, x: float) -> float: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: str) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: str) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @staticmethod
    def MaxValue() -> int: ...
    @staticmethod
    def MinValue() -> int: ...
    @staticmethod
    def box(x: int) -> int: ...
    @staticmethod
    def byte2double(x: int) -> float: ...
    @staticmethod
    def byte2float(x: int) -> float: ...
    @staticmethod
    def byte2int(x: int) -> int: ...
    @staticmethod
    def byte2long(x: int) -> int: ...
    @staticmethod
    def byte2short(x: int) -> int: ...
    def toByte(self) -> int: ...
    def toChar(self) -> str: ...
    def toDouble(self) -> float: ...
    def toFloat(self) -> float: ...
    def toInt(self) -> int: ...
    def toLong(self) -> int: ...
    def toShort(self) -> int: ...
    @staticmethod
    def toString() -> str: ...
    def unary_$minus(self) -> int: ...
    def unary_$plus(self) -> int: ...
    def unary_$tilde(self) -> int: ...
    @staticmethod
    def unbox(x: typing.Any) -> int: ...

class Char:
    def __init__(self): ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: str) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: str) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: float) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: float) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: str) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: float) -> float: ...
    @typing.overload
    def $div(self, x: float) -> float: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: str) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: str) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: float) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: float) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: str) -> bool: ...
    @typing.overload
    def $greater(self, x: float) -> bool: ...
    @typing.overload
    def $greater(self, x: float) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: str) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: float) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: float) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: str) -> bool: ...
    @typing.overload
    def $less(self, x: float) -> bool: ...
    @typing.overload
    def $less(self, x: float) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: str) -> bool: ...
    @typing.overload
    def $less$eq(self, x: float) -> bool: ...
    @typing.overload
    def $less$eq(self, x: float) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$less(self, x: int) -> int: ...
    @typing.overload
    def $less$less(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: float) -> float: ...
    @typing.overload
    def $minus(self, x: float) -> float: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: str) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: float) -> float: ...
    @typing.overload
    def $percent(self, x: float) -> float: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: str) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: float) -> float: ...
    @typing.overload
    def $plus(self, x: float) -> float: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: str) -> int: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: str) -> str: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: float) -> float: ...
    @typing.overload
    def $times(self, x: float) -> float: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: str) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: str) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @staticmethod
    def MaxValue() -> str: ...
    @staticmethod
    def MinValue() -> str: ...
    @staticmethod
    def box(x: str) -> str: ...
    @staticmethod
    def char2double(x: str) -> float: ...
    @staticmethod
    def char2float(x: str) -> float: ...
    @staticmethod
    def char2int(x: str) -> int: ...
    @staticmethod
    def char2long(x: str) -> int: ...
    def toByte(self) -> int: ...
    def toChar(self) -> str: ...
    def toDouble(self) -> float: ...
    def toFloat(self) -> float: ...
    def toInt(self) -> int: ...
    def toLong(self) -> int: ...
    def toShort(self) -> int: ...
    @staticmethod
    def toString() -> str: ...
    def unary_$minus(self) -> int: ...
    def unary_$plus(self) -> int: ...
    def unary_$tilde(self) -> int: ...
    @staticmethod
    def unbox(x: typing.Any) -> str: ...

class Cloneable(java.lang.Cloneable): ...

class Console:
    @staticmethod
    def BLACK() -> str: ...
    @staticmethod
    def BLACK_B() -> str: ...
    @staticmethod
    def BLINK() -> str: ...
    @staticmethod
    def BLUE() -> str: ...
    @staticmethod
    def BLUE_B() -> str: ...
    @staticmethod
    def BOLD() -> str: ...
    @staticmethod
    def CYAN() -> str: ...
    @staticmethod
    def CYAN_B() -> str: ...
    @staticmethod
    def GREEN() -> str: ...
    @staticmethod
    def GREEN_B() -> str: ...
    @staticmethod
    def INVISIBLE() -> str: ...
    @staticmethod
    def MAGENTA() -> str: ...
    @staticmethod
    def MAGENTA_B() -> str: ...
    @staticmethod
    def RED() -> str: ...
    @staticmethod
    def RED_B() -> str: ...
    @staticmethod
    def RESET() -> str: ...
    @staticmethod
    def REVERSED() -> str: ...
    @staticmethod
    def UNDERLINED() -> str: ...
    @staticmethod
    def WHITE() -> str: ...
    @staticmethod
    def WHITE_B() -> str: ...
    @staticmethod
    def YELLOW() -> str: ...
    @staticmethod
    def YELLOW_B() -> str: ...
    @staticmethod
    def err() -> java.io.PrintStream: ...
    @staticmethod
    def flush() -> None: ...
    @staticmethod
    def out() -> java.io.PrintStream: ...
    @staticmethod
    def printf(text: str, args: scala.collection.Seq[typing.Any]) -> None: ...
    @typing.overload
    @staticmethod
    def println() -> None: ...
    @typing.overload
    @staticmethod
    def println(x: typing.Any) -> None: ...
    @staticmethod
    def readBoolean() -> bool: ...
    @staticmethod
    def readByte() -> int: ...
    @staticmethod
    def readChar() -> str: ...
    @staticmethod
    def readDouble() -> float: ...
    @staticmethod
    def readFloat() -> float: ...
    @staticmethod
    def readInt() -> int: ...
    @typing.overload
    @staticmethod
    def readLine() -> str: ...
    @typing.overload
    @staticmethod
    def readLine(text: str, args: scala.collection.Seq[typing.Any]) -> str: ...
    @staticmethod
    def readLong() -> int: ...
    @staticmethod
    def readShort() -> int: ...
    @staticmethod
    def readf(format: str) -> scala.collection.immutable.List[typing.Any]: ...
    @staticmethod
    def readf1(format: str) -> typing.Any: ...
    @staticmethod
    def readf2(format: str) -> 'Tuple2'[typing.Any, typing.Any]: ...
    @staticmethod
    def readf3(format: str) -> 'Tuple3'[typing.Any, typing.Any, typing.Any]: ...
    @typing.overload
    @staticmethod
    def setErr(err: java.io.OutputStream) -> None: ...
    @typing.overload
    @staticmethod
    def setErr(err: java.io.PrintStream) -> None: ...
    @typing.overload
    @staticmethod
    def setIn(in_: java.io.InputStream) -> None: ...
    @typing.overload
    @staticmethod
    def setIn(reader: java.io.Reader) -> None: ...
    @typing.overload
    @staticmethod
    def setOut(out: java.io.OutputStream) -> None: ...
    @typing.overload
    @staticmethod
    def setOut(out: java.io.PrintStream) -> None: ...
    _withErr_0__T = typing.TypeVar('_withErr_0__T')  # <T>
    _withErr_1__T = typing.TypeVar('_withErr_1__T')  # <T>
    @typing.overload
    @staticmethod
    def withErr(err: java.io.OutputStream, thunk: 'Function0'[_withErr_0__T]) -> _withErr_0__T: ...
    @typing.overload
    @staticmethod
    def withErr(err: java.io.PrintStream, thunk: 'Function0'[_withErr_1__T]) -> _withErr_1__T: ...
    _withIn_0__T = typing.TypeVar('_withIn_0__T')  # <T>
    _withIn_1__T = typing.TypeVar('_withIn_1__T')  # <T>
    @typing.overload
    @staticmethod
    def withIn(in_: java.io.InputStream, thunk: 'Function0'[_withIn_0__T]) -> _withIn_0__T: ...
    @typing.overload
    @staticmethod
    def withIn(reader: java.io.Reader, thunk: 'Function0'[_withIn_1__T]) -> _withIn_1__T: ...
    _withOut_0__T = typing.TypeVar('_withOut_0__T')  # <T>
    _withOut_1__T = typing.TypeVar('_withOut_1__T')  # <T>
    @typing.overload
    @staticmethod
    def withOut(out: java.io.OutputStream, thunk: 'Function0'[_withOut_0__T]) -> _withOut_0__T: ...
    @typing.overload
    @staticmethod
    def withOut(out: java.io.PrintStream, thunk: 'Function0'[_withOut_1__T]) -> _withOut_1__T: ...

class DelayedInit:
    def delayedInit(self, x: 'Function0'[scala.runtime.BoxedUnit]) -> None: ...

class DeprecatedConsole:
    def __init__(self): ...
    def readBoolean(self) -> bool: ...
    def readByte(self) -> int: ...
    def readChar(self) -> str: ...
    def readDouble(self) -> float: ...
    def readFloat(self) -> float: ...
    def readInt(self) -> int: ...
    @typing.overload
    def readLine(self) -> str: ...
    @typing.overload
    def readLine(self, text: str, args: scala.collection.Seq[typing.Any]) -> str: ...
    def readLong(self) -> int: ...
    def readShort(self) -> int: ...
    def readf(self, format: str) -> scala.collection.immutable.List[typing.Any]: ...
    def readf1(self, format: str) -> typing.Any: ...
    def readf2(self, format: str) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def readf3(self, format: str) -> 'Tuple3'[typing.Any, typing.Any, typing.Any]: ...
    @typing.overload
    def setErr(self, err: java.io.OutputStream) -> None: ...
    @typing.overload
    def setErr(self, err: java.io.PrintStream) -> None: ...
    def setErrDirect(self, err: java.io.PrintStream) -> None: ...
    @typing.overload
    def setIn(self, in_: java.io.InputStream) -> None: ...
    @typing.overload
    def setIn(self, reader: java.io.Reader) -> None: ...
    def setInDirect(self, in_: java.io.BufferedReader) -> None: ...
    @typing.overload
    def setOut(self, out: java.io.OutputStream) -> None: ...
    @typing.overload
    def setOut(self, out: java.io.PrintStream) -> None: ...
    def setOutDirect(self, out: java.io.PrintStream) -> None: ...

class DeprecatedPredef:
    @staticmethod
    def $init$($this: 'DeprecatedPredef') -> None: ...
    _any2ArrowAssoc__A = typing.TypeVar('_any2ArrowAssoc__A')  # <A>
    def any2ArrowAssoc(self, x: _any2ArrowAssoc__A) -> _any2ArrowAssoc__A: ...
    _any2Ensuring__A = typing.TypeVar('_any2Ensuring__A')  # <A>
    def any2Ensuring(self, x: _any2Ensuring__A) -> _any2Ensuring__A: ...
    def any2stringfmt(self, x: typing.Any) -> typing.Any: ...
    def arrayToCharSequence(self, xs: typing.List[str]) -> java.lang.CharSequence: ...
    def exceptionWrapper(self, exc: java.lang.Throwable) -> java.lang.Throwable: ...
    def readBoolean(self) -> bool: ...
    def readByte(self) -> int: ...
    def readChar(self) -> str: ...
    def readDouble(self) -> float: ...
    def readFloat(self) -> float: ...
    def readInt(self) -> int: ...
    @typing.overload
    def readLine(self) -> str: ...
    @typing.overload
    def readLine(self, text: str, args: scala.collection.Seq[typing.Any]) -> str: ...
    def readLong(self) -> int: ...
    def readShort(self) -> int: ...
    def readf(self, format: str) -> scala.collection.immutable.List[typing.Any]: ...
    def readf1(self, format: str) -> typing.Any: ...
    def readf2(self, format: str) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def readf3(self, format: str) -> 'Tuple3'[typing.Any, typing.Any, typing.Any]: ...
    def seqToCharSequence(self, xs: scala.collection.IndexedSeq[typing.Any]) -> java.lang.CharSequence: ...

class Double:
    def __init__(self): ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: str) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: float) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: float) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $div(self, x: int) -> float: ...
    @typing.overload
    def $div(self, x: str) -> float: ...
    @typing.overload
    def $div(self, x: float) -> float: ...
    @typing.overload
    def $div(self, x: float) -> float: ...
    @typing.overload
    def $div(self, x: int) -> float: ...
    @typing.overload
    def $div(self, x: int) -> float: ...
    @typing.overload
    def $div(self, x: int) -> float: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: str) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: float) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: float) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: str) -> bool: ...
    @typing.overload
    def $greater(self, x: float) -> bool: ...
    @typing.overload
    def $greater(self, x: float) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: str) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: float) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: float) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: str) -> bool: ...
    @typing.overload
    def $less(self, x: float) -> bool: ...
    @typing.overload
    def $less(self, x: float) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: str) -> bool: ...
    @typing.overload
    def $less$eq(self, x: float) -> bool: ...
    @typing.overload
    def $less$eq(self, x: float) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $minus(self, x: int) -> float: ...
    @typing.overload
    def $minus(self, x: str) -> float: ...
    @typing.overload
    def $minus(self, x: float) -> float: ...
    @typing.overload
    def $minus(self, x: float) -> float: ...
    @typing.overload
    def $minus(self, x: int) -> float: ...
    @typing.overload
    def $minus(self, x: int) -> float: ...
    @typing.overload
    def $minus(self, x: int) -> float: ...
    @typing.overload
    def $percent(self, x: int) -> float: ...
    @typing.overload
    def $percent(self, x: str) -> float: ...
    @typing.overload
    def $percent(self, x: float) -> float: ...
    @typing.overload
    def $percent(self, x: float) -> float: ...
    @typing.overload
    def $percent(self, x: int) -> float: ...
    @typing.overload
    def $percent(self, x: int) -> float: ...
    @typing.overload
    def $percent(self, x: int) -> float: ...
    @typing.overload
    def $plus(self, x: int) -> float: ...
    @typing.overload
    def $plus(self, x: str) -> float: ...
    @typing.overload
    def $plus(self, x: float) -> float: ...
    @typing.overload
    def $plus(self, x: float) -> float: ...
    @typing.overload
    def $plus(self, x: int) -> float: ...
    @typing.overload
    def $plus(self, x: int) -> float: ...
    @typing.overload
    def $plus(self, x: int) -> float: ...
    @typing.overload
    def $plus(self, x: str) -> str: ...
    @typing.overload
    def $times(self, x: int) -> float: ...
    @typing.overload
    def $times(self, x: str) -> float: ...
    @typing.overload
    def $times(self, x: float) -> float: ...
    @typing.overload
    def $times(self, x: float) -> float: ...
    @typing.overload
    def $times(self, x: int) -> float: ...
    @typing.overload
    def $times(self, x: int) -> float: ...
    @typing.overload
    def $times(self, x: int) -> float: ...
    @staticmethod
    def MaxValue() -> float: ...
    @staticmethod
    def MinPositiveValue() -> float: ...
    @staticmethod
    def MinValue() -> float: ...
    @staticmethod
    def NaN() -> float: ...
    @staticmethod
    def NegativeInfinity() -> float: ...
    @staticmethod
    def PositiveInfinity() -> float: ...
    @staticmethod
    def box(x: float) -> float: ...
    def toByte(self) -> int: ...
    def toChar(self) -> str: ...
    def toDouble(self) -> float: ...
    def toFloat(self) -> float: ...
    def toInt(self) -> int: ...
    def toLong(self) -> int: ...
    def toShort(self) -> int: ...
    @staticmethod
    def toString() -> str: ...
    def unary_$minus(self) -> float: ...
    def unary_$plus(self) -> float: ...
    @staticmethod
    def unbox(x: typing.Any) -> float: ...

class Dynamic: ...

class Equals:
    def canEqual(self, that: typing.Any) -> bool: ...
    def equals(self, that: typing.Any) -> bool: ...

class FallbackArrayBuilding:
    def __init__(self): ...
    _fallbackCanBuildFrom__T = typing.TypeVar('_fallbackCanBuildFrom__T')  # <T>
    def fallbackCanBuildFrom(self, m: 'Predef.DummyImplicit') -> scala.collection.generic.CanBuildFrom[typing.Any, _fallbackCanBuildFrom__T, scala.collection.mutable.ArraySeq[_fallbackCanBuildFrom__T]]: ...

class Float:
    def __init__(self): ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: str) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: float) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: float) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $div(self, x: float) -> float: ...
    @typing.overload
    def $div(self, x: int) -> float: ...
    @typing.overload
    def $div(self, x: str) -> float: ...
    @typing.overload
    def $div(self, x: float) -> float: ...
    @typing.overload
    def $div(self, x: int) -> float: ...
    @typing.overload
    def $div(self, x: int) -> float: ...
    @typing.overload
    def $div(self, x: int) -> float: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: str) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: float) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: float) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: str) -> bool: ...
    @typing.overload
    def $greater(self, x: float) -> bool: ...
    @typing.overload
    def $greater(self, x: float) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: str) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: float) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: float) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: str) -> bool: ...
    @typing.overload
    def $less(self, x: float) -> bool: ...
    @typing.overload
    def $less(self, x: float) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: str) -> bool: ...
    @typing.overload
    def $less$eq(self, x: float) -> bool: ...
    @typing.overload
    def $less$eq(self, x: float) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $minus(self, x: float) -> float: ...
    @typing.overload
    def $minus(self, x: int) -> float: ...
    @typing.overload
    def $minus(self, x: str) -> float: ...
    @typing.overload
    def $minus(self, x: float) -> float: ...
    @typing.overload
    def $minus(self, x: int) -> float: ...
    @typing.overload
    def $minus(self, x: int) -> float: ...
    @typing.overload
    def $minus(self, x: int) -> float: ...
    @typing.overload
    def $percent(self, x: float) -> float: ...
    @typing.overload
    def $percent(self, x: int) -> float: ...
    @typing.overload
    def $percent(self, x: str) -> float: ...
    @typing.overload
    def $percent(self, x: float) -> float: ...
    @typing.overload
    def $percent(self, x: int) -> float: ...
    @typing.overload
    def $percent(self, x: int) -> float: ...
    @typing.overload
    def $percent(self, x: int) -> float: ...
    @typing.overload
    def $plus(self, x: float) -> float: ...
    @typing.overload
    def $plus(self, x: int) -> float: ...
    @typing.overload
    def $plus(self, x: str) -> float: ...
    @typing.overload
    def $plus(self, x: float) -> float: ...
    @typing.overload
    def $plus(self, x: int) -> float: ...
    @typing.overload
    def $plus(self, x: int) -> float: ...
    @typing.overload
    def $plus(self, x: int) -> float: ...
    @typing.overload
    def $plus(self, x: str) -> str: ...
    @typing.overload
    def $times(self, x: float) -> float: ...
    @typing.overload
    def $times(self, x: int) -> float: ...
    @typing.overload
    def $times(self, x: str) -> float: ...
    @typing.overload
    def $times(self, x: float) -> float: ...
    @typing.overload
    def $times(self, x: int) -> float: ...
    @typing.overload
    def $times(self, x: int) -> float: ...
    @typing.overload
    def $times(self, x: int) -> float: ...
    @staticmethod
    def MaxValue() -> float: ...
    @staticmethod
    def MinPositiveValue() -> float: ...
    @staticmethod
    def MinValue() -> float: ...
    @staticmethod
    def NaN() -> float: ...
    @staticmethod
    def NegativeInfinity() -> float: ...
    @staticmethod
    def PositiveInfinity() -> float: ...
    @staticmethod
    def box(x: float) -> float: ...
    @staticmethod
    def float2double(x: float) -> float: ...
    def toByte(self) -> int: ...
    def toChar(self) -> str: ...
    def toDouble(self) -> float: ...
    def toFloat(self) -> float: ...
    def toInt(self) -> int: ...
    def toLong(self) -> int: ...
    def toShort(self) -> int: ...
    @staticmethod
    def toString() -> str: ...
    def unary_$minus(self) -> float: ...
    def unary_$plus(self) -> float: ...
    @staticmethod
    def unbox(x: typing.Any) -> float: ...

class Function:
    _chain__a = typing.TypeVar('_chain__a')  # <a>
    @staticmethod
    def chain(fs: scala.collection.Seq['Function1'[_chain__a, _chain__a]]) -> 'Function1'[_chain__a, _chain__a]: ...
    _const__T = typing.TypeVar('_const__T')  # <T>
    _const__U = typing.TypeVar('_const__U')  # <U>
    @staticmethod
    def const(x: _const__T, y: _const__U) -> _const__T: ...
    _tupled_0__a1 = typing.TypeVar('_tupled_0__a1')  # <a1>
    _tupled_0__a2 = typing.TypeVar('_tupled_0__a2')  # <a2>
    _tupled_0__b = typing.TypeVar('_tupled_0__b')  # <b>
    _tupled_1__a1 = typing.TypeVar('_tupled_1__a1')  # <a1>
    _tupled_1__a2 = typing.TypeVar('_tupled_1__a2')  # <a2>
    _tupled_1__a3 = typing.TypeVar('_tupled_1__a3')  # <a3>
    _tupled_1__b = typing.TypeVar('_tupled_1__b')  # <b>
    _tupled_2__a1 = typing.TypeVar('_tupled_2__a1')  # <a1>
    _tupled_2__a2 = typing.TypeVar('_tupled_2__a2')  # <a2>
    _tupled_2__a3 = typing.TypeVar('_tupled_2__a3')  # <a3>
    _tupled_2__a4 = typing.TypeVar('_tupled_2__a4')  # <a4>
    _tupled_2__b = typing.TypeVar('_tupled_2__b')  # <b>
    _tupled_3__a1 = typing.TypeVar('_tupled_3__a1')  # <a1>
    _tupled_3__a2 = typing.TypeVar('_tupled_3__a2')  # <a2>
    _tupled_3__a3 = typing.TypeVar('_tupled_3__a3')  # <a3>
    _tupled_3__a4 = typing.TypeVar('_tupled_3__a4')  # <a4>
    _tupled_3__a5 = typing.TypeVar('_tupled_3__a5')  # <a5>
    _tupled_3__b = typing.TypeVar('_tupled_3__b')  # <b>
    @typing.overload
    @staticmethod
    def tupled(f: 'Function2'[_tupled_0__a1, _tupled_0__a2, _tupled_0__b]) -> 'Function1'['Tuple2'[_tupled_0__a1, _tupled_0__a2], _tupled_0__b]: ...
    @typing.overload
    @staticmethod
    def tupled(f: 'Function3'[_tupled_1__a1, _tupled_1__a2, _tupled_1__a3, _tupled_1__b]) -> 'Function1'['Tuple3'[_tupled_1__a1, _tupled_1__a2, _tupled_1__a3], _tupled_1__b]: ...
    @typing.overload
    @staticmethod
    def tupled(f: 'Function4'[_tupled_2__a1, _tupled_2__a2, _tupled_2__a3, _tupled_2__a4, _tupled_2__b]) -> 'Function1'['Tuple4'[_tupled_2__a1, _tupled_2__a2, _tupled_2__a3, _tupled_2__a4], _tupled_2__b]: ...
    @typing.overload
    @staticmethod
    def tupled(f: 'Function5'[_tupled_3__a1, _tupled_3__a2, _tupled_3__a3, _tupled_3__a4, _tupled_3__a5, _tupled_3__b]) -> 'Function1'['Tuple5'[_tupled_3__a1, _tupled_3__a2, _tupled_3__a3, _tupled_3__a4, _tupled_3__a5], _tupled_3__b]: ...
    _uncurried_0__a1 = typing.TypeVar('_uncurried_0__a1')  # <a1>
    _uncurried_0__a2 = typing.TypeVar('_uncurried_0__a2')  # <a2>
    _uncurried_0__b = typing.TypeVar('_uncurried_0__b')  # <b>
    _uncurried_1__a1 = typing.TypeVar('_uncurried_1__a1')  # <a1>
    _uncurried_1__a2 = typing.TypeVar('_uncurried_1__a2')  # <a2>
    _uncurried_1__a3 = typing.TypeVar('_uncurried_1__a3')  # <a3>
    _uncurried_1__b = typing.TypeVar('_uncurried_1__b')  # <b>
    _uncurried_2__a1 = typing.TypeVar('_uncurried_2__a1')  # <a1>
    _uncurried_2__a2 = typing.TypeVar('_uncurried_2__a2')  # <a2>
    _uncurried_2__a3 = typing.TypeVar('_uncurried_2__a3')  # <a3>
    _uncurried_2__a4 = typing.TypeVar('_uncurried_2__a4')  # <a4>
    _uncurried_2__b = typing.TypeVar('_uncurried_2__b')  # <b>
    _uncurried_3__a1 = typing.TypeVar('_uncurried_3__a1')  # <a1>
    _uncurried_3__a2 = typing.TypeVar('_uncurried_3__a2')  # <a2>
    _uncurried_3__a3 = typing.TypeVar('_uncurried_3__a3')  # <a3>
    _uncurried_3__a4 = typing.TypeVar('_uncurried_3__a4')  # <a4>
    _uncurried_3__a5 = typing.TypeVar('_uncurried_3__a5')  # <a5>
    _uncurried_3__b = typing.TypeVar('_uncurried_3__b')  # <b>
    @typing.overload
    @staticmethod
    def uncurried(f: 'Function1'[_uncurried_0__a1, 'Function1'[_uncurried_0__a2, _uncurried_0__b]]) -> 'Function2'[_uncurried_0__a1, _uncurried_0__a2, _uncurried_0__b]: ...
    @typing.overload
    @staticmethod
    def uncurried(f: 'Function1'[_uncurried_1__a1, 'Function1'[_uncurried_1__a2, 'Function1'[_uncurried_1__a3, _uncurried_1__b]]]) -> 'Function3'[_uncurried_1__a1, _uncurried_1__a2, _uncurried_1__a3, _uncurried_1__b]: ...
    @typing.overload
    @staticmethod
    def uncurried(f: 'Function1'[_uncurried_2__a1, 'Function1'[_uncurried_2__a2, 'Function1'[_uncurried_2__a3, 'Function1'[_uncurried_2__a4, _uncurried_2__b]]]]) -> 'Function4'[_uncurried_2__a1, _uncurried_2__a2, _uncurried_2__a3, _uncurried_2__a4, _uncurried_2__b]: ...
    @typing.overload
    @staticmethod
    def uncurried(f: 'Function1'[_uncurried_3__a1, 'Function1'[_uncurried_3__a2, 'Function1'[_uncurried_3__a3, 'Function1'[_uncurried_3__a4, 'Function1'[_uncurried_3__a5, _uncurried_3__b]]]]]) -> 'Function5'[_uncurried_3__a1, _uncurried_3__a2, _uncurried_3__a3, _uncurried_3__a4, _uncurried_3__a5, _uncurried_3__b]: ...
    _unlift__T = typing.TypeVar('_unlift__T')  # <T>
    _unlift__R = typing.TypeVar('_unlift__R')  # <R>
    @staticmethod
    def unlift(f: 'Function1'[_unlift__T, 'Option'[_unlift__R]]) -> 'PartialFunction'[_unlift__T, _unlift__R]: ...
    _untupled_0__a1 = typing.TypeVar('_untupled_0__a1')  # <a1>
    _untupled_0__a2 = typing.TypeVar('_untupled_0__a2')  # <a2>
    _untupled_0__b = typing.TypeVar('_untupled_0__b')  # <b>
    _untupled_1__a1 = typing.TypeVar('_untupled_1__a1')  # <a1>
    _untupled_1__a2 = typing.TypeVar('_untupled_1__a2')  # <a2>
    _untupled_1__a3 = typing.TypeVar('_untupled_1__a3')  # <a3>
    _untupled_1__b = typing.TypeVar('_untupled_1__b')  # <b>
    _untupled_2__a1 = typing.TypeVar('_untupled_2__a1')  # <a1>
    _untupled_2__a2 = typing.TypeVar('_untupled_2__a2')  # <a2>
    _untupled_2__a3 = typing.TypeVar('_untupled_2__a3')  # <a3>
    _untupled_2__a4 = typing.TypeVar('_untupled_2__a4')  # <a4>
    _untupled_2__b = typing.TypeVar('_untupled_2__b')  # <b>
    _untupled_3__a1 = typing.TypeVar('_untupled_3__a1')  # <a1>
    _untupled_3__a2 = typing.TypeVar('_untupled_3__a2')  # <a2>
    _untupled_3__a3 = typing.TypeVar('_untupled_3__a3')  # <a3>
    _untupled_3__a4 = typing.TypeVar('_untupled_3__a4')  # <a4>
    _untupled_3__a5 = typing.TypeVar('_untupled_3__a5')  # <a5>
    _untupled_3__b = typing.TypeVar('_untupled_3__b')  # <b>
    @typing.overload
    @staticmethod
    def untupled(f: 'Function1'['Tuple2'[_untupled_0__a1, _untupled_0__a2], _untupled_0__b]) -> 'Function2'[_untupled_0__a1, _untupled_0__a2, _untupled_0__b]: ...
    @typing.overload
    @staticmethod
    def untupled(f: 'Function1'['Tuple3'[_untupled_1__a1, _untupled_1__a2, _untupled_1__a3], _untupled_1__b]) -> 'Function3'[_untupled_1__a1, _untupled_1__a2, _untupled_1__a3, _untupled_1__b]: ...
    @typing.overload
    @staticmethod
    def untupled(f: 'Function1'['Tuple4'[_untupled_2__a1, _untupled_2__a2, _untupled_2__a3, _untupled_2__a4], _untupled_2__b]) -> 'Function4'[_untupled_2__a1, _untupled_2__a2, _untupled_2__a3, _untupled_2__a4, _untupled_2__b]: ...
    @typing.overload
    @staticmethod
    def untupled(f: 'Function1'['Tuple5'[_untupled_3__a1, _untupled_3__a2, _untupled_3__a3, _untupled_3__a4, _untupled_3__a5], _untupled_3__b]) -> 'Function5'[_untupled_3__a1, _untupled_3__a2, _untupled_3__a3, _untupled_3__a4, _untupled_3__a5, _untupled_3__b]: ...

_Function0__R = typing.TypeVar('_Function0__R')  # <R>
class Function0(typing.Generic[_Function0__R]):
    @staticmethod
    def $init$($this: 'Function0') -> None: ...
    def apply(self) -> _Function0__R: ...
    def apply$mcB$sp(self) -> int: ...
    def apply$mcC$sp(self) -> str: ...
    def apply$mcD$sp(self) -> float: ...
    def apply$mcF$sp(self) -> float: ...
    def apply$mcI$sp(self) -> int: ...
    def apply$mcJ$sp(self) -> int: ...
    def apply$mcS$sp(self) -> int: ...
    def apply$mcV$sp(self) -> None: ...
    def apply$mcZ$sp(self) -> bool: ...
    def toString(self) -> str: ...

_Function1__T1 = typing.TypeVar('_Function1__T1')  # <T1>
_Function1__R = typing.TypeVar('_Function1__R')  # <R>
class Function1(typing.Generic[_Function1__T1, _Function1__R]):
    @staticmethod
    def $init$($this: 'Function1') -> None: ...
    _andThen__A = typing.TypeVar('_andThen__A')  # <A>
    def andThen(self, g: 'Function1'[_Function1__R, _andThen__A]) -> 'Function1'[_Function1__T1, _andThen__A]: ...
    def apply(self, v1: _Function1__T1) -> _Function1__R: ...
    def apply$mcDD$sp(self, v1: float) -> float: ...
    def apply$mcDF$sp(self, v1: float) -> float: ...
    def apply$mcDI$sp(self, v1: int) -> float: ...
    def apply$mcDJ$sp(self, v1: int) -> float: ...
    def apply$mcFD$sp(self, v1: float) -> float: ...
    def apply$mcFF$sp(self, v1: float) -> float: ...
    def apply$mcFI$sp(self, v1: int) -> float: ...
    def apply$mcFJ$sp(self, v1: int) -> float: ...
    def apply$mcID$sp(self, v1: float) -> int: ...
    def apply$mcIF$sp(self, v1: float) -> int: ...
    def apply$mcII$sp(self, v1: int) -> int: ...
    def apply$mcIJ$sp(self, v1: int) -> int: ...
    def apply$mcJD$sp(self, v1: float) -> int: ...
    def apply$mcJF$sp(self, v1: float) -> int: ...
    def apply$mcJI$sp(self, v1: int) -> int: ...
    def apply$mcJJ$sp(self, v1: int) -> int: ...
    def apply$mcVD$sp(self, v1: float) -> None: ...
    def apply$mcVF$sp(self, v1: float) -> None: ...
    def apply$mcVI$sp(self, v1: int) -> None: ...
    def apply$mcVJ$sp(self, v1: int) -> None: ...
    def apply$mcZD$sp(self, v1: float) -> bool: ...
    def apply$mcZF$sp(self, v1: float) -> bool: ...
    def apply$mcZI$sp(self, v1: int) -> bool: ...
    def apply$mcZJ$sp(self, v1: int) -> bool: ...
    _compose__A = typing.TypeVar('_compose__A')  # <A>
    def compose(self, g: 'Function1'[_compose__A, _Function1__T1]) -> 'Function1'[_compose__A, _Function1__R]: ...
    def toString(self) -> str: ...

_Function10__T1 = typing.TypeVar('_Function10__T1')  # <T1>
_Function10__T2 = typing.TypeVar('_Function10__T2')  # <T2>
_Function10__T3 = typing.TypeVar('_Function10__T3')  # <T3>
_Function10__T4 = typing.TypeVar('_Function10__T4')  # <T4>
_Function10__T5 = typing.TypeVar('_Function10__T5')  # <T5>
_Function10__T6 = typing.TypeVar('_Function10__T6')  # <T6>
_Function10__T7 = typing.TypeVar('_Function10__T7')  # <T7>
_Function10__T8 = typing.TypeVar('_Function10__T8')  # <T8>
_Function10__T9 = typing.TypeVar('_Function10__T9')  # <T9>
_Function10__T10 = typing.TypeVar('_Function10__T10')  # <T10>
_Function10__R = typing.TypeVar('_Function10__R')  # <R>
class Function10(typing.Generic[_Function10__T1, _Function10__T2, _Function10__T3, _Function10__T4, _Function10__T5, _Function10__T6, _Function10__T7, _Function10__T8, _Function10__T9, _Function10__T10, _Function10__R]):
    @staticmethod
    def $init$($this: 'Function10') -> None: ...
    def apply(self, v1: _Function10__T1, v2: _Function10__T2, v3: _Function10__T3, v4: _Function10__T4, v5: _Function10__T5, v6: _Function10__T6, v7: _Function10__T7, v8: _Function10__T8, v9: _Function10__T9, v10: _Function10__T10) -> _Function10__R: ...
    def curried(self) -> Function1[_Function10__T1, Function1[_Function10__T2, Function1[_Function10__T3, Function1[_Function10__T4, Function1[_Function10__T5, Function1[_Function10__T6, Function1[_Function10__T7, Function1[_Function10__T8, Function1[_Function10__T9, Function1[_Function10__T10, _Function10__R]]]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple10'[_Function10__T1, _Function10__T2, _Function10__T3, _Function10__T4, _Function10__T5, _Function10__T6, _Function10__T7, _Function10__T8, _Function10__T9, _Function10__T10], _Function10__R]: ...

_Function11__T1 = typing.TypeVar('_Function11__T1')  # <T1>
_Function11__T2 = typing.TypeVar('_Function11__T2')  # <T2>
_Function11__T3 = typing.TypeVar('_Function11__T3')  # <T3>
_Function11__T4 = typing.TypeVar('_Function11__T4')  # <T4>
_Function11__T5 = typing.TypeVar('_Function11__T5')  # <T5>
_Function11__T6 = typing.TypeVar('_Function11__T6')  # <T6>
_Function11__T7 = typing.TypeVar('_Function11__T7')  # <T7>
_Function11__T8 = typing.TypeVar('_Function11__T8')  # <T8>
_Function11__T9 = typing.TypeVar('_Function11__T9')  # <T9>
_Function11__T10 = typing.TypeVar('_Function11__T10')  # <T10>
_Function11__T11 = typing.TypeVar('_Function11__T11')  # <T11>
_Function11__R = typing.TypeVar('_Function11__R')  # <R>
class Function11(typing.Generic[_Function11__T1, _Function11__T2, _Function11__T3, _Function11__T4, _Function11__T5, _Function11__T6, _Function11__T7, _Function11__T8, _Function11__T9, _Function11__T10, _Function11__T11, _Function11__R]):
    @staticmethod
    def $init$($this: 'Function11') -> None: ...
    def apply(self, v1: _Function11__T1, v2: _Function11__T2, v3: _Function11__T3, v4: _Function11__T4, v5: _Function11__T5, v6: _Function11__T6, v7: _Function11__T7, v8: _Function11__T8, v9: _Function11__T9, v10: _Function11__T10, v11: _Function11__T11) -> _Function11__R: ...
    def curried(self) -> Function1[_Function11__T1, Function1[_Function11__T2, Function1[_Function11__T3, Function1[_Function11__T4, Function1[_Function11__T5, Function1[_Function11__T6, Function1[_Function11__T7, Function1[_Function11__T8, Function1[_Function11__T9, Function1[_Function11__T10, Function1[_Function11__T11, _Function11__R]]]]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple11'[_Function11__T1, _Function11__T2, _Function11__T3, _Function11__T4, _Function11__T5, _Function11__T6, _Function11__T7, _Function11__T8, _Function11__T9, _Function11__T10, _Function11__T11], _Function11__R]: ...

_Function12__T1 = typing.TypeVar('_Function12__T1')  # <T1>
_Function12__T2 = typing.TypeVar('_Function12__T2')  # <T2>
_Function12__T3 = typing.TypeVar('_Function12__T3')  # <T3>
_Function12__T4 = typing.TypeVar('_Function12__T4')  # <T4>
_Function12__T5 = typing.TypeVar('_Function12__T5')  # <T5>
_Function12__T6 = typing.TypeVar('_Function12__T6')  # <T6>
_Function12__T7 = typing.TypeVar('_Function12__T7')  # <T7>
_Function12__T8 = typing.TypeVar('_Function12__T8')  # <T8>
_Function12__T9 = typing.TypeVar('_Function12__T9')  # <T9>
_Function12__T10 = typing.TypeVar('_Function12__T10')  # <T10>
_Function12__T11 = typing.TypeVar('_Function12__T11')  # <T11>
_Function12__T12 = typing.TypeVar('_Function12__T12')  # <T12>
_Function12__R = typing.TypeVar('_Function12__R')  # <R>
class Function12(typing.Generic[_Function12__T1, _Function12__T2, _Function12__T3, _Function12__T4, _Function12__T5, _Function12__T6, _Function12__T7, _Function12__T8, _Function12__T9, _Function12__T10, _Function12__T11, _Function12__T12, _Function12__R]):
    @staticmethod
    def $init$($this: 'Function12') -> None: ...
    def apply(self, v1: _Function12__T1, v2: _Function12__T2, v3: _Function12__T3, v4: _Function12__T4, v5: _Function12__T5, v6: _Function12__T6, v7: _Function12__T7, v8: _Function12__T8, v9: _Function12__T9, v10: _Function12__T10, v11: _Function12__T11, v12: _Function12__T12) -> _Function12__R: ...
    def curried(self) -> Function1[_Function12__T1, Function1[_Function12__T2, Function1[_Function12__T3, Function1[_Function12__T4, Function1[_Function12__T5, Function1[_Function12__T6, Function1[_Function12__T7, Function1[_Function12__T8, Function1[_Function12__T9, Function1[_Function12__T10, Function1[_Function12__T11, Function1[_Function12__T12, _Function12__R]]]]]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple12'[_Function12__T1, _Function12__T2, _Function12__T3, _Function12__T4, _Function12__T5, _Function12__T6, _Function12__T7, _Function12__T8, _Function12__T9, _Function12__T10, _Function12__T11, _Function12__T12], _Function12__R]: ...

_Function13__T1 = typing.TypeVar('_Function13__T1')  # <T1>
_Function13__T2 = typing.TypeVar('_Function13__T2')  # <T2>
_Function13__T3 = typing.TypeVar('_Function13__T3')  # <T3>
_Function13__T4 = typing.TypeVar('_Function13__T4')  # <T4>
_Function13__T5 = typing.TypeVar('_Function13__T5')  # <T5>
_Function13__T6 = typing.TypeVar('_Function13__T6')  # <T6>
_Function13__T7 = typing.TypeVar('_Function13__T7')  # <T7>
_Function13__T8 = typing.TypeVar('_Function13__T8')  # <T8>
_Function13__T9 = typing.TypeVar('_Function13__T9')  # <T9>
_Function13__T10 = typing.TypeVar('_Function13__T10')  # <T10>
_Function13__T11 = typing.TypeVar('_Function13__T11')  # <T11>
_Function13__T12 = typing.TypeVar('_Function13__T12')  # <T12>
_Function13__T13 = typing.TypeVar('_Function13__T13')  # <T13>
_Function13__R = typing.TypeVar('_Function13__R')  # <R>
class Function13(typing.Generic[_Function13__T1, _Function13__T2, _Function13__T3, _Function13__T4, _Function13__T5, _Function13__T6, _Function13__T7, _Function13__T8, _Function13__T9, _Function13__T10, _Function13__T11, _Function13__T12, _Function13__T13, _Function13__R]):
    @staticmethod
    def $init$($this: 'Function13') -> None: ...
    def apply(self, v1: _Function13__T1, v2: _Function13__T2, v3: _Function13__T3, v4: _Function13__T4, v5: _Function13__T5, v6: _Function13__T6, v7: _Function13__T7, v8: _Function13__T8, v9: _Function13__T9, v10: _Function13__T10, v11: _Function13__T11, v12: _Function13__T12, v13: _Function13__T13) -> _Function13__R: ...
    def curried(self) -> Function1[_Function13__T1, Function1[_Function13__T2, Function1[_Function13__T3, Function1[_Function13__T4, Function1[_Function13__T5, Function1[_Function13__T6, Function1[_Function13__T7, Function1[_Function13__T8, Function1[_Function13__T9, Function1[_Function13__T10, Function1[_Function13__T11, Function1[_Function13__T12, Function1[_Function13__T13, _Function13__R]]]]]]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple13'[_Function13__T1, _Function13__T2, _Function13__T3, _Function13__T4, _Function13__T5, _Function13__T6, _Function13__T7, _Function13__T8, _Function13__T9, _Function13__T10, _Function13__T11, _Function13__T12, _Function13__T13], _Function13__R]: ...

_Function14__T1 = typing.TypeVar('_Function14__T1')  # <T1>
_Function14__T2 = typing.TypeVar('_Function14__T2')  # <T2>
_Function14__T3 = typing.TypeVar('_Function14__T3')  # <T3>
_Function14__T4 = typing.TypeVar('_Function14__T4')  # <T4>
_Function14__T5 = typing.TypeVar('_Function14__T5')  # <T5>
_Function14__T6 = typing.TypeVar('_Function14__T6')  # <T6>
_Function14__T7 = typing.TypeVar('_Function14__T7')  # <T7>
_Function14__T8 = typing.TypeVar('_Function14__T8')  # <T8>
_Function14__T9 = typing.TypeVar('_Function14__T9')  # <T9>
_Function14__T10 = typing.TypeVar('_Function14__T10')  # <T10>
_Function14__T11 = typing.TypeVar('_Function14__T11')  # <T11>
_Function14__T12 = typing.TypeVar('_Function14__T12')  # <T12>
_Function14__T13 = typing.TypeVar('_Function14__T13')  # <T13>
_Function14__T14 = typing.TypeVar('_Function14__T14')  # <T14>
_Function14__R = typing.TypeVar('_Function14__R')  # <R>
class Function14(typing.Generic[_Function14__T1, _Function14__T2, _Function14__T3, _Function14__T4, _Function14__T5, _Function14__T6, _Function14__T7, _Function14__T8, _Function14__T9, _Function14__T10, _Function14__T11, _Function14__T12, _Function14__T13, _Function14__T14, _Function14__R]):
    @staticmethod
    def $init$($this: 'Function14') -> None: ...
    def apply(self, v1: _Function14__T1, v2: _Function14__T2, v3: _Function14__T3, v4: _Function14__T4, v5: _Function14__T5, v6: _Function14__T6, v7: _Function14__T7, v8: _Function14__T8, v9: _Function14__T9, v10: _Function14__T10, v11: _Function14__T11, v12: _Function14__T12, v13: _Function14__T13, v14: _Function14__T14) -> _Function14__R: ...
    def curried(self) -> Function1[_Function14__T1, Function1[_Function14__T2, Function1[_Function14__T3, Function1[_Function14__T4, Function1[_Function14__T5, Function1[_Function14__T6, Function1[_Function14__T7, Function1[_Function14__T8, Function1[_Function14__T9, Function1[_Function14__T10, Function1[_Function14__T11, Function1[_Function14__T12, Function1[_Function14__T13, Function1[_Function14__T14, _Function14__R]]]]]]]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple14'[_Function14__T1, _Function14__T2, _Function14__T3, _Function14__T4, _Function14__T5, _Function14__T6, _Function14__T7, _Function14__T8, _Function14__T9, _Function14__T10, _Function14__T11, _Function14__T12, _Function14__T13, _Function14__T14], _Function14__R]: ...

_Function15__T1 = typing.TypeVar('_Function15__T1')  # <T1>
_Function15__T2 = typing.TypeVar('_Function15__T2')  # <T2>
_Function15__T3 = typing.TypeVar('_Function15__T3')  # <T3>
_Function15__T4 = typing.TypeVar('_Function15__T4')  # <T4>
_Function15__T5 = typing.TypeVar('_Function15__T5')  # <T5>
_Function15__T6 = typing.TypeVar('_Function15__T6')  # <T6>
_Function15__T7 = typing.TypeVar('_Function15__T7')  # <T7>
_Function15__T8 = typing.TypeVar('_Function15__T8')  # <T8>
_Function15__T9 = typing.TypeVar('_Function15__T9')  # <T9>
_Function15__T10 = typing.TypeVar('_Function15__T10')  # <T10>
_Function15__T11 = typing.TypeVar('_Function15__T11')  # <T11>
_Function15__T12 = typing.TypeVar('_Function15__T12')  # <T12>
_Function15__T13 = typing.TypeVar('_Function15__T13')  # <T13>
_Function15__T14 = typing.TypeVar('_Function15__T14')  # <T14>
_Function15__T15 = typing.TypeVar('_Function15__T15')  # <T15>
_Function15__R = typing.TypeVar('_Function15__R')  # <R>
class Function15(typing.Generic[_Function15__T1, _Function15__T2, _Function15__T3, _Function15__T4, _Function15__T5, _Function15__T6, _Function15__T7, _Function15__T8, _Function15__T9, _Function15__T10, _Function15__T11, _Function15__T12, _Function15__T13, _Function15__T14, _Function15__T15, _Function15__R]):
    @staticmethod
    def $init$($this: 'Function15') -> None: ...
    def apply(self, v1: _Function15__T1, v2: _Function15__T2, v3: _Function15__T3, v4: _Function15__T4, v5: _Function15__T5, v6: _Function15__T6, v7: _Function15__T7, v8: _Function15__T8, v9: _Function15__T9, v10: _Function15__T10, v11: _Function15__T11, v12: _Function15__T12, v13: _Function15__T13, v14: _Function15__T14, v15: _Function15__T15) -> _Function15__R: ...
    def curried(self) -> Function1[_Function15__T1, Function1[_Function15__T2, Function1[_Function15__T3, Function1[_Function15__T4, Function1[_Function15__T5, Function1[_Function15__T6, Function1[_Function15__T7, Function1[_Function15__T8, Function1[_Function15__T9, Function1[_Function15__T10, Function1[_Function15__T11, Function1[_Function15__T12, Function1[_Function15__T13, Function1[_Function15__T14, Function1[_Function15__T15, _Function15__R]]]]]]]]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple15'[_Function15__T1, _Function15__T2, _Function15__T3, _Function15__T4, _Function15__T5, _Function15__T6, _Function15__T7, _Function15__T8, _Function15__T9, _Function15__T10, _Function15__T11, _Function15__T12, _Function15__T13, _Function15__T14, _Function15__T15], _Function15__R]: ...

_Function16__T1 = typing.TypeVar('_Function16__T1')  # <T1>
_Function16__T2 = typing.TypeVar('_Function16__T2')  # <T2>
_Function16__T3 = typing.TypeVar('_Function16__T3')  # <T3>
_Function16__T4 = typing.TypeVar('_Function16__T4')  # <T4>
_Function16__T5 = typing.TypeVar('_Function16__T5')  # <T5>
_Function16__T6 = typing.TypeVar('_Function16__T6')  # <T6>
_Function16__T7 = typing.TypeVar('_Function16__T7')  # <T7>
_Function16__T8 = typing.TypeVar('_Function16__T8')  # <T8>
_Function16__T9 = typing.TypeVar('_Function16__T9')  # <T9>
_Function16__T10 = typing.TypeVar('_Function16__T10')  # <T10>
_Function16__T11 = typing.TypeVar('_Function16__T11')  # <T11>
_Function16__T12 = typing.TypeVar('_Function16__T12')  # <T12>
_Function16__T13 = typing.TypeVar('_Function16__T13')  # <T13>
_Function16__T14 = typing.TypeVar('_Function16__T14')  # <T14>
_Function16__T15 = typing.TypeVar('_Function16__T15')  # <T15>
_Function16__T16 = typing.TypeVar('_Function16__T16')  # <T16>
_Function16__R = typing.TypeVar('_Function16__R')  # <R>
class Function16(typing.Generic[_Function16__T1, _Function16__T2, _Function16__T3, _Function16__T4, _Function16__T5, _Function16__T6, _Function16__T7, _Function16__T8, _Function16__T9, _Function16__T10, _Function16__T11, _Function16__T12, _Function16__T13, _Function16__T14, _Function16__T15, _Function16__T16, _Function16__R]):
    @staticmethod
    def $init$($this: 'Function16') -> None: ...
    def apply(self, v1: _Function16__T1, v2: _Function16__T2, v3: _Function16__T3, v4: _Function16__T4, v5: _Function16__T5, v6: _Function16__T6, v7: _Function16__T7, v8: _Function16__T8, v9: _Function16__T9, v10: _Function16__T10, v11: _Function16__T11, v12: _Function16__T12, v13: _Function16__T13, v14: _Function16__T14, v15: _Function16__T15, v16: _Function16__T16) -> _Function16__R: ...
    def curried(self) -> Function1[_Function16__T1, Function1[_Function16__T2, Function1[_Function16__T3, Function1[_Function16__T4, Function1[_Function16__T5, Function1[_Function16__T6, Function1[_Function16__T7, Function1[_Function16__T8, Function1[_Function16__T9, Function1[_Function16__T10, Function1[_Function16__T11, Function1[_Function16__T12, Function1[_Function16__T13, Function1[_Function16__T14, Function1[_Function16__T15, Function1[_Function16__T16, _Function16__R]]]]]]]]]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple16'[_Function16__T1, _Function16__T2, _Function16__T3, _Function16__T4, _Function16__T5, _Function16__T6, _Function16__T7, _Function16__T8, _Function16__T9, _Function16__T10, _Function16__T11, _Function16__T12, _Function16__T13, _Function16__T14, _Function16__T15, _Function16__T16], _Function16__R]: ...

_Function17__T1 = typing.TypeVar('_Function17__T1')  # <T1>
_Function17__T2 = typing.TypeVar('_Function17__T2')  # <T2>
_Function17__T3 = typing.TypeVar('_Function17__T3')  # <T3>
_Function17__T4 = typing.TypeVar('_Function17__T4')  # <T4>
_Function17__T5 = typing.TypeVar('_Function17__T5')  # <T5>
_Function17__T6 = typing.TypeVar('_Function17__T6')  # <T6>
_Function17__T7 = typing.TypeVar('_Function17__T7')  # <T7>
_Function17__T8 = typing.TypeVar('_Function17__T8')  # <T8>
_Function17__T9 = typing.TypeVar('_Function17__T9')  # <T9>
_Function17__T10 = typing.TypeVar('_Function17__T10')  # <T10>
_Function17__T11 = typing.TypeVar('_Function17__T11')  # <T11>
_Function17__T12 = typing.TypeVar('_Function17__T12')  # <T12>
_Function17__T13 = typing.TypeVar('_Function17__T13')  # <T13>
_Function17__T14 = typing.TypeVar('_Function17__T14')  # <T14>
_Function17__T15 = typing.TypeVar('_Function17__T15')  # <T15>
_Function17__T16 = typing.TypeVar('_Function17__T16')  # <T16>
_Function17__T17 = typing.TypeVar('_Function17__T17')  # <T17>
_Function17__R = typing.TypeVar('_Function17__R')  # <R>
class Function17(typing.Generic[_Function17__T1, _Function17__T2, _Function17__T3, _Function17__T4, _Function17__T5, _Function17__T6, _Function17__T7, _Function17__T8, _Function17__T9, _Function17__T10, _Function17__T11, _Function17__T12, _Function17__T13, _Function17__T14, _Function17__T15, _Function17__T16, _Function17__T17, _Function17__R]):
    @staticmethod
    def $init$($this: 'Function17') -> None: ...
    def apply(self, v1: _Function17__T1, v2: _Function17__T2, v3: _Function17__T3, v4: _Function17__T4, v5: _Function17__T5, v6: _Function17__T6, v7: _Function17__T7, v8: _Function17__T8, v9: _Function17__T9, v10: _Function17__T10, v11: _Function17__T11, v12: _Function17__T12, v13: _Function17__T13, v14: _Function17__T14, v15: _Function17__T15, v16: _Function17__T16, v17: _Function17__T17) -> _Function17__R: ...
    def curried(self) -> Function1[_Function17__T1, Function1[_Function17__T2, Function1[_Function17__T3, Function1[_Function17__T4, Function1[_Function17__T5, Function1[_Function17__T6, Function1[_Function17__T7, Function1[_Function17__T8, Function1[_Function17__T9, Function1[_Function17__T10, Function1[_Function17__T11, Function1[_Function17__T12, Function1[_Function17__T13, Function1[_Function17__T14, Function1[_Function17__T15, Function1[_Function17__T16, Function1[_Function17__T17, _Function17__R]]]]]]]]]]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple17'[_Function17__T1, _Function17__T2, _Function17__T3, _Function17__T4, _Function17__T5, _Function17__T6, _Function17__T7, _Function17__T8, _Function17__T9, _Function17__T10, _Function17__T11, _Function17__T12, _Function17__T13, _Function17__T14, _Function17__T15, _Function17__T16, _Function17__T17], _Function17__R]: ...

_Function18__T1 = typing.TypeVar('_Function18__T1')  # <T1>
_Function18__T2 = typing.TypeVar('_Function18__T2')  # <T2>
_Function18__T3 = typing.TypeVar('_Function18__T3')  # <T3>
_Function18__T4 = typing.TypeVar('_Function18__T4')  # <T4>
_Function18__T5 = typing.TypeVar('_Function18__T5')  # <T5>
_Function18__T6 = typing.TypeVar('_Function18__T6')  # <T6>
_Function18__T7 = typing.TypeVar('_Function18__T7')  # <T7>
_Function18__T8 = typing.TypeVar('_Function18__T8')  # <T8>
_Function18__T9 = typing.TypeVar('_Function18__T9')  # <T9>
_Function18__T10 = typing.TypeVar('_Function18__T10')  # <T10>
_Function18__T11 = typing.TypeVar('_Function18__T11')  # <T11>
_Function18__T12 = typing.TypeVar('_Function18__T12')  # <T12>
_Function18__T13 = typing.TypeVar('_Function18__T13')  # <T13>
_Function18__T14 = typing.TypeVar('_Function18__T14')  # <T14>
_Function18__T15 = typing.TypeVar('_Function18__T15')  # <T15>
_Function18__T16 = typing.TypeVar('_Function18__T16')  # <T16>
_Function18__T17 = typing.TypeVar('_Function18__T17')  # <T17>
_Function18__T18 = typing.TypeVar('_Function18__T18')  # <T18>
_Function18__R = typing.TypeVar('_Function18__R')  # <R>
class Function18(typing.Generic[_Function18__T1, _Function18__T2, _Function18__T3, _Function18__T4, _Function18__T5, _Function18__T6, _Function18__T7, _Function18__T8, _Function18__T9, _Function18__T10, _Function18__T11, _Function18__T12, _Function18__T13, _Function18__T14, _Function18__T15, _Function18__T16, _Function18__T17, _Function18__T18, _Function18__R]):
    @staticmethod
    def $init$($this: 'Function18') -> None: ...
    def apply(self, v1: _Function18__T1, v2: _Function18__T2, v3: _Function18__T3, v4: _Function18__T4, v5: _Function18__T5, v6: _Function18__T6, v7: _Function18__T7, v8: _Function18__T8, v9: _Function18__T9, v10: _Function18__T10, v11: _Function18__T11, v12: _Function18__T12, v13: _Function18__T13, v14: _Function18__T14, v15: _Function18__T15, v16: _Function18__T16, v17: _Function18__T17, v18: _Function18__T18) -> _Function18__R: ...
    def curried(self) -> Function1[_Function18__T1, Function1[_Function18__T2, Function1[_Function18__T3, Function1[_Function18__T4, Function1[_Function18__T5, Function1[_Function18__T6, Function1[_Function18__T7, Function1[_Function18__T8, Function1[_Function18__T9, Function1[_Function18__T10, Function1[_Function18__T11, Function1[_Function18__T12, Function1[_Function18__T13, Function1[_Function18__T14, Function1[_Function18__T15, Function1[_Function18__T16, Function1[_Function18__T17, Function1[_Function18__T18, _Function18__R]]]]]]]]]]]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple18'[_Function18__T1, _Function18__T2, _Function18__T3, _Function18__T4, _Function18__T5, _Function18__T6, _Function18__T7, _Function18__T8, _Function18__T9, _Function18__T10, _Function18__T11, _Function18__T12, _Function18__T13, _Function18__T14, _Function18__T15, _Function18__T16, _Function18__T17, _Function18__T18], _Function18__R]: ...

_Function19__T1 = typing.TypeVar('_Function19__T1')  # <T1>
_Function19__T2 = typing.TypeVar('_Function19__T2')  # <T2>
_Function19__T3 = typing.TypeVar('_Function19__T3')  # <T3>
_Function19__T4 = typing.TypeVar('_Function19__T4')  # <T4>
_Function19__T5 = typing.TypeVar('_Function19__T5')  # <T5>
_Function19__T6 = typing.TypeVar('_Function19__T6')  # <T6>
_Function19__T7 = typing.TypeVar('_Function19__T7')  # <T7>
_Function19__T8 = typing.TypeVar('_Function19__T8')  # <T8>
_Function19__T9 = typing.TypeVar('_Function19__T9')  # <T9>
_Function19__T10 = typing.TypeVar('_Function19__T10')  # <T10>
_Function19__T11 = typing.TypeVar('_Function19__T11')  # <T11>
_Function19__T12 = typing.TypeVar('_Function19__T12')  # <T12>
_Function19__T13 = typing.TypeVar('_Function19__T13')  # <T13>
_Function19__T14 = typing.TypeVar('_Function19__T14')  # <T14>
_Function19__T15 = typing.TypeVar('_Function19__T15')  # <T15>
_Function19__T16 = typing.TypeVar('_Function19__T16')  # <T16>
_Function19__T17 = typing.TypeVar('_Function19__T17')  # <T17>
_Function19__T18 = typing.TypeVar('_Function19__T18')  # <T18>
_Function19__T19 = typing.TypeVar('_Function19__T19')  # <T19>
_Function19__R = typing.TypeVar('_Function19__R')  # <R>
class Function19(typing.Generic[_Function19__T1, _Function19__T2, _Function19__T3, _Function19__T4, _Function19__T5, _Function19__T6, _Function19__T7, _Function19__T8, _Function19__T9, _Function19__T10, _Function19__T11, _Function19__T12, _Function19__T13, _Function19__T14, _Function19__T15, _Function19__T16, _Function19__T17, _Function19__T18, _Function19__T19, _Function19__R]):
    @staticmethod
    def $init$($this: 'Function19') -> None: ...
    def apply(self, v1: _Function19__T1, v2: _Function19__T2, v3: _Function19__T3, v4: _Function19__T4, v5: _Function19__T5, v6: _Function19__T6, v7: _Function19__T7, v8: _Function19__T8, v9: _Function19__T9, v10: _Function19__T10, v11: _Function19__T11, v12: _Function19__T12, v13: _Function19__T13, v14: _Function19__T14, v15: _Function19__T15, v16: _Function19__T16, v17: _Function19__T17, v18: _Function19__T18, v19: _Function19__T19) -> _Function19__R: ...
    def curried(self) -> Function1[_Function19__T1, Function1[_Function19__T2, Function1[_Function19__T3, Function1[_Function19__T4, Function1[_Function19__T5, Function1[_Function19__T6, Function1[_Function19__T7, Function1[_Function19__T8, Function1[_Function19__T9, Function1[_Function19__T10, Function1[_Function19__T11, Function1[_Function19__T12, Function1[_Function19__T13, Function1[_Function19__T14, Function1[_Function19__T15, Function1[_Function19__T16, Function1[_Function19__T17, Function1[_Function19__T18, Function1[_Function19__T19, _Function19__R]]]]]]]]]]]]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple19'[_Function19__T1, _Function19__T2, _Function19__T3, _Function19__T4, _Function19__T5, _Function19__T6, _Function19__T7, _Function19__T8, _Function19__T9, _Function19__T10, _Function19__T11, _Function19__T12, _Function19__T13, _Function19__T14, _Function19__T15, _Function19__T16, _Function19__T17, _Function19__T18, _Function19__T19], _Function19__R]: ...

_Function2__T1 = typing.TypeVar('_Function2__T1')  # <T1>
_Function2__T2 = typing.TypeVar('_Function2__T2')  # <T2>
_Function2__R = typing.TypeVar('_Function2__R')  # <R>
class Function2(typing.Generic[_Function2__T1, _Function2__T2, _Function2__R]):
    @staticmethod
    def $init$($this: 'Function2') -> None: ...
    def apply(self, v1: _Function2__T1, v2: _Function2__T2) -> _Function2__R: ...
    def apply$mcDDD$sp(self, v1: float, v2: float) -> float: ...
    def apply$mcDDI$sp(self, v1: float, v2: int) -> float: ...
    def apply$mcDDJ$sp(self, v1: float, v2: int) -> float: ...
    def apply$mcDID$sp(self, v1: int, v2: float) -> float: ...
    def apply$mcDII$sp(self, v1: int, v2: int) -> float: ...
    def apply$mcDIJ$sp(self, v1: int, v2: int) -> float: ...
    def apply$mcDJD$sp(self, v1: int, v2: float) -> float: ...
    def apply$mcDJI$sp(self, v1: int, v2: int) -> float: ...
    def apply$mcDJJ$sp(self, v1: int, v2: int) -> float: ...
    def apply$mcFDD$sp(self, v1: float, v2: float) -> float: ...
    def apply$mcFDI$sp(self, v1: float, v2: int) -> float: ...
    def apply$mcFDJ$sp(self, v1: float, v2: int) -> float: ...
    def apply$mcFID$sp(self, v1: int, v2: float) -> float: ...
    def apply$mcFII$sp(self, v1: int, v2: int) -> float: ...
    def apply$mcFIJ$sp(self, v1: int, v2: int) -> float: ...
    def apply$mcFJD$sp(self, v1: int, v2: float) -> float: ...
    def apply$mcFJI$sp(self, v1: int, v2: int) -> float: ...
    def apply$mcFJJ$sp(self, v1: int, v2: int) -> float: ...
    def apply$mcIDD$sp(self, v1: float, v2: float) -> int: ...
    def apply$mcIDI$sp(self, v1: float, v2: int) -> int: ...
    def apply$mcIDJ$sp(self, v1: float, v2: int) -> int: ...
    def apply$mcIID$sp(self, v1: int, v2: float) -> int: ...
    def apply$mcIII$sp(self, v1: int, v2: int) -> int: ...
    def apply$mcIIJ$sp(self, v1: int, v2: int) -> int: ...
    def apply$mcIJD$sp(self, v1: int, v2: float) -> int: ...
    def apply$mcIJI$sp(self, v1: int, v2: int) -> int: ...
    def apply$mcIJJ$sp(self, v1: int, v2: int) -> int: ...
    def apply$mcJDD$sp(self, v1: float, v2: float) -> int: ...
    def apply$mcJDI$sp(self, v1: float, v2: int) -> int: ...
    def apply$mcJDJ$sp(self, v1: float, v2: int) -> int: ...
    def apply$mcJID$sp(self, v1: int, v2: float) -> int: ...
    def apply$mcJII$sp(self, v1: int, v2: int) -> int: ...
    def apply$mcJIJ$sp(self, v1: int, v2: int) -> int: ...
    def apply$mcJJD$sp(self, v1: int, v2: float) -> int: ...
    def apply$mcJJI$sp(self, v1: int, v2: int) -> int: ...
    def apply$mcJJJ$sp(self, v1: int, v2: int) -> int: ...
    def apply$mcVDD$sp(self, v1: float, v2: float) -> None: ...
    def apply$mcVDI$sp(self, v1: float, v2: int) -> None: ...
    def apply$mcVDJ$sp(self, v1: float, v2: int) -> None: ...
    def apply$mcVID$sp(self, v1: int, v2: float) -> None: ...
    def apply$mcVII$sp(self, v1: int, v2: int) -> None: ...
    def apply$mcVIJ$sp(self, v1: int, v2: int) -> None: ...
    def apply$mcVJD$sp(self, v1: int, v2: float) -> None: ...
    def apply$mcVJI$sp(self, v1: int, v2: int) -> None: ...
    def apply$mcVJJ$sp(self, v1: int, v2: int) -> None: ...
    def apply$mcZDD$sp(self, v1: float, v2: float) -> bool: ...
    def apply$mcZDI$sp(self, v1: float, v2: int) -> bool: ...
    def apply$mcZDJ$sp(self, v1: float, v2: int) -> bool: ...
    def apply$mcZID$sp(self, v1: int, v2: float) -> bool: ...
    def apply$mcZII$sp(self, v1: int, v2: int) -> bool: ...
    def apply$mcZIJ$sp(self, v1: int, v2: int) -> bool: ...
    def apply$mcZJD$sp(self, v1: int, v2: float) -> bool: ...
    def apply$mcZJI$sp(self, v1: int, v2: int) -> bool: ...
    def apply$mcZJJ$sp(self, v1: int, v2: int) -> bool: ...
    def curried(self) -> Function1[_Function2__T1, Function1[_Function2__T2, _Function2__R]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple2'[_Function2__T1, _Function2__T2], _Function2__R]: ...

_Function20__T1 = typing.TypeVar('_Function20__T1')  # <T1>
_Function20__T2 = typing.TypeVar('_Function20__T2')  # <T2>
_Function20__T3 = typing.TypeVar('_Function20__T3')  # <T3>
_Function20__T4 = typing.TypeVar('_Function20__T4')  # <T4>
_Function20__T5 = typing.TypeVar('_Function20__T5')  # <T5>
_Function20__T6 = typing.TypeVar('_Function20__T6')  # <T6>
_Function20__T7 = typing.TypeVar('_Function20__T7')  # <T7>
_Function20__T8 = typing.TypeVar('_Function20__T8')  # <T8>
_Function20__T9 = typing.TypeVar('_Function20__T9')  # <T9>
_Function20__T10 = typing.TypeVar('_Function20__T10')  # <T10>
_Function20__T11 = typing.TypeVar('_Function20__T11')  # <T11>
_Function20__T12 = typing.TypeVar('_Function20__T12')  # <T12>
_Function20__T13 = typing.TypeVar('_Function20__T13')  # <T13>
_Function20__T14 = typing.TypeVar('_Function20__T14')  # <T14>
_Function20__T15 = typing.TypeVar('_Function20__T15')  # <T15>
_Function20__T16 = typing.TypeVar('_Function20__T16')  # <T16>
_Function20__T17 = typing.TypeVar('_Function20__T17')  # <T17>
_Function20__T18 = typing.TypeVar('_Function20__T18')  # <T18>
_Function20__T19 = typing.TypeVar('_Function20__T19')  # <T19>
_Function20__T20 = typing.TypeVar('_Function20__T20')  # <T20>
_Function20__R = typing.TypeVar('_Function20__R')  # <R>
class Function20(typing.Generic[_Function20__T1, _Function20__T2, _Function20__T3, _Function20__T4, _Function20__T5, _Function20__T6, _Function20__T7, _Function20__T8, _Function20__T9, _Function20__T10, _Function20__T11, _Function20__T12, _Function20__T13, _Function20__T14, _Function20__T15, _Function20__T16, _Function20__T17, _Function20__T18, _Function20__T19, _Function20__T20, _Function20__R]):
    @staticmethod
    def $init$($this: 'Function20') -> None: ...
    def apply(self, v1: _Function20__T1, v2: _Function20__T2, v3: _Function20__T3, v4: _Function20__T4, v5: _Function20__T5, v6: _Function20__T6, v7: _Function20__T7, v8: _Function20__T8, v9: _Function20__T9, v10: _Function20__T10, v11: _Function20__T11, v12: _Function20__T12, v13: _Function20__T13, v14: _Function20__T14, v15: _Function20__T15, v16: _Function20__T16, v17: _Function20__T17, v18: _Function20__T18, v19: _Function20__T19, v20: _Function20__T20) -> _Function20__R: ...
    def curried(self) -> Function1[_Function20__T1, Function1[_Function20__T2, Function1[_Function20__T3, Function1[_Function20__T4, Function1[_Function20__T5, Function1[_Function20__T6, Function1[_Function20__T7, Function1[_Function20__T8, Function1[_Function20__T9, Function1[_Function20__T10, Function1[_Function20__T11, Function1[_Function20__T12, Function1[_Function20__T13, Function1[_Function20__T14, Function1[_Function20__T15, Function1[_Function20__T16, Function1[_Function20__T17, Function1[_Function20__T18, Function1[_Function20__T19, Function1[_Function20__T20, _Function20__R]]]]]]]]]]]]]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple20'[_Function20__T1, _Function20__T2, _Function20__T3, _Function20__T4, _Function20__T5, _Function20__T6, _Function20__T7, _Function20__T8, _Function20__T9, _Function20__T10, _Function20__T11, _Function20__T12, _Function20__T13, _Function20__T14, _Function20__T15, _Function20__T16, _Function20__T17, _Function20__T18, _Function20__T19, _Function20__T20], _Function20__R]: ...

_Function21__T1 = typing.TypeVar('_Function21__T1')  # <T1>
_Function21__T2 = typing.TypeVar('_Function21__T2')  # <T2>
_Function21__T3 = typing.TypeVar('_Function21__T3')  # <T3>
_Function21__T4 = typing.TypeVar('_Function21__T4')  # <T4>
_Function21__T5 = typing.TypeVar('_Function21__T5')  # <T5>
_Function21__T6 = typing.TypeVar('_Function21__T6')  # <T6>
_Function21__T7 = typing.TypeVar('_Function21__T7')  # <T7>
_Function21__T8 = typing.TypeVar('_Function21__T8')  # <T8>
_Function21__T9 = typing.TypeVar('_Function21__T9')  # <T9>
_Function21__T10 = typing.TypeVar('_Function21__T10')  # <T10>
_Function21__T11 = typing.TypeVar('_Function21__T11')  # <T11>
_Function21__T12 = typing.TypeVar('_Function21__T12')  # <T12>
_Function21__T13 = typing.TypeVar('_Function21__T13')  # <T13>
_Function21__T14 = typing.TypeVar('_Function21__T14')  # <T14>
_Function21__T15 = typing.TypeVar('_Function21__T15')  # <T15>
_Function21__T16 = typing.TypeVar('_Function21__T16')  # <T16>
_Function21__T17 = typing.TypeVar('_Function21__T17')  # <T17>
_Function21__T18 = typing.TypeVar('_Function21__T18')  # <T18>
_Function21__T19 = typing.TypeVar('_Function21__T19')  # <T19>
_Function21__T20 = typing.TypeVar('_Function21__T20')  # <T20>
_Function21__T21 = typing.TypeVar('_Function21__T21')  # <T21>
_Function21__R = typing.TypeVar('_Function21__R')  # <R>
class Function21(typing.Generic[_Function21__T1, _Function21__T2, _Function21__T3, _Function21__T4, _Function21__T5, _Function21__T6, _Function21__T7, _Function21__T8, _Function21__T9, _Function21__T10, _Function21__T11, _Function21__T12, _Function21__T13, _Function21__T14, _Function21__T15, _Function21__T16, _Function21__T17, _Function21__T18, _Function21__T19, _Function21__T20, _Function21__T21, _Function21__R]):
    @staticmethod
    def $init$($this: 'Function21') -> None: ...
    def apply(self, v1: _Function21__T1, v2: _Function21__T2, v3: _Function21__T3, v4: _Function21__T4, v5: _Function21__T5, v6: _Function21__T6, v7: _Function21__T7, v8: _Function21__T8, v9: _Function21__T9, v10: _Function21__T10, v11: _Function21__T11, v12: _Function21__T12, v13: _Function21__T13, v14: _Function21__T14, v15: _Function21__T15, v16: _Function21__T16, v17: _Function21__T17, v18: _Function21__T18, v19: _Function21__T19, v20: _Function21__T20, v21: _Function21__T21) -> _Function21__R: ...
    def curried(self) -> Function1[_Function21__T1, Function1[_Function21__T2, Function1[_Function21__T3, Function1[_Function21__T4, Function1[_Function21__T5, Function1[_Function21__T6, Function1[_Function21__T7, Function1[_Function21__T8, Function1[_Function21__T9, Function1[_Function21__T10, Function1[_Function21__T11, Function1[_Function21__T12, Function1[_Function21__T13, Function1[_Function21__T14, Function1[_Function21__T15, Function1[_Function21__T16, Function1[_Function21__T17, Function1[_Function21__T18, Function1[_Function21__T19, Function1[_Function21__T20, Function1[_Function21__T21, _Function21__R]]]]]]]]]]]]]]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple21'[_Function21__T1, _Function21__T2, _Function21__T3, _Function21__T4, _Function21__T5, _Function21__T6, _Function21__T7, _Function21__T8, _Function21__T9, _Function21__T10, _Function21__T11, _Function21__T12, _Function21__T13, _Function21__T14, _Function21__T15, _Function21__T16, _Function21__T17, _Function21__T18, _Function21__T19, _Function21__T20, _Function21__T21], _Function21__R]: ...

_Function22__T1 = typing.TypeVar('_Function22__T1')  # <T1>
_Function22__T2 = typing.TypeVar('_Function22__T2')  # <T2>
_Function22__T3 = typing.TypeVar('_Function22__T3')  # <T3>
_Function22__T4 = typing.TypeVar('_Function22__T4')  # <T4>
_Function22__T5 = typing.TypeVar('_Function22__T5')  # <T5>
_Function22__T6 = typing.TypeVar('_Function22__T6')  # <T6>
_Function22__T7 = typing.TypeVar('_Function22__T7')  # <T7>
_Function22__T8 = typing.TypeVar('_Function22__T8')  # <T8>
_Function22__T9 = typing.TypeVar('_Function22__T9')  # <T9>
_Function22__T10 = typing.TypeVar('_Function22__T10')  # <T10>
_Function22__T11 = typing.TypeVar('_Function22__T11')  # <T11>
_Function22__T12 = typing.TypeVar('_Function22__T12')  # <T12>
_Function22__T13 = typing.TypeVar('_Function22__T13')  # <T13>
_Function22__T14 = typing.TypeVar('_Function22__T14')  # <T14>
_Function22__T15 = typing.TypeVar('_Function22__T15')  # <T15>
_Function22__T16 = typing.TypeVar('_Function22__T16')  # <T16>
_Function22__T17 = typing.TypeVar('_Function22__T17')  # <T17>
_Function22__T18 = typing.TypeVar('_Function22__T18')  # <T18>
_Function22__T19 = typing.TypeVar('_Function22__T19')  # <T19>
_Function22__T20 = typing.TypeVar('_Function22__T20')  # <T20>
_Function22__T21 = typing.TypeVar('_Function22__T21')  # <T21>
_Function22__T22 = typing.TypeVar('_Function22__T22')  # <T22>
_Function22__R = typing.TypeVar('_Function22__R')  # <R>
class Function22(typing.Generic[_Function22__T1, _Function22__T2, _Function22__T3, _Function22__T4, _Function22__T5, _Function22__T6, _Function22__T7, _Function22__T8, _Function22__T9, _Function22__T10, _Function22__T11, _Function22__T12, _Function22__T13, _Function22__T14, _Function22__T15, _Function22__T16, _Function22__T17, _Function22__T18, _Function22__T19, _Function22__T20, _Function22__T21, _Function22__T22, _Function22__R]):
    @staticmethod
    def $init$($this: 'Function22') -> None: ...
    def apply(self, v1: _Function22__T1, v2: _Function22__T2, v3: _Function22__T3, v4: _Function22__T4, v5: _Function22__T5, v6: _Function22__T6, v7: _Function22__T7, v8: _Function22__T8, v9: _Function22__T9, v10: _Function22__T10, v11: _Function22__T11, v12: _Function22__T12, v13: _Function22__T13, v14: _Function22__T14, v15: _Function22__T15, v16: _Function22__T16, v17: _Function22__T17, v18: _Function22__T18, v19: _Function22__T19, v20: _Function22__T20, v21: _Function22__T21, v22: _Function22__T22) -> _Function22__R: ...
    def curried(self) -> Function1[_Function22__T1, Function1[_Function22__T2, Function1[_Function22__T3, Function1[_Function22__T4, Function1[_Function22__T5, Function1[_Function22__T6, Function1[_Function22__T7, Function1[_Function22__T8, Function1[_Function22__T9, Function1[_Function22__T10, Function1[_Function22__T11, Function1[_Function22__T12, Function1[_Function22__T13, Function1[_Function22__T14, Function1[_Function22__T15, Function1[_Function22__T16, Function1[_Function22__T17, Function1[_Function22__T18, Function1[_Function22__T19, Function1[_Function22__T20, Function1[_Function22__T21, Function1[_Function22__T22, _Function22__R]]]]]]]]]]]]]]]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple22'[_Function22__T1, _Function22__T2, _Function22__T3, _Function22__T4, _Function22__T5, _Function22__T6, _Function22__T7, _Function22__T8, _Function22__T9, _Function22__T10, _Function22__T11, _Function22__T12, _Function22__T13, _Function22__T14, _Function22__T15, _Function22__T16, _Function22__T17, _Function22__T18, _Function22__T19, _Function22__T20, _Function22__T21, _Function22__T22], _Function22__R]: ...

_Function3__T1 = typing.TypeVar('_Function3__T1')  # <T1>
_Function3__T2 = typing.TypeVar('_Function3__T2')  # <T2>
_Function3__T3 = typing.TypeVar('_Function3__T3')  # <T3>
_Function3__R = typing.TypeVar('_Function3__R')  # <R>
class Function3(typing.Generic[_Function3__T1, _Function3__T2, _Function3__T3, _Function3__R]):
    @staticmethod
    def $init$($this: 'Function3') -> None: ...
    def apply(self, v1: _Function3__T1, v2: _Function3__T2, v3: _Function3__T3) -> _Function3__R: ...
    def curried(self) -> Function1[_Function3__T1, Function1[_Function3__T2, Function1[_Function3__T3, _Function3__R]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple3'[_Function3__T1, _Function3__T2, _Function3__T3], _Function3__R]: ...

_Function4__T1 = typing.TypeVar('_Function4__T1')  # <T1>
_Function4__T2 = typing.TypeVar('_Function4__T2')  # <T2>
_Function4__T3 = typing.TypeVar('_Function4__T3')  # <T3>
_Function4__T4 = typing.TypeVar('_Function4__T4')  # <T4>
_Function4__R = typing.TypeVar('_Function4__R')  # <R>
class Function4(typing.Generic[_Function4__T1, _Function4__T2, _Function4__T3, _Function4__T4, _Function4__R]):
    @staticmethod
    def $init$($this: 'Function4') -> None: ...
    def apply(self, v1: _Function4__T1, v2: _Function4__T2, v3: _Function4__T3, v4: _Function4__T4) -> _Function4__R: ...
    def curried(self) -> Function1[_Function4__T1, Function1[_Function4__T2, Function1[_Function4__T3, Function1[_Function4__T4, _Function4__R]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple4'[_Function4__T1, _Function4__T2, _Function4__T3, _Function4__T4], _Function4__R]: ...

_Function5__T1 = typing.TypeVar('_Function5__T1')  # <T1>
_Function5__T2 = typing.TypeVar('_Function5__T2')  # <T2>
_Function5__T3 = typing.TypeVar('_Function5__T3')  # <T3>
_Function5__T4 = typing.TypeVar('_Function5__T4')  # <T4>
_Function5__T5 = typing.TypeVar('_Function5__T5')  # <T5>
_Function5__R = typing.TypeVar('_Function5__R')  # <R>
class Function5(typing.Generic[_Function5__T1, _Function5__T2, _Function5__T3, _Function5__T4, _Function5__T5, _Function5__R]):
    @staticmethod
    def $init$($this: 'Function5') -> None: ...
    def apply(self, v1: _Function5__T1, v2: _Function5__T2, v3: _Function5__T3, v4: _Function5__T4, v5: _Function5__T5) -> _Function5__R: ...
    def curried(self) -> Function1[_Function5__T1, Function1[_Function5__T2, Function1[_Function5__T3, Function1[_Function5__T4, Function1[_Function5__T5, _Function5__R]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple5'[_Function5__T1, _Function5__T2, _Function5__T3, _Function5__T4, _Function5__T5], _Function5__R]: ...

_Function6__T1 = typing.TypeVar('_Function6__T1')  # <T1>
_Function6__T2 = typing.TypeVar('_Function6__T2')  # <T2>
_Function6__T3 = typing.TypeVar('_Function6__T3')  # <T3>
_Function6__T4 = typing.TypeVar('_Function6__T4')  # <T4>
_Function6__T5 = typing.TypeVar('_Function6__T5')  # <T5>
_Function6__T6 = typing.TypeVar('_Function6__T6')  # <T6>
_Function6__R = typing.TypeVar('_Function6__R')  # <R>
class Function6(typing.Generic[_Function6__T1, _Function6__T2, _Function6__T3, _Function6__T4, _Function6__T5, _Function6__T6, _Function6__R]):
    @staticmethod
    def $init$($this: 'Function6') -> None: ...
    def apply(self, v1: _Function6__T1, v2: _Function6__T2, v3: _Function6__T3, v4: _Function6__T4, v5: _Function6__T5, v6: _Function6__T6) -> _Function6__R: ...
    def curried(self) -> Function1[_Function6__T1, Function1[_Function6__T2, Function1[_Function6__T3, Function1[_Function6__T4, Function1[_Function6__T5, Function1[_Function6__T6, _Function6__R]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple6'[_Function6__T1, _Function6__T2, _Function6__T3, _Function6__T4, _Function6__T5, _Function6__T6], _Function6__R]: ...

_Function7__T1 = typing.TypeVar('_Function7__T1')  # <T1>
_Function7__T2 = typing.TypeVar('_Function7__T2')  # <T2>
_Function7__T3 = typing.TypeVar('_Function7__T3')  # <T3>
_Function7__T4 = typing.TypeVar('_Function7__T4')  # <T4>
_Function7__T5 = typing.TypeVar('_Function7__T5')  # <T5>
_Function7__T6 = typing.TypeVar('_Function7__T6')  # <T6>
_Function7__T7 = typing.TypeVar('_Function7__T7')  # <T7>
_Function7__R = typing.TypeVar('_Function7__R')  # <R>
class Function7(typing.Generic[_Function7__T1, _Function7__T2, _Function7__T3, _Function7__T4, _Function7__T5, _Function7__T6, _Function7__T7, _Function7__R]):
    @staticmethod
    def $init$($this: 'Function7') -> None: ...
    def apply(self, v1: _Function7__T1, v2: _Function7__T2, v3: _Function7__T3, v4: _Function7__T4, v5: _Function7__T5, v6: _Function7__T6, v7: _Function7__T7) -> _Function7__R: ...
    def curried(self) -> Function1[_Function7__T1, Function1[_Function7__T2, Function1[_Function7__T3, Function1[_Function7__T4, Function1[_Function7__T5, Function1[_Function7__T6, Function1[_Function7__T7, _Function7__R]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple7'[_Function7__T1, _Function7__T2, _Function7__T3, _Function7__T4, _Function7__T5, _Function7__T6, _Function7__T7], _Function7__R]: ...

_Function8__T1 = typing.TypeVar('_Function8__T1')  # <T1>
_Function8__T2 = typing.TypeVar('_Function8__T2')  # <T2>
_Function8__T3 = typing.TypeVar('_Function8__T3')  # <T3>
_Function8__T4 = typing.TypeVar('_Function8__T4')  # <T4>
_Function8__T5 = typing.TypeVar('_Function8__T5')  # <T5>
_Function8__T6 = typing.TypeVar('_Function8__T6')  # <T6>
_Function8__T7 = typing.TypeVar('_Function8__T7')  # <T7>
_Function8__T8 = typing.TypeVar('_Function8__T8')  # <T8>
_Function8__R = typing.TypeVar('_Function8__R')  # <R>
class Function8(typing.Generic[_Function8__T1, _Function8__T2, _Function8__T3, _Function8__T4, _Function8__T5, _Function8__T6, _Function8__T7, _Function8__T8, _Function8__R]):
    @staticmethod
    def $init$($this: 'Function8') -> None: ...
    def apply(self, v1: _Function8__T1, v2: _Function8__T2, v3: _Function8__T3, v4: _Function8__T4, v5: _Function8__T5, v6: _Function8__T6, v7: _Function8__T7, v8: _Function8__T8) -> _Function8__R: ...
    def curried(self) -> Function1[_Function8__T1, Function1[_Function8__T2, Function1[_Function8__T3, Function1[_Function8__T4, Function1[_Function8__T5, Function1[_Function8__T6, Function1[_Function8__T7, Function1[_Function8__T8, _Function8__R]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple8'[_Function8__T1, _Function8__T2, _Function8__T3, _Function8__T4, _Function8__T5, _Function8__T6, _Function8__T7, _Function8__T8], _Function8__R]: ...

_Function9__T1 = typing.TypeVar('_Function9__T1')  # <T1>
_Function9__T2 = typing.TypeVar('_Function9__T2')  # <T2>
_Function9__T3 = typing.TypeVar('_Function9__T3')  # <T3>
_Function9__T4 = typing.TypeVar('_Function9__T4')  # <T4>
_Function9__T5 = typing.TypeVar('_Function9__T5')  # <T5>
_Function9__T6 = typing.TypeVar('_Function9__T6')  # <T6>
_Function9__T7 = typing.TypeVar('_Function9__T7')  # <T7>
_Function9__T8 = typing.TypeVar('_Function9__T8')  # <T8>
_Function9__T9 = typing.TypeVar('_Function9__T9')  # <T9>
_Function9__R = typing.TypeVar('_Function9__R')  # <R>
class Function9(typing.Generic[_Function9__T1, _Function9__T2, _Function9__T3, _Function9__T4, _Function9__T5, _Function9__T6, _Function9__T7, _Function9__T8, _Function9__T9, _Function9__R]):
    @staticmethod
    def $init$($this: 'Function9') -> None: ...
    def apply(self, v1: _Function9__T1, v2: _Function9__T2, v3: _Function9__T3, v4: _Function9__T4, v5: _Function9__T5, v6: _Function9__T6, v7: _Function9__T7, v8: _Function9__T8, v9: _Function9__T9) -> _Function9__R: ...
    def curried(self) -> Function1[_Function9__T1, Function1[_Function9__T2, Function1[_Function9__T3, Function1[_Function9__T4, Function1[_Function9__T5, Function1[_Function9__T6, Function1[_Function9__T7, Function1[_Function9__T8, Function1[_Function9__T9, _Function9__R]]]]]]]]]: ...
    def toString(self) -> str: ...
    def tupled(self) -> Function1['Tuple9'[_Function9__T1, _Function9__T2, _Function9__T3, _Function9__T4, _Function9__T5, _Function9__T6, _Function9__T7, _Function9__T8, _Function9__T9], _Function9__R]: ...

class Immutable: ...

class Int:
    def __init__(self): ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: str) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: str) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: float) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: float) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: str) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: float) -> float: ...
    @typing.overload
    def $div(self, x: float) -> float: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: str) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: str) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: float) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: float) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: str) -> bool: ...
    @typing.overload
    def $greater(self, x: float) -> bool: ...
    @typing.overload
    def $greater(self, x: float) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: str) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: float) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: float) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: str) -> bool: ...
    @typing.overload
    def $less(self, x: float) -> bool: ...
    @typing.overload
    def $less(self, x: float) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: str) -> bool: ...
    @typing.overload
    def $less$eq(self, x: float) -> bool: ...
    @typing.overload
    def $less$eq(self, x: float) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$less(self, x: int) -> int: ...
    @typing.overload
    def $less$less(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: float) -> float: ...
    @typing.overload
    def $minus(self, x: float) -> float: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: str) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: float) -> float: ...
    @typing.overload
    def $percent(self, x: float) -> float: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: str) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: float) -> float: ...
    @typing.overload
    def $plus(self, x: float) -> float: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: str) -> int: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: str) -> str: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: float) -> float: ...
    @typing.overload
    def $times(self, x: float) -> float: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: str) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: str) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @staticmethod
    def MaxValue() -> int: ...
    @staticmethod
    def MinValue() -> int: ...
    @staticmethod
    def box(x: int) -> int: ...
    @staticmethod
    def int2double(x: int) -> float: ...
    @staticmethod
    def int2float(x: int) -> float: ...
    @staticmethod
    def int2long(x: int) -> int: ...
    def toByte(self) -> int: ...
    def toChar(self) -> str: ...
    def toDouble(self) -> float: ...
    def toFloat(self) -> float: ...
    def toInt(self) -> int: ...
    def toLong(self) -> int: ...
    def toShort(self) -> int: ...
    @staticmethod
    def toString() -> str: ...
    def unary_$minus(self) -> int: ...
    def unary_$plus(self) -> int: ...
    def unary_$tilde(self) -> int: ...
    @staticmethod
    def unbox(x: typing.Any) -> int: ...

class Long:
    def __init__(self): ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: str) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: str) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: float) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: float) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: str) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: float) -> float: ...
    @typing.overload
    def $div(self, x: float) -> float: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: str) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: str) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: float) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: float) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: str) -> bool: ...
    @typing.overload
    def $greater(self, x: float) -> bool: ...
    @typing.overload
    def $greater(self, x: float) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: str) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: float) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: float) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: str) -> bool: ...
    @typing.overload
    def $less(self, x: float) -> bool: ...
    @typing.overload
    def $less(self, x: float) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: str) -> bool: ...
    @typing.overload
    def $less$eq(self, x: float) -> bool: ...
    @typing.overload
    def $less$eq(self, x: float) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$less(self, x: int) -> int: ...
    @typing.overload
    def $less$less(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: float) -> float: ...
    @typing.overload
    def $minus(self, x: float) -> float: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: str) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: float) -> float: ...
    @typing.overload
    def $percent(self, x: float) -> float: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: str) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: float) -> float: ...
    @typing.overload
    def $plus(self, x: float) -> float: ...
    @typing.overload
    def $plus(self, x: str) -> str: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: str) -> int: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: float) -> float: ...
    @typing.overload
    def $times(self, x: float) -> float: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: str) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: str) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @staticmethod
    def MaxValue() -> int: ...
    @staticmethod
    def MinValue() -> int: ...
    @staticmethod
    def box(x: int) -> int: ...
    @staticmethod
    def long2double(x: int) -> float: ...
    @staticmethod
    def long2float(x: int) -> float: ...
    def toByte(self) -> int: ...
    def toChar(self) -> str: ...
    def toDouble(self) -> float: ...
    def toFloat(self) -> float: ...
    def toInt(self) -> int: ...
    def toLong(self) -> int: ...
    def toShort(self) -> int: ...
    @staticmethod
    def toString() -> str: ...
    def unary_$minus(self) -> int: ...
    def unary_$plus(self) -> int: ...
    def unary_$tilde(self) -> int: ...
    @staticmethod
    def unbox(x: typing.Any) -> int: ...

class LowPriorityImplicits:
    def __init__(self): ...
    def booleanWrapper(self, x: bool) -> bool: ...
    def byteWrapper(self, x: int) -> int: ...
    def charWrapper(self, c: str) -> str: ...
    def doubleWrapper(self, x: float) -> float: ...
    _fallbackStringCanBuildFrom__T = typing.TypeVar('_fallbackStringCanBuildFrom__T')  # <T>
    def fallbackStringCanBuildFrom(self) -> scala.collection.generic.CanBuildFrom[str, _fallbackStringCanBuildFrom__T, scala.collection.immutable.IndexedSeq[_fallbackStringCanBuildFrom__T]]: ...
    def floatWrapper(self, x: float) -> float: ...
    _genericWrapArray__T = typing.TypeVar('_genericWrapArray__T')  # <T>
    def genericWrapArray(self, xs: typing.Any) -> scala.collection.mutable.WrappedArray[_genericWrapArray__T]: ...
    def intWrapper(self, x: int) -> int: ...
    def longWrapper(self, x: int) -> int: ...
    def shortWrapper(self, x: int) -> int: ...
    def unwrapString(self, ws: scala.collection.immutable.WrappedString) -> str: ...
    def wrapBooleanArray(self, xs: typing.List[bool]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    def wrapByteArray(self, xs: typing.List[int]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    def wrapCharArray(self, xs: typing.List[str]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    def wrapDoubleArray(self, xs: typing.List[float]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    def wrapFloatArray(self, xs: typing.List[float]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    def wrapIntArray(self, xs: typing.List[int]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    def wrapLongArray(self, xs: typing.List[int]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    _wrapRefArray__T = typing.TypeVar('_wrapRefArray__T')  # <T>
    def wrapRefArray(self, xs: typing.List[_wrapRefArray__T]) -> scala.collection.mutable.WrappedArray[_wrapRefArray__T]: ...
    def wrapShortArray(self, xs: typing.List[int]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    def wrapString(self, s: str) -> scala.collection.immutable.WrappedString: ...
    def wrapUnitArray(self, xs: typing.List[scala.runtime.BoxedUnit]) -> scala.collection.mutable.WrappedArray[scala.runtime.BoxedUnit]: ...

class MatchError(java.lang.RuntimeException):
    def __init__(self, obj: typing.Any): ...
    def getMessage(self) -> str: ...

class Mutable: ...

class None:
    @staticmethod
    def canEqual(x$1: typing.Any) -> bool: ...
    _collect__B = typing.TypeVar('_collect__B')  # <B>
    @staticmethod
    def collect(pf: 'PartialFunction'[scala.runtime.Nothing., _collect__B]) -> 'Option'[_collect__B]: ...
    _contains__A1 = typing.TypeVar('_contains__A1')  # <A1>
    @staticmethod
    def contains(elem: _contains__A1) -> bool: ...
    @staticmethod
    def exists(p: Function1[scala.runtime.Nothing., typing.Any]) -> bool: ...
    @staticmethod
    def filter(p: Function1[scala.runtime.Nothing., typing.Any]) -> 'Option'[scala.runtime.Nothing.]: ...
    @staticmethod
    def filterNot(p: Function1[scala.runtime.Nothing., typing.Any]) -> 'Option'[scala.runtime.Nothing.]: ...
    _flatMap__B = typing.TypeVar('_flatMap__B')  # <B>
    @staticmethod
    def flatMap(f: Function1[scala.runtime.Nothing., 'Option'[_flatMap__B]]) -> 'Option'[_flatMap__B]: ...
    _flatten__B = typing.TypeVar('_flatten__B')  # <B>
    @staticmethod
    def flatten(ev: 'Predef..less.colon.less'[scala.runtime.Nothing., 'Option'[_flatten__B]]) -> 'Option'[_flatten__B]: ...
    _fold__B = typing.TypeVar('_fold__B')  # <B>
    @staticmethod
    def fold(ifEmpty: Function0[_fold__B], f: Function1[scala.runtime.Nothing., _fold__B]) -> _fold__B: ...
    @staticmethod
    def forall(p: Function1[scala.runtime.Nothing., typing.Any]) -> bool: ...
    _foreach__U = typing.TypeVar('_foreach__U')  # <U>
    @staticmethod
    def foreach(f: Function1[scala.runtime.Nothing., _foreach__U]) -> None: ...
    @staticmethod
    def get() -> scala.runtime.Nothing.: ...
    _getOrElse__B = typing.TypeVar('_getOrElse__B')  # <B>
    @staticmethod
    def getOrElse(default: Function0[_getOrElse__B]) -> _getOrElse__B: ...
    @staticmethod
    def hashCode() -> int: ...
    @staticmethod
    def isDefined() -> bool: ...
    @staticmethod
    def isEmpty() -> bool: ...
    @staticmethod
    def iterator() -> scala.collection.Iterator[scala.runtime.Nothing.]: ...
    _map__B = typing.TypeVar('_map__B')  # <B>
    @staticmethod
    def map(f: Function1[scala.runtime.Nothing., _map__B]) -> 'Option'[_map__B]: ...
    @staticmethod
    def nonEmpty() -> bool: ...
    _orElse__B = typing.TypeVar('_orElse__B')  # <B>
    @staticmethod
    def orElse(alternative: Function0['Option'[_orElse__B]]) -> 'Option'[_orElse__B]: ...
    _orNull__A1 = typing.TypeVar('_orNull__A1')  # <A1>
    @staticmethod
    def orNull(ev: 'Predef..less.colon.less'[scala.runtime.Null., _orNull__A1]) -> _orNull__A1: ...
    @staticmethod
    def productArity() -> int: ...
    @staticmethod
    def productElement(x$1: int) -> typing.Any: ...
    @staticmethod
    def productIterator() -> scala.collection.Iterator[typing.Any]: ...
    @staticmethod
    def productPrefix() -> str: ...
    _toLeft__X = typing.TypeVar('_toLeft__X')  # <X>
    @staticmethod
    def toLeft(right: Function0[_toLeft__X]) -> scala.util.Either[scala.runtime.Nothing., _toLeft__X]: ...
    @staticmethod
    def toList() -> scala.collection.immutable.List[scala.runtime.Nothing.]: ...
    _toRight__X = typing.TypeVar('_toRight__X')  # <X>
    @staticmethod
    def toRight(left: Function0[_toRight__X]) -> scala.util.Either[_toRight__X, scala.runtime.Nothing.]: ...
    @staticmethod
    def toString() -> str: ...
    @staticmethod
    def withFilter(p: Function1[scala.runtime.Nothing., typing.Any]) -> 'Option.WithFilter': ...

class NotImplementedError(java.lang.Error):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, msg: str): ...

class NotNull: ...

class SerialVersionUID(scala.annotation.Annotation, scala.annotation.ClassfileAnnotation):
    def __init__(self, value: int): ...

class Serializable(java.io.Serializable): ...

class Short:
    def __init__(self): ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: str) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $amp(self, x: int) -> int: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: str) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: float) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: float) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bang$eq(self, x: int) -> bool: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: str) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $bar(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: float) -> float: ...
    @typing.overload
    def $div(self, x: float) -> float: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: str) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $div(self, x: int) -> int: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: str) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: float) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: float) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $eq$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: str) -> bool: ...
    @typing.overload
    def $greater(self, x: float) -> bool: ...
    @typing.overload
    def $greater(self, x: float) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: str) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: float) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: float) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$eq(self, x: int) -> bool: ...
    @typing.overload
    def $greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $greater$greater$greater(self, x: int) -> int: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: str) -> bool: ...
    @typing.overload
    def $less(self, x: float) -> bool: ...
    @typing.overload
    def $less(self, x: float) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: str) -> bool: ...
    @typing.overload
    def $less$eq(self, x: float) -> bool: ...
    @typing.overload
    def $less$eq(self, x: float) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$eq(self, x: int) -> bool: ...
    @typing.overload
    def $less$less(self, x: int) -> int: ...
    @typing.overload
    def $less$less(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: float) -> float: ...
    @typing.overload
    def $minus(self, x: float) -> float: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: str) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $minus(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: float) -> float: ...
    @typing.overload
    def $percent(self, x: float) -> float: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: str) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $percent(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: float) -> float: ...
    @typing.overload
    def $plus(self, x: float) -> float: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: str) -> int: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $plus(self, x: str) -> str: ...
    @typing.overload
    def $plus(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: float) -> float: ...
    @typing.overload
    def $times(self, x: float) -> float: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: str) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $times(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: str) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @typing.overload
    def $up(self, x: int) -> int: ...
    @staticmethod
    def MaxValue() -> int: ...
    @staticmethod
    def MinValue() -> int: ...
    @staticmethod
    def box(x: int) -> int: ...
    @staticmethod
    def short2double(x: int) -> float: ...
    @staticmethod
    def short2float(x: int) -> float: ...
    @staticmethod
    def short2int(x: int) -> int: ...
    @staticmethod
    def short2long(x: int) -> int: ...
    def toByte(self) -> int: ...
    def toChar(self) -> str: ...
    def toDouble(self) -> float: ...
    def toFloat(self) -> float: ...
    def toInt(self) -> int: ...
    def toLong(self) -> int: ...
    def toShort(self) -> int: ...
    @staticmethod
    def toString() -> str: ...
    def unary_$minus(self) -> int: ...
    def unary_$plus(self) -> int: ...
    def unary_$tilde(self) -> int: ...
    @staticmethod
    def unbox(x: typing.Any) -> int: ...

class UninitializedError(java.lang.RuntimeException):
    def __init__(self): ...

_UniquenessCache__K = typing.TypeVar('_UniquenessCache__K')  # <K>
_UniquenessCache__V = typing.TypeVar('_UniquenessCache__V')  # <V>
class UniquenessCache(typing.Generic[_UniquenessCache__K, _UniquenessCache__V]):
    def __init__(self): ...
    def apply(self, name: _UniquenessCache__K) -> _UniquenessCache__V: ...
    def keyFromValue(self, v: _UniquenessCache__V) -> 'Option'[_UniquenessCache__K]: ...
    def unapply(self, other: _UniquenessCache__V) -> 'Option'[_UniquenessCache__K]: ...
    def valueFromKey(self, k: _UniquenessCache__K) -> _UniquenessCache__V: ...

class Unit:
    def __init__(self): ...
    @staticmethod
    def box(x: scala.runtime.BoxedUnit) -> scala.runtime.BoxedUnit: ...
    @staticmethod
    def toString() -> str: ...
    @staticmethod
    def unbox(x: typing.Any) -> None: ...

class deprecated(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self, message: str, since: str): ...
    @staticmethod
    def $lessinit$greater$default$1() -> str: ...
    @staticmethod
    def $lessinit$greater$default$2() -> str: ...

class deprecatedInheritance(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self, message: str, since: str): ...
    @staticmethod
    def $lessinit$greater$default$1() -> str: ...
    @staticmethod
    def $lessinit$greater$default$2() -> str: ...

class deprecatedName(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self, name: 'Symbol', since: str): ...
    @staticmethod
    def $lessinit$greater$default$1() -> 'Symbol': ...
    @staticmethod
    def $lessinit$greater$default$2() -> str: ...

class deprecatedOverriding(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self, message: str, since: str): ...
    @staticmethod
    def $lessinit$greater$default$1() -> str: ...
    @staticmethod
    def $lessinit$greater$default$2() -> str: ...

class inline(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class language:
    @staticmethod
    def dynamics() -> 'languageFeature.dynamics': ...
    @staticmethod
    def existentials() -> 'languageFeature.existentials': ...
    @staticmethod
    def higherKinds() -> 'languageFeature.higherKinds': ...
    @staticmethod
    def implicitConversions() -> 'languageFeature.implicitConversions': ...
    @staticmethod
    def postfixOps() -> 'languageFeature.postfixOps': ...
    @staticmethod
    def reflectiveCalls() -> 'languageFeature.reflectiveCalls': ...
    class experimental$:
        MODULE$: typing.ClassVar['language.experimental.'] = ...
        def __init__(self): ...
        def macros(self) -> 'languageFeature.experimental.macros': ...

class native(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class noinline(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class package:
    @staticmethod
    def $colon$colon() -> scala.collection.immutable..colon.colon.: ...
    @staticmethod
    def $colon$plus() -> scala.collection..colon.plus.: ...
    @staticmethod
    def $hash$colon$colon() -> scala.collection.immutable.Stream..hash.colon.colon.: ...
    @staticmethod
    def $plus$colon() -> scala.collection..plus.colon.: ...
    @staticmethod
    def AnyRef() -> 'Specializable': ...
    @staticmethod
    def BigDecimal() -> scala.math.BigDecimal.: ...
    @staticmethod
    def BigInt() -> scala.math.BigInt.: ...
    @staticmethod
    def Either() -> scala.util.Either.: ...
    @staticmethod
    def Equiv() -> scala.math.Equiv.: ...
    @staticmethod
    def Fractional() -> scala.math.Fractional.: ...
    @staticmethod
    def IndexedSeq() -> scala.collection.IndexedSeq.: ...
    @staticmethod
    def Integral() -> scala.math.Integral.: ...
    @staticmethod
    def Iterable() -> scala.collection.Iterable.: ...
    @staticmethod
    def Iterator() -> scala.collection.Iterator.: ...
    @staticmethod
    def Left() -> scala.util.Left.: ...
    @staticmethod
    def List() -> scala.collection.immutable.List.: ...
    @staticmethod
    def Nil() -> scala.collection.immutable.Nil.: ...
    @staticmethod
    def Numeric() -> scala.math.Numeric.: ...
    @staticmethod
    def Ordered() -> scala.math.Ordered.: ...
    @staticmethod
    def Ordering() -> scala.math.Ordering.: ...
    @staticmethod
    def Range() -> scala.collection.immutable.Range.: ...
    @staticmethod
    def Right() -> scala.util.Right.: ...
    @staticmethod
    def Seq() -> scala.collection.Seq.: ...
    @staticmethod
    def Stream() -> scala.collection.immutable.Stream.: ...
    @staticmethod
    def StringBuilder() -> scala.collection.mutable.StringBuilder.: ...
    @staticmethod
    def Traversable() -> scala.collection.Traversable.: ...
    @staticmethod
    def Vector() -> scala.collection.immutable.Vector.: ...

class remote(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class specialized(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, group: 'Specializable.SpecializedGroup'): ...
    @typing.overload
    def __init__(self, types: scala.collection.Seq['Specializable']): ...

_throws__T = typing.TypeVar('_throws__T', bound=java.lang.Throwable)  # <T>
class throws(scala.annotation.Annotation, scala.annotation.StaticAnnotation, typing.Generic[_throws__T]):
    @typing.overload
    def __init__(self, clazz: typing.Type[_throws__T]): ...
    @typing.overload
    def __init__(self, cause: str): ...
    _$lessinit$greater$default$1__T = typing.TypeVar('_$lessinit$greater$default$1__T', bound=java.lang.Throwable)  # <T>
    @staticmethod
    def $lessinit$greater$default$1() -> str: ...

class transient(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class unchecked(scala.annotation.Annotation):
    def __init__(self): ...

class volatile(scala.annotation.Annotation, scala.annotation.StaticAnnotation):
    def __init__(self): ...

class App(DelayedInit):
    @staticmethod
    def $init$($this: 'App') -> None: ...
    def args(self) -> typing.List[str]: ...
    def delayedInit(self, body: Function0[scala.runtime.BoxedUnit]) -> None: ...
    def executionStart(self) -> int: ...
    def main(self, args: typing.List[str]) -> None: ...
    def scala$App$$_args(self) -> typing.List[str]: ...
    def scala$App$$_args_$eq(self, x$1: typing.List[str]) -> None: ...
    def scala$App$$initCode(self) -> scala.collection.mutable.ListBuffer[Function0[scala.runtime.BoxedUnit]]: ...
    def scala$App$_setter_$executionStart_$eq(self, x$1: int) -> None: ...
    def scala$App$_setter_$scala$App$$initCode_$eq(self, x$1: scala.collection.mutable.ListBuffer[Function0[scala.runtime.BoxedUnit]]) -> None: ...

_Predef____eq__colon__eq__From = typing.TypeVar('_Predef____eq__colon__eq__From')  # <From>
_Predef____eq__colon__eq__To = typing.TypeVar('_Predef____eq__colon__eq__To')  # <To>
_Predef____less__colon__less__From = typing.TypeVar('_Predef____less__colon__less__From')  # <From>
_Predef____less__colon__less__To = typing.TypeVar('_Predef____less__colon__less__To')  # <To>
_Predef__ArrowAssoc__A = typing.TypeVar('_Predef__ArrowAssoc__A')  # <A>
_Predef__Ensuring__A = typing.TypeVar('_Predef__Ensuring__A')  # <A>
_Predef__StringFormat__A = typing.TypeVar('_Predef__StringFormat__A')  # <A>
_Predef__any2stringadd__A = typing.TypeVar('_Predef__any2stringadd__A')  # <A>
class Predef:
    _$conforms__A = typing.TypeVar('_$conforms__A')  # <A>
    @staticmethod
    def $conforms() -> 'Predef..less.colon.less'[_.conforms__A, _.conforms__A]: ...
    @staticmethod
    def $qmark$qmark$qmark() -> scala.runtime.Nothing.: ...
    @staticmethod
    def Boolean2boolean(x: bool) -> bool: ...
    @staticmethod
    def Byte2byte(x: int) -> int: ...
    @staticmethod
    def Character2char(x: str) -> str: ...
    @staticmethod
    def ClassManifest() -> scala.reflect.ClassManifestFactory.: ...
    @staticmethod
    def Double2double(x: float) -> float: ...
    @staticmethod
    def Float2float(x: float) -> float: ...
    @staticmethod
    def Integer2int(x: int) -> int: ...
    @staticmethod
    def Long2long(x: int) -> int: ...
    @staticmethod
    def Manifest() -> scala.reflect.ManifestFactory.: ...
    @staticmethod
    def Map() -> scala.collection.immutable.Map.: ...
    @staticmethod
    def NoManifest() -> scala.reflect.NoManifest.: ...
    @staticmethod
    def Set() -> scala.collection.immutable.Set.: ...
    @staticmethod
    def Short2short(x: int) -> int: ...
    @staticmethod
    def StringCanBuildFrom() -> scala.collection.generic.CanBuildFrom[str, typing.Any, str]: ...
    @staticmethod
    def any2ArrowAssoc(x: typing.Any) -> typing.Any: ...
    @staticmethod
    def any2Ensuring(x: typing.Any) -> typing.Any: ...
    @staticmethod
    def any2stringfmt(x: typing.Any) -> typing.Any: ...
    @staticmethod
    def arrayToCharSequence(xs: typing.List[str]) -> java.lang.CharSequence: ...
    @typing.overload
    @staticmethod
    def assume(assumption: bool) -> None: ...
    @typing.overload
    @staticmethod
    def assume(assumption: bool, message: Function0[typing.Any]) -> None: ...
    @staticmethod
    def augmentString(x: str) -> str: ...
    @staticmethod
    def boolean2Boolean(x: bool) -> bool: ...
    @staticmethod
    def booleanArrayOps(xs: typing.List[bool]) -> typing.List[bool]: ...
    @staticmethod
    def booleanWrapper(x: bool) -> bool: ...
    @staticmethod
    def byte2Byte(x: int) -> int: ...
    @staticmethod
    def byteArrayOps(xs: typing.List[int]) -> typing.List[int]: ...
    @staticmethod
    def byteWrapper(x: int) -> int: ...
    @staticmethod
    def char2Character(x: str) -> str: ...
    @staticmethod
    def charArrayOps(xs: typing.List[str]) -> typing.List[str]: ...
    @staticmethod
    def charWrapper(c: str) -> str: ...
    _classManifest__T = typing.TypeVar('_classManifest__T')  # <T>
    @staticmethod
    def classManifest(m: scala.reflect.ClassTag[_classManifest__T]) -> scala.reflect.ClassTag[_classManifest__T]: ...
    _classOf__T = typing.TypeVar('_classOf__T')  # <T>
    @staticmethod
    def classOf() -> typing.Type[_classOf__T]: ...
    _conforms__A = typing.TypeVar('_conforms__A')  # <A>
    @staticmethod
    def conforms() -> 'Predef..less.colon.less'[_conforms__A, _conforms__A]: ...
    @staticmethod
    def double2Double(x: float) -> float: ...
    @staticmethod
    def doubleArrayOps(xs: typing.List[float]) -> typing.List[float]: ...
    @staticmethod
    def doubleWrapper(x: float) -> float: ...
    @staticmethod
    def exceptionWrapper(exc: java.lang.Throwable) -> java.lang.Throwable: ...
    _fallbackStringCanBuildFrom__T = typing.TypeVar('_fallbackStringCanBuildFrom__T')  # <T>
    @staticmethod
    def fallbackStringCanBuildFrom() -> scala.collection.generic.CanBuildFrom[str, _fallbackStringCanBuildFrom__T, scala.collection.immutable.IndexedSeq[_fallbackStringCanBuildFrom__T]]: ...
    @staticmethod
    def float2Float(x: float) -> float: ...
    @staticmethod
    def floatArrayOps(xs: typing.List[float]) -> typing.List[float]: ...
    @staticmethod
    def floatWrapper(x: float) -> float: ...
    _genericArrayOps__T = typing.TypeVar('_genericArrayOps__T')  # <T>
    @staticmethod
    def genericArrayOps(xs: typing.Any) -> scala.collection.mutable.ArrayOps[_genericArrayOps__T]: ...
    _genericWrapArray__T = typing.TypeVar('_genericWrapArray__T')  # <T>
    @staticmethod
    def genericWrapArray(xs: typing.Any) -> scala.collection.mutable.WrappedArray[_genericWrapArray__T]: ...
    _identity__A = typing.TypeVar('_identity__A')  # <A>
    @staticmethod
    def identity(x: _identity__A) -> _identity__A: ...
    _implicitly__T = typing.TypeVar('_implicitly__T')  # <T>
    @staticmethod
    def implicitly(e: _implicitly__T) -> _implicitly__T: ...
    @staticmethod
    def int2Integer(x: int) -> int: ...
    @staticmethod
    def intArrayOps(xs: typing.List[int]) -> typing.List[int]: ...
    @staticmethod
    def intWrapper(x: int) -> int: ...
    _locally__T = typing.TypeVar('_locally__T')  # <T>
    @staticmethod
    def locally(x: _locally__T) -> _locally__T: ...
    @staticmethod
    def long2Long(x: int) -> int: ...
    @staticmethod
    def longArrayOps(xs: typing.List[int]) -> typing.List[int]: ...
    @staticmethod
    def longWrapper(x: int) -> int: ...
    _manifest__T = typing.TypeVar('_manifest__T')  # <T>
    @staticmethod
    def manifest(m: scala.reflect.Manifest[_manifest__T]) -> scala.reflect.Manifest[_manifest__T]: ...
    _optManifest__T = typing.TypeVar('_optManifest__T')  # <T>
    @staticmethod
    def optManifest(m: scala.reflect.OptManifest[_optManifest__T]) -> scala.reflect.OptManifest[_optManifest__T]: ...
    @staticmethod
    def printf(text: str, xs: scala.collection.Seq[typing.Any]) -> None: ...
    @typing.overload
    @staticmethod
    def println() -> None: ...
    @typing.overload
    @staticmethod
    def println(x: typing.Any) -> None: ...
    @staticmethod
    def readBoolean() -> bool: ...
    @staticmethod
    def readByte() -> int: ...
    @staticmethod
    def readChar() -> str: ...
    @staticmethod
    def readDouble() -> float: ...
    @staticmethod
    def readFloat() -> float: ...
    @staticmethod
    def readInt() -> int: ...
    @typing.overload
    @staticmethod
    def readLine() -> str: ...
    @typing.overload
    @staticmethod
    def readLine(text: str, args: scala.collection.Seq[typing.Any]) -> str: ...
    @staticmethod
    def readLong() -> int: ...
    @staticmethod
    def readShort() -> int: ...
    @staticmethod
    def readf(format: str) -> scala.collection.immutable.List[typing.Any]: ...
    @staticmethod
    def readf1(format: str) -> typing.Any: ...
    @staticmethod
    def readf2(format: str) -> 'Tuple2'[typing.Any, typing.Any]: ...
    @staticmethod
    def readf3(format: str) -> 'Tuple3'[typing.Any, typing.Any, typing.Any]: ...
    @staticmethod
    def refArrayOps(xs: typing.List[typing.Any]) -> typing.List[typing.Any]: ...
    @typing.overload
    @staticmethod
    def require(requirement: bool) -> None: ...
    @typing.overload
    @staticmethod
    def require(requirement: bool, message: Function0[typing.Any]) -> None: ...
    @staticmethod
    def seqToCharSequence(xs: scala.collection.IndexedSeq[typing.Any]) -> java.lang.CharSequence: ...
    @staticmethod
    def short2Short(x: int) -> int: ...
    @staticmethod
    def shortArrayOps(xs: typing.List[int]) -> typing.List[int]: ...
    @staticmethod
    def shortWrapper(x: int) -> int: ...
    @staticmethod
    def tuple2ToZippedOps(x: 'Tuple2') -> 'Tuple2': ...
    @staticmethod
    def tuple3ToZippedOps(x: 'Tuple3') -> 'Tuple3': ...
    @staticmethod
    def unaugmentString(x: str) -> str: ...
    @staticmethod
    def unitArrayOps(xs: typing.List[scala.runtime.BoxedUnit]) -> typing.List[scala.runtime.BoxedUnit]: ...
    @staticmethod
    def unwrapString(ws: scala.collection.immutable.WrappedString) -> str: ...
    @staticmethod
    def wrapBooleanArray(xs: typing.List[bool]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    @staticmethod
    def wrapByteArray(xs: typing.List[int]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    @staticmethod
    def wrapCharArray(xs: typing.List[str]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    @staticmethod
    def wrapDoubleArray(xs: typing.List[float]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    @staticmethod
    def wrapFloatArray(xs: typing.List[float]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    @staticmethod
    def wrapIntArray(xs: typing.List[int]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    @staticmethod
    def wrapLongArray(xs: typing.List[int]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    _wrapRefArray__T = typing.TypeVar('_wrapRefArray__T')  # <T>
    @staticmethod
    def wrapRefArray(xs: typing.List[_wrapRefArray__T]) -> scala.collection.mutable.WrappedArray[_wrapRefArray__T]: ...
    @staticmethod
    def wrapShortArray(xs: typing.List[int]) -> scala.collection.mutable.WrappedArray[typing.Any]: ...
    @staticmethod
    def wrapString(s: str) -> scala.collection.immutable.WrappedString: ...
    @staticmethod
    def wrapUnitArray(xs: typing.List[scala.runtime.BoxedUnit]) -> scala.collection.mutable.WrappedArray[scala.runtime.BoxedUnit]: ...
    class $eq$colon$eq(Function1[_Predef____eq__colon__eq__From, _Predef____eq__colon__eq__To], Serializable, typing.Generic[_Predef____eq__colon__eq__From, _Predef____eq__colon__eq__To]):
        def __init__(self): ...
        _andThen__A = typing.TypeVar('_andThen__A')  # <A>
        def andThen(self, g: Function1[_Predef____eq__colon__eq__To, _andThen__A]) -> Function1[_Predef____eq__colon__eq__From, _andThen__A]: ...
        def apply$mcDD$sp(self, v1: float) -> float: ...
        def apply$mcDF$sp(self, v1: float) -> float: ...
        def apply$mcDI$sp(self, v1: int) -> float: ...
        def apply$mcDJ$sp(self, v1: int) -> float: ...
        def apply$mcFD$sp(self, v1: float) -> float: ...
        def apply$mcFF$sp(self, v1: float) -> float: ...
        def apply$mcFI$sp(self, v1: int) -> float: ...
        def apply$mcFJ$sp(self, v1: int) -> float: ...
        def apply$mcID$sp(self, v1: float) -> int: ...
        def apply$mcIF$sp(self, v1: float) -> int: ...
        def apply$mcII$sp(self, v1: int) -> int: ...
        def apply$mcIJ$sp(self, v1: int) -> int: ...
        def apply$mcJD$sp(self, v1: float) -> int: ...
        def apply$mcJF$sp(self, v1: float) -> int: ...
        def apply$mcJI$sp(self, v1: int) -> int: ...
        def apply$mcJJ$sp(self, v1: int) -> int: ...
        def apply$mcVD$sp(self, v1: float) -> None: ...
        def apply$mcVF$sp(self, v1: float) -> None: ...
        def apply$mcVI$sp(self, v1: int) -> None: ...
        def apply$mcVJ$sp(self, v1: int) -> None: ...
        def apply$mcZD$sp(self, v1: float) -> bool: ...
        def apply$mcZF$sp(self, v1: float) -> bool: ...
        def apply$mcZI$sp(self, v1: int) -> bool: ...
        def apply$mcZJ$sp(self, v1: int) -> bool: ...
        _compose__A = typing.TypeVar('_compose__A')  # <A>
        def compose(self, g: Function1[_compose__A, _Predef____eq__colon__eq__From]) -> Function1[_compose__A, _Predef____eq__colon__eq__To]: ...
        def toString(self) -> str: ...
    class $eq$colon$eq$(Serializable):
        MODULE$: typing.ClassVar['Predef..eq.colon.eq.'] = ...
        def __init__(self): ...
        _tpEquals__A = typing.TypeVar('_tpEquals__A')  # <A>
        def tpEquals(self) -> 'Predef..eq.colon.eq'[_tpEquals__A, _tpEquals__A]: ...
    class $less$colon$less(Function1[_Predef____less__colon__less__From, _Predef____less__colon__less__To], Serializable, typing.Generic[_Predef____less__colon__less__From, _Predef____less__colon__less__To]):
        def __init__(self): ...
        _andThen__A = typing.TypeVar('_andThen__A')  # <A>
        def andThen(self, g: Function1[_Predef____less__colon__less__To, _andThen__A]) -> Function1[_Predef____less__colon__less__From, _andThen__A]: ...
        def apply$mcDD$sp(self, v1: float) -> float: ...
        def apply$mcDF$sp(self, v1: float) -> float: ...
        def apply$mcDI$sp(self, v1: int) -> float: ...
        def apply$mcDJ$sp(self, v1: int) -> float: ...
        def apply$mcFD$sp(self, v1: float) -> float: ...
        def apply$mcFF$sp(self, v1: float) -> float: ...
        def apply$mcFI$sp(self, v1: int) -> float: ...
        def apply$mcFJ$sp(self, v1: int) -> float: ...
        def apply$mcID$sp(self, v1: float) -> int: ...
        def apply$mcIF$sp(self, v1: float) -> int: ...
        def apply$mcII$sp(self, v1: int) -> int: ...
        def apply$mcIJ$sp(self, v1: int) -> int: ...
        def apply$mcJD$sp(self, v1: float) -> int: ...
        def apply$mcJF$sp(self, v1: float) -> int: ...
        def apply$mcJI$sp(self, v1: int) -> int: ...
        def apply$mcJJ$sp(self, v1: int) -> int: ...
        def apply$mcVD$sp(self, v1: float) -> None: ...
        def apply$mcVF$sp(self, v1: float) -> None: ...
        def apply$mcVI$sp(self, v1: int) -> None: ...
        def apply$mcVJ$sp(self, v1: int) -> None: ...
        def apply$mcZD$sp(self, v1: float) -> bool: ...
        def apply$mcZF$sp(self, v1: float) -> bool: ...
        def apply$mcZI$sp(self, v1: int) -> bool: ...
        def apply$mcZJ$sp(self, v1: int) -> bool: ...
        _compose__A = typing.TypeVar('_compose__A')  # <A>
        def compose(self, g: Function1[_compose__A, _Predef____less__colon__less__From]) -> Function1[_compose__A, _Predef____less__colon__less__To]: ...
        def toString(self) -> str: ...
    class ArrayCharSequence(java.lang.CharSequence):
        def __init__(self, __arrayOfChars: typing.List[str]): ...
        def __arrayOfChars(self) -> typing.List[str]: ...
        def charAt(self, index: int) -> str: ...
        def chars(self) -> java.util.stream.IntStream: ...
        def codePoints(self) -> java.util.stream.IntStream: ...
        def length(self) -> int: ...
        def subSequence(self, start: int, end: int) -> java.lang.CharSequence: ...
        def toString(self) -> str: ...
    class ArrowAssoc(typing.Generic[_Predef__ArrowAssoc__A]):
        def __init__(self, self): ...
        _$minus$greater__B = typing.TypeVar('_$minus$greater__B')  # <B>
        def $minus$greater(self, y: _.minus.greater__B) -> 'Tuple2'[_Predef__ArrowAssoc__A, _.minus.greater__B]: ...
        _$u2192__B = typing.TypeVar('_$u2192__B')  # <B>
        def $u2192(self, y: _.u2192__B) -> 'Tuple2'[_Predef__ArrowAssoc__A, _.u2192__B]: ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def scala$Predef$ArrowAssoc$$self(self) -> _Predef__ArrowAssoc__A: ...
    class ArrowAssoc$:
        MODULE$: typing.ClassVar['Predef.ArrowAssoc.'] = ...
        def __init__(self): ...
        _$minus$greater$extension__B = typing.TypeVar('_$minus$greater$extension__B')  # <B>
        _$minus$greater$extension__A = typing.TypeVar('_$minus$greater$extension__A')  # <A>
        def $minus$greater$extension(self, $this: _.minus.greater.extension__A, y: _.minus.greater.extension__B) -> 'Tuple2'[_.minus.greater.extension__A, _.minus.greater.extension__B]: ...
        _$u2192$extension__B = typing.TypeVar('_$u2192$extension__B')  # <B>
        _$u2192$extension__A = typing.TypeVar('_$u2192$extension__A')  # <A>
        def $u2192$extension(self, $this: _.u2192.extension__A, y: _.u2192.extension__B) -> 'Tuple2'[_.u2192.extension__A, _.u2192.extension__B]: ...
        _equals$extension__A = typing.TypeVar('_equals$extension__A')  # <A>
        def equals$extension(self, $this: _equals.extension__A, x$1: typing.Any) -> bool: ...
        _hashCode$extension__A = typing.TypeVar('_hashCode$extension__A')  # <A>
        def hashCode$extension(self, $this: _hashCode.extension__A) -> int: ...
    class DummyImplicit:
        def __init__(self): ...
    class DummyImplicit$:
        MODULE$: typing.ClassVar['Predef.DummyImplicit.'] = ...
        def __init__(self): ...
        def dummyImplicit(self) -> 'Predef.DummyImplicit': ...
    class Ensuring(typing.Generic[_Predef__Ensuring__A]):
        def __init__(self, self): ...
        @typing.overload
        def ensuring(self, cond: bool) -> _Predef__Ensuring__A: ...
        @typing.overload
        def ensuring(self, cond: bool, msg: Function0[typing.Any]) -> _Predef__Ensuring__A: ...
        @typing.overload
        def ensuring(self, cond: Function1[_Predef__Ensuring__A, typing.Any]) -> _Predef__Ensuring__A: ...
        @typing.overload
        def ensuring(self, cond: Function1[_Predef__Ensuring__A, typing.Any], msg: Function0[typing.Any]) -> _Predef__Ensuring__A: ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def scala$Predef$Ensuring$$self(self) -> _Predef__Ensuring__A: ...
    class Ensuring$:
        MODULE$: typing.ClassVar['Predef.Ensuring.'] = ...
        def __init__(self): ...
        _ensuring$extension0__A = typing.TypeVar('_ensuring$extension0__A')  # <A>
        def ensuring$extension0(self, $this: _ensuring.extension0__A, cond: bool) -> _ensuring.extension0__A: ...
        _ensuring$extension1__A = typing.TypeVar('_ensuring$extension1__A')  # <A>
        def ensuring$extension1(self, $this: _ensuring.extension1__A, cond: bool, msg: Function0[typing.Any]) -> _ensuring.extension1__A: ...
        _ensuring$extension2__A = typing.TypeVar('_ensuring$extension2__A')  # <A>
        def ensuring$extension2(self, $this: _ensuring.extension2__A, cond: Function1[_ensuring.extension2__A, typing.Any]) -> _ensuring.extension2__A: ...
        _ensuring$extension3__A = typing.TypeVar('_ensuring$extension3__A')  # <A>
        def ensuring$extension3(self, $this: _ensuring.extension3__A, cond: Function1[_ensuring.extension3__A, typing.Any], msg: Function0[typing.Any]) -> _ensuring.extension3__A: ...
        _equals$extension__A = typing.TypeVar('_equals$extension__A')  # <A>
        def equals$extension(self, $this: _equals.extension__A, x$1: typing.Any) -> bool: ...
        _hashCode$extension__A = typing.TypeVar('_hashCode$extension__A')  # <A>
        def hashCode$extension(self, $this: _hashCode.extension__A) -> int: ...
    class Pair$:
        MODULE$: typing.ClassVar['Predef.Pair.'] = ...
        def __init__(self): ...
        _apply__A = typing.TypeVar('_apply__A')  # <A>
        _apply__B = typing.TypeVar('_apply__B')  # <B>
        def apply(self, x: _apply__A, y: _apply__B) -> 'Tuple2'[_apply__A, _apply__B]: ...
        _unapply__A = typing.TypeVar('_unapply__A')  # <A>
        _unapply__B = typing.TypeVar('_unapply__B')  # <B>
        def unapply(self, x: 'Tuple2'[_unapply__A, _unapply__B]) -> 'Option'['Tuple2'[_unapply__A, _unapply__B]]: ...
    class RichException:
        def __init__(self, self): ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def getStackTraceString(self) -> str: ...
        def hashCode(self) -> int: ...
        def scala$Predef$RichException$$self(self) -> java.lang.Throwable: ...
    class RichException$:
        MODULE$: typing.ClassVar['Predef.RichException.'] = ...
        def __init__(self): ...
        def equals$extension(self, $this: java.lang.Throwable, x$1: typing.Any) -> bool: ...
        def getStackTraceString$extension(self, $this: java.lang.Throwable) -> str: ...
        def hashCode$extension(self, $this: java.lang.Throwable) -> int: ...
    class SeqCharSequence(java.lang.CharSequence):
        def __init__(self, __sequenceOfChars: scala.collection.IndexedSeq[typing.Any]): ...
        def __sequenceOfChars(self) -> scala.collection.IndexedSeq[typing.Any]: ...
        def charAt(self, index: int) -> str: ...
        def chars(self) -> java.util.stream.IntStream: ...
        def codePoints(self) -> java.util.stream.IntStream: ...
        def length(self) -> int: ...
        def subSequence(self, start: int, end: int) -> java.lang.CharSequence: ...
        def toString(self) -> str: ...
    class StringFormat(typing.Generic[_Predef__StringFormat__A]):
        def __init__(self, self): ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def formatted(self, fmtstr: str) -> str: ...
        def hashCode(self) -> int: ...
        def scala$Predef$StringFormat$$self(self) -> _Predef__StringFormat__A: ...
    class StringFormat$:
        MODULE$: typing.ClassVar['Predef.StringFormat.'] = ...
        def __init__(self): ...
        _equals$extension__A = typing.TypeVar('_equals$extension__A')  # <A>
        def equals$extension(self, $this: _equals.extension__A, x$1: typing.Any) -> bool: ...
        _formatted$extension__A = typing.TypeVar('_formatted$extension__A')  # <A>
        def formatted$extension(self, $this: _formatted.extension__A, fmtstr: str) -> str: ...
        _hashCode$extension__A = typing.TypeVar('_hashCode$extension__A')  # <A>
        def hashCode$extension(self, $this: _hashCode.extension__A) -> int: ...
    class Triple$:
        MODULE$: typing.ClassVar['Predef.Triple.'] = ...
        def __init__(self): ...
        _apply__A = typing.TypeVar('_apply__A')  # <A>
        _apply__B = typing.TypeVar('_apply__B')  # <B>
        _apply__C = typing.TypeVar('_apply__C')  # <C>
        def apply(self, x: _apply__A, y: _apply__B, z: _apply__C) -> 'Tuple3'[_apply__A, _apply__B, _apply__C]: ...
        _unapply__A = typing.TypeVar('_unapply__A')  # <A>
        _unapply__B = typing.TypeVar('_unapply__B')  # <B>
        _unapply__C = typing.TypeVar('_unapply__C')  # <C>
        def unapply(self, x: 'Tuple3'[_unapply__A, _unapply__B, _unapply__C]) -> 'Option'['Tuple3'[_unapply__A, _unapply__B, _unapply__C]]: ...
    class any2stringadd(typing.Generic[_Predef__any2stringadd__A]):
        def __init__(self, self): ...
        def $plus(self, other: str) -> str: ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def scala$Predef$any2stringadd$$self(self) -> _Predef__any2stringadd__A: ...
    class any2stringadd$:
        MODULE$: typing.ClassVar['Predef.any2stringadd.'] = ...
        def __init__(self): ...
        _$plus$extension__A = typing.TypeVar('_$plus$extension__A')  # <A>
        def $plus$extension(self, $this: _.plus.extension__A, other: str) -> str: ...
        _equals$extension__A = typing.TypeVar('_equals$extension__A')  # <A>
        def equals$extension(self, $this: _equals.extension__A, x$1: typing.Any) -> bool: ...
        _hashCode$extension__A = typing.TypeVar('_hashCode$extension__A')  # <A>
        def hashCode$extension(self, $this: _hashCode.extension__A) -> int: ...

class Product(Equals):
    @staticmethod
    def $init$($this: 'Product') -> None: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...

_Responder__A = typing.TypeVar('_Responder__A')  # <A>
class Responder(Serializable, typing.Generic[_Responder__A]):
    def __init__(self): ...
    _constant__A = typing.TypeVar('_constant__A')  # <A>
    @staticmethod
    def constant(x: _constant__A) -> 'Responder'[_constant__A]: ...
    def filter(self, p: Function1[_Responder__A, typing.Any]) -> 'Responder'[_Responder__A]: ...
    _flatMap__B = typing.TypeVar('_flatMap__B')  # <B>
    def flatMap(self, f: Function1[_Responder__A, 'Responder'[_flatMap__B]]) -> 'Responder'[_flatMap__B]: ...
    def foreach(self, k: Function1[_Responder__A, scala.runtime.BoxedUnit]) -> None: ...
    _loop__A = typing.TypeVar('_loop__A')  # <A>
    @staticmethod
    def loop(r: 'Responder'[scala.runtime.BoxedUnit]) -> 'Responder'[scala.runtime.Nothing.]: ...
    _loopWhile__A = typing.TypeVar('_loopWhile__A')  # <A>
    @staticmethod
    def loopWhile(cond: Function0[typing.Any], r: 'Responder'[scala.runtime.BoxedUnit]) -> 'Responder'[scala.runtime.BoxedUnit]: ...
    _map__B = typing.TypeVar('_map__B')  # <B>
    def map(self, f: Function1[_Responder__A, _map__B]) -> 'Responder'[_map__B]: ...
    def respond(self, k: Function1[_Responder__A, scala.runtime.BoxedUnit]) -> None: ...
    _run__A = typing.TypeVar('_run__A')  # <A>
    @staticmethod
    def run(r: 'Responder'[_run__A]) -> 'Option'[_run__A]: ...
    def toString(self) -> str: ...

class Symbol(Serializable):
    def __init__(self, name: str): ...
    @staticmethod
    def apply(name: str) -> 'Symbol': ...
    def equals(self, other: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def name(self) -> str: ...
    def toString(self) -> str: ...
    @staticmethod
    def unapply(other: typing.Any) -> 'Option': ...

_Option__A = typing.TypeVar('_Option__A')  # <A>
class Option(Product, Serializable, typing.Generic[_Option__A]):
    serialVersionUID: typing.ClassVar[int] = ...
    def __init__(self): ...
    _apply__A = typing.TypeVar('_apply__A')  # <A>
    @staticmethod
    def apply(x: _apply__A) -> 'Option'[_apply__A]: ...
    _collect__B = typing.TypeVar('_collect__B')  # <B>
    def collect(self, pf: 'PartialFunction'[_Option__A, _collect__B]) -> 'Option'[_collect__B]: ...
    _contains__A1 = typing.TypeVar('_contains__A1')  # <A1>
    def contains(self, elem: _contains__A1) -> bool: ...
    _empty__A = typing.TypeVar('_empty__A')  # <A>
    @staticmethod
    def empty() -> 'Option'[_empty__A]: ...
    def exists(self, p: Function1[_Option__A, typing.Any]) -> bool: ...
    def filter(self, p: Function1[_Option__A, typing.Any]) -> 'Option'[_Option__A]: ...
    def filterNot(self, p: Function1[_Option__A, typing.Any]) -> 'Option'[_Option__A]: ...
    _flatMap__B = typing.TypeVar('_flatMap__B')  # <B>
    def flatMap(self, f: Function1[_Option__A, 'Option'[_flatMap__B]]) -> 'Option'[_flatMap__B]: ...
    _flatten__B = typing.TypeVar('_flatten__B')  # <B>
    def flatten(self, ev: Predef..less.colon.less[_Option__A, 'Option'[_flatten__B]]) -> 'Option'[_flatten__B]: ...
    _fold__B = typing.TypeVar('_fold__B')  # <B>
    def fold(self, ifEmpty: Function0[_fold__B], f: Function1[_Option__A, _fold__B]) -> _fold__B: ...
    def forall(self, p: Function1[_Option__A, typing.Any]) -> bool: ...
    _foreach__U = typing.TypeVar('_foreach__U')  # <U>
    def foreach(self, f: Function1[_Option__A, _foreach__U]) -> None: ...
    def get(self) -> _Option__A: ...
    _getOrElse__B = typing.TypeVar('_getOrElse__B')  # <B>
    def getOrElse(self, default: Function0[_getOrElse__B]) -> _getOrElse__B: ...
    def isDefined(self) -> bool: ...
    def isEmpty(self) -> bool: ...
    def iterator(self) -> scala.collection.Iterator[_Option__A]: ...
    _map__B = typing.TypeVar('_map__B')  # <B>
    def map(self, f: Function1[_Option__A, _map__B]) -> 'Option'[_map__B]: ...
    def nonEmpty(self) -> bool: ...
    _option2Iterable__A = typing.TypeVar('_option2Iterable__A')  # <A>
    @staticmethod
    def option2Iterable(xo: 'Option'[_option2Iterable__A]) -> scala.collection.Iterable[_option2Iterable__A]: ...
    _orElse__B = typing.TypeVar('_orElse__B')  # <B>
    def orElse(self, alternative: Function0['Option'[_orElse__B]]) -> 'Option'[_orElse__B]: ...
    _orNull__A1 = typing.TypeVar('_orNull__A1')  # <A1>
    def orNull(self, ev: Predef..less.colon.less[scala.runtime.Null., _orNull__A1]) -> _orNull__A1: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    _toLeft__X = typing.TypeVar('_toLeft__X')  # <X>
    def toLeft(self, right: Function0[_toLeft__X]) -> scala.util.Either[_Option__A, _toLeft__X]: ...
    def toList(self) -> scala.collection.immutable.List[_Option__A]: ...
    _toRight__X = typing.TypeVar('_toRight__X')  # <X>
    def toRight(self, left: Function0[_toRight__X]) -> scala.util.Either[_toRight__X, _Option__A]: ...
    def withFilter(self, p: Function1[_Option__A, typing.Any]) -> 'Option.WithFilter': ...
    class WithFilter:
        $outer: 'Option' = ...
        def __init__(self, $outer: 'Option', p: Function1[_Option__A, typing.Any]): ...
        _flatMap__B = typing.TypeVar('_flatMap__B')  # <B>
        def flatMap(self, f: Function1[_Option__A, 'Option'[_flatMap__B]]) -> 'Option'[_flatMap__B]: ...
        _foreach__U = typing.TypeVar('_foreach__U')  # <U>
        def foreach(self, f: Function1[_Option__A, _foreach__U]) -> None: ...
        _map__B = typing.TypeVar('_map__B')  # <B>
        def map(self, f: Function1[_Option__A, _map__B]) -> 'Option'[_map__B]: ...
        def withFilter(self, q: Function1[_Option__A, typing.Any]) -> 'Option.WithFilter': ...

_Product1__T1 = typing.TypeVar('_Product1__T1')  # <T1>
class Product1(Product, typing.Generic[_Product1__T1]):
    @staticmethod
    def $init$($this: 'Product1') -> None: ...
    def _1(self) -> _Product1__T1: ...
    def _1$mcD$sp(self) -> float: ...
    def _1$mcI$sp(self) -> int: ...
    def _1$mcJ$sp(self) -> int: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    @staticmethod
    def unapply(x: 'Product1'[_unapply__T1]) -> Option['Product1'[_unapply__T1]]: ...

_Product10__T1 = typing.TypeVar('_Product10__T1')  # <T1>
_Product10__T2 = typing.TypeVar('_Product10__T2')  # <T2>
_Product10__T3 = typing.TypeVar('_Product10__T3')  # <T3>
_Product10__T4 = typing.TypeVar('_Product10__T4')  # <T4>
_Product10__T5 = typing.TypeVar('_Product10__T5')  # <T5>
_Product10__T6 = typing.TypeVar('_Product10__T6')  # <T6>
_Product10__T7 = typing.TypeVar('_Product10__T7')  # <T7>
_Product10__T8 = typing.TypeVar('_Product10__T8')  # <T8>
_Product10__T9 = typing.TypeVar('_Product10__T9')  # <T9>
_Product10__T10 = typing.TypeVar('_Product10__T10')  # <T10>
class Product10(Product, typing.Generic[_Product10__T1, _Product10__T2, _Product10__T3, _Product10__T4, _Product10__T5, _Product10__T6, _Product10__T7, _Product10__T8, _Product10__T9, _Product10__T10]):
    @staticmethod
    def $init$($this: 'Product10') -> None: ...
    def _1(self) -> _Product10__T1: ...
    def _10(self) -> _Product10__T10: ...
    def _2(self) -> _Product10__T2: ...
    def _3(self) -> _Product10__T3: ...
    def _4(self) -> _Product10__T4: ...
    def _5(self) -> _Product10__T5: ...
    def _6(self) -> _Product10__T6: ...
    def _7(self) -> _Product10__T7: ...
    def _8(self) -> _Product10__T8: ...
    def _9(self) -> _Product10__T9: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    @staticmethod
    def unapply(x: 'Product10'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10]) -> Option['Product10'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10]]: ...

_Product11__T1 = typing.TypeVar('_Product11__T1')  # <T1>
_Product11__T2 = typing.TypeVar('_Product11__T2')  # <T2>
_Product11__T3 = typing.TypeVar('_Product11__T3')  # <T3>
_Product11__T4 = typing.TypeVar('_Product11__T4')  # <T4>
_Product11__T5 = typing.TypeVar('_Product11__T5')  # <T5>
_Product11__T6 = typing.TypeVar('_Product11__T6')  # <T6>
_Product11__T7 = typing.TypeVar('_Product11__T7')  # <T7>
_Product11__T8 = typing.TypeVar('_Product11__T8')  # <T8>
_Product11__T9 = typing.TypeVar('_Product11__T9')  # <T9>
_Product11__T10 = typing.TypeVar('_Product11__T10')  # <T10>
_Product11__T11 = typing.TypeVar('_Product11__T11')  # <T11>
class Product11(Product, typing.Generic[_Product11__T1, _Product11__T2, _Product11__T3, _Product11__T4, _Product11__T5, _Product11__T6, _Product11__T7, _Product11__T8, _Product11__T9, _Product11__T10, _Product11__T11]):
    @staticmethod
    def $init$($this: 'Product11') -> None: ...
    def _1(self) -> _Product11__T1: ...
    def _10(self) -> _Product11__T10: ...
    def _11(self) -> _Product11__T11: ...
    def _2(self) -> _Product11__T2: ...
    def _3(self) -> _Product11__T3: ...
    def _4(self) -> _Product11__T4: ...
    def _5(self) -> _Product11__T5: ...
    def _6(self) -> _Product11__T6: ...
    def _7(self) -> _Product11__T7: ...
    def _8(self) -> _Product11__T8: ...
    def _9(self) -> _Product11__T9: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    @staticmethod
    def unapply(x: 'Product11'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11]) -> Option['Product11'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11]]: ...

_Product12__T1 = typing.TypeVar('_Product12__T1')  # <T1>
_Product12__T2 = typing.TypeVar('_Product12__T2')  # <T2>
_Product12__T3 = typing.TypeVar('_Product12__T3')  # <T3>
_Product12__T4 = typing.TypeVar('_Product12__T4')  # <T4>
_Product12__T5 = typing.TypeVar('_Product12__T5')  # <T5>
_Product12__T6 = typing.TypeVar('_Product12__T6')  # <T6>
_Product12__T7 = typing.TypeVar('_Product12__T7')  # <T7>
_Product12__T8 = typing.TypeVar('_Product12__T8')  # <T8>
_Product12__T9 = typing.TypeVar('_Product12__T9')  # <T9>
_Product12__T10 = typing.TypeVar('_Product12__T10')  # <T10>
_Product12__T11 = typing.TypeVar('_Product12__T11')  # <T11>
_Product12__T12 = typing.TypeVar('_Product12__T12')  # <T12>
class Product12(Product, typing.Generic[_Product12__T1, _Product12__T2, _Product12__T3, _Product12__T4, _Product12__T5, _Product12__T6, _Product12__T7, _Product12__T8, _Product12__T9, _Product12__T10, _Product12__T11, _Product12__T12]):
    @staticmethod
    def $init$($this: 'Product12') -> None: ...
    def _1(self) -> _Product12__T1: ...
    def _10(self) -> _Product12__T10: ...
    def _11(self) -> _Product12__T11: ...
    def _12(self) -> _Product12__T12: ...
    def _2(self) -> _Product12__T2: ...
    def _3(self) -> _Product12__T3: ...
    def _4(self) -> _Product12__T4: ...
    def _5(self) -> _Product12__T5: ...
    def _6(self) -> _Product12__T6: ...
    def _7(self) -> _Product12__T7: ...
    def _8(self) -> _Product12__T8: ...
    def _9(self) -> _Product12__T9: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    @staticmethod
    def unapply(x: 'Product12'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12]) -> Option['Product12'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12]]: ...

_Product13__T1 = typing.TypeVar('_Product13__T1')  # <T1>
_Product13__T2 = typing.TypeVar('_Product13__T2')  # <T2>
_Product13__T3 = typing.TypeVar('_Product13__T3')  # <T3>
_Product13__T4 = typing.TypeVar('_Product13__T4')  # <T4>
_Product13__T5 = typing.TypeVar('_Product13__T5')  # <T5>
_Product13__T6 = typing.TypeVar('_Product13__T6')  # <T6>
_Product13__T7 = typing.TypeVar('_Product13__T7')  # <T7>
_Product13__T8 = typing.TypeVar('_Product13__T8')  # <T8>
_Product13__T9 = typing.TypeVar('_Product13__T9')  # <T9>
_Product13__T10 = typing.TypeVar('_Product13__T10')  # <T10>
_Product13__T11 = typing.TypeVar('_Product13__T11')  # <T11>
_Product13__T12 = typing.TypeVar('_Product13__T12')  # <T12>
_Product13__T13 = typing.TypeVar('_Product13__T13')  # <T13>
class Product13(Product, typing.Generic[_Product13__T1, _Product13__T2, _Product13__T3, _Product13__T4, _Product13__T5, _Product13__T6, _Product13__T7, _Product13__T8, _Product13__T9, _Product13__T10, _Product13__T11, _Product13__T12, _Product13__T13]):
    @staticmethod
    def $init$($this: 'Product13') -> None: ...
    def _1(self) -> _Product13__T1: ...
    def _10(self) -> _Product13__T10: ...
    def _11(self) -> _Product13__T11: ...
    def _12(self) -> _Product13__T12: ...
    def _13(self) -> _Product13__T13: ...
    def _2(self) -> _Product13__T2: ...
    def _3(self) -> _Product13__T3: ...
    def _4(self) -> _Product13__T4: ...
    def _5(self) -> _Product13__T5: ...
    def _6(self) -> _Product13__T6: ...
    def _7(self) -> _Product13__T7: ...
    def _8(self) -> _Product13__T8: ...
    def _9(self) -> _Product13__T9: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    @staticmethod
    def unapply(x: 'Product13'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13]) -> Option['Product13'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13]]: ...

_Product14__T1 = typing.TypeVar('_Product14__T1')  # <T1>
_Product14__T2 = typing.TypeVar('_Product14__T2')  # <T2>
_Product14__T3 = typing.TypeVar('_Product14__T3')  # <T3>
_Product14__T4 = typing.TypeVar('_Product14__T4')  # <T4>
_Product14__T5 = typing.TypeVar('_Product14__T5')  # <T5>
_Product14__T6 = typing.TypeVar('_Product14__T6')  # <T6>
_Product14__T7 = typing.TypeVar('_Product14__T7')  # <T7>
_Product14__T8 = typing.TypeVar('_Product14__T8')  # <T8>
_Product14__T9 = typing.TypeVar('_Product14__T9')  # <T9>
_Product14__T10 = typing.TypeVar('_Product14__T10')  # <T10>
_Product14__T11 = typing.TypeVar('_Product14__T11')  # <T11>
_Product14__T12 = typing.TypeVar('_Product14__T12')  # <T12>
_Product14__T13 = typing.TypeVar('_Product14__T13')  # <T13>
_Product14__T14 = typing.TypeVar('_Product14__T14')  # <T14>
class Product14(Product, typing.Generic[_Product14__T1, _Product14__T2, _Product14__T3, _Product14__T4, _Product14__T5, _Product14__T6, _Product14__T7, _Product14__T8, _Product14__T9, _Product14__T10, _Product14__T11, _Product14__T12, _Product14__T13, _Product14__T14]):
    @staticmethod
    def $init$($this: 'Product14') -> None: ...
    def _1(self) -> _Product14__T1: ...
    def _10(self) -> _Product14__T10: ...
    def _11(self) -> _Product14__T11: ...
    def _12(self) -> _Product14__T12: ...
    def _13(self) -> _Product14__T13: ...
    def _14(self) -> _Product14__T14: ...
    def _2(self) -> _Product14__T2: ...
    def _3(self) -> _Product14__T3: ...
    def _4(self) -> _Product14__T4: ...
    def _5(self) -> _Product14__T5: ...
    def _6(self) -> _Product14__T6: ...
    def _7(self) -> _Product14__T7: ...
    def _8(self) -> _Product14__T8: ...
    def _9(self) -> _Product14__T9: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    @staticmethod
    def unapply(x: 'Product14'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14]) -> Option['Product14'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14]]: ...

_Product15__T1 = typing.TypeVar('_Product15__T1')  # <T1>
_Product15__T2 = typing.TypeVar('_Product15__T2')  # <T2>
_Product15__T3 = typing.TypeVar('_Product15__T3')  # <T3>
_Product15__T4 = typing.TypeVar('_Product15__T4')  # <T4>
_Product15__T5 = typing.TypeVar('_Product15__T5')  # <T5>
_Product15__T6 = typing.TypeVar('_Product15__T6')  # <T6>
_Product15__T7 = typing.TypeVar('_Product15__T7')  # <T7>
_Product15__T8 = typing.TypeVar('_Product15__T8')  # <T8>
_Product15__T9 = typing.TypeVar('_Product15__T9')  # <T9>
_Product15__T10 = typing.TypeVar('_Product15__T10')  # <T10>
_Product15__T11 = typing.TypeVar('_Product15__T11')  # <T11>
_Product15__T12 = typing.TypeVar('_Product15__T12')  # <T12>
_Product15__T13 = typing.TypeVar('_Product15__T13')  # <T13>
_Product15__T14 = typing.TypeVar('_Product15__T14')  # <T14>
_Product15__T15 = typing.TypeVar('_Product15__T15')  # <T15>
class Product15(Product, typing.Generic[_Product15__T1, _Product15__T2, _Product15__T3, _Product15__T4, _Product15__T5, _Product15__T6, _Product15__T7, _Product15__T8, _Product15__T9, _Product15__T10, _Product15__T11, _Product15__T12, _Product15__T13, _Product15__T14, _Product15__T15]):
    @staticmethod
    def $init$($this: 'Product15') -> None: ...
    def _1(self) -> _Product15__T1: ...
    def _10(self) -> _Product15__T10: ...
    def _11(self) -> _Product15__T11: ...
    def _12(self) -> _Product15__T12: ...
    def _13(self) -> _Product15__T13: ...
    def _14(self) -> _Product15__T14: ...
    def _15(self) -> _Product15__T15: ...
    def _2(self) -> _Product15__T2: ...
    def _3(self) -> _Product15__T3: ...
    def _4(self) -> _Product15__T4: ...
    def _5(self) -> _Product15__T5: ...
    def _6(self) -> _Product15__T6: ...
    def _7(self) -> _Product15__T7: ...
    def _8(self) -> _Product15__T8: ...
    def _9(self) -> _Product15__T9: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    @staticmethod
    def unapply(x: 'Product15'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15]) -> Option['Product15'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15]]: ...

_Product16__T1 = typing.TypeVar('_Product16__T1')  # <T1>
_Product16__T2 = typing.TypeVar('_Product16__T2')  # <T2>
_Product16__T3 = typing.TypeVar('_Product16__T3')  # <T3>
_Product16__T4 = typing.TypeVar('_Product16__T4')  # <T4>
_Product16__T5 = typing.TypeVar('_Product16__T5')  # <T5>
_Product16__T6 = typing.TypeVar('_Product16__T6')  # <T6>
_Product16__T7 = typing.TypeVar('_Product16__T7')  # <T7>
_Product16__T8 = typing.TypeVar('_Product16__T8')  # <T8>
_Product16__T9 = typing.TypeVar('_Product16__T9')  # <T9>
_Product16__T10 = typing.TypeVar('_Product16__T10')  # <T10>
_Product16__T11 = typing.TypeVar('_Product16__T11')  # <T11>
_Product16__T12 = typing.TypeVar('_Product16__T12')  # <T12>
_Product16__T13 = typing.TypeVar('_Product16__T13')  # <T13>
_Product16__T14 = typing.TypeVar('_Product16__T14')  # <T14>
_Product16__T15 = typing.TypeVar('_Product16__T15')  # <T15>
_Product16__T16 = typing.TypeVar('_Product16__T16')  # <T16>
class Product16(Product, typing.Generic[_Product16__T1, _Product16__T2, _Product16__T3, _Product16__T4, _Product16__T5, _Product16__T6, _Product16__T7, _Product16__T8, _Product16__T9, _Product16__T10, _Product16__T11, _Product16__T12, _Product16__T13, _Product16__T14, _Product16__T15, _Product16__T16]):
    @staticmethod
    def $init$($this: 'Product16') -> None: ...
    def _1(self) -> _Product16__T1: ...
    def _10(self) -> _Product16__T10: ...
    def _11(self) -> _Product16__T11: ...
    def _12(self) -> _Product16__T12: ...
    def _13(self) -> _Product16__T13: ...
    def _14(self) -> _Product16__T14: ...
    def _15(self) -> _Product16__T15: ...
    def _16(self) -> _Product16__T16: ...
    def _2(self) -> _Product16__T2: ...
    def _3(self) -> _Product16__T3: ...
    def _4(self) -> _Product16__T4: ...
    def _5(self) -> _Product16__T5: ...
    def _6(self) -> _Product16__T6: ...
    def _7(self) -> _Product16__T7: ...
    def _8(self) -> _Product16__T8: ...
    def _9(self) -> _Product16__T9: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    _unapply__T16 = typing.TypeVar('_unapply__T16')  # <T16>
    @staticmethod
    def unapply(x: 'Product16'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16]) -> Option['Product16'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16]]: ...

_Product17__T1 = typing.TypeVar('_Product17__T1')  # <T1>
_Product17__T2 = typing.TypeVar('_Product17__T2')  # <T2>
_Product17__T3 = typing.TypeVar('_Product17__T3')  # <T3>
_Product17__T4 = typing.TypeVar('_Product17__T4')  # <T4>
_Product17__T5 = typing.TypeVar('_Product17__T5')  # <T5>
_Product17__T6 = typing.TypeVar('_Product17__T6')  # <T6>
_Product17__T7 = typing.TypeVar('_Product17__T7')  # <T7>
_Product17__T8 = typing.TypeVar('_Product17__T8')  # <T8>
_Product17__T9 = typing.TypeVar('_Product17__T9')  # <T9>
_Product17__T10 = typing.TypeVar('_Product17__T10')  # <T10>
_Product17__T11 = typing.TypeVar('_Product17__T11')  # <T11>
_Product17__T12 = typing.TypeVar('_Product17__T12')  # <T12>
_Product17__T13 = typing.TypeVar('_Product17__T13')  # <T13>
_Product17__T14 = typing.TypeVar('_Product17__T14')  # <T14>
_Product17__T15 = typing.TypeVar('_Product17__T15')  # <T15>
_Product17__T16 = typing.TypeVar('_Product17__T16')  # <T16>
_Product17__T17 = typing.TypeVar('_Product17__T17')  # <T17>
class Product17(Product, typing.Generic[_Product17__T1, _Product17__T2, _Product17__T3, _Product17__T4, _Product17__T5, _Product17__T6, _Product17__T7, _Product17__T8, _Product17__T9, _Product17__T10, _Product17__T11, _Product17__T12, _Product17__T13, _Product17__T14, _Product17__T15, _Product17__T16, _Product17__T17]):
    @staticmethod
    def $init$($this: 'Product17') -> None: ...
    def _1(self) -> _Product17__T1: ...
    def _10(self) -> _Product17__T10: ...
    def _11(self) -> _Product17__T11: ...
    def _12(self) -> _Product17__T12: ...
    def _13(self) -> _Product17__T13: ...
    def _14(self) -> _Product17__T14: ...
    def _15(self) -> _Product17__T15: ...
    def _16(self) -> _Product17__T16: ...
    def _17(self) -> _Product17__T17: ...
    def _2(self) -> _Product17__T2: ...
    def _3(self) -> _Product17__T3: ...
    def _4(self) -> _Product17__T4: ...
    def _5(self) -> _Product17__T5: ...
    def _6(self) -> _Product17__T6: ...
    def _7(self) -> _Product17__T7: ...
    def _8(self) -> _Product17__T8: ...
    def _9(self) -> _Product17__T9: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    _unapply__T16 = typing.TypeVar('_unapply__T16')  # <T16>
    _unapply__T17 = typing.TypeVar('_unapply__T17')  # <T17>
    @staticmethod
    def unapply(x: 'Product17'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17]) -> Option['Product17'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17]]: ...

_Product18__T1 = typing.TypeVar('_Product18__T1')  # <T1>
_Product18__T2 = typing.TypeVar('_Product18__T2')  # <T2>
_Product18__T3 = typing.TypeVar('_Product18__T3')  # <T3>
_Product18__T4 = typing.TypeVar('_Product18__T4')  # <T4>
_Product18__T5 = typing.TypeVar('_Product18__T5')  # <T5>
_Product18__T6 = typing.TypeVar('_Product18__T6')  # <T6>
_Product18__T7 = typing.TypeVar('_Product18__T7')  # <T7>
_Product18__T8 = typing.TypeVar('_Product18__T8')  # <T8>
_Product18__T9 = typing.TypeVar('_Product18__T9')  # <T9>
_Product18__T10 = typing.TypeVar('_Product18__T10')  # <T10>
_Product18__T11 = typing.TypeVar('_Product18__T11')  # <T11>
_Product18__T12 = typing.TypeVar('_Product18__T12')  # <T12>
_Product18__T13 = typing.TypeVar('_Product18__T13')  # <T13>
_Product18__T14 = typing.TypeVar('_Product18__T14')  # <T14>
_Product18__T15 = typing.TypeVar('_Product18__T15')  # <T15>
_Product18__T16 = typing.TypeVar('_Product18__T16')  # <T16>
_Product18__T17 = typing.TypeVar('_Product18__T17')  # <T17>
_Product18__T18 = typing.TypeVar('_Product18__T18')  # <T18>
class Product18(Product, typing.Generic[_Product18__T1, _Product18__T2, _Product18__T3, _Product18__T4, _Product18__T5, _Product18__T6, _Product18__T7, _Product18__T8, _Product18__T9, _Product18__T10, _Product18__T11, _Product18__T12, _Product18__T13, _Product18__T14, _Product18__T15, _Product18__T16, _Product18__T17, _Product18__T18]):
    @staticmethod
    def $init$($this: 'Product18') -> None: ...
    def _1(self) -> _Product18__T1: ...
    def _10(self) -> _Product18__T10: ...
    def _11(self) -> _Product18__T11: ...
    def _12(self) -> _Product18__T12: ...
    def _13(self) -> _Product18__T13: ...
    def _14(self) -> _Product18__T14: ...
    def _15(self) -> _Product18__T15: ...
    def _16(self) -> _Product18__T16: ...
    def _17(self) -> _Product18__T17: ...
    def _18(self) -> _Product18__T18: ...
    def _2(self) -> _Product18__T2: ...
    def _3(self) -> _Product18__T3: ...
    def _4(self) -> _Product18__T4: ...
    def _5(self) -> _Product18__T5: ...
    def _6(self) -> _Product18__T6: ...
    def _7(self) -> _Product18__T7: ...
    def _8(self) -> _Product18__T8: ...
    def _9(self) -> _Product18__T9: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    _unapply__T16 = typing.TypeVar('_unapply__T16')  # <T16>
    _unapply__T17 = typing.TypeVar('_unapply__T17')  # <T17>
    _unapply__T18 = typing.TypeVar('_unapply__T18')  # <T18>
    @staticmethod
    def unapply(x: 'Product18'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18]) -> Option['Product18'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18]]: ...

_Product19__T1 = typing.TypeVar('_Product19__T1')  # <T1>
_Product19__T2 = typing.TypeVar('_Product19__T2')  # <T2>
_Product19__T3 = typing.TypeVar('_Product19__T3')  # <T3>
_Product19__T4 = typing.TypeVar('_Product19__T4')  # <T4>
_Product19__T5 = typing.TypeVar('_Product19__T5')  # <T5>
_Product19__T6 = typing.TypeVar('_Product19__T6')  # <T6>
_Product19__T7 = typing.TypeVar('_Product19__T7')  # <T7>
_Product19__T8 = typing.TypeVar('_Product19__T8')  # <T8>
_Product19__T9 = typing.TypeVar('_Product19__T9')  # <T9>
_Product19__T10 = typing.TypeVar('_Product19__T10')  # <T10>
_Product19__T11 = typing.TypeVar('_Product19__T11')  # <T11>
_Product19__T12 = typing.TypeVar('_Product19__T12')  # <T12>
_Product19__T13 = typing.TypeVar('_Product19__T13')  # <T13>
_Product19__T14 = typing.TypeVar('_Product19__T14')  # <T14>
_Product19__T15 = typing.TypeVar('_Product19__T15')  # <T15>
_Product19__T16 = typing.TypeVar('_Product19__T16')  # <T16>
_Product19__T17 = typing.TypeVar('_Product19__T17')  # <T17>
_Product19__T18 = typing.TypeVar('_Product19__T18')  # <T18>
_Product19__T19 = typing.TypeVar('_Product19__T19')  # <T19>
class Product19(Product, typing.Generic[_Product19__T1, _Product19__T2, _Product19__T3, _Product19__T4, _Product19__T5, _Product19__T6, _Product19__T7, _Product19__T8, _Product19__T9, _Product19__T10, _Product19__T11, _Product19__T12, _Product19__T13, _Product19__T14, _Product19__T15, _Product19__T16, _Product19__T17, _Product19__T18, _Product19__T19]):
    @staticmethod
    def $init$($this: 'Product19') -> None: ...
    def _1(self) -> _Product19__T1: ...
    def _10(self) -> _Product19__T10: ...
    def _11(self) -> _Product19__T11: ...
    def _12(self) -> _Product19__T12: ...
    def _13(self) -> _Product19__T13: ...
    def _14(self) -> _Product19__T14: ...
    def _15(self) -> _Product19__T15: ...
    def _16(self) -> _Product19__T16: ...
    def _17(self) -> _Product19__T17: ...
    def _18(self) -> _Product19__T18: ...
    def _19(self) -> _Product19__T19: ...
    def _2(self) -> _Product19__T2: ...
    def _3(self) -> _Product19__T3: ...
    def _4(self) -> _Product19__T4: ...
    def _5(self) -> _Product19__T5: ...
    def _6(self) -> _Product19__T6: ...
    def _7(self) -> _Product19__T7: ...
    def _8(self) -> _Product19__T8: ...
    def _9(self) -> _Product19__T9: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    _unapply__T16 = typing.TypeVar('_unapply__T16')  # <T16>
    _unapply__T17 = typing.TypeVar('_unapply__T17')  # <T17>
    _unapply__T18 = typing.TypeVar('_unapply__T18')  # <T18>
    _unapply__T19 = typing.TypeVar('_unapply__T19')  # <T19>
    @staticmethod
    def unapply(x: 'Product19'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19]) -> Option['Product19'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19]]: ...

_Product2__T1 = typing.TypeVar('_Product2__T1')  # <T1>
_Product2__T2 = typing.TypeVar('_Product2__T2')  # <T2>
class Product2(Product, typing.Generic[_Product2__T1, _Product2__T2]):
    @staticmethod
    def $init$($this: 'Product2') -> None: ...
    def _1(self) -> _Product2__T1: ...
    def _1$mcD$sp(self) -> float: ...
    def _1$mcI$sp(self) -> int: ...
    def _1$mcJ$sp(self) -> int: ...
    def _2(self) -> _Product2__T2: ...
    def _2$mcD$sp(self) -> float: ...
    def _2$mcI$sp(self) -> int: ...
    def _2$mcJ$sp(self) -> int: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    @staticmethod
    def unapply(x: 'Product2'[_unapply__T1, _unapply__T2]) -> Option['Product2'[_unapply__T1, _unapply__T2]]: ...

_Product20__T1 = typing.TypeVar('_Product20__T1')  # <T1>
_Product20__T2 = typing.TypeVar('_Product20__T2')  # <T2>
_Product20__T3 = typing.TypeVar('_Product20__T3')  # <T3>
_Product20__T4 = typing.TypeVar('_Product20__T4')  # <T4>
_Product20__T5 = typing.TypeVar('_Product20__T5')  # <T5>
_Product20__T6 = typing.TypeVar('_Product20__T6')  # <T6>
_Product20__T7 = typing.TypeVar('_Product20__T7')  # <T7>
_Product20__T8 = typing.TypeVar('_Product20__T8')  # <T8>
_Product20__T9 = typing.TypeVar('_Product20__T9')  # <T9>
_Product20__T10 = typing.TypeVar('_Product20__T10')  # <T10>
_Product20__T11 = typing.TypeVar('_Product20__T11')  # <T11>
_Product20__T12 = typing.TypeVar('_Product20__T12')  # <T12>
_Product20__T13 = typing.TypeVar('_Product20__T13')  # <T13>
_Product20__T14 = typing.TypeVar('_Product20__T14')  # <T14>
_Product20__T15 = typing.TypeVar('_Product20__T15')  # <T15>
_Product20__T16 = typing.TypeVar('_Product20__T16')  # <T16>
_Product20__T17 = typing.TypeVar('_Product20__T17')  # <T17>
_Product20__T18 = typing.TypeVar('_Product20__T18')  # <T18>
_Product20__T19 = typing.TypeVar('_Product20__T19')  # <T19>
_Product20__T20 = typing.TypeVar('_Product20__T20')  # <T20>
class Product20(Product, typing.Generic[_Product20__T1, _Product20__T2, _Product20__T3, _Product20__T4, _Product20__T5, _Product20__T6, _Product20__T7, _Product20__T8, _Product20__T9, _Product20__T10, _Product20__T11, _Product20__T12, _Product20__T13, _Product20__T14, _Product20__T15, _Product20__T16, _Product20__T17, _Product20__T18, _Product20__T19, _Product20__T20]):
    @staticmethod
    def $init$($this: 'Product20') -> None: ...
    def _1(self) -> _Product20__T1: ...
    def _10(self) -> _Product20__T10: ...
    def _11(self) -> _Product20__T11: ...
    def _12(self) -> _Product20__T12: ...
    def _13(self) -> _Product20__T13: ...
    def _14(self) -> _Product20__T14: ...
    def _15(self) -> _Product20__T15: ...
    def _16(self) -> _Product20__T16: ...
    def _17(self) -> _Product20__T17: ...
    def _18(self) -> _Product20__T18: ...
    def _19(self) -> _Product20__T19: ...
    def _2(self) -> _Product20__T2: ...
    def _20(self) -> _Product20__T20: ...
    def _3(self) -> _Product20__T3: ...
    def _4(self) -> _Product20__T4: ...
    def _5(self) -> _Product20__T5: ...
    def _6(self) -> _Product20__T6: ...
    def _7(self) -> _Product20__T7: ...
    def _8(self) -> _Product20__T8: ...
    def _9(self) -> _Product20__T9: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    _unapply__T16 = typing.TypeVar('_unapply__T16')  # <T16>
    _unapply__T17 = typing.TypeVar('_unapply__T17')  # <T17>
    _unapply__T18 = typing.TypeVar('_unapply__T18')  # <T18>
    _unapply__T19 = typing.TypeVar('_unapply__T19')  # <T19>
    _unapply__T20 = typing.TypeVar('_unapply__T20')  # <T20>
    @staticmethod
    def unapply(x: 'Product20'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19, _unapply__T20]) -> Option['Product20'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19, _unapply__T20]]: ...

_Product21__T1 = typing.TypeVar('_Product21__T1')  # <T1>
_Product21__T2 = typing.TypeVar('_Product21__T2')  # <T2>
_Product21__T3 = typing.TypeVar('_Product21__T3')  # <T3>
_Product21__T4 = typing.TypeVar('_Product21__T4')  # <T4>
_Product21__T5 = typing.TypeVar('_Product21__T5')  # <T5>
_Product21__T6 = typing.TypeVar('_Product21__T6')  # <T6>
_Product21__T7 = typing.TypeVar('_Product21__T7')  # <T7>
_Product21__T8 = typing.TypeVar('_Product21__T8')  # <T8>
_Product21__T9 = typing.TypeVar('_Product21__T9')  # <T9>
_Product21__T10 = typing.TypeVar('_Product21__T10')  # <T10>
_Product21__T11 = typing.TypeVar('_Product21__T11')  # <T11>
_Product21__T12 = typing.TypeVar('_Product21__T12')  # <T12>
_Product21__T13 = typing.TypeVar('_Product21__T13')  # <T13>
_Product21__T14 = typing.TypeVar('_Product21__T14')  # <T14>
_Product21__T15 = typing.TypeVar('_Product21__T15')  # <T15>
_Product21__T16 = typing.TypeVar('_Product21__T16')  # <T16>
_Product21__T17 = typing.TypeVar('_Product21__T17')  # <T17>
_Product21__T18 = typing.TypeVar('_Product21__T18')  # <T18>
_Product21__T19 = typing.TypeVar('_Product21__T19')  # <T19>
_Product21__T20 = typing.TypeVar('_Product21__T20')  # <T20>
_Product21__T21 = typing.TypeVar('_Product21__T21')  # <T21>
class Product21(Product, typing.Generic[_Product21__T1, _Product21__T2, _Product21__T3, _Product21__T4, _Product21__T5, _Product21__T6, _Product21__T7, _Product21__T8, _Product21__T9, _Product21__T10, _Product21__T11, _Product21__T12, _Product21__T13, _Product21__T14, _Product21__T15, _Product21__T16, _Product21__T17, _Product21__T18, _Product21__T19, _Product21__T20, _Product21__T21]):
    @staticmethod
    def $init$($this: 'Product21') -> None: ...
    def _1(self) -> _Product21__T1: ...
    def _10(self) -> _Product21__T10: ...
    def _11(self) -> _Product21__T11: ...
    def _12(self) -> _Product21__T12: ...
    def _13(self) -> _Product21__T13: ...
    def _14(self) -> _Product21__T14: ...
    def _15(self) -> _Product21__T15: ...
    def _16(self) -> _Product21__T16: ...
    def _17(self) -> _Product21__T17: ...
    def _18(self) -> _Product21__T18: ...
    def _19(self) -> _Product21__T19: ...
    def _2(self) -> _Product21__T2: ...
    def _20(self) -> _Product21__T20: ...
    def _21(self) -> _Product21__T21: ...
    def _3(self) -> _Product21__T3: ...
    def _4(self) -> _Product21__T4: ...
    def _5(self) -> _Product21__T5: ...
    def _6(self) -> _Product21__T6: ...
    def _7(self) -> _Product21__T7: ...
    def _8(self) -> _Product21__T8: ...
    def _9(self) -> _Product21__T9: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    _unapply__T16 = typing.TypeVar('_unapply__T16')  # <T16>
    _unapply__T17 = typing.TypeVar('_unapply__T17')  # <T17>
    _unapply__T18 = typing.TypeVar('_unapply__T18')  # <T18>
    _unapply__T19 = typing.TypeVar('_unapply__T19')  # <T19>
    _unapply__T20 = typing.TypeVar('_unapply__T20')  # <T20>
    _unapply__T21 = typing.TypeVar('_unapply__T21')  # <T21>
    @staticmethod
    def unapply(x: 'Product21'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19, _unapply__T20, _unapply__T21]) -> Option['Product21'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19, _unapply__T20, _unapply__T21]]: ...

_Product22__T1 = typing.TypeVar('_Product22__T1')  # <T1>
_Product22__T2 = typing.TypeVar('_Product22__T2')  # <T2>
_Product22__T3 = typing.TypeVar('_Product22__T3')  # <T3>
_Product22__T4 = typing.TypeVar('_Product22__T4')  # <T4>
_Product22__T5 = typing.TypeVar('_Product22__T5')  # <T5>
_Product22__T6 = typing.TypeVar('_Product22__T6')  # <T6>
_Product22__T7 = typing.TypeVar('_Product22__T7')  # <T7>
_Product22__T8 = typing.TypeVar('_Product22__T8')  # <T8>
_Product22__T9 = typing.TypeVar('_Product22__T9')  # <T9>
_Product22__T10 = typing.TypeVar('_Product22__T10')  # <T10>
_Product22__T11 = typing.TypeVar('_Product22__T11')  # <T11>
_Product22__T12 = typing.TypeVar('_Product22__T12')  # <T12>
_Product22__T13 = typing.TypeVar('_Product22__T13')  # <T13>
_Product22__T14 = typing.TypeVar('_Product22__T14')  # <T14>
_Product22__T15 = typing.TypeVar('_Product22__T15')  # <T15>
_Product22__T16 = typing.TypeVar('_Product22__T16')  # <T16>
_Product22__T17 = typing.TypeVar('_Product22__T17')  # <T17>
_Product22__T18 = typing.TypeVar('_Product22__T18')  # <T18>
_Product22__T19 = typing.TypeVar('_Product22__T19')  # <T19>
_Product22__T20 = typing.TypeVar('_Product22__T20')  # <T20>
_Product22__T21 = typing.TypeVar('_Product22__T21')  # <T21>
_Product22__T22 = typing.TypeVar('_Product22__T22')  # <T22>
class Product22(Product, typing.Generic[_Product22__T1, _Product22__T2, _Product22__T3, _Product22__T4, _Product22__T5, _Product22__T6, _Product22__T7, _Product22__T8, _Product22__T9, _Product22__T10, _Product22__T11, _Product22__T12, _Product22__T13, _Product22__T14, _Product22__T15, _Product22__T16, _Product22__T17, _Product22__T18, _Product22__T19, _Product22__T20, _Product22__T21, _Product22__T22]):
    @staticmethod
    def $init$($this: 'Product22') -> None: ...
    def _1(self) -> _Product22__T1: ...
    def _10(self) -> _Product22__T10: ...
    def _11(self) -> _Product22__T11: ...
    def _12(self) -> _Product22__T12: ...
    def _13(self) -> _Product22__T13: ...
    def _14(self) -> _Product22__T14: ...
    def _15(self) -> _Product22__T15: ...
    def _16(self) -> _Product22__T16: ...
    def _17(self) -> _Product22__T17: ...
    def _18(self) -> _Product22__T18: ...
    def _19(self) -> _Product22__T19: ...
    def _2(self) -> _Product22__T2: ...
    def _20(self) -> _Product22__T20: ...
    def _21(self) -> _Product22__T21: ...
    def _22(self) -> _Product22__T22: ...
    def _3(self) -> _Product22__T3: ...
    def _4(self) -> _Product22__T4: ...
    def _5(self) -> _Product22__T5: ...
    def _6(self) -> _Product22__T6: ...
    def _7(self) -> _Product22__T7: ...
    def _8(self) -> _Product22__T8: ...
    def _9(self) -> _Product22__T9: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    _unapply__T16 = typing.TypeVar('_unapply__T16')  # <T16>
    _unapply__T17 = typing.TypeVar('_unapply__T17')  # <T17>
    _unapply__T18 = typing.TypeVar('_unapply__T18')  # <T18>
    _unapply__T19 = typing.TypeVar('_unapply__T19')  # <T19>
    _unapply__T20 = typing.TypeVar('_unapply__T20')  # <T20>
    _unapply__T21 = typing.TypeVar('_unapply__T21')  # <T21>
    _unapply__T22 = typing.TypeVar('_unapply__T22')  # <T22>
    @staticmethod
    def unapply(x: 'Product22'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19, _unapply__T20, _unapply__T21, _unapply__T22]) -> Option['Product22'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19, _unapply__T20, _unapply__T21, _unapply__T22]]: ...

_Product3__T1 = typing.TypeVar('_Product3__T1')  # <T1>
_Product3__T2 = typing.TypeVar('_Product3__T2')  # <T2>
_Product3__T3 = typing.TypeVar('_Product3__T3')  # <T3>
class Product3(Product, typing.Generic[_Product3__T1, _Product3__T2, _Product3__T3]):
    @staticmethod
    def $init$($this: 'Product3') -> None: ...
    def _1(self) -> _Product3__T1: ...
    def _2(self) -> _Product3__T2: ...
    def _3(self) -> _Product3__T3: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    @staticmethod
    def unapply(x: 'Product3'[_unapply__T1, _unapply__T2, _unapply__T3]) -> Option['Product3'[_unapply__T1, _unapply__T2, _unapply__T3]]: ...

_Product4__T1 = typing.TypeVar('_Product4__T1')  # <T1>
_Product4__T2 = typing.TypeVar('_Product4__T2')  # <T2>
_Product4__T3 = typing.TypeVar('_Product4__T3')  # <T3>
_Product4__T4 = typing.TypeVar('_Product4__T4')  # <T4>
class Product4(Product, typing.Generic[_Product4__T1, _Product4__T2, _Product4__T3, _Product4__T4]):
    @staticmethod
    def $init$($this: 'Product4') -> None: ...
    def _1(self) -> _Product4__T1: ...
    def _2(self) -> _Product4__T2: ...
    def _3(self) -> _Product4__T3: ...
    def _4(self) -> _Product4__T4: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    @staticmethod
    def unapply(x: 'Product4'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4]) -> Option['Product4'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4]]: ...

_Product5__T1 = typing.TypeVar('_Product5__T1')  # <T1>
_Product5__T2 = typing.TypeVar('_Product5__T2')  # <T2>
_Product5__T3 = typing.TypeVar('_Product5__T3')  # <T3>
_Product5__T4 = typing.TypeVar('_Product5__T4')  # <T4>
_Product5__T5 = typing.TypeVar('_Product5__T5')  # <T5>
class Product5(Product, typing.Generic[_Product5__T1, _Product5__T2, _Product5__T3, _Product5__T4, _Product5__T5]):
    @staticmethod
    def $init$($this: 'Product5') -> None: ...
    def _1(self) -> _Product5__T1: ...
    def _2(self) -> _Product5__T2: ...
    def _3(self) -> _Product5__T3: ...
    def _4(self) -> _Product5__T4: ...
    def _5(self) -> _Product5__T5: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    @staticmethod
    def unapply(x: 'Product5'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5]) -> Option['Product5'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5]]: ...

_Product6__T1 = typing.TypeVar('_Product6__T1')  # <T1>
_Product6__T2 = typing.TypeVar('_Product6__T2')  # <T2>
_Product6__T3 = typing.TypeVar('_Product6__T3')  # <T3>
_Product6__T4 = typing.TypeVar('_Product6__T4')  # <T4>
_Product6__T5 = typing.TypeVar('_Product6__T5')  # <T5>
_Product6__T6 = typing.TypeVar('_Product6__T6')  # <T6>
class Product6(Product, typing.Generic[_Product6__T1, _Product6__T2, _Product6__T3, _Product6__T4, _Product6__T5, _Product6__T6]):
    @staticmethod
    def $init$($this: 'Product6') -> None: ...
    def _1(self) -> _Product6__T1: ...
    def _2(self) -> _Product6__T2: ...
    def _3(self) -> _Product6__T3: ...
    def _4(self) -> _Product6__T4: ...
    def _5(self) -> _Product6__T5: ...
    def _6(self) -> _Product6__T6: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    @staticmethod
    def unapply(x: 'Product6'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6]) -> Option['Product6'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6]]: ...

_Product7__T1 = typing.TypeVar('_Product7__T1')  # <T1>
_Product7__T2 = typing.TypeVar('_Product7__T2')  # <T2>
_Product7__T3 = typing.TypeVar('_Product7__T3')  # <T3>
_Product7__T4 = typing.TypeVar('_Product7__T4')  # <T4>
_Product7__T5 = typing.TypeVar('_Product7__T5')  # <T5>
_Product7__T6 = typing.TypeVar('_Product7__T6')  # <T6>
_Product7__T7 = typing.TypeVar('_Product7__T7')  # <T7>
class Product7(Product, typing.Generic[_Product7__T1, _Product7__T2, _Product7__T3, _Product7__T4, _Product7__T5, _Product7__T6, _Product7__T7]):
    @staticmethod
    def $init$($this: 'Product7') -> None: ...
    def _1(self) -> _Product7__T1: ...
    def _2(self) -> _Product7__T2: ...
    def _3(self) -> _Product7__T3: ...
    def _4(self) -> _Product7__T4: ...
    def _5(self) -> _Product7__T5: ...
    def _6(self) -> _Product7__T6: ...
    def _7(self) -> _Product7__T7: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    @staticmethod
    def unapply(x: 'Product7'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7]) -> Option['Product7'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7]]: ...

_Product8__T1 = typing.TypeVar('_Product8__T1')  # <T1>
_Product8__T2 = typing.TypeVar('_Product8__T2')  # <T2>
_Product8__T3 = typing.TypeVar('_Product8__T3')  # <T3>
_Product8__T4 = typing.TypeVar('_Product8__T4')  # <T4>
_Product8__T5 = typing.TypeVar('_Product8__T5')  # <T5>
_Product8__T6 = typing.TypeVar('_Product8__T6')  # <T6>
_Product8__T7 = typing.TypeVar('_Product8__T7')  # <T7>
_Product8__T8 = typing.TypeVar('_Product8__T8')  # <T8>
class Product8(Product, typing.Generic[_Product8__T1, _Product8__T2, _Product8__T3, _Product8__T4, _Product8__T5, _Product8__T6, _Product8__T7, _Product8__T8]):
    @staticmethod
    def $init$($this: 'Product8') -> None: ...
    def _1(self) -> _Product8__T1: ...
    def _2(self) -> _Product8__T2: ...
    def _3(self) -> _Product8__T3: ...
    def _4(self) -> _Product8__T4: ...
    def _5(self) -> _Product8__T5: ...
    def _6(self) -> _Product8__T6: ...
    def _7(self) -> _Product8__T7: ...
    def _8(self) -> _Product8__T8: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    @staticmethod
    def unapply(x: 'Product8'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8]) -> Option['Product8'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8]]: ...

_Product9__T1 = typing.TypeVar('_Product9__T1')  # <T1>
_Product9__T2 = typing.TypeVar('_Product9__T2')  # <T2>
_Product9__T3 = typing.TypeVar('_Product9__T3')  # <T3>
_Product9__T4 = typing.TypeVar('_Product9__T4')  # <T4>
_Product9__T5 = typing.TypeVar('_Product9__T5')  # <T5>
_Product9__T6 = typing.TypeVar('_Product9__T6')  # <T6>
_Product9__T7 = typing.TypeVar('_Product9__T7')  # <T7>
_Product9__T8 = typing.TypeVar('_Product9__T8')  # <T8>
_Product9__T9 = typing.TypeVar('_Product9__T9')  # <T9>
class Product9(Product, typing.Generic[_Product9__T1, _Product9__T2, _Product9__T3, _Product9__T4, _Product9__T5, _Product9__T6, _Product9__T7, _Product9__T8, _Product9__T9]):
    @staticmethod
    def $init$($this: 'Product9') -> None: ...
    def _1(self) -> _Product9__T1: ...
    def _2(self) -> _Product9__T2: ...
    def _3(self) -> _Product9__T3: ...
    def _4(self) -> _Product9__T4: ...
    def _5(self) -> _Product9__T5: ...
    def _6(self) -> _Product9__T6: ...
    def _7(self) -> _Product9__T7: ...
    def _8(self) -> _Product9__T8: ...
    def _9(self) -> _Product9__T9: ...
    def equals(self, that: typing.Any) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    @staticmethod
    def unapply(x: 'Product9'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9]) -> Option['Product9'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9]]: ...

class ScalaReflectionException(java.lang.Exception, Product, Serializable):
    def __init__(self, msg: str): ...
    _andThen__A = typing.TypeVar('_andThen__A')  # <A>
    @staticmethod
    def andThen(g: Function1['ScalaReflectionException', _andThen__A]) -> Function1[str, _andThen__A]: ...
    @staticmethod
    def apply(msg: str) -> 'ScalaReflectionException': ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _compose__A = typing.TypeVar('_compose__A')  # <A>
    @staticmethod
    def compose(g: Function1[_compose__A, str]) -> Function1[_compose__A, 'ScalaReflectionException']: ...
    def copy(self, msg: str) -> 'ScalaReflectionException': ...
    def copy$default$1(self) -> str: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def msg(self) -> str: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    @staticmethod
    def unapply(x$0: 'ScalaReflectionException') -> Option[str]: ...

class StringContext(Product, Serializable):
    def __init__(self, parts: scala.collection.Seq[str]): ...
    @staticmethod
    def apply(parts: scala.collection.Seq[str]) -> 'StringContext': ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    def checkLengths(self, args: scala.collection.Seq[typing.Any]) -> None: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def parts(self) -> scala.collection.Seq[str]: ...
    @staticmethod
    def processEscapes(str: str) -> str: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def raw(self, args: scala.collection.Seq[typing.Any]) -> str: ...
    def s(self, args: scala.collection.Seq[typing.Any]) -> str: ...
    def standardInterpolator(self, process: Function1[str, str], args: scala.collection.Seq[typing.Any]) -> str: ...
    def toString(self) -> str: ...
    @staticmethod
    def treatEscapes(str: str) -> str: ...
    @staticmethod
    def unapplySeq(x$0: 'StringContext') -> Option[scala.collection.Seq[str]]: ...
    class InvalidEscapeException(java.lang.IllegalArgumentException):
        def __init__(self, str: str, index: int): ...
        def index(self) -> int: ...

class UninitializedFieldError(java.lang.RuntimeException, Product, Serializable):
    @typing.overload
    def __init__(self, obj: typing.Any): ...
    @typing.overload
    def __init__(self, msg: str): ...
    _andThen__A = typing.TypeVar('_andThen__A')  # <A>
    @staticmethod
    def andThen(g: Function1['UninitializedFieldError', _andThen__A]) -> Function1[str, _andThen__A]: ...
    @staticmethod
    def apply(msg: str) -> 'UninitializedFieldError': ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _compose__A = typing.TypeVar('_compose__A')  # <A>
    @staticmethod
    def compose(g: Function1[_compose__A, str]) -> Function1[_compose__A, 'UninitializedFieldError']: ...
    def copy(self, msg: str) -> 'UninitializedFieldError': ...
    def copy$default$1(self) -> str: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def msg(self) -> str: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    @staticmethod
    def unapply(x$0: 'UninitializedFieldError') -> Option[str]: ...

_Some__A = typing.TypeVar('_Some__A')  # <A>
class Some(Option[_Some__A], typing.Generic[_Some__A]):
    serialVersionUID: typing.ClassVar[int] = ...
    def __init__(self, value: _Some__A): ...
    _apply_0__A = typing.TypeVar('_apply_0__A')  # <A>
    _apply_1__A = typing.TypeVar('_apply_1__A')  # <A>
    @typing.overload
    @staticmethod
    def apply(x: _apply_0__A) -> Option[_apply_0__A]: ...
    @typing.overload
    @staticmethod
    def apply(value: _apply_1__A) -> 'Some'[_apply_1__A]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__A = typing.TypeVar('_copy__A')  # <A>
    def copy(self, value: typing.Any) -> 'Some'[typing.Any]: ...
    _copy$default$1__A = typing.TypeVar('_copy$default$1__A')  # <A>
    def copy$default$1(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def get(self) -> _Some__A: ...
    def hashCode(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__A = typing.TypeVar('_unapply__A')  # <A>
    @staticmethod
    def unapply(x$0: 'Some'[_unapply__A]) -> Option[_unapply__A]: ...
    def value(self) -> _Some__A: ...
    def x(self) -> _Some__A: ...

_Tuple1__T1 = typing.TypeVar('_Tuple1__T1')  # <T1>
class Tuple1(Product1[_Tuple1__T1], Serializable, typing.Generic[_Tuple1__T1]):
    _1: typing.Any = ...
    def __init__(self, _1: _Tuple1__T1): ...
    def _1(self) -> _Tuple1__T1: ...
    def _1$mcD$sp(self) -> float: ...
    def _1$mcI$sp(self) -> int: ...
    def _1$mcJ$sp(self) -> int: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    @staticmethod
    def apply(_1: _apply__T1) -> 'Tuple1'[_apply__T1]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    def copy(self, _1: typing.Any) -> 'Tuple1'[typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$1$mcD$sp__T1 = typing.TypeVar('_copy$default$1$mcD$sp__T1')  # <T1>
    def copy$default$1$mcD$sp(self) -> float: ...
    _copy$default$1$mcI$sp__T1 = typing.TypeVar('_copy$default$1$mcI$sp__T1')  # <T1>
    def copy$default$1$mcI$sp(self) -> int: ...
    _copy$default$1$mcJ$sp__T1 = typing.TypeVar('_copy$default$1$mcJ$sp__T1')  # <T1>
    def copy$default$1$mcJ$sp(self) -> int: ...
    def copy$mDc$sp(self, _1: float) -> 'Tuple1'[typing.Any]: ...
    def copy$mIc$sp(self, _1: int) -> 'Tuple1'[typing.Any]: ...
    def copy$mJc$sp(self, _1: int) -> 'Tuple1'[typing.Any]: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def specInstance$(self) -> bool: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    @staticmethod
    def unapply(x$0: 'Tuple1'[_unapply__T1]) -> Option[_unapply__T1]: ...

_Tuple10__T1 = typing.TypeVar('_Tuple10__T1')  # <T1>
_Tuple10__T2 = typing.TypeVar('_Tuple10__T2')  # <T2>
_Tuple10__T3 = typing.TypeVar('_Tuple10__T3')  # <T3>
_Tuple10__T4 = typing.TypeVar('_Tuple10__T4')  # <T4>
_Tuple10__T5 = typing.TypeVar('_Tuple10__T5')  # <T5>
_Tuple10__T6 = typing.TypeVar('_Tuple10__T6')  # <T6>
_Tuple10__T7 = typing.TypeVar('_Tuple10__T7')  # <T7>
_Tuple10__T8 = typing.TypeVar('_Tuple10__T8')  # <T8>
_Tuple10__T9 = typing.TypeVar('_Tuple10__T9')  # <T9>
_Tuple10__T10 = typing.TypeVar('_Tuple10__T10')  # <T10>
class Tuple10(Product10[_Tuple10__T1, _Tuple10__T2, _Tuple10__T3, _Tuple10__T4, _Tuple10__T5, _Tuple10__T6, _Tuple10__T7, _Tuple10__T8, _Tuple10__T9, _Tuple10__T10], Serializable, typing.Generic[_Tuple10__T1, _Tuple10__T2, _Tuple10__T3, _Tuple10__T4, _Tuple10__T5, _Tuple10__T6, _Tuple10__T7, _Tuple10__T8, _Tuple10__T9, _Tuple10__T10]):
    def __init__(self, _1: _Tuple10__T1, _2: _Tuple10__T2, _3: _Tuple10__T3, _4: _Tuple10__T4, _5: _Tuple10__T5, _6: _Tuple10__T6, _7: _Tuple10__T7, _8: _Tuple10__T8, _9: _Tuple10__T9, _10: _Tuple10__T10): ...
    def _1(self) -> _Tuple10__T1: ...
    def _10(self) -> _Tuple10__T10: ...
    def _2(self) -> _Tuple10__T2: ...
    def _3(self) -> _Tuple10__T3: ...
    def _4(self) -> _Tuple10__T4: ...
    def _5(self) -> _Tuple10__T5: ...
    def _6(self) -> _Tuple10__T6: ...
    def _7(self) -> _Tuple10__T7: ...
    def _8(self) -> _Tuple10__T8: ...
    def _9(self) -> _Tuple10__T9: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    _apply__T9 = typing.TypeVar('_apply__T9')  # <T9>
    _apply__T10 = typing.TypeVar('_apply__T10')  # <T10>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8, _9: _apply__T9, _10: _apply__T10) -> 'Tuple10'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8, _apply__T9, _apply__T10]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    _copy__T9 = typing.TypeVar('_copy__T9')  # <T9>
    _copy__T10 = typing.TypeVar('_copy__T10')  # <T10>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any, _9: typing.Any, _10: typing.Any) -> 'Tuple10'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    _copy$default$1__T9 = typing.TypeVar('_copy$default$1__T9')  # <T9>
    _copy$default$1__T10 = typing.TypeVar('_copy$default$1__T10')  # <T10>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$10__T1 = typing.TypeVar('_copy$default$10__T1')  # <T1>
    _copy$default$10__T2 = typing.TypeVar('_copy$default$10__T2')  # <T2>
    _copy$default$10__T3 = typing.TypeVar('_copy$default$10__T3')  # <T3>
    _copy$default$10__T4 = typing.TypeVar('_copy$default$10__T4')  # <T4>
    _copy$default$10__T5 = typing.TypeVar('_copy$default$10__T5')  # <T5>
    _copy$default$10__T6 = typing.TypeVar('_copy$default$10__T6')  # <T6>
    _copy$default$10__T7 = typing.TypeVar('_copy$default$10__T7')  # <T7>
    _copy$default$10__T8 = typing.TypeVar('_copy$default$10__T8')  # <T8>
    _copy$default$10__T9 = typing.TypeVar('_copy$default$10__T9')  # <T9>
    _copy$default$10__T10 = typing.TypeVar('_copy$default$10__T10')  # <T10>
    def copy$default$10(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    _copy$default$2__T9 = typing.TypeVar('_copy$default$2__T9')  # <T9>
    _copy$default$2__T10 = typing.TypeVar('_copy$default$2__T10')  # <T10>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    _copy$default$3__T9 = typing.TypeVar('_copy$default$3__T9')  # <T9>
    _copy$default$3__T10 = typing.TypeVar('_copy$default$3__T10')  # <T10>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    _copy$default$4__T9 = typing.TypeVar('_copy$default$4__T9')  # <T9>
    _copy$default$4__T10 = typing.TypeVar('_copy$default$4__T10')  # <T10>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    _copy$default$5__T9 = typing.TypeVar('_copy$default$5__T9')  # <T9>
    _copy$default$5__T10 = typing.TypeVar('_copy$default$5__T10')  # <T10>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    _copy$default$6__T9 = typing.TypeVar('_copy$default$6__T9')  # <T9>
    _copy$default$6__T10 = typing.TypeVar('_copy$default$6__T10')  # <T10>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    _copy$default$7__T9 = typing.TypeVar('_copy$default$7__T9')  # <T9>
    _copy$default$7__T10 = typing.TypeVar('_copy$default$7__T10')  # <T10>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    _copy$default$8__T9 = typing.TypeVar('_copy$default$8__T9')  # <T9>
    _copy$default$8__T10 = typing.TypeVar('_copy$default$8__T10')  # <T10>
    def copy$default$8(self) -> typing.Any: ...
    _copy$default$9__T1 = typing.TypeVar('_copy$default$9__T1')  # <T1>
    _copy$default$9__T2 = typing.TypeVar('_copy$default$9__T2')  # <T2>
    _copy$default$9__T3 = typing.TypeVar('_copy$default$9__T3')  # <T3>
    _copy$default$9__T4 = typing.TypeVar('_copy$default$9__T4')  # <T4>
    _copy$default$9__T5 = typing.TypeVar('_copy$default$9__T5')  # <T5>
    _copy$default$9__T6 = typing.TypeVar('_copy$default$9__T6')  # <T6>
    _copy$default$9__T7 = typing.TypeVar('_copy$default$9__T7')  # <T7>
    _copy$default$9__T8 = typing.TypeVar('_copy$default$9__T8')  # <T8>
    _copy$default$9__T9 = typing.TypeVar('_copy$default$9__T9')  # <T9>
    _copy$default$9__T10 = typing.TypeVar('_copy$default$9__T10')  # <T10>
    def copy$default$9(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    @staticmethod
    def unapply(x$0: 'Tuple10'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10]) -> Option['Tuple10'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10]]: ...

_Tuple11__T1 = typing.TypeVar('_Tuple11__T1')  # <T1>
_Tuple11__T2 = typing.TypeVar('_Tuple11__T2')  # <T2>
_Tuple11__T3 = typing.TypeVar('_Tuple11__T3')  # <T3>
_Tuple11__T4 = typing.TypeVar('_Tuple11__T4')  # <T4>
_Tuple11__T5 = typing.TypeVar('_Tuple11__T5')  # <T5>
_Tuple11__T6 = typing.TypeVar('_Tuple11__T6')  # <T6>
_Tuple11__T7 = typing.TypeVar('_Tuple11__T7')  # <T7>
_Tuple11__T8 = typing.TypeVar('_Tuple11__T8')  # <T8>
_Tuple11__T9 = typing.TypeVar('_Tuple11__T9')  # <T9>
_Tuple11__T10 = typing.TypeVar('_Tuple11__T10')  # <T10>
_Tuple11__T11 = typing.TypeVar('_Tuple11__T11')  # <T11>
class Tuple11(Product11[_Tuple11__T1, _Tuple11__T2, _Tuple11__T3, _Tuple11__T4, _Tuple11__T5, _Tuple11__T6, _Tuple11__T7, _Tuple11__T8, _Tuple11__T9, _Tuple11__T10, _Tuple11__T11], Serializable, typing.Generic[_Tuple11__T1, _Tuple11__T2, _Tuple11__T3, _Tuple11__T4, _Tuple11__T5, _Tuple11__T6, _Tuple11__T7, _Tuple11__T8, _Tuple11__T9, _Tuple11__T10, _Tuple11__T11]):
    def __init__(self, _1: _Tuple11__T1, _2: _Tuple11__T2, _3: _Tuple11__T3, _4: _Tuple11__T4, _5: _Tuple11__T5, _6: _Tuple11__T6, _7: _Tuple11__T7, _8: _Tuple11__T8, _9: _Tuple11__T9, _10: _Tuple11__T10, _11: _Tuple11__T11): ...
    def _1(self) -> _Tuple11__T1: ...
    def _10(self) -> _Tuple11__T10: ...
    def _11(self) -> _Tuple11__T11: ...
    def _2(self) -> _Tuple11__T2: ...
    def _3(self) -> _Tuple11__T3: ...
    def _4(self) -> _Tuple11__T4: ...
    def _5(self) -> _Tuple11__T5: ...
    def _6(self) -> _Tuple11__T6: ...
    def _7(self) -> _Tuple11__T7: ...
    def _8(self) -> _Tuple11__T8: ...
    def _9(self) -> _Tuple11__T9: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    _apply__T9 = typing.TypeVar('_apply__T9')  # <T9>
    _apply__T10 = typing.TypeVar('_apply__T10')  # <T10>
    _apply__T11 = typing.TypeVar('_apply__T11')  # <T11>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8, _9: _apply__T9, _10: _apply__T10, _11: _apply__T11) -> 'Tuple11'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8, _apply__T9, _apply__T10, _apply__T11]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    _copy__T9 = typing.TypeVar('_copy__T9')  # <T9>
    _copy__T10 = typing.TypeVar('_copy__T10')  # <T10>
    _copy__T11 = typing.TypeVar('_copy__T11')  # <T11>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any, _9: typing.Any, _10: typing.Any, _11: typing.Any) -> 'Tuple11'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    _copy$default$1__T9 = typing.TypeVar('_copy$default$1__T9')  # <T9>
    _copy$default$1__T10 = typing.TypeVar('_copy$default$1__T10')  # <T10>
    _copy$default$1__T11 = typing.TypeVar('_copy$default$1__T11')  # <T11>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$10__T1 = typing.TypeVar('_copy$default$10__T1')  # <T1>
    _copy$default$10__T2 = typing.TypeVar('_copy$default$10__T2')  # <T2>
    _copy$default$10__T3 = typing.TypeVar('_copy$default$10__T3')  # <T3>
    _copy$default$10__T4 = typing.TypeVar('_copy$default$10__T4')  # <T4>
    _copy$default$10__T5 = typing.TypeVar('_copy$default$10__T5')  # <T5>
    _copy$default$10__T6 = typing.TypeVar('_copy$default$10__T6')  # <T6>
    _copy$default$10__T7 = typing.TypeVar('_copy$default$10__T7')  # <T7>
    _copy$default$10__T8 = typing.TypeVar('_copy$default$10__T8')  # <T8>
    _copy$default$10__T9 = typing.TypeVar('_copy$default$10__T9')  # <T9>
    _copy$default$10__T10 = typing.TypeVar('_copy$default$10__T10')  # <T10>
    _copy$default$10__T11 = typing.TypeVar('_copy$default$10__T11')  # <T11>
    def copy$default$10(self) -> typing.Any: ...
    _copy$default$11__T1 = typing.TypeVar('_copy$default$11__T1')  # <T1>
    _copy$default$11__T2 = typing.TypeVar('_copy$default$11__T2')  # <T2>
    _copy$default$11__T3 = typing.TypeVar('_copy$default$11__T3')  # <T3>
    _copy$default$11__T4 = typing.TypeVar('_copy$default$11__T4')  # <T4>
    _copy$default$11__T5 = typing.TypeVar('_copy$default$11__T5')  # <T5>
    _copy$default$11__T6 = typing.TypeVar('_copy$default$11__T6')  # <T6>
    _copy$default$11__T7 = typing.TypeVar('_copy$default$11__T7')  # <T7>
    _copy$default$11__T8 = typing.TypeVar('_copy$default$11__T8')  # <T8>
    _copy$default$11__T9 = typing.TypeVar('_copy$default$11__T9')  # <T9>
    _copy$default$11__T10 = typing.TypeVar('_copy$default$11__T10')  # <T10>
    _copy$default$11__T11 = typing.TypeVar('_copy$default$11__T11')  # <T11>
    def copy$default$11(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    _copy$default$2__T9 = typing.TypeVar('_copy$default$2__T9')  # <T9>
    _copy$default$2__T10 = typing.TypeVar('_copy$default$2__T10')  # <T10>
    _copy$default$2__T11 = typing.TypeVar('_copy$default$2__T11')  # <T11>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    _copy$default$3__T9 = typing.TypeVar('_copy$default$3__T9')  # <T9>
    _copy$default$3__T10 = typing.TypeVar('_copy$default$3__T10')  # <T10>
    _copy$default$3__T11 = typing.TypeVar('_copy$default$3__T11')  # <T11>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    _copy$default$4__T9 = typing.TypeVar('_copy$default$4__T9')  # <T9>
    _copy$default$4__T10 = typing.TypeVar('_copy$default$4__T10')  # <T10>
    _copy$default$4__T11 = typing.TypeVar('_copy$default$4__T11')  # <T11>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    _copy$default$5__T9 = typing.TypeVar('_copy$default$5__T9')  # <T9>
    _copy$default$5__T10 = typing.TypeVar('_copy$default$5__T10')  # <T10>
    _copy$default$5__T11 = typing.TypeVar('_copy$default$5__T11')  # <T11>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    _copy$default$6__T9 = typing.TypeVar('_copy$default$6__T9')  # <T9>
    _copy$default$6__T10 = typing.TypeVar('_copy$default$6__T10')  # <T10>
    _copy$default$6__T11 = typing.TypeVar('_copy$default$6__T11')  # <T11>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    _copy$default$7__T9 = typing.TypeVar('_copy$default$7__T9')  # <T9>
    _copy$default$7__T10 = typing.TypeVar('_copy$default$7__T10')  # <T10>
    _copy$default$7__T11 = typing.TypeVar('_copy$default$7__T11')  # <T11>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    _copy$default$8__T9 = typing.TypeVar('_copy$default$8__T9')  # <T9>
    _copy$default$8__T10 = typing.TypeVar('_copy$default$8__T10')  # <T10>
    _copy$default$8__T11 = typing.TypeVar('_copy$default$8__T11')  # <T11>
    def copy$default$8(self) -> typing.Any: ...
    _copy$default$9__T1 = typing.TypeVar('_copy$default$9__T1')  # <T1>
    _copy$default$9__T2 = typing.TypeVar('_copy$default$9__T2')  # <T2>
    _copy$default$9__T3 = typing.TypeVar('_copy$default$9__T3')  # <T3>
    _copy$default$9__T4 = typing.TypeVar('_copy$default$9__T4')  # <T4>
    _copy$default$9__T5 = typing.TypeVar('_copy$default$9__T5')  # <T5>
    _copy$default$9__T6 = typing.TypeVar('_copy$default$9__T6')  # <T6>
    _copy$default$9__T7 = typing.TypeVar('_copy$default$9__T7')  # <T7>
    _copy$default$9__T8 = typing.TypeVar('_copy$default$9__T8')  # <T8>
    _copy$default$9__T9 = typing.TypeVar('_copy$default$9__T9')  # <T9>
    _copy$default$9__T10 = typing.TypeVar('_copy$default$9__T10')  # <T10>
    _copy$default$9__T11 = typing.TypeVar('_copy$default$9__T11')  # <T11>
    def copy$default$9(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    @staticmethod
    def unapply(x$0: 'Tuple11'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11]) -> Option['Tuple11'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11]]: ...

_Tuple12__T1 = typing.TypeVar('_Tuple12__T1')  # <T1>
_Tuple12__T2 = typing.TypeVar('_Tuple12__T2')  # <T2>
_Tuple12__T3 = typing.TypeVar('_Tuple12__T3')  # <T3>
_Tuple12__T4 = typing.TypeVar('_Tuple12__T4')  # <T4>
_Tuple12__T5 = typing.TypeVar('_Tuple12__T5')  # <T5>
_Tuple12__T6 = typing.TypeVar('_Tuple12__T6')  # <T6>
_Tuple12__T7 = typing.TypeVar('_Tuple12__T7')  # <T7>
_Tuple12__T8 = typing.TypeVar('_Tuple12__T8')  # <T8>
_Tuple12__T9 = typing.TypeVar('_Tuple12__T9')  # <T9>
_Tuple12__T10 = typing.TypeVar('_Tuple12__T10')  # <T10>
_Tuple12__T11 = typing.TypeVar('_Tuple12__T11')  # <T11>
_Tuple12__T12 = typing.TypeVar('_Tuple12__T12')  # <T12>
class Tuple12(Product12[_Tuple12__T1, _Tuple12__T2, _Tuple12__T3, _Tuple12__T4, _Tuple12__T5, _Tuple12__T6, _Tuple12__T7, _Tuple12__T8, _Tuple12__T9, _Tuple12__T10, _Tuple12__T11, _Tuple12__T12], Serializable, typing.Generic[_Tuple12__T1, _Tuple12__T2, _Tuple12__T3, _Tuple12__T4, _Tuple12__T5, _Tuple12__T6, _Tuple12__T7, _Tuple12__T8, _Tuple12__T9, _Tuple12__T10, _Tuple12__T11, _Tuple12__T12]):
    def __init__(self, _1: _Tuple12__T1, _2: _Tuple12__T2, _3: _Tuple12__T3, _4: _Tuple12__T4, _5: _Tuple12__T5, _6: _Tuple12__T6, _7: _Tuple12__T7, _8: _Tuple12__T8, _9: _Tuple12__T9, _10: _Tuple12__T10, _11: _Tuple12__T11, _12: _Tuple12__T12): ...
    def _1(self) -> _Tuple12__T1: ...
    def _10(self) -> _Tuple12__T10: ...
    def _11(self) -> _Tuple12__T11: ...
    def _12(self) -> _Tuple12__T12: ...
    def _2(self) -> _Tuple12__T2: ...
    def _3(self) -> _Tuple12__T3: ...
    def _4(self) -> _Tuple12__T4: ...
    def _5(self) -> _Tuple12__T5: ...
    def _6(self) -> _Tuple12__T6: ...
    def _7(self) -> _Tuple12__T7: ...
    def _8(self) -> _Tuple12__T8: ...
    def _9(self) -> _Tuple12__T9: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    _apply__T9 = typing.TypeVar('_apply__T9')  # <T9>
    _apply__T10 = typing.TypeVar('_apply__T10')  # <T10>
    _apply__T11 = typing.TypeVar('_apply__T11')  # <T11>
    _apply__T12 = typing.TypeVar('_apply__T12')  # <T12>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8, _9: _apply__T9, _10: _apply__T10, _11: _apply__T11, _12: _apply__T12) -> 'Tuple12'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8, _apply__T9, _apply__T10, _apply__T11, _apply__T12]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    _copy__T9 = typing.TypeVar('_copy__T9')  # <T9>
    _copy__T10 = typing.TypeVar('_copy__T10')  # <T10>
    _copy__T11 = typing.TypeVar('_copy__T11')  # <T11>
    _copy__T12 = typing.TypeVar('_copy__T12')  # <T12>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any, _9: typing.Any, _10: typing.Any, _11: typing.Any, _12: typing.Any) -> 'Tuple12'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    _copy$default$1__T9 = typing.TypeVar('_copy$default$1__T9')  # <T9>
    _copy$default$1__T10 = typing.TypeVar('_copy$default$1__T10')  # <T10>
    _copy$default$1__T11 = typing.TypeVar('_copy$default$1__T11')  # <T11>
    _copy$default$1__T12 = typing.TypeVar('_copy$default$1__T12')  # <T12>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$10__T1 = typing.TypeVar('_copy$default$10__T1')  # <T1>
    _copy$default$10__T2 = typing.TypeVar('_copy$default$10__T2')  # <T2>
    _copy$default$10__T3 = typing.TypeVar('_copy$default$10__T3')  # <T3>
    _copy$default$10__T4 = typing.TypeVar('_copy$default$10__T4')  # <T4>
    _copy$default$10__T5 = typing.TypeVar('_copy$default$10__T5')  # <T5>
    _copy$default$10__T6 = typing.TypeVar('_copy$default$10__T6')  # <T6>
    _copy$default$10__T7 = typing.TypeVar('_copy$default$10__T7')  # <T7>
    _copy$default$10__T8 = typing.TypeVar('_copy$default$10__T8')  # <T8>
    _copy$default$10__T9 = typing.TypeVar('_copy$default$10__T9')  # <T9>
    _copy$default$10__T10 = typing.TypeVar('_copy$default$10__T10')  # <T10>
    _copy$default$10__T11 = typing.TypeVar('_copy$default$10__T11')  # <T11>
    _copy$default$10__T12 = typing.TypeVar('_copy$default$10__T12')  # <T12>
    def copy$default$10(self) -> typing.Any: ...
    _copy$default$11__T1 = typing.TypeVar('_copy$default$11__T1')  # <T1>
    _copy$default$11__T2 = typing.TypeVar('_copy$default$11__T2')  # <T2>
    _copy$default$11__T3 = typing.TypeVar('_copy$default$11__T3')  # <T3>
    _copy$default$11__T4 = typing.TypeVar('_copy$default$11__T4')  # <T4>
    _copy$default$11__T5 = typing.TypeVar('_copy$default$11__T5')  # <T5>
    _copy$default$11__T6 = typing.TypeVar('_copy$default$11__T6')  # <T6>
    _copy$default$11__T7 = typing.TypeVar('_copy$default$11__T7')  # <T7>
    _copy$default$11__T8 = typing.TypeVar('_copy$default$11__T8')  # <T8>
    _copy$default$11__T9 = typing.TypeVar('_copy$default$11__T9')  # <T9>
    _copy$default$11__T10 = typing.TypeVar('_copy$default$11__T10')  # <T10>
    _copy$default$11__T11 = typing.TypeVar('_copy$default$11__T11')  # <T11>
    _copy$default$11__T12 = typing.TypeVar('_copy$default$11__T12')  # <T12>
    def copy$default$11(self) -> typing.Any: ...
    _copy$default$12__T1 = typing.TypeVar('_copy$default$12__T1')  # <T1>
    _copy$default$12__T2 = typing.TypeVar('_copy$default$12__T2')  # <T2>
    _copy$default$12__T3 = typing.TypeVar('_copy$default$12__T3')  # <T3>
    _copy$default$12__T4 = typing.TypeVar('_copy$default$12__T4')  # <T4>
    _copy$default$12__T5 = typing.TypeVar('_copy$default$12__T5')  # <T5>
    _copy$default$12__T6 = typing.TypeVar('_copy$default$12__T6')  # <T6>
    _copy$default$12__T7 = typing.TypeVar('_copy$default$12__T7')  # <T7>
    _copy$default$12__T8 = typing.TypeVar('_copy$default$12__T8')  # <T8>
    _copy$default$12__T9 = typing.TypeVar('_copy$default$12__T9')  # <T9>
    _copy$default$12__T10 = typing.TypeVar('_copy$default$12__T10')  # <T10>
    _copy$default$12__T11 = typing.TypeVar('_copy$default$12__T11')  # <T11>
    _copy$default$12__T12 = typing.TypeVar('_copy$default$12__T12')  # <T12>
    def copy$default$12(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    _copy$default$2__T9 = typing.TypeVar('_copy$default$2__T9')  # <T9>
    _copy$default$2__T10 = typing.TypeVar('_copy$default$2__T10')  # <T10>
    _copy$default$2__T11 = typing.TypeVar('_copy$default$2__T11')  # <T11>
    _copy$default$2__T12 = typing.TypeVar('_copy$default$2__T12')  # <T12>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    _copy$default$3__T9 = typing.TypeVar('_copy$default$3__T9')  # <T9>
    _copy$default$3__T10 = typing.TypeVar('_copy$default$3__T10')  # <T10>
    _copy$default$3__T11 = typing.TypeVar('_copy$default$3__T11')  # <T11>
    _copy$default$3__T12 = typing.TypeVar('_copy$default$3__T12')  # <T12>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    _copy$default$4__T9 = typing.TypeVar('_copy$default$4__T9')  # <T9>
    _copy$default$4__T10 = typing.TypeVar('_copy$default$4__T10')  # <T10>
    _copy$default$4__T11 = typing.TypeVar('_copy$default$4__T11')  # <T11>
    _copy$default$4__T12 = typing.TypeVar('_copy$default$4__T12')  # <T12>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    _copy$default$5__T9 = typing.TypeVar('_copy$default$5__T9')  # <T9>
    _copy$default$5__T10 = typing.TypeVar('_copy$default$5__T10')  # <T10>
    _copy$default$5__T11 = typing.TypeVar('_copy$default$5__T11')  # <T11>
    _copy$default$5__T12 = typing.TypeVar('_copy$default$5__T12')  # <T12>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    _copy$default$6__T9 = typing.TypeVar('_copy$default$6__T9')  # <T9>
    _copy$default$6__T10 = typing.TypeVar('_copy$default$6__T10')  # <T10>
    _copy$default$6__T11 = typing.TypeVar('_copy$default$6__T11')  # <T11>
    _copy$default$6__T12 = typing.TypeVar('_copy$default$6__T12')  # <T12>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    _copy$default$7__T9 = typing.TypeVar('_copy$default$7__T9')  # <T9>
    _copy$default$7__T10 = typing.TypeVar('_copy$default$7__T10')  # <T10>
    _copy$default$7__T11 = typing.TypeVar('_copy$default$7__T11')  # <T11>
    _copy$default$7__T12 = typing.TypeVar('_copy$default$7__T12')  # <T12>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    _copy$default$8__T9 = typing.TypeVar('_copy$default$8__T9')  # <T9>
    _copy$default$8__T10 = typing.TypeVar('_copy$default$8__T10')  # <T10>
    _copy$default$8__T11 = typing.TypeVar('_copy$default$8__T11')  # <T11>
    _copy$default$8__T12 = typing.TypeVar('_copy$default$8__T12')  # <T12>
    def copy$default$8(self) -> typing.Any: ...
    _copy$default$9__T1 = typing.TypeVar('_copy$default$9__T1')  # <T1>
    _copy$default$9__T2 = typing.TypeVar('_copy$default$9__T2')  # <T2>
    _copy$default$9__T3 = typing.TypeVar('_copy$default$9__T3')  # <T3>
    _copy$default$9__T4 = typing.TypeVar('_copy$default$9__T4')  # <T4>
    _copy$default$9__T5 = typing.TypeVar('_copy$default$9__T5')  # <T5>
    _copy$default$9__T6 = typing.TypeVar('_copy$default$9__T6')  # <T6>
    _copy$default$9__T7 = typing.TypeVar('_copy$default$9__T7')  # <T7>
    _copy$default$9__T8 = typing.TypeVar('_copy$default$9__T8')  # <T8>
    _copy$default$9__T9 = typing.TypeVar('_copy$default$9__T9')  # <T9>
    _copy$default$9__T10 = typing.TypeVar('_copy$default$9__T10')  # <T10>
    _copy$default$9__T11 = typing.TypeVar('_copy$default$9__T11')  # <T11>
    _copy$default$9__T12 = typing.TypeVar('_copy$default$9__T12')  # <T12>
    def copy$default$9(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    @staticmethod
    def unapply(x$0: 'Tuple12'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12]) -> Option['Tuple12'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12]]: ...

_Tuple13__T1 = typing.TypeVar('_Tuple13__T1')  # <T1>
_Tuple13__T2 = typing.TypeVar('_Tuple13__T2')  # <T2>
_Tuple13__T3 = typing.TypeVar('_Tuple13__T3')  # <T3>
_Tuple13__T4 = typing.TypeVar('_Tuple13__T4')  # <T4>
_Tuple13__T5 = typing.TypeVar('_Tuple13__T5')  # <T5>
_Tuple13__T6 = typing.TypeVar('_Tuple13__T6')  # <T6>
_Tuple13__T7 = typing.TypeVar('_Tuple13__T7')  # <T7>
_Tuple13__T8 = typing.TypeVar('_Tuple13__T8')  # <T8>
_Tuple13__T9 = typing.TypeVar('_Tuple13__T9')  # <T9>
_Tuple13__T10 = typing.TypeVar('_Tuple13__T10')  # <T10>
_Tuple13__T11 = typing.TypeVar('_Tuple13__T11')  # <T11>
_Tuple13__T12 = typing.TypeVar('_Tuple13__T12')  # <T12>
_Tuple13__T13 = typing.TypeVar('_Tuple13__T13')  # <T13>
class Tuple13(Product13[_Tuple13__T1, _Tuple13__T2, _Tuple13__T3, _Tuple13__T4, _Tuple13__T5, _Tuple13__T6, _Tuple13__T7, _Tuple13__T8, _Tuple13__T9, _Tuple13__T10, _Tuple13__T11, _Tuple13__T12, _Tuple13__T13], Serializable, typing.Generic[_Tuple13__T1, _Tuple13__T2, _Tuple13__T3, _Tuple13__T4, _Tuple13__T5, _Tuple13__T6, _Tuple13__T7, _Tuple13__T8, _Tuple13__T9, _Tuple13__T10, _Tuple13__T11, _Tuple13__T12, _Tuple13__T13]):
    def __init__(self, _1: _Tuple13__T1, _2: _Tuple13__T2, _3: _Tuple13__T3, _4: _Tuple13__T4, _5: _Tuple13__T5, _6: _Tuple13__T6, _7: _Tuple13__T7, _8: _Tuple13__T8, _9: _Tuple13__T9, _10: _Tuple13__T10, _11: _Tuple13__T11, _12: _Tuple13__T12, _13: _Tuple13__T13): ...
    def _1(self) -> _Tuple13__T1: ...
    def _10(self) -> _Tuple13__T10: ...
    def _11(self) -> _Tuple13__T11: ...
    def _12(self) -> _Tuple13__T12: ...
    def _13(self) -> _Tuple13__T13: ...
    def _2(self) -> _Tuple13__T2: ...
    def _3(self) -> _Tuple13__T3: ...
    def _4(self) -> _Tuple13__T4: ...
    def _5(self) -> _Tuple13__T5: ...
    def _6(self) -> _Tuple13__T6: ...
    def _7(self) -> _Tuple13__T7: ...
    def _8(self) -> _Tuple13__T8: ...
    def _9(self) -> _Tuple13__T9: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    _apply__T9 = typing.TypeVar('_apply__T9')  # <T9>
    _apply__T10 = typing.TypeVar('_apply__T10')  # <T10>
    _apply__T11 = typing.TypeVar('_apply__T11')  # <T11>
    _apply__T12 = typing.TypeVar('_apply__T12')  # <T12>
    _apply__T13 = typing.TypeVar('_apply__T13')  # <T13>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8, _9: _apply__T9, _10: _apply__T10, _11: _apply__T11, _12: _apply__T12, _13: _apply__T13) -> 'Tuple13'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8, _apply__T9, _apply__T10, _apply__T11, _apply__T12, _apply__T13]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    _copy__T9 = typing.TypeVar('_copy__T9')  # <T9>
    _copy__T10 = typing.TypeVar('_copy__T10')  # <T10>
    _copy__T11 = typing.TypeVar('_copy__T11')  # <T11>
    _copy__T12 = typing.TypeVar('_copy__T12')  # <T12>
    _copy__T13 = typing.TypeVar('_copy__T13')  # <T13>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any, _9: typing.Any, _10: typing.Any, _11: typing.Any, _12: typing.Any, _13: typing.Any) -> 'Tuple13'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    _copy$default$1__T9 = typing.TypeVar('_copy$default$1__T9')  # <T9>
    _copy$default$1__T10 = typing.TypeVar('_copy$default$1__T10')  # <T10>
    _copy$default$1__T11 = typing.TypeVar('_copy$default$1__T11')  # <T11>
    _copy$default$1__T12 = typing.TypeVar('_copy$default$1__T12')  # <T12>
    _copy$default$1__T13 = typing.TypeVar('_copy$default$1__T13')  # <T13>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$10__T1 = typing.TypeVar('_copy$default$10__T1')  # <T1>
    _copy$default$10__T2 = typing.TypeVar('_copy$default$10__T2')  # <T2>
    _copy$default$10__T3 = typing.TypeVar('_copy$default$10__T3')  # <T3>
    _copy$default$10__T4 = typing.TypeVar('_copy$default$10__T4')  # <T4>
    _copy$default$10__T5 = typing.TypeVar('_copy$default$10__T5')  # <T5>
    _copy$default$10__T6 = typing.TypeVar('_copy$default$10__T6')  # <T6>
    _copy$default$10__T7 = typing.TypeVar('_copy$default$10__T7')  # <T7>
    _copy$default$10__T8 = typing.TypeVar('_copy$default$10__T8')  # <T8>
    _copy$default$10__T9 = typing.TypeVar('_copy$default$10__T9')  # <T9>
    _copy$default$10__T10 = typing.TypeVar('_copy$default$10__T10')  # <T10>
    _copy$default$10__T11 = typing.TypeVar('_copy$default$10__T11')  # <T11>
    _copy$default$10__T12 = typing.TypeVar('_copy$default$10__T12')  # <T12>
    _copy$default$10__T13 = typing.TypeVar('_copy$default$10__T13')  # <T13>
    def copy$default$10(self) -> typing.Any: ...
    _copy$default$11__T1 = typing.TypeVar('_copy$default$11__T1')  # <T1>
    _copy$default$11__T2 = typing.TypeVar('_copy$default$11__T2')  # <T2>
    _copy$default$11__T3 = typing.TypeVar('_copy$default$11__T3')  # <T3>
    _copy$default$11__T4 = typing.TypeVar('_copy$default$11__T4')  # <T4>
    _copy$default$11__T5 = typing.TypeVar('_copy$default$11__T5')  # <T5>
    _copy$default$11__T6 = typing.TypeVar('_copy$default$11__T6')  # <T6>
    _copy$default$11__T7 = typing.TypeVar('_copy$default$11__T7')  # <T7>
    _copy$default$11__T8 = typing.TypeVar('_copy$default$11__T8')  # <T8>
    _copy$default$11__T9 = typing.TypeVar('_copy$default$11__T9')  # <T9>
    _copy$default$11__T10 = typing.TypeVar('_copy$default$11__T10')  # <T10>
    _copy$default$11__T11 = typing.TypeVar('_copy$default$11__T11')  # <T11>
    _copy$default$11__T12 = typing.TypeVar('_copy$default$11__T12')  # <T12>
    _copy$default$11__T13 = typing.TypeVar('_copy$default$11__T13')  # <T13>
    def copy$default$11(self) -> typing.Any: ...
    _copy$default$12__T1 = typing.TypeVar('_copy$default$12__T1')  # <T1>
    _copy$default$12__T2 = typing.TypeVar('_copy$default$12__T2')  # <T2>
    _copy$default$12__T3 = typing.TypeVar('_copy$default$12__T3')  # <T3>
    _copy$default$12__T4 = typing.TypeVar('_copy$default$12__T4')  # <T4>
    _copy$default$12__T5 = typing.TypeVar('_copy$default$12__T5')  # <T5>
    _copy$default$12__T6 = typing.TypeVar('_copy$default$12__T6')  # <T6>
    _copy$default$12__T7 = typing.TypeVar('_copy$default$12__T7')  # <T7>
    _copy$default$12__T8 = typing.TypeVar('_copy$default$12__T8')  # <T8>
    _copy$default$12__T9 = typing.TypeVar('_copy$default$12__T9')  # <T9>
    _copy$default$12__T10 = typing.TypeVar('_copy$default$12__T10')  # <T10>
    _copy$default$12__T11 = typing.TypeVar('_copy$default$12__T11')  # <T11>
    _copy$default$12__T12 = typing.TypeVar('_copy$default$12__T12')  # <T12>
    _copy$default$12__T13 = typing.TypeVar('_copy$default$12__T13')  # <T13>
    def copy$default$12(self) -> typing.Any: ...
    _copy$default$13__T1 = typing.TypeVar('_copy$default$13__T1')  # <T1>
    _copy$default$13__T2 = typing.TypeVar('_copy$default$13__T2')  # <T2>
    _copy$default$13__T3 = typing.TypeVar('_copy$default$13__T3')  # <T3>
    _copy$default$13__T4 = typing.TypeVar('_copy$default$13__T4')  # <T4>
    _copy$default$13__T5 = typing.TypeVar('_copy$default$13__T5')  # <T5>
    _copy$default$13__T6 = typing.TypeVar('_copy$default$13__T6')  # <T6>
    _copy$default$13__T7 = typing.TypeVar('_copy$default$13__T7')  # <T7>
    _copy$default$13__T8 = typing.TypeVar('_copy$default$13__T8')  # <T8>
    _copy$default$13__T9 = typing.TypeVar('_copy$default$13__T9')  # <T9>
    _copy$default$13__T10 = typing.TypeVar('_copy$default$13__T10')  # <T10>
    _copy$default$13__T11 = typing.TypeVar('_copy$default$13__T11')  # <T11>
    _copy$default$13__T12 = typing.TypeVar('_copy$default$13__T12')  # <T12>
    _copy$default$13__T13 = typing.TypeVar('_copy$default$13__T13')  # <T13>
    def copy$default$13(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    _copy$default$2__T9 = typing.TypeVar('_copy$default$2__T9')  # <T9>
    _copy$default$2__T10 = typing.TypeVar('_copy$default$2__T10')  # <T10>
    _copy$default$2__T11 = typing.TypeVar('_copy$default$2__T11')  # <T11>
    _copy$default$2__T12 = typing.TypeVar('_copy$default$2__T12')  # <T12>
    _copy$default$2__T13 = typing.TypeVar('_copy$default$2__T13')  # <T13>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    _copy$default$3__T9 = typing.TypeVar('_copy$default$3__T9')  # <T9>
    _copy$default$3__T10 = typing.TypeVar('_copy$default$3__T10')  # <T10>
    _copy$default$3__T11 = typing.TypeVar('_copy$default$3__T11')  # <T11>
    _copy$default$3__T12 = typing.TypeVar('_copy$default$3__T12')  # <T12>
    _copy$default$3__T13 = typing.TypeVar('_copy$default$3__T13')  # <T13>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    _copy$default$4__T9 = typing.TypeVar('_copy$default$4__T9')  # <T9>
    _copy$default$4__T10 = typing.TypeVar('_copy$default$4__T10')  # <T10>
    _copy$default$4__T11 = typing.TypeVar('_copy$default$4__T11')  # <T11>
    _copy$default$4__T12 = typing.TypeVar('_copy$default$4__T12')  # <T12>
    _copy$default$4__T13 = typing.TypeVar('_copy$default$4__T13')  # <T13>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    _copy$default$5__T9 = typing.TypeVar('_copy$default$5__T9')  # <T9>
    _copy$default$5__T10 = typing.TypeVar('_copy$default$5__T10')  # <T10>
    _copy$default$5__T11 = typing.TypeVar('_copy$default$5__T11')  # <T11>
    _copy$default$5__T12 = typing.TypeVar('_copy$default$5__T12')  # <T12>
    _copy$default$5__T13 = typing.TypeVar('_copy$default$5__T13')  # <T13>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    _copy$default$6__T9 = typing.TypeVar('_copy$default$6__T9')  # <T9>
    _copy$default$6__T10 = typing.TypeVar('_copy$default$6__T10')  # <T10>
    _copy$default$6__T11 = typing.TypeVar('_copy$default$6__T11')  # <T11>
    _copy$default$6__T12 = typing.TypeVar('_copy$default$6__T12')  # <T12>
    _copy$default$6__T13 = typing.TypeVar('_copy$default$6__T13')  # <T13>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    _copy$default$7__T9 = typing.TypeVar('_copy$default$7__T9')  # <T9>
    _copy$default$7__T10 = typing.TypeVar('_copy$default$7__T10')  # <T10>
    _copy$default$7__T11 = typing.TypeVar('_copy$default$7__T11')  # <T11>
    _copy$default$7__T12 = typing.TypeVar('_copy$default$7__T12')  # <T12>
    _copy$default$7__T13 = typing.TypeVar('_copy$default$7__T13')  # <T13>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    _copy$default$8__T9 = typing.TypeVar('_copy$default$8__T9')  # <T9>
    _copy$default$8__T10 = typing.TypeVar('_copy$default$8__T10')  # <T10>
    _copy$default$8__T11 = typing.TypeVar('_copy$default$8__T11')  # <T11>
    _copy$default$8__T12 = typing.TypeVar('_copy$default$8__T12')  # <T12>
    _copy$default$8__T13 = typing.TypeVar('_copy$default$8__T13')  # <T13>
    def copy$default$8(self) -> typing.Any: ...
    _copy$default$9__T1 = typing.TypeVar('_copy$default$9__T1')  # <T1>
    _copy$default$9__T2 = typing.TypeVar('_copy$default$9__T2')  # <T2>
    _copy$default$9__T3 = typing.TypeVar('_copy$default$9__T3')  # <T3>
    _copy$default$9__T4 = typing.TypeVar('_copy$default$9__T4')  # <T4>
    _copy$default$9__T5 = typing.TypeVar('_copy$default$9__T5')  # <T5>
    _copy$default$9__T6 = typing.TypeVar('_copy$default$9__T6')  # <T6>
    _copy$default$9__T7 = typing.TypeVar('_copy$default$9__T7')  # <T7>
    _copy$default$9__T8 = typing.TypeVar('_copy$default$9__T8')  # <T8>
    _copy$default$9__T9 = typing.TypeVar('_copy$default$9__T9')  # <T9>
    _copy$default$9__T10 = typing.TypeVar('_copy$default$9__T10')  # <T10>
    _copy$default$9__T11 = typing.TypeVar('_copy$default$9__T11')  # <T11>
    _copy$default$9__T12 = typing.TypeVar('_copy$default$9__T12')  # <T12>
    _copy$default$9__T13 = typing.TypeVar('_copy$default$9__T13')  # <T13>
    def copy$default$9(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    @staticmethod
    def unapply(x$0: 'Tuple13'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13]) -> Option['Tuple13'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13]]: ...

_Tuple14__T1 = typing.TypeVar('_Tuple14__T1')  # <T1>
_Tuple14__T2 = typing.TypeVar('_Tuple14__T2')  # <T2>
_Tuple14__T3 = typing.TypeVar('_Tuple14__T3')  # <T3>
_Tuple14__T4 = typing.TypeVar('_Tuple14__T4')  # <T4>
_Tuple14__T5 = typing.TypeVar('_Tuple14__T5')  # <T5>
_Tuple14__T6 = typing.TypeVar('_Tuple14__T6')  # <T6>
_Tuple14__T7 = typing.TypeVar('_Tuple14__T7')  # <T7>
_Tuple14__T8 = typing.TypeVar('_Tuple14__T8')  # <T8>
_Tuple14__T9 = typing.TypeVar('_Tuple14__T9')  # <T9>
_Tuple14__T10 = typing.TypeVar('_Tuple14__T10')  # <T10>
_Tuple14__T11 = typing.TypeVar('_Tuple14__T11')  # <T11>
_Tuple14__T12 = typing.TypeVar('_Tuple14__T12')  # <T12>
_Tuple14__T13 = typing.TypeVar('_Tuple14__T13')  # <T13>
_Tuple14__T14 = typing.TypeVar('_Tuple14__T14')  # <T14>
class Tuple14(Product14[_Tuple14__T1, _Tuple14__T2, _Tuple14__T3, _Tuple14__T4, _Tuple14__T5, _Tuple14__T6, _Tuple14__T7, _Tuple14__T8, _Tuple14__T9, _Tuple14__T10, _Tuple14__T11, _Tuple14__T12, _Tuple14__T13, _Tuple14__T14], Serializable, typing.Generic[_Tuple14__T1, _Tuple14__T2, _Tuple14__T3, _Tuple14__T4, _Tuple14__T5, _Tuple14__T6, _Tuple14__T7, _Tuple14__T8, _Tuple14__T9, _Tuple14__T10, _Tuple14__T11, _Tuple14__T12, _Tuple14__T13, _Tuple14__T14]):
    def __init__(self, _1: _Tuple14__T1, _2: _Tuple14__T2, _3: _Tuple14__T3, _4: _Tuple14__T4, _5: _Tuple14__T5, _6: _Tuple14__T6, _7: _Tuple14__T7, _8: _Tuple14__T8, _9: _Tuple14__T9, _10: _Tuple14__T10, _11: _Tuple14__T11, _12: _Tuple14__T12, _13: _Tuple14__T13, _14: _Tuple14__T14): ...
    def _1(self) -> _Tuple14__T1: ...
    def _10(self) -> _Tuple14__T10: ...
    def _11(self) -> _Tuple14__T11: ...
    def _12(self) -> _Tuple14__T12: ...
    def _13(self) -> _Tuple14__T13: ...
    def _14(self) -> _Tuple14__T14: ...
    def _2(self) -> _Tuple14__T2: ...
    def _3(self) -> _Tuple14__T3: ...
    def _4(self) -> _Tuple14__T4: ...
    def _5(self) -> _Tuple14__T5: ...
    def _6(self) -> _Tuple14__T6: ...
    def _7(self) -> _Tuple14__T7: ...
    def _8(self) -> _Tuple14__T8: ...
    def _9(self) -> _Tuple14__T9: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    _apply__T9 = typing.TypeVar('_apply__T9')  # <T9>
    _apply__T10 = typing.TypeVar('_apply__T10')  # <T10>
    _apply__T11 = typing.TypeVar('_apply__T11')  # <T11>
    _apply__T12 = typing.TypeVar('_apply__T12')  # <T12>
    _apply__T13 = typing.TypeVar('_apply__T13')  # <T13>
    _apply__T14 = typing.TypeVar('_apply__T14')  # <T14>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8, _9: _apply__T9, _10: _apply__T10, _11: _apply__T11, _12: _apply__T12, _13: _apply__T13, _14: _apply__T14) -> 'Tuple14'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8, _apply__T9, _apply__T10, _apply__T11, _apply__T12, _apply__T13, _apply__T14]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    _copy__T9 = typing.TypeVar('_copy__T9')  # <T9>
    _copy__T10 = typing.TypeVar('_copy__T10')  # <T10>
    _copy__T11 = typing.TypeVar('_copy__T11')  # <T11>
    _copy__T12 = typing.TypeVar('_copy__T12')  # <T12>
    _copy__T13 = typing.TypeVar('_copy__T13')  # <T13>
    _copy__T14 = typing.TypeVar('_copy__T14')  # <T14>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any, _9: typing.Any, _10: typing.Any, _11: typing.Any, _12: typing.Any, _13: typing.Any, _14: typing.Any) -> 'Tuple14'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    _copy$default$1__T9 = typing.TypeVar('_copy$default$1__T9')  # <T9>
    _copy$default$1__T10 = typing.TypeVar('_copy$default$1__T10')  # <T10>
    _copy$default$1__T11 = typing.TypeVar('_copy$default$1__T11')  # <T11>
    _copy$default$1__T12 = typing.TypeVar('_copy$default$1__T12')  # <T12>
    _copy$default$1__T13 = typing.TypeVar('_copy$default$1__T13')  # <T13>
    _copy$default$1__T14 = typing.TypeVar('_copy$default$1__T14')  # <T14>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$10__T1 = typing.TypeVar('_copy$default$10__T1')  # <T1>
    _copy$default$10__T2 = typing.TypeVar('_copy$default$10__T2')  # <T2>
    _copy$default$10__T3 = typing.TypeVar('_copy$default$10__T3')  # <T3>
    _copy$default$10__T4 = typing.TypeVar('_copy$default$10__T4')  # <T4>
    _copy$default$10__T5 = typing.TypeVar('_copy$default$10__T5')  # <T5>
    _copy$default$10__T6 = typing.TypeVar('_copy$default$10__T6')  # <T6>
    _copy$default$10__T7 = typing.TypeVar('_copy$default$10__T7')  # <T7>
    _copy$default$10__T8 = typing.TypeVar('_copy$default$10__T8')  # <T8>
    _copy$default$10__T9 = typing.TypeVar('_copy$default$10__T9')  # <T9>
    _copy$default$10__T10 = typing.TypeVar('_copy$default$10__T10')  # <T10>
    _copy$default$10__T11 = typing.TypeVar('_copy$default$10__T11')  # <T11>
    _copy$default$10__T12 = typing.TypeVar('_copy$default$10__T12')  # <T12>
    _copy$default$10__T13 = typing.TypeVar('_copy$default$10__T13')  # <T13>
    _copy$default$10__T14 = typing.TypeVar('_copy$default$10__T14')  # <T14>
    def copy$default$10(self) -> typing.Any: ...
    _copy$default$11__T1 = typing.TypeVar('_copy$default$11__T1')  # <T1>
    _copy$default$11__T2 = typing.TypeVar('_copy$default$11__T2')  # <T2>
    _copy$default$11__T3 = typing.TypeVar('_copy$default$11__T3')  # <T3>
    _copy$default$11__T4 = typing.TypeVar('_copy$default$11__T4')  # <T4>
    _copy$default$11__T5 = typing.TypeVar('_copy$default$11__T5')  # <T5>
    _copy$default$11__T6 = typing.TypeVar('_copy$default$11__T6')  # <T6>
    _copy$default$11__T7 = typing.TypeVar('_copy$default$11__T7')  # <T7>
    _copy$default$11__T8 = typing.TypeVar('_copy$default$11__T8')  # <T8>
    _copy$default$11__T9 = typing.TypeVar('_copy$default$11__T9')  # <T9>
    _copy$default$11__T10 = typing.TypeVar('_copy$default$11__T10')  # <T10>
    _copy$default$11__T11 = typing.TypeVar('_copy$default$11__T11')  # <T11>
    _copy$default$11__T12 = typing.TypeVar('_copy$default$11__T12')  # <T12>
    _copy$default$11__T13 = typing.TypeVar('_copy$default$11__T13')  # <T13>
    _copy$default$11__T14 = typing.TypeVar('_copy$default$11__T14')  # <T14>
    def copy$default$11(self) -> typing.Any: ...
    _copy$default$12__T1 = typing.TypeVar('_copy$default$12__T1')  # <T1>
    _copy$default$12__T2 = typing.TypeVar('_copy$default$12__T2')  # <T2>
    _copy$default$12__T3 = typing.TypeVar('_copy$default$12__T3')  # <T3>
    _copy$default$12__T4 = typing.TypeVar('_copy$default$12__T4')  # <T4>
    _copy$default$12__T5 = typing.TypeVar('_copy$default$12__T5')  # <T5>
    _copy$default$12__T6 = typing.TypeVar('_copy$default$12__T6')  # <T6>
    _copy$default$12__T7 = typing.TypeVar('_copy$default$12__T7')  # <T7>
    _copy$default$12__T8 = typing.TypeVar('_copy$default$12__T8')  # <T8>
    _copy$default$12__T9 = typing.TypeVar('_copy$default$12__T9')  # <T9>
    _copy$default$12__T10 = typing.TypeVar('_copy$default$12__T10')  # <T10>
    _copy$default$12__T11 = typing.TypeVar('_copy$default$12__T11')  # <T11>
    _copy$default$12__T12 = typing.TypeVar('_copy$default$12__T12')  # <T12>
    _copy$default$12__T13 = typing.TypeVar('_copy$default$12__T13')  # <T13>
    _copy$default$12__T14 = typing.TypeVar('_copy$default$12__T14')  # <T14>
    def copy$default$12(self) -> typing.Any: ...
    _copy$default$13__T1 = typing.TypeVar('_copy$default$13__T1')  # <T1>
    _copy$default$13__T2 = typing.TypeVar('_copy$default$13__T2')  # <T2>
    _copy$default$13__T3 = typing.TypeVar('_copy$default$13__T3')  # <T3>
    _copy$default$13__T4 = typing.TypeVar('_copy$default$13__T4')  # <T4>
    _copy$default$13__T5 = typing.TypeVar('_copy$default$13__T5')  # <T5>
    _copy$default$13__T6 = typing.TypeVar('_copy$default$13__T6')  # <T6>
    _copy$default$13__T7 = typing.TypeVar('_copy$default$13__T7')  # <T7>
    _copy$default$13__T8 = typing.TypeVar('_copy$default$13__T8')  # <T8>
    _copy$default$13__T9 = typing.TypeVar('_copy$default$13__T9')  # <T9>
    _copy$default$13__T10 = typing.TypeVar('_copy$default$13__T10')  # <T10>
    _copy$default$13__T11 = typing.TypeVar('_copy$default$13__T11')  # <T11>
    _copy$default$13__T12 = typing.TypeVar('_copy$default$13__T12')  # <T12>
    _copy$default$13__T13 = typing.TypeVar('_copy$default$13__T13')  # <T13>
    _copy$default$13__T14 = typing.TypeVar('_copy$default$13__T14')  # <T14>
    def copy$default$13(self) -> typing.Any: ...
    _copy$default$14__T1 = typing.TypeVar('_copy$default$14__T1')  # <T1>
    _copy$default$14__T2 = typing.TypeVar('_copy$default$14__T2')  # <T2>
    _copy$default$14__T3 = typing.TypeVar('_copy$default$14__T3')  # <T3>
    _copy$default$14__T4 = typing.TypeVar('_copy$default$14__T4')  # <T4>
    _copy$default$14__T5 = typing.TypeVar('_copy$default$14__T5')  # <T5>
    _copy$default$14__T6 = typing.TypeVar('_copy$default$14__T6')  # <T6>
    _copy$default$14__T7 = typing.TypeVar('_copy$default$14__T7')  # <T7>
    _copy$default$14__T8 = typing.TypeVar('_copy$default$14__T8')  # <T8>
    _copy$default$14__T9 = typing.TypeVar('_copy$default$14__T9')  # <T9>
    _copy$default$14__T10 = typing.TypeVar('_copy$default$14__T10')  # <T10>
    _copy$default$14__T11 = typing.TypeVar('_copy$default$14__T11')  # <T11>
    _copy$default$14__T12 = typing.TypeVar('_copy$default$14__T12')  # <T12>
    _copy$default$14__T13 = typing.TypeVar('_copy$default$14__T13')  # <T13>
    _copy$default$14__T14 = typing.TypeVar('_copy$default$14__T14')  # <T14>
    def copy$default$14(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    _copy$default$2__T9 = typing.TypeVar('_copy$default$2__T9')  # <T9>
    _copy$default$2__T10 = typing.TypeVar('_copy$default$2__T10')  # <T10>
    _copy$default$2__T11 = typing.TypeVar('_copy$default$2__T11')  # <T11>
    _copy$default$2__T12 = typing.TypeVar('_copy$default$2__T12')  # <T12>
    _copy$default$2__T13 = typing.TypeVar('_copy$default$2__T13')  # <T13>
    _copy$default$2__T14 = typing.TypeVar('_copy$default$2__T14')  # <T14>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    _copy$default$3__T9 = typing.TypeVar('_copy$default$3__T9')  # <T9>
    _copy$default$3__T10 = typing.TypeVar('_copy$default$3__T10')  # <T10>
    _copy$default$3__T11 = typing.TypeVar('_copy$default$3__T11')  # <T11>
    _copy$default$3__T12 = typing.TypeVar('_copy$default$3__T12')  # <T12>
    _copy$default$3__T13 = typing.TypeVar('_copy$default$3__T13')  # <T13>
    _copy$default$3__T14 = typing.TypeVar('_copy$default$3__T14')  # <T14>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    _copy$default$4__T9 = typing.TypeVar('_copy$default$4__T9')  # <T9>
    _copy$default$4__T10 = typing.TypeVar('_copy$default$4__T10')  # <T10>
    _copy$default$4__T11 = typing.TypeVar('_copy$default$4__T11')  # <T11>
    _copy$default$4__T12 = typing.TypeVar('_copy$default$4__T12')  # <T12>
    _copy$default$4__T13 = typing.TypeVar('_copy$default$4__T13')  # <T13>
    _copy$default$4__T14 = typing.TypeVar('_copy$default$4__T14')  # <T14>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    _copy$default$5__T9 = typing.TypeVar('_copy$default$5__T9')  # <T9>
    _copy$default$5__T10 = typing.TypeVar('_copy$default$5__T10')  # <T10>
    _copy$default$5__T11 = typing.TypeVar('_copy$default$5__T11')  # <T11>
    _copy$default$5__T12 = typing.TypeVar('_copy$default$5__T12')  # <T12>
    _copy$default$5__T13 = typing.TypeVar('_copy$default$5__T13')  # <T13>
    _copy$default$5__T14 = typing.TypeVar('_copy$default$5__T14')  # <T14>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    _copy$default$6__T9 = typing.TypeVar('_copy$default$6__T9')  # <T9>
    _copy$default$6__T10 = typing.TypeVar('_copy$default$6__T10')  # <T10>
    _copy$default$6__T11 = typing.TypeVar('_copy$default$6__T11')  # <T11>
    _copy$default$6__T12 = typing.TypeVar('_copy$default$6__T12')  # <T12>
    _copy$default$6__T13 = typing.TypeVar('_copy$default$6__T13')  # <T13>
    _copy$default$6__T14 = typing.TypeVar('_copy$default$6__T14')  # <T14>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    _copy$default$7__T9 = typing.TypeVar('_copy$default$7__T9')  # <T9>
    _copy$default$7__T10 = typing.TypeVar('_copy$default$7__T10')  # <T10>
    _copy$default$7__T11 = typing.TypeVar('_copy$default$7__T11')  # <T11>
    _copy$default$7__T12 = typing.TypeVar('_copy$default$7__T12')  # <T12>
    _copy$default$7__T13 = typing.TypeVar('_copy$default$7__T13')  # <T13>
    _copy$default$7__T14 = typing.TypeVar('_copy$default$7__T14')  # <T14>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    _copy$default$8__T9 = typing.TypeVar('_copy$default$8__T9')  # <T9>
    _copy$default$8__T10 = typing.TypeVar('_copy$default$8__T10')  # <T10>
    _copy$default$8__T11 = typing.TypeVar('_copy$default$8__T11')  # <T11>
    _copy$default$8__T12 = typing.TypeVar('_copy$default$8__T12')  # <T12>
    _copy$default$8__T13 = typing.TypeVar('_copy$default$8__T13')  # <T13>
    _copy$default$8__T14 = typing.TypeVar('_copy$default$8__T14')  # <T14>
    def copy$default$8(self) -> typing.Any: ...
    _copy$default$9__T1 = typing.TypeVar('_copy$default$9__T1')  # <T1>
    _copy$default$9__T2 = typing.TypeVar('_copy$default$9__T2')  # <T2>
    _copy$default$9__T3 = typing.TypeVar('_copy$default$9__T3')  # <T3>
    _copy$default$9__T4 = typing.TypeVar('_copy$default$9__T4')  # <T4>
    _copy$default$9__T5 = typing.TypeVar('_copy$default$9__T5')  # <T5>
    _copy$default$9__T6 = typing.TypeVar('_copy$default$9__T6')  # <T6>
    _copy$default$9__T7 = typing.TypeVar('_copy$default$9__T7')  # <T7>
    _copy$default$9__T8 = typing.TypeVar('_copy$default$9__T8')  # <T8>
    _copy$default$9__T9 = typing.TypeVar('_copy$default$9__T9')  # <T9>
    _copy$default$9__T10 = typing.TypeVar('_copy$default$9__T10')  # <T10>
    _copy$default$9__T11 = typing.TypeVar('_copy$default$9__T11')  # <T11>
    _copy$default$9__T12 = typing.TypeVar('_copy$default$9__T12')  # <T12>
    _copy$default$9__T13 = typing.TypeVar('_copy$default$9__T13')  # <T13>
    _copy$default$9__T14 = typing.TypeVar('_copy$default$9__T14')  # <T14>
    def copy$default$9(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    @staticmethod
    def unapply(x$0: 'Tuple14'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14]) -> Option['Tuple14'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14]]: ...

_Tuple15__T1 = typing.TypeVar('_Tuple15__T1')  # <T1>
_Tuple15__T2 = typing.TypeVar('_Tuple15__T2')  # <T2>
_Tuple15__T3 = typing.TypeVar('_Tuple15__T3')  # <T3>
_Tuple15__T4 = typing.TypeVar('_Tuple15__T4')  # <T4>
_Tuple15__T5 = typing.TypeVar('_Tuple15__T5')  # <T5>
_Tuple15__T6 = typing.TypeVar('_Tuple15__T6')  # <T6>
_Tuple15__T7 = typing.TypeVar('_Tuple15__T7')  # <T7>
_Tuple15__T8 = typing.TypeVar('_Tuple15__T8')  # <T8>
_Tuple15__T9 = typing.TypeVar('_Tuple15__T9')  # <T9>
_Tuple15__T10 = typing.TypeVar('_Tuple15__T10')  # <T10>
_Tuple15__T11 = typing.TypeVar('_Tuple15__T11')  # <T11>
_Tuple15__T12 = typing.TypeVar('_Tuple15__T12')  # <T12>
_Tuple15__T13 = typing.TypeVar('_Tuple15__T13')  # <T13>
_Tuple15__T14 = typing.TypeVar('_Tuple15__T14')  # <T14>
_Tuple15__T15 = typing.TypeVar('_Tuple15__T15')  # <T15>
class Tuple15(Product15[_Tuple15__T1, _Tuple15__T2, _Tuple15__T3, _Tuple15__T4, _Tuple15__T5, _Tuple15__T6, _Tuple15__T7, _Tuple15__T8, _Tuple15__T9, _Tuple15__T10, _Tuple15__T11, _Tuple15__T12, _Tuple15__T13, _Tuple15__T14, _Tuple15__T15], Serializable, typing.Generic[_Tuple15__T1, _Tuple15__T2, _Tuple15__T3, _Tuple15__T4, _Tuple15__T5, _Tuple15__T6, _Tuple15__T7, _Tuple15__T8, _Tuple15__T9, _Tuple15__T10, _Tuple15__T11, _Tuple15__T12, _Tuple15__T13, _Tuple15__T14, _Tuple15__T15]):
    def __init__(self, _1: _Tuple15__T1, _2: _Tuple15__T2, _3: _Tuple15__T3, _4: _Tuple15__T4, _5: _Tuple15__T5, _6: _Tuple15__T6, _7: _Tuple15__T7, _8: _Tuple15__T8, _9: _Tuple15__T9, _10: _Tuple15__T10, _11: _Tuple15__T11, _12: _Tuple15__T12, _13: _Tuple15__T13, _14: _Tuple15__T14, _15: _Tuple15__T15): ...
    def _1(self) -> _Tuple15__T1: ...
    def _10(self) -> _Tuple15__T10: ...
    def _11(self) -> _Tuple15__T11: ...
    def _12(self) -> _Tuple15__T12: ...
    def _13(self) -> _Tuple15__T13: ...
    def _14(self) -> _Tuple15__T14: ...
    def _15(self) -> _Tuple15__T15: ...
    def _2(self) -> _Tuple15__T2: ...
    def _3(self) -> _Tuple15__T3: ...
    def _4(self) -> _Tuple15__T4: ...
    def _5(self) -> _Tuple15__T5: ...
    def _6(self) -> _Tuple15__T6: ...
    def _7(self) -> _Tuple15__T7: ...
    def _8(self) -> _Tuple15__T8: ...
    def _9(self) -> _Tuple15__T9: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    _apply__T9 = typing.TypeVar('_apply__T9')  # <T9>
    _apply__T10 = typing.TypeVar('_apply__T10')  # <T10>
    _apply__T11 = typing.TypeVar('_apply__T11')  # <T11>
    _apply__T12 = typing.TypeVar('_apply__T12')  # <T12>
    _apply__T13 = typing.TypeVar('_apply__T13')  # <T13>
    _apply__T14 = typing.TypeVar('_apply__T14')  # <T14>
    _apply__T15 = typing.TypeVar('_apply__T15')  # <T15>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8, _9: _apply__T9, _10: _apply__T10, _11: _apply__T11, _12: _apply__T12, _13: _apply__T13, _14: _apply__T14, _15: _apply__T15) -> 'Tuple15'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8, _apply__T9, _apply__T10, _apply__T11, _apply__T12, _apply__T13, _apply__T14, _apply__T15]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    _copy__T9 = typing.TypeVar('_copy__T9')  # <T9>
    _copy__T10 = typing.TypeVar('_copy__T10')  # <T10>
    _copy__T11 = typing.TypeVar('_copy__T11')  # <T11>
    _copy__T12 = typing.TypeVar('_copy__T12')  # <T12>
    _copy__T13 = typing.TypeVar('_copy__T13')  # <T13>
    _copy__T14 = typing.TypeVar('_copy__T14')  # <T14>
    _copy__T15 = typing.TypeVar('_copy__T15')  # <T15>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any, _9: typing.Any, _10: typing.Any, _11: typing.Any, _12: typing.Any, _13: typing.Any, _14: typing.Any, _15: typing.Any) -> 'Tuple15'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    _copy$default$1__T9 = typing.TypeVar('_copy$default$1__T9')  # <T9>
    _copy$default$1__T10 = typing.TypeVar('_copy$default$1__T10')  # <T10>
    _copy$default$1__T11 = typing.TypeVar('_copy$default$1__T11')  # <T11>
    _copy$default$1__T12 = typing.TypeVar('_copy$default$1__T12')  # <T12>
    _copy$default$1__T13 = typing.TypeVar('_copy$default$1__T13')  # <T13>
    _copy$default$1__T14 = typing.TypeVar('_copy$default$1__T14')  # <T14>
    _copy$default$1__T15 = typing.TypeVar('_copy$default$1__T15')  # <T15>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$10__T1 = typing.TypeVar('_copy$default$10__T1')  # <T1>
    _copy$default$10__T2 = typing.TypeVar('_copy$default$10__T2')  # <T2>
    _copy$default$10__T3 = typing.TypeVar('_copy$default$10__T3')  # <T3>
    _copy$default$10__T4 = typing.TypeVar('_copy$default$10__T4')  # <T4>
    _copy$default$10__T5 = typing.TypeVar('_copy$default$10__T5')  # <T5>
    _copy$default$10__T6 = typing.TypeVar('_copy$default$10__T6')  # <T6>
    _copy$default$10__T7 = typing.TypeVar('_copy$default$10__T7')  # <T7>
    _copy$default$10__T8 = typing.TypeVar('_copy$default$10__T8')  # <T8>
    _copy$default$10__T9 = typing.TypeVar('_copy$default$10__T9')  # <T9>
    _copy$default$10__T10 = typing.TypeVar('_copy$default$10__T10')  # <T10>
    _copy$default$10__T11 = typing.TypeVar('_copy$default$10__T11')  # <T11>
    _copy$default$10__T12 = typing.TypeVar('_copy$default$10__T12')  # <T12>
    _copy$default$10__T13 = typing.TypeVar('_copy$default$10__T13')  # <T13>
    _copy$default$10__T14 = typing.TypeVar('_copy$default$10__T14')  # <T14>
    _copy$default$10__T15 = typing.TypeVar('_copy$default$10__T15')  # <T15>
    def copy$default$10(self) -> typing.Any: ...
    _copy$default$11__T1 = typing.TypeVar('_copy$default$11__T1')  # <T1>
    _copy$default$11__T2 = typing.TypeVar('_copy$default$11__T2')  # <T2>
    _copy$default$11__T3 = typing.TypeVar('_copy$default$11__T3')  # <T3>
    _copy$default$11__T4 = typing.TypeVar('_copy$default$11__T4')  # <T4>
    _copy$default$11__T5 = typing.TypeVar('_copy$default$11__T5')  # <T5>
    _copy$default$11__T6 = typing.TypeVar('_copy$default$11__T6')  # <T6>
    _copy$default$11__T7 = typing.TypeVar('_copy$default$11__T7')  # <T7>
    _copy$default$11__T8 = typing.TypeVar('_copy$default$11__T8')  # <T8>
    _copy$default$11__T9 = typing.TypeVar('_copy$default$11__T9')  # <T9>
    _copy$default$11__T10 = typing.TypeVar('_copy$default$11__T10')  # <T10>
    _copy$default$11__T11 = typing.TypeVar('_copy$default$11__T11')  # <T11>
    _copy$default$11__T12 = typing.TypeVar('_copy$default$11__T12')  # <T12>
    _copy$default$11__T13 = typing.TypeVar('_copy$default$11__T13')  # <T13>
    _copy$default$11__T14 = typing.TypeVar('_copy$default$11__T14')  # <T14>
    _copy$default$11__T15 = typing.TypeVar('_copy$default$11__T15')  # <T15>
    def copy$default$11(self) -> typing.Any: ...
    _copy$default$12__T1 = typing.TypeVar('_copy$default$12__T1')  # <T1>
    _copy$default$12__T2 = typing.TypeVar('_copy$default$12__T2')  # <T2>
    _copy$default$12__T3 = typing.TypeVar('_copy$default$12__T3')  # <T3>
    _copy$default$12__T4 = typing.TypeVar('_copy$default$12__T4')  # <T4>
    _copy$default$12__T5 = typing.TypeVar('_copy$default$12__T5')  # <T5>
    _copy$default$12__T6 = typing.TypeVar('_copy$default$12__T6')  # <T6>
    _copy$default$12__T7 = typing.TypeVar('_copy$default$12__T7')  # <T7>
    _copy$default$12__T8 = typing.TypeVar('_copy$default$12__T8')  # <T8>
    _copy$default$12__T9 = typing.TypeVar('_copy$default$12__T9')  # <T9>
    _copy$default$12__T10 = typing.TypeVar('_copy$default$12__T10')  # <T10>
    _copy$default$12__T11 = typing.TypeVar('_copy$default$12__T11')  # <T11>
    _copy$default$12__T12 = typing.TypeVar('_copy$default$12__T12')  # <T12>
    _copy$default$12__T13 = typing.TypeVar('_copy$default$12__T13')  # <T13>
    _copy$default$12__T14 = typing.TypeVar('_copy$default$12__T14')  # <T14>
    _copy$default$12__T15 = typing.TypeVar('_copy$default$12__T15')  # <T15>
    def copy$default$12(self) -> typing.Any: ...
    _copy$default$13__T1 = typing.TypeVar('_copy$default$13__T1')  # <T1>
    _copy$default$13__T2 = typing.TypeVar('_copy$default$13__T2')  # <T2>
    _copy$default$13__T3 = typing.TypeVar('_copy$default$13__T3')  # <T3>
    _copy$default$13__T4 = typing.TypeVar('_copy$default$13__T4')  # <T4>
    _copy$default$13__T5 = typing.TypeVar('_copy$default$13__T5')  # <T5>
    _copy$default$13__T6 = typing.TypeVar('_copy$default$13__T6')  # <T6>
    _copy$default$13__T7 = typing.TypeVar('_copy$default$13__T7')  # <T7>
    _copy$default$13__T8 = typing.TypeVar('_copy$default$13__T8')  # <T8>
    _copy$default$13__T9 = typing.TypeVar('_copy$default$13__T9')  # <T9>
    _copy$default$13__T10 = typing.TypeVar('_copy$default$13__T10')  # <T10>
    _copy$default$13__T11 = typing.TypeVar('_copy$default$13__T11')  # <T11>
    _copy$default$13__T12 = typing.TypeVar('_copy$default$13__T12')  # <T12>
    _copy$default$13__T13 = typing.TypeVar('_copy$default$13__T13')  # <T13>
    _copy$default$13__T14 = typing.TypeVar('_copy$default$13__T14')  # <T14>
    _copy$default$13__T15 = typing.TypeVar('_copy$default$13__T15')  # <T15>
    def copy$default$13(self) -> typing.Any: ...
    _copy$default$14__T1 = typing.TypeVar('_copy$default$14__T1')  # <T1>
    _copy$default$14__T2 = typing.TypeVar('_copy$default$14__T2')  # <T2>
    _copy$default$14__T3 = typing.TypeVar('_copy$default$14__T3')  # <T3>
    _copy$default$14__T4 = typing.TypeVar('_copy$default$14__T4')  # <T4>
    _copy$default$14__T5 = typing.TypeVar('_copy$default$14__T5')  # <T5>
    _copy$default$14__T6 = typing.TypeVar('_copy$default$14__T6')  # <T6>
    _copy$default$14__T7 = typing.TypeVar('_copy$default$14__T7')  # <T7>
    _copy$default$14__T8 = typing.TypeVar('_copy$default$14__T8')  # <T8>
    _copy$default$14__T9 = typing.TypeVar('_copy$default$14__T9')  # <T9>
    _copy$default$14__T10 = typing.TypeVar('_copy$default$14__T10')  # <T10>
    _copy$default$14__T11 = typing.TypeVar('_copy$default$14__T11')  # <T11>
    _copy$default$14__T12 = typing.TypeVar('_copy$default$14__T12')  # <T12>
    _copy$default$14__T13 = typing.TypeVar('_copy$default$14__T13')  # <T13>
    _copy$default$14__T14 = typing.TypeVar('_copy$default$14__T14')  # <T14>
    _copy$default$14__T15 = typing.TypeVar('_copy$default$14__T15')  # <T15>
    def copy$default$14(self) -> typing.Any: ...
    _copy$default$15__T1 = typing.TypeVar('_copy$default$15__T1')  # <T1>
    _copy$default$15__T2 = typing.TypeVar('_copy$default$15__T2')  # <T2>
    _copy$default$15__T3 = typing.TypeVar('_copy$default$15__T3')  # <T3>
    _copy$default$15__T4 = typing.TypeVar('_copy$default$15__T4')  # <T4>
    _copy$default$15__T5 = typing.TypeVar('_copy$default$15__T5')  # <T5>
    _copy$default$15__T6 = typing.TypeVar('_copy$default$15__T6')  # <T6>
    _copy$default$15__T7 = typing.TypeVar('_copy$default$15__T7')  # <T7>
    _copy$default$15__T8 = typing.TypeVar('_copy$default$15__T8')  # <T8>
    _copy$default$15__T9 = typing.TypeVar('_copy$default$15__T9')  # <T9>
    _copy$default$15__T10 = typing.TypeVar('_copy$default$15__T10')  # <T10>
    _copy$default$15__T11 = typing.TypeVar('_copy$default$15__T11')  # <T11>
    _copy$default$15__T12 = typing.TypeVar('_copy$default$15__T12')  # <T12>
    _copy$default$15__T13 = typing.TypeVar('_copy$default$15__T13')  # <T13>
    _copy$default$15__T14 = typing.TypeVar('_copy$default$15__T14')  # <T14>
    _copy$default$15__T15 = typing.TypeVar('_copy$default$15__T15')  # <T15>
    def copy$default$15(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    _copy$default$2__T9 = typing.TypeVar('_copy$default$2__T9')  # <T9>
    _copy$default$2__T10 = typing.TypeVar('_copy$default$2__T10')  # <T10>
    _copy$default$2__T11 = typing.TypeVar('_copy$default$2__T11')  # <T11>
    _copy$default$2__T12 = typing.TypeVar('_copy$default$2__T12')  # <T12>
    _copy$default$2__T13 = typing.TypeVar('_copy$default$2__T13')  # <T13>
    _copy$default$2__T14 = typing.TypeVar('_copy$default$2__T14')  # <T14>
    _copy$default$2__T15 = typing.TypeVar('_copy$default$2__T15')  # <T15>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    _copy$default$3__T9 = typing.TypeVar('_copy$default$3__T9')  # <T9>
    _copy$default$3__T10 = typing.TypeVar('_copy$default$3__T10')  # <T10>
    _copy$default$3__T11 = typing.TypeVar('_copy$default$3__T11')  # <T11>
    _copy$default$3__T12 = typing.TypeVar('_copy$default$3__T12')  # <T12>
    _copy$default$3__T13 = typing.TypeVar('_copy$default$3__T13')  # <T13>
    _copy$default$3__T14 = typing.TypeVar('_copy$default$3__T14')  # <T14>
    _copy$default$3__T15 = typing.TypeVar('_copy$default$3__T15')  # <T15>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    _copy$default$4__T9 = typing.TypeVar('_copy$default$4__T9')  # <T9>
    _copy$default$4__T10 = typing.TypeVar('_copy$default$4__T10')  # <T10>
    _copy$default$4__T11 = typing.TypeVar('_copy$default$4__T11')  # <T11>
    _copy$default$4__T12 = typing.TypeVar('_copy$default$4__T12')  # <T12>
    _copy$default$4__T13 = typing.TypeVar('_copy$default$4__T13')  # <T13>
    _copy$default$4__T14 = typing.TypeVar('_copy$default$4__T14')  # <T14>
    _copy$default$4__T15 = typing.TypeVar('_copy$default$4__T15')  # <T15>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    _copy$default$5__T9 = typing.TypeVar('_copy$default$5__T9')  # <T9>
    _copy$default$5__T10 = typing.TypeVar('_copy$default$5__T10')  # <T10>
    _copy$default$5__T11 = typing.TypeVar('_copy$default$5__T11')  # <T11>
    _copy$default$5__T12 = typing.TypeVar('_copy$default$5__T12')  # <T12>
    _copy$default$5__T13 = typing.TypeVar('_copy$default$5__T13')  # <T13>
    _copy$default$5__T14 = typing.TypeVar('_copy$default$5__T14')  # <T14>
    _copy$default$5__T15 = typing.TypeVar('_copy$default$5__T15')  # <T15>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    _copy$default$6__T9 = typing.TypeVar('_copy$default$6__T9')  # <T9>
    _copy$default$6__T10 = typing.TypeVar('_copy$default$6__T10')  # <T10>
    _copy$default$6__T11 = typing.TypeVar('_copy$default$6__T11')  # <T11>
    _copy$default$6__T12 = typing.TypeVar('_copy$default$6__T12')  # <T12>
    _copy$default$6__T13 = typing.TypeVar('_copy$default$6__T13')  # <T13>
    _copy$default$6__T14 = typing.TypeVar('_copy$default$6__T14')  # <T14>
    _copy$default$6__T15 = typing.TypeVar('_copy$default$6__T15')  # <T15>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    _copy$default$7__T9 = typing.TypeVar('_copy$default$7__T9')  # <T9>
    _copy$default$7__T10 = typing.TypeVar('_copy$default$7__T10')  # <T10>
    _copy$default$7__T11 = typing.TypeVar('_copy$default$7__T11')  # <T11>
    _copy$default$7__T12 = typing.TypeVar('_copy$default$7__T12')  # <T12>
    _copy$default$7__T13 = typing.TypeVar('_copy$default$7__T13')  # <T13>
    _copy$default$7__T14 = typing.TypeVar('_copy$default$7__T14')  # <T14>
    _copy$default$7__T15 = typing.TypeVar('_copy$default$7__T15')  # <T15>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    _copy$default$8__T9 = typing.TypeVar('_copy$default$8__T9')  # <T9>
    _copy$default$8__T10 = typing.TypeVar('_copy$default$8__T10')  # <T10>
    _copy$default$8__T11 = typing.TypeVar('_copy$default$8__T11')  # <T11>
    _copy$default$8__T12 = typing.TypeVar('_copy$default$8__T12')  # <T12>
    _copy$default$8__T13 = typing.TypeVar('_copy$default$8__T13')  # <T13>
    _copy$default$8__T14 = typing.TypeVar('_copy$default$8__T14')  # <T14>
    _copy$default$8__T15 = typing.TypeVar('_copy$default$8__T15')  # <T15>
    def copy$default$8(self) -> typing.Any: ...
    _copy$default$9__T1 = typing.TypeVar('_copy$default$9__T1')  # <T1>
    _copy$default$9__T2 = typing.TypeVar('_copy$default$9__T2')  # <T2>
    _copy$default$9__T3 = typing.TypeVar('_copy$default$9__T3')  # <T3>
    _copy$default$9__T4 = typing.TypeVar('_copy$default$9__T4')  # <T4>
    _copy$default$9__T5 = typing.TypeVar('_copy$default$9__T5')  # <T5>
    _copy$default$9__T6 = typing.TypeVar('_copy$default$9__T6')  # <T6>
    _copy$default$9__T7 = typing.TypeVar('_copy$default$9__T7')  # <T7>
    _copy$default$9__T8 = typing.TypeVar('_copy$default$9__T8')  # <T8>
    _copy$default$9__T9 = typing.TypeVar('_copy$default$9__T9')  # <T9>
    _copy$default$9__T10 = typing.TypeVar('_copy$default$9__T10')  # <T10>
    _copy$default$9__T11 = typing.TypeVar('_copy$default$9__T11')  # <T11>
    _copy$default$9__T12 = typing.TypeVar('_copy$default$9__T12')  # <T12>
    _copy$default$9__T13 = typing.TypeVar('_copy$default$9__T13')  # <T13>
    _copy$default$9__T14 = typing.TypeVar('_copy$default$9__T14')  # <T14>
    _copy$default$9__T15 = typing.TypeVar('_copy$default$9__T15')  # <T15>
    def copy$default$9(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    @staticmethod
    def unapply(x$0: 'Tuple15'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15]) -> Option['Tuple15'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15]]: ...

_Tuple16__T1 = typing.TypeVar('_Tuple16__T1')  # <T1>
_Tuple16__T2 = typing.TypeVar('_Tuple16__T2')  # <T2>
_Tuple16__T3 = typing.TypeVar('_Tuple16__T3')  # <T3>
_Tuple16__T4 = typing.TypeVar('_Tuple16__T4')  # <T4>
_Tuple16__T5 = typing.TypeVar('_Tuple16__T5')  # <T5>
_Tuple16__T6 = typing.TypeVar('_Tuple16__T6')  # <T6>
_Tuple16__T7 = typing.TypeVar('_Tuple16__T7')  # <T7>
_Tuple16__T8 = typing.TypeVar('_Tuple16__T8')  # <T8>
_Tuple16__T9 = typing.TypeVar('_Tuple16__T9')  # <T9>
_Tuple16__T10 = typing.TypeVar('_Tuple16__T10')  # <T10>
_Tuple16__T11 = typing.TypeVar('_Tuple16__T11')  # <T11>
_Tuple16__T12 = typing.TypeVar('_Tuple16__T12')  # <T12>
_Tuple16__T13 = typing.TypeVar('_Tuple16__T13')  # <T13>
_Tuple16__T14 = typing.TypeVar('_Tuple16__T14')  # <T14>
_Tuple16__T15 = typing.TypeVar('_Tuple16__T15')  # <T15>
_Tuple16__T16 = typing.TypeVar('_Tuple16__T16')  # <T16>
class Tuple16(Product16[_Tuple16__T1, _Tuple16__T2, _Tuple16__T3, _Tuple16__T4, _Tuple16__T5, _Tuple16__T6, _Tuple16__T7, _Tuple16__T8, _Tuple16__T9, _Tuple16__T10, _Tuple16__T11, _Tuple16__T12, _Tuple16__T13, _Tuple16__T14, _Tuple16__T15, _Tuple16__T16], Serializable, typing.Generic[_Tuple16__T1, _Tuple16__T2, _Tuple16__T3, _Tuple16__T4, _Tuple16__T5, _Tuple16__T6, _Tuple16__T7, _Tuple16__T8, _Tuple16__T9, _Tuple16__T10, _Tuple16__T11, _Tuple16__T12, _Tuple16__T13, _Tuple16__T14, _Tuple16__T15, _Tuple16__T16]):
    def __init__(self, _1: _Tuple16__T1, _2: _Tuple16__T2, _3: _Tuple16__T3, _4: _Tuple16__T4, _5: _Tuple16__T5, _6: _Tuple16__T6, _7: _Tuple16__T7, _8: _Tuple16__T8, _9: _Tuple16__T9, _10: _Tuple16__T10, _11: _Tuple16__T11, _12: _Tuple16__T12, _13: _Tuple16__T13, _14: _Tuple16__T14, _15: _Tuple16__T15, _16: _Tuple16__T16): ...
    def _1(self) -> _Tuple16__T1: ...
    def _10(self) -> _Tuple16__T10: ...
    def _11(self) -> _Tuple16__T11: ...
    def _12(self) -> _Tuple16__T12: ...
    def _13(self) -> _Tuple16__T13: ...
    def _14(self) -> _Tuple16__T14: ...
    def _15(self) -> _Tuple16__T15: ...
    def _16(self) -> _Tuple16__T16: ...
    def _2(self) -> _Tuple16__T2: ...
    def _3(self) -> _Tuple16__T3: ...
    def _4(self) -> _Tuple16__T4: ...
    def _5(self) -> _Tuple16__T5: ...
    def _6(self) -> _Tuple16__T6: ...
    def _7(self) -> _Tuple16__T7: ...
    def _8(self) -> _Tuple16__T8: ...
    def _9(self) -> _Tuple16__T9: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    _apply__T9 = typing.TypeVar('_apply__T9')  # <T9>
    _apply__T10 = typing.TypeVar('_apply__T10')  # <T10>
    _apply__T11 = typing.TypeVar('_apply__T11')  # <T11>
    _apply__T12 = typing.TypeVar('_apply__T12')  # <T12>
    _apply__T13 = typing.TypeVar('_apply__T13')  # <T13>
    _apply__T14 = typing.TypeVar('_apply__T14')  # <T14>
    _apply__T15 = typing.TypeVar('_apply__T15')  # <T15>
    _apply__T16 = typing.TypeVar('_apply__T16')  # <T16>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8, _9: _apply__T9, _10: _apply__T10, _11: _apply__T11, _12: _apply__T12, _13: _apply__T13, _14: _apply__T14, _15: _apply__T15, _16: _apply__T16) -> 'Tuple16'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8, _apply__T9, _apply__T10, _apply__T11, _apply__T12, _apply__T13, _apply__T14, _apply__T15, _apply__T16]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    _copy__T9 = typing.TypeVar('_copy__T9')  # <T9>
    _copy__T10 = typing.TypeVar('_copy__T10')  # <T10>
    _copy__T11 = typing.TypeVar('_copy__T11')  # <T11>
    _copy__T12 = typing.TypeVar('_copy__T12')  # <T12>
    _copy__T13 = typing.TypeVar('_copy__T13')  # <T13>
    _copy__T14 = typing.TypeVar('_copy__T14')  # <T14>
    _copy__T15 = typing.TypeVar('_copy__T15')  # <T15>
    _copy__T16 = typing.TypeVar('_copy__T16')  # <T16>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any, _9: typing.Any, _10: typing.Any, _11: typing.Any, _12: typing.Any, _13: typing.Any, _14: typing.Any, _15: typing.Any, _16: typing.Any) -> 'Tuple16'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    _copy$default$1__T9 = typing.TypeVar('_copy$default$1__T9')  # <T9>
    _copy$default$1__T10 = typing.TypeVar('_copy$default$1__T10')  # <T10>
    _copy$default$1__T11 = typing.TypeVar('_copy$default$1__T11')  # <T11>
    _copy$default$1__T12 = typing.TypeVar('_copy$default$1__T12')  # <T12>
    _copy$default$1__T13 = typing.TypeVar('_copy$default$1__T13')  # <T13>
    _copy$default$1__T14 = typing.TypeVar('_copy$default$1__T14')  # <T14>
    _copy$default$1__T15 = typing.TypeVar('_copy$default$1__T15')  # <T15>
    _copy$default$1__T16 = typing.TypeVar('_copy$default$1__T16')  # <T16>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$10__T1 = typing.TypeVar('_copy$default$10__T1')  # <T1>
    _copy$default$10__T2 = typing.TypeVar('_copy$default$10__T2')  # <T2>
    _copy$default$10__T3 = typing.TypeVar('_copy$default$10__T3')  # <T3>
    _copy$default$10__T4 = typing.TypeVar('_copy$default$10__T4')  # <T4>
    _copy$default$10__T5 = typing.TypeVar('_copy$default$10__T5')  # <T5>
    _copy$default$10__T6 = typing.TypeVar('_copy$default$10__T6')  # <T6>
    _copy$default$10__T7 = typing.TypeVar('_copy$default$10__T7')  # <T7>
    _copy$default$10__T8 = typing.TypeVar('_copy$default$10__T8')  # <T8>
    _copy$default$10__T9 = typing.TypeVar('_copy$default$10__T9')  # <T9>
    _copy$default$10__T10 = typing.TypeVar('_copy$default$10__T10')  # <T10>
    _copy$default$10__T11 = typing.TypeVar('_copy$default$10__T11')  # <T11>
    _copy$default$10__T12 = typing.TypeVar('_copy$default$10__T12')  # <T12>
    _copy$default$10__T13 = typing.TypeVar('_copy$default$10__T13')  # <T13>
    _copy$default$10__T14 = typing.TypeVar('_copy$default$10__T14')  # <T14>
    _copy$default$10__T15 = typing.TypeVar('_copy$default$10__T15')  # <T15>
    _copy$default$10__T16 = typing.TypeVar('_copy$default$10__T16')  # <T16>
    def copy$default$10(self) -> typing.Any: ...
    _copy$default$11__T1 = typing.TypeVar('_copy$default$11__T1')  # <T1>
    _copy$default$11__T2 = typing.TypeVar('_copy$default$11__T2')  # <T2>
    _copy$default$11__T3 = typing.TypeVar('_copy$default$11__T3')  # <T3>
    _copy$default$11__T4 = typing.TypeVar('_copy$default$11__T4')  # <T4>
    _copy$default$11__T5 = typing.TypeVar('_copy$default$11__T5')  # <T5>
    _copy$default$11__T6 = typing.TypeVar('_copy$default$11__T6')  # <T6>
    _copy$default$11__T7 = typing.TypeVar('_copy$default$11__T7')  # <T7>
    _copy$default$11__T8 = typing.TypeVar('_copy$default$11__T8')  # <T8>
    _copy$default$11__T9 = typing.TypeVar('_copy$default$11__T9')  # <T9>
    _copy$default$11__T10 = typing.TypeVar('_copy$default$11__T10')  # <T10>
    _copy$default$11__T11 = typing.TypeVar('_copy$default$11__T11')  # <T11>
    _copy$default$11__T12 = typing.TypeVar('_copy$default$11__T12')  # <T12>
    _copy$default$11__T13 = typing.TypeVar('_copy$default$11__T13')  # <T13>
    _copy$default$11__T14 = typing.TypeVar('_copy$default$11__T14')  # <T14>
    _copy$default$11__T15 = typing.TypeVar('_copy$default$11__T15')  # <T15>
    _copy$default$11__T16 = typing.TypeVar('_copy$default$11__T16')  # <T16>
    def copy$default$11(self) -> typing.Any: ...
    _copy$default$12__T1 = typing.TypeVar('_copy$default$12__T1')  # <T1>
    _copy$default$12__T2 = typing.TypeVar('_copy$default$12__T2')  # <T2>
    _copy$default$12__T3 = typing.TypeVar('_copy$default$12__T3')  # <T3>
    _copy$default$12__T4 = typing.TypeVar('_copy$default$12__T4')  # <T4>
    _copy$default$12__T5 = typing.TypeVar('_copy$default$12__T5')  # <T5>
    _copy$default$12__T6 = typing.TypeVar('_copy$default$12__T6')  # <T6>
    _copy$default$12__T7 = typing.TypeVar('_copy$default$12__T7')  # <T7>
    _copy$default$12__T8 = typing.TypeVar('_copy$default$12__T8')  # <T8>
    _copy$default$12__T9 = typing.TypeVar('_copy$default$12__T9')  # <T9>
    _copy$default$12__T10 = typing.TypeVar('_copy$default$12__T10')  # <T10>
    _copy$default$12__T11 = typing.TypeVar('_copy$default$12__T11')  # <T11>
    _copy$default$12__T12 = typing.TypeVar('_copy$default$12__T12')  # <T12>
    _copy$default$12__T13 = typing.TypeVar('_copy$default$12__T13')  # <T13>
    _copy$default$12__T14 = typing.TypeVar('_copy$default$12__T14')  # <T14>
    _copy$default$12__T15 = typing.TypeVar('_copy$default$12__T15')  # <T15>
    _copy$default$12__T16 = typing.TypeVar('_copy$default$12__T16')  # <T16>
    def copy$default$12(self) -> typing.Any: ...
    _copy$default$13__T1 = typing.TypeVar('_copy$default$13__T1')  # <T1>
    _copy$default$13__T2 = typing.TypeVar('_copy$default$13__T2')  # <T2>
    _copy$default$13__T3 = typing.TypeVar('_copy$default$13__T3')  # <T3>
    _copy$default$13__T4 = typing.TypeVar('_copy$default$13__T4')  # <T4>
    _copy$default$13__T5 = typing.TypeVar('_copy$default$13__T5')  # <T5>
    _copy$default$13__T6 = typing.TypeVar('_copy$default$13__T6')  # <T6>
    _copy$default$13__T7 = typing.TypeVar('_copy$default$13__T7')  # <T7>
    _copy$default$13__T8 = typing.TypeVar('_copy$default$13__T8')  # <T8>
    _copy$default$13__T9 = typing.TypeVar('_copy$default$13__T9')  # <T9>
    _copy$default$13__T10 = typing.TypeVar('_copy$default$13__T10')  # <T10>
    _copy$default$13__T11 = typing.TypeVar('_copy$default$13__T11')  # <T11>
    _copy$default$13__T12 = typing.TypeVar('_copy$default$13__T12')  # <T12>
    _copy$default$13__T13 = typing.TypeVar('_copy$default$13__T13')  # <T13>
    _copy$default$13__T14 = typing.TypeVar('_copy$default$13__T14')  # <T14>
    _copy$default$13__T15 = typing.TypeVar('_copy$default$13__T15')  # <T15>
    _copy$default$13__T16 = typing.TypeVar('_copy$default$13__T16')  # <T16>
    def copy$default$13(self) -> typing.Any: ...
    _copy$default$14__T1 = typing.TypeVar('_copy$default$14__T1')  # <T1>
    _copy$default$14__T2 = typing.TypeVar('_copy$default$14__T2')  # <T2>
    _copy$default$14__T3 = typing.TypeVar('_copy$default$14__T3')  # <T3>
    _copy$default$14__T4 = typing.TypeVar('_copy$default$14__T4')  # <T4>
    _copy$default$14__T5 = typing.TypeVar('_copy$default$14__T5')  # <T5>
    _copy$default$14__T6 = typing.TypeVar('_copy$default$14__T6')  # <T6>
    _copy$default$14__T7 = typing.TypeVar('_copy$default$14__T7')  # <T7>
    _copy$default$14__T8 = typing.TypeVar('_copy$default$14__T8')  # <T8>
    _copy$default$14__T9 = typing.TypeVar('_copy$default$14__T9')  # <T9>
    _copy$default$14__T10 = typing.TypeVar('_copy$default$14__T10')  # <T10>
    _copy$default$14__T11 = typing.TypeVar('_copy$default$14__T11')  # <T11>
    _copy$default$14__T12 = typing.TypeVar('_copy$default$14__T12')  # <T12>
    _copy$default$14__T13 = typing.TypeVar('_copy$default$14__T13')  # <T13>
    _copy$default$14__T14 = typing.TypeVar('_copy$default$14__T14')  # <T14>
    _copy$default$14__T15 = typing.TypeVar('_copy$default$14__T15')  # <T15>
    _copy$default$14__T16 = typing.TypeVar('_copy$default$14__T16')  # <T16>
    def copy$default$14(self) -> typing.Any: ...
    _copy$default$15__T1 = typing.TypeVar('_copy$default$15__T1')  # <T1>
    _copy$default$15__T2 = typing.TypeVar('_copy$default$15__T2')  # <T2>
    _copy$default$15__T3 = typing.TypeVar('_copy$default$15__T3')  # <T3>
    _copy$default$15__T4 = typing.TypeVar('_copy$default$15__T4')  # <T4>
    _copy$default$15__T5 = typing.TypeVar('_copy$default$15__T5')  # <T5>
    _copy$default$15__T6 = typing.TypeVar('_copy$default$15__T6')  # <T6>
    _copy$default$15__T7 = typing.TypeVar('_copy$default$15__T7')  # <T7>
    _copy$default$15__T8 = typing.TypeVar('_copy$default$15__T8')  # <T8>
    _copy$default$15__T9 = typing.TypeVar('_copy$default$15__T9')  # <T9>
    _copy$default$15__T10 = typing.TypeVar('_copy$default$15__T10')  # <T10>
    _copy$default$15__T11 = typing.TypeVar('_copy$default$15__T11')  # <T11>
    _copy$default$15__T12 = typing.TypeVar('_copy$default$15__T12')  # <T12>
    _copy$default$15__T13 = typing.TypeVar('_copy$default$15__T13')  # <T13>
    _copy$default$15__T14 = typing.TypeVar('_copy$default$15__T14')  # <T14>
    _copy$default$15__T15 = typing.TypeVar('_copy$default$15__T15')  # <T15>
    _copy$default$15__T16 = typing.TypeVar('_copy$default$15__T16')  # <T16>
    def copy$default$15(self) -> typing.Any: ...
    _copy$default$16__T1 = typing.TypeVar('_copy$default$16__T1')  # <T1>
    _copy$default$16__T2 = typing.TypeVar('_copy$default$16__T2')  # <T2>
    _copy$default$16__T3 = typing.TypeVar('_copy$default$16__T3')  # <T3>
    _copy$default$16__T4 = typing.TypeVar('_copy$default$16__T4')  # <T4>
    _copy$default$16__T5 = typing.TypeVar('_copy$default$16__T5')  # <T5>
    _copy$default$16__T6 = typing.TypeVar('_copy$default$16__T6')  # <T6>
    _copy$default$16__T7 = typing.TypeVar('_copy$default$16__T7')  # <T7>
    _copy$default$16__T8 = typing.TypeVar('_copy$default$16__T8')  # <T8>
    _copy$default$16__T9 = typing.TypeVar('_copy$default$16__T9')  # <T9>
    _copy$default$16__T10 = typing.TypeVar('_copy$default$16__T10')  # <T10>
    _copy$default$16__T11 = typing.TypeVar('_copy$default$16__T11')  # <T11>
    _copy$default$16__T12 = typing.TypeVar('_copy$default$16__T12')  # <T12>
    _copy$default$16__T13 = typing.TypeVar('_copy$default$16__T13')  # <T13>
    _copy$default$16__T14 = typing.TypeVar('_copy$default$16__T14')  # <T14>
    _copy$default$16__T15 = typing.TypeVar('_copy$default$16__T15')  # <T15>
    _copy$default$16__T16 = typing.TypeVar('_copy$default$16__T16')  # <T16>
    def copy$default$16(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    _copy$default$2__T9 = typing.TypeVar('_copy$default$2__T9')  # <T9>
    _copy$default$2__T10 = typing.TypeVar('_copy$default$2__T10')  # <T10>
    _copy$default$2__T11 = typing.TypeVar('_copy$default$2__T11')  # <T11>
    _copy$default$2__T12 = typing.TypeVar('_copy$default$2__T12')  # <T12>
    _copy$default$2__T13 = typing.TypeVar('_copy$default$2__T13')  # <T13>
    _copy$default$2__T14 = typing.TypeVar('_copy$default$2__T14')  # <T14>
    _copy$default$2__T15 = typing.TypeVar('_copy$default$2__T15')  # <T15>
    _copy$default$2__T16 = typing.TypeVar('_copy$default$2__T16')  # <T16>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    _copy$default$3__T9 = typing.TypeVar('_copy$default$3__T9')  # <T9>
    _copy$default$3__T10 = typing.TypeVar('_copy$default$3__T10')  # <T10>
    _copy$default$3__T11 = typing.TypeVar('_copy$default$3__T11')  # <T11>
    _copy$default$3__T12 = typing.TypeVar('_copy$default$3__T12')  # <T12>
    _copy$default$3__T13 = typing.TypeVar('_copy$default$3__T13')  # <T13>
    _copy$default$3__T14 = typing.TypeVar('_copy$default$3__T14')  # <T14>
    _copy$default$3__T15 = typing.TypeVar('_copy$default$3__T15')  # <T15>
    _copy$default$3__T16 = typing.TypeVar('_copy$default$3__T16')  # <T16>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    _copy$default$4__T9 = typing.TypeVar('_copy$default$4__T9')  # <T9>
    _copy$default$4__T10 = typing.TypeVar('_copy$default$4__T10')  # <T10>
    _copy$default$4__T11 = typing.TypeVar('_copy$default$4__T11')  # <T11>
    _copy$default$4__T12 = typing.TypeVar('_copy$default$4__T12')  # <T12>
    _copy$default$4__T13 = typing.TypeVar('_copy$default$4__T13')  # <T13>
    _copy$default$4__T14 = typing.TypeVar('_copy$default$4__T14')  # <T14>
    _copy$default$4__T15 = typing.TypeVar('_copy$default$4__T15')  # <T15>
    _copy$default$4__T16 = typing.TypeVar('_copy$default$4__T16')  # <T16>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    _copy$default$5__T9 = typing.TypeVar('_copy$default$5__T9')  # <T9>
    _copy$default$5__T10 = typing.TypeVar('_copy$default$5__T10')  # <T10>
    _copy$default$5__T11 = typing.TypeVar('_copy$default$5__T11')  # <T11>
    _copy$default$5__T12 = typing.TypeVar('_copy$default$5__T12')  # <T12>
    _copy$default$5__T13 = typing.TypeVar('_copy$default$5__T13')  # <T13>
    _copy$default$5__T14 = typing.TypeVar('_copy$default$5__T14')  # <T14>
    _copy$default$5__T15 = typing.TypeVar('_copy$default$5__T15')  # <T15>
    _copy$default$5__T16 = typing.TypeVar('_copy$default$5__T16')  # <T16>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    _copy$default$6__T9 = typing.TypeVar('_copy$default$6__T9')  # <T9>
    _copy$default$6__T10 = typing.TypeVar('_copy$default$6__T10')  # <T10>
    _copy$default$6__T11 = typing.TypeVar('_copy$default$6__T11')  # <T11>
    _copy$default$6__T12 = typing.TypeVar('_copy$default$6__T12')  # <T12>
    _copy$default$6__T13 = typing.TypeVar('_copy$default$6__T13')  # <T13>
    _copy$default$6__T14 = typing.TypeVar('_copy$default$6__T14')  # <T14>
    _copy$default$6__T15 = typing.TypeVar('_copy$default$6__T15')  # <T15>
    _copy$default$6__T16 = typing.TypeVar('_copy$default$6__T16')  # <T16>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    _copy$default$7__T9 = typing.TypeVar('_copy$default$7__T9')  # <T9>
    _copy$default$7__T10 = typing.TypeVar('_copy$default$7__T10')  # <T10>
    _copy$default$7__T11 = typing.TypeVar('_copy$default$7__T11')  # <T11>
    _copy$default$7__T12 = typing.TypeVar('_copy$default$7__T12')  # <T12>
    _copy$default$7__T13 = typing.TypeVar('_copy$default$7__T13')  # <T13>
    _copy$default$7__T14 = typing.TypeVar('_copy$default$7__T14')  # <T14>
    _copy$default$7__T15 = typing.TypeVar('_copy$default$7__T15')  # <T15>
    _copy$default$7__T16 = typing.TypeVar('_copy$default$7__T16')  # <T16>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    _copy$default$8__T9 = typing.TypeVar('_copy$default$8__T9')  # <T9>
    _copy$default$8__T10 = typing.TypeVar('_copy$default$8__T10')  # <T10>
    _copy$default$8__T11 = typing.TypeVar('_copy$default$8__T11')  # <T11>
    _copy$default$8__T12 = typing.TypeVar('_copy$default$8__T12')  # <T12>
    _copy$default$8__T13 = typing.TypeVar('_copy$default$8__T13')  # <T13>
    _copy$default$8__T14 = typing.TypeVar('_copy$default$8__T14')  # <T14>
    _copy$default$8__T15 = typing.TypeVar('_copy$default$8__T15')  # <T15>
    _copy$default$8__T16 = typing.TypeVar('_copy$default$8__T16')  # <T16>
    def copy$default$8(self) -> typing.Any: ...
    _copy$default$9__T1 = typing.TypeVar('_copy$default$9__T1')  # <T1>
    _copy$default$9__T2 = typing.TypeVar('_copy$default$9__T2')  # <T2>
    _copy$default$9__T3 = typing.TypeVar('_copy$default$9__T3')  # <T3>
    _copy$default$9__T4 = typing.TypeVar('_copy$default$9__T4')  # <T4>
    _copy$default$9__T5 = typing.TypeVar('_copy$default$9__T5')  # <T5>
    _copy$default$9__T6 = typing.TypeVar('_copy$default$9__T6')  # <T6>
    _copy$default$9__T7 = typing.TypeVar('_copy$default$9__T7')  # <T7>
    _copy$default$9__T8 = typing.TypeVar('_copy$default$9__T8')  # <T8>
    _copy$default$9__T9 = typing.TypeVar('_copy$default$9__T9')  # <T9>
    _copy$default$9__T10 = typing.TypeVar('_copy$default$9__T10')  # <T10>
    _copy$default$9__T11 = typing.TypeVar('_copy$default$9__T11')  # <T11>
    _copy$default$9__T12 = typing.TypeVar('_copy$default$9__T12')  # <T12>
    _copy$default$9__T13 = typing.TypeVar('_copy$default$9__T13')  # <T13>
    _copy$default$9__T14 = typing.TypeVar('_copy$default$9__T14')  # <T14>
    _copy$default$9__T15 = typing.TypeVar('_copy$default$9__T15')  # <T15>
    _copy$default$9__T16 = typing.TypeVar('_copy$default$9__T16')  # <T16>
    def copy$default$9(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    _unapply__T16 = typing.TypeVar('_unapply__T16')  # <T16>
    @staticmethod
    def unapply(x$0: 'Tuple16'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16]) -> Option['Tuple16'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16]]: ...

_Tuple17__T1 = typing.TypeVar('_Tuple17__T1')  # <T1>
_Tuple17__T2 = typing.TypeVar('_Tuple17__T2')  # <T2>
_Tuple17__T3 = typing.TypeVar('_Tuple17__T3')  # <T3>
_Tuple17__T4 = typing.TypeVar('_Tuple17__T4')  # <T4>
_Tuple17__T5 = typing.TypeVar('_Tuple17__T5')  # <T5>
_Tuple17__T6 = typing.TypeVar('_Tuple17__T6')  # <T6>
_Tuple17__T7 = typing.TypeVar('_Tuple17__T7')  # <T7>
_Tuple17__T8 = typing.TypeVar('_Tuple17__T8')  # <T8>
_Tuple17__T9 = typing.TypeVar('_Tuple17__T9')  # <T9>
_Tuple17__T10 = typing.TypeVar('_Tuple17__T10')  # <T10>
_Tuple17__T11 = typing.TypeVar('_Tuple17__T11')  # <T11>
_Tuple17__T12 = typing.TypeVar('_Tuple17__T12')  # <T12>
_Tuple17__T13 = typing.TypeVar('_Tuple17__T13')  # <T13>
_Tuple17__T14 = typing.TypeVar('_Tuple17__T14')  # <T14>
_Tuple17__T15 = typing.TypeVar('_Tuple17__T15')  # <T15>
_Tuple17__T16 = typing.TypeVar('_Tuple17__T16')  # <T16>
_Tuple17__T17 = typing.TypeVar('_Tuple17__T17')  # <T17>
class Tuple17(Product17[_Tuple17__T1, _Tuple17__T2, _Tuple17__T3, _Tuple17__T4, _Tuple17__T5, _Tuple17__T6, _Tuple17__T7, _Tuple17__T8, _Tuple17__T9, _Tuple17__T10, _Tuple17__T11, _Tuple17__T12, _Tuple17__T13, _Tuple17__T14, _Tuple17__T15, _Tuple17__T16, _Tuple17__T17], Serializable, typing.Generic[_Tuple17__T1, _Tuple17__T2, _Tuple17__T3, _Tuple17__T4, _Tuple17__T5, _Tuple17__T6, _Tuple17__T7, _Tuple17__T8, _Tuple17__T9, _Tuple17__T10, _Tuple17__T11, _Tuple17__T12, _Tuple17__T13, _Tuple17__T14, _Tuple17__T15, _Tuple17__T16, _Tuple17__T17]):
    def __init__(self, _1: _Tuple17__T1, _2: _Tuple17__T2, _3: _Tuple17__T3, _4: _Tuple17__T4, _5: _Tuple17__T5, _6: _Tuple17__T6, _7: _Tuple17__T7, _8: _Tuple17__T8, _9: _Tuple17__T9, _10: _Tuple17__T10, _11: _Tuple17__T11, _12: _Tuple17__T12, _13: _Tuple17__T13, _14: _Tuple17__T14, _15: _Tuple17__T15, _16: _Tuple17__T16, _17: _Tuple17__T17): ...
    def _1(self) -> _Tuple17__T1: ...
    def _10(self) -> _Tuple17__T10: ...
    def _11(self) -> _Tuple17__T11: ...
    def _12(self) -> _Tuple17__T12: ...
    def _13(self) -> _Tuple17__T13: ...
    def _14(self) -> _Tuple17__T14: ...
    def _15(self) -> _Tuple17__T15: ...
    def _16(self) -> _Tuple17__T16: ...
    def _17(self) -> _Tuple17__T17: ...
    def _2(self) -> _Tuple17__T2: ...
    def _3(self) -> _Tuple17__T3: ...
    def _4(self) -> _Tuple17__T4: ...
    def _5(self) -> _Tuple17__T5: ...
    def _6(self) -> _Tuple17__T6: ...
    def _7(self) -> _Tuple17__T7: ...
    def _8(self) -> _Tuple17__T8: ...
    def _9(self) -> _Tuple17__T9: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    _apply__T9 = typing.TypeVar('_apply__T9')  # <T9>
    _apply__T10 = typing.TypeVar('_apply__T10')  # <T10>
    _apply__T11 = typing.TypeVar('_apply__T11')  # <T11>
    _apply__T12 = typing.TypeVar('_apply__T12')  # <T12>
    _apply__T13 = typing.TypeVar('_apply__T13')  # <T13>
    _apply__T14 = typing.TypeVar('_apply__T14')  # <T14>
    _apply__T15 = typing.TypeVar('_apply__T15')  # <T15>
    _apply__T16 = typing.TypeVar('_apply__T16')  # <T16>
    _apply__T17 = typing.TypeVar('_apply__T17')  # <T17>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8, _9: _apply__T9, _10: _apply__T10, _11: _apply__T11, _12: _apply__T12, _13: _apply__T13, _14: _apply__T14, _15: _apply__T15, _16: _apply__T16, _17: _apply__T17) -> 'Tuple17'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8, _apply__T9, _apply__T10, _apply__T11, _apply__T12, _apply__T13, _apply__T14, _apply__T15, _apply__T16, _apply__T17]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    _copy__T9 = typing.TypeVar('_copy__T9')  # <T9>
    _copy__T10 = typing.TypeVar('_copy__T10')  # <T10>
    _copy__T11 = typing.TypeVar('_copy__T11')  # <T11>
    _copy__T12 = typing.TypeVar('_copy__T12')  # <T12>
    _copy__T13 = typing.TypeVar('_copy__T13')  # <T13>
    _copy__T14 = typing.TypeVar('_copy__T14')  # <T14>
    _copy__T15 = typing.TypeVar('_copy__T15')  # <T15>
    _copy__T16 = typing.TypeVar('_copy__T16')  # <T16>
    _copy__T17 = typing.TypeVar('_copy__T17')  # <T17>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any, _9: typing.Any, _10: typing.Any, _11: typing.Any, _12: typing.Any, _13: typing.Any, _14: typing.Any, _15: typing.Any, _16: typing.Any, _17: typing.Any) -> 'Tuple17'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    _copy$default$1__T9 = typing.TypeVar('_copy$default$1__T9')  # <T9>
    _copy$default$1__T10 = typing.TypeVar('_copy$default$1__T10')  # <T10>
    _copy$default$1__T11 = typing.TypeVar('_copy$default$1__T11')  # <T11>
    _copy$default$1__T12 = typing.TypeVar('_copy$default$1__T12')  # <T12>
    _copy$default$1__T13 = typing.TypeVar('_copy$default$1__T13')  # <T13>
    _copy$default$1__T14 = typing.TypeVar('_copy$default$1__T14')  # <T14>
    _copy$default$1__T15 = typing.TypeVar('_copy$default$1__T15')  # <T15>
    _copy$default$1__T16 = typing.TypeVar('_copy$default$1__T16')  # <T16>
    _copy$default$1__T17 = typing.TypeVar('_copy$default$1__T17')  # <T17>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$10__T1 = typing.TypeVar('_copy$default$10__T1')  # <T1>
    _copy$default$10__T2 = typing.TypeVar('_copy$default$10__T2')  # <T2>
    _copy$default$10__T3 = typing.TypeVar('_copy$default$10__T3')  # <T3>
    _copy$default$10__T4 = typing.TypeVar('_copy$default$10__T4')  # <T4>
    _copy$default$10__T5 = typing.TypeVar('_copy$default$10__T5')  # <T5>
    _copy$default$10__T6 = typing.TypeVar('_copy$default$10__T6')  # <T6>
    _copy$default$10__T7 = typing.TypeVar('_copy$default$10__T7')  # <T7>
    _copy$default$10__T8 = typing.TypeVar('_copy$default$10__T8')  # <T8>
    _copy$default$10__T9 = typing.TypeVar('_copy$default$10__T9')  # <T9>
    _copy$default$10__T10 = typing.TypeVar('_copy$default$10__T10')  # <T10>
    _copy$default$10__T11 = typing.TypeVar('_copy$default$10__T11')  # <T11>
    _copy$default$10__T12 = typing.TypeVar('_copy$default$10__T12')  # <T12>
    _copy$default$10__T13 = typing.TypeVar('_copy$default$10__T13')  # <T13>
    _copy$default$10__T14 = typing.TypeVar('_copy$default$10__T14')  # <T14>
    _copy$default$10__T15 = typing.TypeVar('_copy$default$10__T15')  # <T15>
    _copy$default$10__T16 = typing.TypeVar('_copy$default$10__T16')  # <T16>
    _copy$default$10__T17 = typing.TypeVar('_copy$default$10__T17')  # <T17>
    def copy$default$10(self) -> typing.Any: ...
    _copy$default$11__T1 = typing.TypeVar('_copy$default$11__T1')  # <T1>
    _copy$default$11__T2 = typing.TypeVar('_copy$default$11__T2')  # <T2>
    _copy$default$11__T3 = typing.TypeVar('_copy$default$11__T3')  # <T3>
    _copy$default$11__T4 = typing.TypeVar('_copy$default$11__T4')  # <T4>
    _copy$default$11__T5 = typing.TypeVar('_copy$default$11__T5')  # <T5>
    _copy$default$11__T6 = typing.TypeVar('_copy$default$11__T6')  # <T6>
    _copy$default$11__T7 = typing.TypeVar('_copy$default$11__T7')  # <T7>
    _copy$default$11__T8 = typing.TypeVar('_copy$default$11__T8')  # <T8>
    _copy$default$11__T9 = typing.TypeVar('_copy$default$11__T9')  # <T9>
    _copy$default$11__T10 = typing.TypeVar('_copy$default$11__T10')  # <T10>
    _copy$default$11__T11 = typing.TypeVar('_copy$default$11__T11')  # <T11>
    _copy$default$11__T12 = typing.TypeVar('_copy$default$11__T12')  # <T12>
    _copy$default$11__T13 = typing.TypeVar('_copy$default$11__T13')  # <T13>
    _copy$default$11__T14 = typing.TypeVar('_copy$default$11__T14')  # <T14>
    _copy$default$11__T15 = typing.TypeVar('_copy$default$11__T15')  # <T15>
    _copy$default$11__T16 = typing.TypeVar('_copy$default$11__T16')  # <T16>
    _copy$default$11__T17 = typing.TypeVar('_copy$default$11__T17')  # <T17>
    def copy$default$11(self) -> typing.Any: ...
    _copy$default$12__T1 = typing.TypeVar('_copy$default$12__T1')  # <T1>
    _copy$default$12__T2 = typing.TypeVar('_copy$default$12__T2')  # <T2>
    _copy$default$12__T3 = typing.TypeVar('_copy$default$12__T3')  # <T3>
    _copy$default$12__T4 = typing.TypeVar('_copy$default$12__T4')  # <T4>
    _copy$default$12__T5 = typing.TypeVar('_copy$default$12__T5')  # <T5>
    _copy$default$12__T6 = typing.TypeVar('_copy$default$12__T6')  # <T6>
    _copy$default$12__T7 = typing.TypeVar('_copy$default$12__T7')  # <T7>
    _copy$default$12__T8 = typing.TypeVar('_copy$default$12__T8')  # <T8>
    _copy$default$12__T9 = typing.TypeVar('_copy$default$12__T9')  # <T9>
    _copy$default$12__T10 = typing.TypeVar('_copy$default$12__T10')  # <T10>
    _copy$default$12__T11 = typing.TypeVar('_copy$default$12__T11')  # <T11>
    _copy$default$12__T12 = typing.TypeVar('_copy$default$12__T12')  # <T12>
    _copy$default$12__T13 = typing.TypeVar('_copy$default$12__T13')  # <T13>
    _copy$default$12__T14 = typing.TypeVar('_copy$default$12__T14')  # <T14>
    _copy$default$12__T15 = typing.TypeVar('_copy$default$12__T15')  # <T15>
    _copy$default$12__T16 = typing.TypeVar('_copy$default$12__T16')  # <T16>
    _copy$default$12__T17 = typing.TypeVar('_copy$default$12__T17')  # <T17>
    def copy$default$12(self) -> typing.Any: ...
    _copy$default$13__T1 = typing.TypeVar('_copy$default$13__T1')  # <T1>
    _copy$default$13__T2 = typing.TypeVar('_copy$default$13__T2')  # <T2>
    _copy$default$13__T3 = typing.TypeVar('_copy$default$13__T3')  # <T3>
    _copy$default$13__T4 = typing.TypeVar('_copy$default$13__T4')  # <T4>
    _copy$default$13__T5 = typing.TypeVar('_copy$default$13__T5')  # <T5>
    _copy$default$13__T6 = typing.TypeVar('_copy$default$13__T6')  # <T6>
    _copy$default$13__T7 = typing.TypeVar('_copy$default$13__T7')  # <T7>
    _copy$default$13__T8 = typing.TypeVar('_copy$default$13__T8')  # <T8>
    _copy$default$13__T9 = typing.TypeVar('_copy$default$13__T9')  # <T9>
    _copy$default$13__T10 = typing.TypeVar('_copy$default$13__T10')  # <T10>
    _copy$default$13__T11 = typing.TypeVar('_copy$default$13__T11')  # <T11>
    _copy$default$13__T12 = typing.TypeVar('_copy$default$13__T12')  # <T12>
    _copy$default$13__T13 = typing.TypeVar('_copy$default$13__T13')  # <T13>
    _copy$default$13__T14 = typing.TypeVar('_copy$default$13__T14')  # <T14>
    _copy$default$13__T15 = typing.TypeVar('_copy$default$13__T15')  # <T15>
    _copy$default$13__T16 = typing.TypeVar('_copy$default$13__T16')  # <T16>
    _copy$default$13__T17 = typing.TypeVar('_copy$default$13__T17')  # <T17>
    def copy$default$13(self) -> typing.Any: ...
    _copy$default$14__T1 = typing.TypeVar('_copy$default$14__T1')  # <T1>
    _copy$default$14__T2 = typing.TypeVar('_copy$default$14__T2')  # <T2>
    _copy$default$14__T3 = typing.TypeVar('_copy$default$14__T3')  # <T3>
    _copy$default$14__T4 = typing.TypeVar('_copy$default$14__T4')  # <T4>
    _copy$default$14__T5 = typing.TypeVar('_copy$default$14__T5')  # <T5>
    _copy$default$14__T6 = typing.TypeVar('_copy$default$14__T6')  # <T6>
    _copy$default$14__T7 = typing.TypeVar('_copy$default$14__T7')  # <T7>
    _copy$default$14__T8 = typing.TypeVar('_copy$default$14__T8')  # <T8>
    _copy$default$14__T9 = typing.TypeVar('_copy$default$14__T9')  # <T9>
    _copy$default$14__T10 = typing.TypeVar('_copy$default$14__T10')  # <T10>
    _copy$default$14__T11 = typing.TypeVar('_copy$default$14__T11')  # <T11>
    _copy$default$14__T12 = typing.TypeVar('_copy$default$14__T12')  # <T12>
    _copy$default$14__T13 = typing.TypeVar('_copy$default$14__T13')  # <T13>
    _copy$default$14__T14 = typing.TypeVar('_copy$default$14__T14')  # <T14>
    _copy$default$14__T15 = typing.TypeVar('_copy$default$14__T15')  # <T15>
    _copy$default$14__T16 = typing.TypeVar('_copy$default$14__T16')  # <T16>
    _copy$default$14__T17 = typing.TypeVar('_copy$default$14__T17')  # <T17>
    def copy$default$14(self) -> typing.Any: ...
    _copy$default$15__T1 = typing.TypeVar('_copy$default$15__T1')  # <T1>
    _copy$default$15__T2 = typing.TypeVar('_copy$default$15__T2')  # <T2>
    _copy$default$15__T3 = typing.TypeVar('_copy$default$15__T3')  # <T3>
    _copy$default$15__T4 = typing.TypeVar('_copy$default$15__T4')  # <T4>
    _copy$default$15__T5 = typing.TypeVar('_copy$default$15__T5')  # <T5>
    _copy$default$15__T6 = typing.TypeVar('_copy$default$15__T6')  # <T6>
    _copy$default$15__T7 = typing.TypeVar('_copy$default$15__T7')  # <T7>
    _copy$default$15__T8 = typing.TypeVar('_copy$default$15__T8')  # <T8>
    _copy$default$15__T9 = typing.TypeVar('_copy$default$15__T9')  # <T9>
    _copy$default$15__T10 = typing.TypeVar('_copy$default$15__T10')  # <T10>
    _copy$default$15__T11 = typing.TypeVar('_copy$default$15__T11')  # <T11>
    _copy$default$15__T12 = typing.TypeVar('_copy$default$15__T12')  # <T12>
    _copy$default$15__T13 = typing.TypeVar('_copy$default$15__T13')  # <T13>
    _copy$default$15__T14 = typing.TypeVar('_copy$default$15__T14')  # <T14>
    _copy$default$15__T15 = typing.TypeVar('_copy$default$15__T15')  # <T15>
    _copy$default$15__T16 = typing.TypeVar('_copy$default$15__T16')  # <T16>
    _copy$default$15__T17 = typing.TypeVar('_copy$default$15__T17')  # <T17>
    def copy$default$15(self) -> typing.Any: ...
    _copy$default$16__T1 = typing.TypeVar('_copy$default$16__T1')  # <T1>
    _copy$default$16__T2 = typing.TypeVar('_copy$default$16__T2')  # <T2>
    _copy$default$16__T3 = typing.TypeVar('_copy$default$16__T3')  # <T3>
    _copy$default$16__T4 = typing.TypeVar('_copy$default$16__T4')  # <T4>
    _copy$default$16__T5 = typing.TypeVar('_copy$default$16__T5')  # <T5>
    _copy$default$16__T6 = typing.TypeVar('_copy$default$16__T6')  # <T6>
    _copy$default$16__T7 = typing.TypeVar('_copy$default$16__T7')  # <T7>
    _copy$default$16__T8 = typing.TypeVar('_copy$default$16__T8')  # <T8>
    _copy$default$16__T9 = typing.TypeVar('_copy$default$16__T9')  # <T9>
    _copy$default$16__T10 = typing.TypeVar('_copy$default$16__T10')  # <T10>
    _copy$default$16__T11 = typing.TypeVar('_copy$default$16__T11')  # <T11>
    _copy$default$16__T12 = typing.TypeVar('_copy$default$16__T12')  # <T12>
    _copy$default$16__T13 = typing.TypeVar('_copy$default$16__T13')  # <T13>
    _copy$default$16__T14 = typing.TypeVar('_copy$default$16__T14')  # <T14>
    _copy$default$16__T15 = typing.TypeVar('_copy$default$16__T15')  # <T15>
    _copy$default$16__T16 = typing.TypeVar('_copy$default$16__T16')  # <T16>
    _copy$default$16__T17 = typing.TypeVar('_copy$default$16__T17')  # <T17>
    def copy$default$16(self) -> typing.Any: ...
    _copy$default$17__T1 = typing.TypeVar('_copy$default$17__T1')  # <T1>
    _copy$default$17__T2 = typing.TypeVar('_copy$default$17__T2')  # <T2>
    _copy$default$17__T3 = typing.TypeVar('_copy$default$17__T3')  # <T3>
    _copy$default$17__T4 = typing.TypeVar('_copy$default$17__T4')  # <T4>
    _copy$default$17__T5 = typing.TypeVar('_copy$default$17__T5')  # <T5>
    _copy$default$17__T6 = typing.TypeVar('_copy$default$17__T6')  # <T6>
    _copy$default$17__T7 = typing.TypeVar('_copy$default$17__T7')  # <T7>
    _copy$default$17__T8 = typing.TypeVar('_copy$default$17__T8')  # <T8>
    _copy$default$17__T9 = typing.TypeVar('_copy$default$17__T9')  # <T9>
    _copy$default$17__T10 = typing.TypeVar('_copy$default$17__T10')  # <T10>
    _copy$default$17__T11 = typing.TypeVar('_copy$default$17__T11')  # <T11>
    _copy$default$17__T12 = typing.TypeVar('_copy$default$17__T12')  # <T12>
    _copy$default$17__T13 = typing.TypeVar('_copy$default$17__T13')  # <T13>
    _copy$default$17__T14 = typing.TypeVar('_copy$default$17__T14')  # <T14>
    _copy$default$17__T15 = typing.TypeVar('_copy$default$17__T15')  # <T15>
    _copy$default$17__T16 = typing.TypeVar('_copy$default$17__T16')  # <T16>
    _copy$default$17__T17 = typing.TypeVar('_copy$default$17__T17')  # <T17>
    def copy$default$17(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    _copy$default$2__T9 = typing.TypeVar('_copy$default$2__T9')  # <T9>
    _copy$default$2__T10 = typing.TypeVar('_copy$default$2__T10')  # <T10>
    _copy$default$2__T11 = typing.TypeVar('_copy$default$2__T11')  # <T11>
    _copy$default$2__T12 = typing.TypeVar('_copy$default$2__T12')  # <T12>
    _copy$default$2__T13 = typing.TypeVar('_copy$default$2__T13')  # <T13>
    _copy$default$2__T14 = typing.TypeVar('_copy$default$2__T14')  # <T14>
    _copy$default$2__T15 = typing.TypeVar('_copy$default$2__T15')  # <T15>
    _copy$default$2__T16 = typing.TypeVar('_copy$default$2__T16')  # <T16>
    _copy$default$2__T17 = typing.TypeVar('_copy$default$2__T17')  # <T17>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    _copy$default$3__T9 = typing.TypeVar('_copy$default$3__T9')  # <T9>
    _copy$default$3__T10 = typing.TypeVar('_copy$default$3__T10')  # <T10>
    _copy$default$3__T11 = typing.TypeVar('_copy$default$3__T11')  # <T11>
    _copy$default$3__T12 = typing.TypeVar('_copy$default$3__T12')  # <T12>
    _copy$default$3__T13 = typing.TypeVar('_copy$default$3__T13')  # <T13>
    _copy$default$3__T14 = typing.TypeVar('_copy$default$3__T14')  # <T14>
    _copy$default$3__T15 = typing.TypeVar('_copy$default$3__T15')  # <T15>
    _copy$default$3__T16 = typing.TypeVar('_copy$default$3__T16')  # <T16>
    _copy$default$3__T17 = typing.TypeVar('_copy$default$3__T17')  # <T17>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    _copy$default$4__T9 = typing.TypeVar('_copy$default$4__T9')  # <T9>
    _copy$default$4__T10 = typing.TypeVar('_copy$default$4__T10')  # <T10>
    _copy$default$4__T11 = typing.TypeVar('_copy$default$4__T11')  # <T11>
    _copy$default$4__T12 = typing.TypeVar('_copy$default$4__T12')  # <T12>
    _copy$default$4__T13 = typing.TypeVar('_copy$default$4__T13')  # <T13>
    _copy$default$4__T14 = typing.TypeVar('_copy$default$4__T14')  # <T14>
    _copy$default$4__T15 = typing.TypeVar('_copy$default$4__T15')  # <T15>
    _copy$default$4__T16 = typing.TypeVar('_copy$default$4__T16')  # <T16>
    _copy$default$4__T17 = typing.TypeVar('_copy$default$4__T17')  # <T17>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    _copy$default$5__T9 = typing.TypeVar('_copy$default$5__T9')  # <T9>
    _copy$default$5__T10 = typing.TypeVar('_copy$default$5__T10')  # <T10>
    _copy$default$5__T11 = typing.TypeVar('_copy$default$5__T11')  # <T11>
    _copy$default$5__T12 = typing.TypeVar('_copy$default$5__T12')  # <T12>
    _copy$default$5__T13 = typing.TypeVar('_copy$default$5__T13')  # <T13>
    _copy$default$5__T14 = typing.TypeVar('_copy$default$5__T14')  # <T14>
    _copy$default$5__T15 = typing.TypeVar('_copy$default$5__T15')  # <T15>
    _copy$default$5__T16 = typing.TypeVar('_copy$default$5__T16')  # <T16>
    _copy$default$5__T17 = typing.TypeVar('_copy$default$5__T17')  # <T17>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    _copy$default$6__T9 = typing.TypeVar('_copy$default$6__T9')  # <T9>
    _copy$default$6__T10 = typing.TypeVar('_copy$default$6__T10')  # <T10>
    _copy$default$6__T11 = typing.TypeVar('_copy$default$6__T11')  # <T11>
    _copy$default$6__T12 = typing.TypeVar('_copy$default$6__T12')  # <T12>
    _copy$default$6__T13 = typing.TypeVar('_copy$default$6__T13')  # <T13>
    _copy$default$6__T14 = typing.TypeVar('_copy$default$6__T14')  # <T14>
    _copy$default$6__T15 = typing.TypeVar('_copy$default$6__T15')  # <T15>
    _copy$default$6__T16 = typing.TypeVar('_copy$default$6__T16')  # <T16>
    _copy$default$6__T17 = typing.TypeVar('_copy$default$6__T17')  # <T17>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    _copy$default$7__T9 = typing.TypeVar('_copy$default$7__T9')  # <T9>
    _copy$default$7__T10 = typing.TypeVar('_copy$default$7__T10')  # <T10>
    _copy$default$7__T11 = typing.TypeVar('_copy$default$7__T11')  # <T11>
    _copy$default$7__T12 = typing.TypeVar('_copy$default$7__T12')  # <T12>
    _copy$default$7__T13 = typing.TypeVar('_copy$default$7__T13')  # <T13>
    _copy$default$7__T14 = typing.TypeVar('_copy$default$7__T14')  # <T14>
    _copy$default$7__T15 = typing.TypeVar('_copy$default$7__T15')  # <T15>
    _copy$default$7__T16 = typing.TypeVar('_copy$default$7__T16')  # <T16>
    _copy$default$7__T17 = typing.TypeVar('_copy$default$7__T17')  # <T17>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    _copy$default$8__T9 = typing.TypeVar('_copy$default$8__T9')  # <T9>
    _copy$default$8__T10 = typing.TypeVar('_copy$default$8__T10')  # <T10>
    _copy$default$8__T11 = typing.TypeVar('_copy$default$8__T11')  # <T11>
    _copy$default$8__T12 = typing.TypeVar('_copy$default$8__T12')  # <T12>
    _copy$default$8__T13 = typing.TypeVar('_copy$default$8__T13')  # <T13>
    _copy$default$8__T14 = typing.TypeVar('_copy$default$8__T14')  # <T14>
    _copy$default$8__T15 = typing.TypeVar('_copy$default$8__T15')  # <T15>
    _copy$default$8__T16 = typing.TypeVar('_copy$default$8__T16')  # <T16>
    _copy$default$8__T17 = typing.TypeVar('_copy$default$8__T17')  # <T17>
    def copy$default$8(self) -> typing.Any: ...
    _copy$default$9__T1 = typing.TypeVar('_copy$default$9__T1')  # <T1>
    _copy$default$9__T2 = typing.TypeVar('_copy$default$9__T2')  # <T2>
    _copy$default$9__T3 = typing.TypeVar('_copy$default$9__T3')  # <T3>
    _copy$default$9__T4 = typing.TypeVar('_copy$default$9__T4')  # <T4>
    _copy$default$9__T5 = typing.TypeVar('_copy$default$9__T5')  # <T5>
    _copy$default$9__T6 = typing.TypeVar('_copy$default$9__T6')  # <T6>
    _copy$default$9__T7 = typing.TypeVar('_copy$default$9__T7')  # <T7>
    _copy$default$9__T8 = typing.TypeVar('_copy$default$9__T8')  # <T8>
    _copy$default$9__T9 = typing.TypeVar('_copy$default$9__T9')  # <T9>
    _copy$default$9__T10 = typing.TypeVar('_copy$default$9__T10')  # <T10>
    _copy$default$9__T11 = typing.TypeVar('_copy$default$9__T11')  # <T11>
    _copy$default$9__T12 = typing.TypeVar('_copy$default$9__T12')  # <T12>
    _copy$default$9__T13 = typing.TypeVar('_copy$default$9__T13')  # <T13>
    _copy$default$9__T14 = typing.TypeVar('_copy$default$9__T14')  # <T14>
    _copy$default$9__T15 = typing.TypeVar('_copy$default$9__T15')  # <T15>
    _copy$default$9__T16 = typing.TypeVar('_copy$default$9__T16')  # <T16>
    _copy$default$9__T17 = typing.TypeVar('_copy$default$9__T17')  # <T17>
    def copy$default$9(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    _unapply__T16 = typing.TypeVar('_unapply__T16')  # <T16>
    _unapply__T17 = typing.TypeVar('_unapply__T17')  # <T17>
    @staticmethod
    def unapply(x$0: 'Tuple17'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17]) -> Option['Tuple17'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17]]: ...

_Tuple18__T1 = typing.TypeVar('_Tuple18__T1')  # <T1>
_Tuple18__T2 = typing.TypeVar('_Tuple18__T2')  # <T2>
_Tuple18__T3 = typing.TypeVar('_Tuple18__T3')  # <T3>
_Tuple18__T4 = typing.TypeVar('_Tuple18__T4')  # <T4>
_Tuple18__T5 = typing.TypeVar('_Tuple18__T5')  # <T5>
_Tuple18__T6 = typing.TypeVar('_Tuple18__T6')  # <T6>
_Tuple18__T7 = typing.TypeVar('_Tuple18__T7')  # <T7>
_Tuple18__T8 = typing.TypeVar('_Tuple18__T8')  # <T8>
_Tuple18__T9 = typing.TypeVar('_Tuple18__T9')  # <T9>
_Tuple18__T10 = typing.TypeVar('_Tuple18__T10')  # <T10>
_Tuple18__T11 = typing.TypeVar('_Tuple18__T11')  # <T11>
_Tuple18__T12 = typing.TypeVar('_Tuple18__T12')  # <T12>
_Tuple18__T13 = typing.TypeVar('_Tuple18__T13')  # <T13>
_Tuple18__T14 = typing.TypeVar('_Tuple18__T14')  # <T14>
_Tuple18__T15 = typing.TypeVar('_Tuple18__T15')  # <T15>
_Tuple18__T16 = typing.TypeVar('_Tuple18__T16')  # <T16>
_Tuple18__T17 = typing.TypeVar('_Tuple18__T17')  # <T17>
_Tuple18__T18 = typing.TypeVar('_Tuple18__T18')  # <T18>
class Tuple18(Product18[_Tuple18__T1, _Tuple18__T2, _Tuple18__T3, _Tuple18__T4, _Tuple18__T5, _Tuple18__T6, _Tuple18__T7, _Tuple18__T8, _Tuple18__T9, _Tuple18__T10, _Tuple18__T11, _Tuple18__T12, _Tuple18__T13, _Tuple18__T14, _Tuple18__T15, _Tuple18__T16, _Tuple18__T17, _Tuple18__T18], Serializable, typing.Generic[_Tuple18__T1, _Tuple18__T2, _Tuple18__T3, _Tuple18__T4, _Tuple18__T5, _Tuple18__T6, _Tuple18__T7, _Tuple18__T8, _Tuple18__T9, _Tuple18__T10, _Tuple18__T11, _Tuple18__T12, _Tuple18__T13, _Tuple18__T14, _Tuple18__T15, _Tuple18__T16, _Tuple18__T17, _Tuple18__T18]):
    def __init__(self, _1: _Tuple18__T1, _2: _Tuple18__T2, _3: _Tuple18__T3, _4: _Tuple18__T4, _5: _Tuple18__T5, _6: _Tuple18__T6, _7: _Tuple18__T7, _8: _Tuple18__T8, _9: _Tuple18__T9, _10: _Tuple18__T10, _11: _Tuple18__T11, _12: _Tuple18__T12, _13: _Tuple18__T13, _14: _Tuple18__T14, _15: _Tuple18__T15, _16: _Tuple18__T16, _17: _Tuple18__T17, _18: _Tuple18__T18): ...
    def _1(self) -> _Tuple18__T1: ...
    def _10(self) -> _Tuple18__T10: ...
    def _11(self) -> _Tuple18__T11: ...
    def _12(self) -> _Tuple18__T12: ...
    def _13(self) -> _Tuple18__T13: ...
    def _14(self) -> _Tuple18__T14: ...
    def _15(self) -> _Tuple18__T15: ...
    def _16(self) -> _Tuple18__T16: ...
    def _17(self) -> _Tuple18__T17: ...
    def _18(self) -> _Tuple18__T18: ...
    def _2(self) -> _Tuple18__T2: ...
    def _3(self) -> _Tuple18__T3: ...
    def _4(self) -> _Tuple18__T4: ...
    def _5(self) -> _Tuple18__T5: ...
    def _6(self) -> _Tuple18__T6: ...
    def _7(self) -> _Tuple18__T7: ...
    def _8(self) -> _Tuple18__T8: ...
    def _9(self) -> _Tuple18__T9: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    _apply__T9 = typing.TypeVar('_apply__T9')  # <T9>
    _apply__T10 = typing.TypeVar('_apply__T10')  # <T10>
    _apply__T11 = typing.TypeVar('_apply__T11')  # <T11>
    _apply__T12 = typing.TypeVar('_apply__T12')  # <T12>
    _apply__T13 = typing.TypeVar('_apply__T13')  # <T13>
    _apply__T14 = typing.TypeVar('_apply__T14')  # <T14>
    _apply__T15 = typing.TypeVar('_apply__T15')  # <T15>
    _apply__T16 = typing.TypeVar('_apply__T16')  # <T16>
    _apply__T17 = typing.TypeVar('_apply__T17')  # <T17>
    _apply__T18 = typing.TypeVar('_apply__T18')  # <T18>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8, _9: _apply__T9, _10: _apply__T10, _11: _apply__T11, _12: _apply__T12, _13: _apply__T13, _14: _apply__T14, _15: _apply__T15, _16: _apply__T16, _17: _apply__T17, _18: _apply__T18) -> 'Tuple18'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8, _apply__T9, _apply__T10, _apply__T11, _apply__T12, _apply__T13, _apply__T14, _apply__T15, _apply__T16, _apply__T17, _apply__T18]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    _copy__T9 = typing.TypeVar('_copy__T9')  # <T9>
    _copy__T10 = typing.TypeVar('_copy__T10')  # <T10>
    _copy__T11 = typing.TypeVar('_copy__T11')  # <T11>
    _copy__T12 = typing.TypeVar('_copy__T12')  # <T12>
    _copy__T13 = typing.TypeVar('_copy__T13')  # <T13>
    _copy__T14 = typing.TypeVar('_copy__T14')  # <T14>
    _copy__T15 = typing.TypeVar('_copy__T15')  # <T15>
    _copy__T16 = typing.TypeVar('_copy__T16')  # <T16>
    _copy__T17 = typing.TypeVar('_copy__T17')  # <T17>
    _copy__T18 = typing.TypeVar('_copy__T18')  # <T18>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any, _9: typing.Any, _10: typing.Any, _11: typing.Any, _12: typing.Any, _13: typing.Any, _14: typing.Any, _15: typing.Any, _16: typing.Any, _17: typing.Any, _18: typing.Any) -> 'Tuple18'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    _copy$default$1__T9 = typing.TypeVar('_copy$default$1__T9')  # <T9>
    _copy$default$1__T10 = typing.TypeVar('_copy$default$1__T10')  # <T10>
    _copy$default$1__T11 = typing.TypeVar('_copy$default$1__T11')  # <T11>
    _copy$default$1__T12 = typing.TypeVar('_copy$default$1__T12')  # <T12>
    _copy$default$1__T13 = typing.TypeVar('_copy$default$1__T13')  # <T13>
    _copy$default$1__T14 = typing.TypeVar('_copy$default$1__T14')  # <T14>
    _copy$default$1__T15 = typing.TypeVar('_copy$default$1__T15')  # <T15>
    _copy$default$1__T16 = typing.TypeVar('_copy$default$1__T16')  # <T16>
    _copy$default$1__T17 = typing.TypeVar('_copy$default$1__T17')  # <T17>
    _copy$default$1__T18 = typing.TypeVar('_copy$default$1__T18')  # <T18>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$10__T1 = typing.TypeVar('_copy$default$10__T1')  # <T1>
    _copy$default$10__T2 = typing.TypeVar('_copy$default$10__T2')  # <T2>
    _copy$default$10__T3 = typing.TypeVar('_copy$default$10__T3')  # <T3>
    _copy$default$10__T4 = typing.TypeVar('_copy$default$10__T4')  # <T4>
    _copy$default$10__T5 = typing.TypeVar('_copy$default$10__T5')  # <T5>
    _copy$default$10__T6 = typing.TypeVar('_copy$default$10__T6')  # <T6>
    _copy$default$10__T7 = typing.TypeVar('_copy$default$10__T7')  # <T7>
    _copy$default$10__T8 = typing.TypeVar('_copy$default$10__T8')  # <T8>
    _copy$default$10__T9 = typing.TypeVar('_copy$default$10__T9')  # <T9>
    _copy$default$10__T10 = typing.TypeVar('_copy$default$10__T10')  # <T10>
    _copy$default$10__T11 = typing.TypeVar('_copy$default$10__T11')  # <T11>
    _copy$default$10__T12 = typing.TypeVar('_copy$default$10__T12')  # <T12>
    _copy$default$10__T13 = typing.TypeVar('_copy$default$10__T13')  # <T13>
    _copy$default$10__T14 = typing.TypeVar('_copy$default$10__T14')  # <T14>
    _copy$default$10__T15 = typing.TypeVar('_copy$default$10__T15')  # <T15>
    _copy$default$10__T16 = typing.TypeVar('_copy$default$10__T16')  # <T16>
    _copy$default$10__T17 = typing.TypeVar('_copy$default$10__T17')  # <T17>
    _copy$default$10__T18 = typing.TypeVar('_copy$default$10__T18')  # <T18>
    def copy$default$10(self) -> typing.Any: ...
    _copy$default$11__T1 = typing.TypeVar('_copy$default$11__T1')  # <T1>
    _copy$default$11__T2 = typing.TypeVar('_copy$default$11__T2')  # <T2>
    _copy$default$11__T3 = typing.TypeVar('_copy$default$11__T3')  # <T3>
    _copy$default$11__T4 = typing.TypeVar('_copy$default$11__T4')  # <T4>
    _copy$default$11__T5 = typing.TypeVar('_copy$default$11__T5')  # <T5>
    _copy$default$11__T6 = typing.TypeVar('_copy$default$11__T6')  # <T6>
    _copy$default$11__T7 = typing.TypeVar('_copy$default$11__T7')  # <T7>
    _copy$default$11__T8 = typing.TypeVar('_copy$default$11__T8')  # <T8>
    _copy$default$11__T9 = typing.TypeVar('_copy$default$11__T9')  # <T9>
    _copy$default$11__T10 = typing.TypeVar('_copy$default$11__T10')  # <T10>
    _copy$default$11__T11 = typing.TypeVar('_copy$default$11__T11')  # <T11>
    _copy$default$11__T12 = typing.TypeVar('_copy$default$11__T12')  # <T12>
    _copy$default$11__T13 = typing.TypeVar('_copy$default$11__T13')  # <T13>
    _copy$default$11__T14 = typing.TypeVar('_copy$default$11__T14')  # <T14>
    _copy$default$11__T15 = typing.TypeVar('_copy$default$11__T15')  # <T15>
    _copy$default$11__T16 = typing.TypeVar('_copy$default$11__T16')  # <T16>
    _copy$default$11__T17 = typing.TypeVar('_copy$default$11__T17')  # <T17>
    _copy$default$11__T18 = typing.TypeVar('_copy$default$11__T18')  # <T18>
    def copy$default$11(self) -> typing.Any: ...
    _copy$default$12__T1 = typing.TypeVar('_copy$default$12__T1')  # <T1>
    _copy$default$12__T2 = typing.TypeVar('_copy$default$12__T2')  # <T2>
    _copy$default$12__T3 = typing.TypeVar('_copy$default$12__T3')  # <T3>
    _copy$default$12__T4 = typing.TypeVar('_copy$default$12__T4')  # <T4>
    _copy$default$12__T5 = typing.TypeVar('_copy$default$12__T5')  # <T5>
    _copy$default$12__T6 = typing.TypeVar('_copy$default$12__T6')  # <T6>
    _copy$default$12__T7 = typing.TypeVar('_copy$default$12__T7')  # <T7>
    _copy$default$12__T8 = typing.TypeVar('_copy$default$12__T8')  # <T8>
    _copy$default$12__T9 = typing.TypeVar('_copy$default$12__T9')  # <T9>
    _copy$default$12__T10 = typing.TypeVar('_copy$default$12__T10')  # <T10>
    _copy$default$12__T11 = typing.TypeVar('_copy$default$12__T11')  # <T11>
    _copy$default$12__T12 = typing.TypeVar('_copy$default$12__T12')  # <T12>
    _copy$default$12__T13 = typing.TypeVar('_copy$default$12__T13')  # <T13>
    _copy$default$12__T14 = typing.TypeVar('_copy$default$12__T14')  # <T14>
    _copy$default$12__T15 = typing.TypeVar('_copy$default$12__T15')  # <T15>
    _copy$default$12__T16 = typing.TypeVar('_copy$default$12__T16')  # <T16>
    _copy$default$12__T17 = typing.TypeVar('_copy$default$12__T17')  # <T17>
    _copy$default$12__T18 = typing.TypeVar('_copy$default$12__T18')  # <T18>
    def copy$default$12(self) -> typing.Any: ...
    _copy$default$13__T1 = typing.TypeVar('_copy$default$13__T1')  # <T1>
    _copy$default$13__T2 = typing.TypeVar('_copy$default$13__T2')  # <T2>
    _copy$default$13__T3 = typing.TypeVar('_copy$default$13__T3')  # <T3>
    _copy$default$13__T4 = typing.TypeVar('_copy$default$13__T4')  # <T4>
    _copy$default$13__T5 = typing.TypeVar('_copy$default$13__T5')  # <T5>
    _copy$default$13__T6 = typing.TypeVar('_copy$default$13__T6')  # <T6>
    _copy$default$13__T7 = typing.TypeVar('_copy$default$13__T7')  # <T7>
    _copy$default$13__T8 = typing.TypeVar('_copy$default$13__T8')  # <T8>
    _copy$default$13__T9 = typing.TypeVar('_copy$default$13__T9')  # <T9>
    _copy$default$13__T10 = typing.TypeVar('_copy$default$13__T10')  # <T10>
    _copy$default$13__T11 = typing.TypeVar('_copy$default$13__T11')  # <T11>
    _copy$default$13__T12 = typing.TypeVar('_copy$default$13__T12')  # <T12>
    _copy$default$13__T13 = typing.TypeVar('_copy$default$13__T13')  # <T13>
    _copy$default$13__T14 = typing.TypeVar('_copy$default$13__T14')  # <T14>
    _copy$default$13__T15 = typing.TypeVar('_copy$default$13__T15')  # <T15>
    _copy$default$13__T16 = typing.TypeVar('_copy$default$13__T16')  # <T16>
    _copy$default$13__T17 = typing.TypeVar('_copy$default$13__T17')  # <T17>
    _copy$default$13__T18 = typing.TypeVar('_copy$default$13__T18')  # <T18>
    def copy$default$13(self) -> typing.Any: ...
    _copy$default$14__T1 = typing.TypeVar('_copy$default$14__T1')  # <T1>
    _copy$default$14__T2 = typing.TypeVar('_copy$default$14__T2')  # <T2>
    _copy$default$14__T3 = typing.TypeVar('_copy$default$14__T3')  # <T3>
    _copy$default$14__T4 = typing.TypeVar('_copy$default$14__T4')  # <T4>
    _copy$default$14__T5 = typing.TypeVar('_copy$default$14__T5')  # <T5>
    _copy$default$14__T6 = typing.TypeVar('_copy$default$14__T6')  # <T6>
    _copy$default$14__T7 = typing.TypeVar('_copy$default$14__T7')  # <T7>
    _copy$default$14__T8 = typing.TypeVar('_copy$default$14__T8')  # <T8>
    _copy$default$14__T9 = typing.TypeVar('_copy$default$14__T9')  # <T9>
    _copy$default$14__T10 = typing.TypeVar('_copy$default$14__T10')  # <T10>
    _copy$default$14__T11 = typing.TypeVar('_copy$default$14__T11')  # <T11>
    _copy$default$14__T12 = typing.TypeVar('_copy$default$14__T12')  # <T12>
    _copy$default$14__T13 = typing.TypeVar('_copy$default$14__T13')  # <T13>
    _copy$default$14__T14 = typing.TypeVar('_copy$default$14__T14')  # <T14>
    _copy$default$14__T15 = typing.TypeVar('_copy$default$14__T15')  # <T15>
    _copy$default$14__T16 = typing.TypeVar('_copy$default$14__T16')  # <T16>
    _copy$default$14__T17 = typing.TypeVar('_copy$default$14__T17')  # <T17>
    _copy$default$14__T18 = typing.TypeVar('_copy$default$14__T18')  # <T18>
    def copy$default$14(self) -> typing.Any: ...
    _copy$default$15__T1 = typing.TypeVar('_copy$default$15__T1')  # <T1>
    _copy$default$15__T2 = typing.TypeVar('_copy$default$15__T2')  # <T2>
    _copy$default$15__T3 = typing.TypeVar('_copy$default$15__T3')  # <T3>
    _copy$default$15__T4 = typing.TypeVar('_copy$default$15__T4')  # <T4>
    _copy$default$15__T5 = typing.TypeVar('_copy$default$15__T5')  # <T5>
    _copy$default$15__T6 = typing.TypeVar('_copy$default$15__T6')  # <T6>
    _copy$default$15__T7 = typing.TypeVar('_copy$default$15__T7')  # <T7>
    _copy$default$15__T8 = typing.TypeVar('_copy$default$15__T8')  # <T8>
    _copy$default$15__T9 = typing.TypeVar('_copy$default$15__T9')  # <T9>
    _copy$default$15__T10 = typing.TypeVar('_copy$default$15__T10')  # <T10>
    _copy$default$15__T11 = typing.TypeVar('_copy$default$15__T11')  # <T11>
    _copy$default$15__T12 = typing.TypeVar('_copy$default$15__T12')  # <T12>
    _copy$default$15__T13 = typing.TypeVar('_copy$default$15__T13')  # <T13>
    _copy$default$15__T14 = typing.TypeVar('_copy$default$15__T14')  # <T14>
    _copy$default$15__T15 = typing.TypeVar('_copy$default$15__T15')  # <T15>
    _copy$default$15__T16 = typing.TypeVar('_copy$default$15__T16')  # <T16>
    _copy$default$15__T17 = typing.TypeVar('_copy$default$15__T17')  # <T17>
    _copy$default$15__T18 = typing.TypeVar('_copy$default$15__T18')  # <T18>
    def copy$default$15(self) -> typing.Any: ...
    _copy$default$16__T1 = typing.TypeVar('_copy$default$16__T1')  # <T1>
    _copy$default$16__T2 = typing.TypeVar('_copy$default$16__T2')  # <T2>
    _copy$default$16__T3 = typing.TypeVar('_copy$default$16__T3')  # <T3>
    _copy$default$16__T4 = typing.TypeVar('_copy$default$16__T4')  # <T4>
    _copy$default$16__T5 = typing.TypeVar('_copy$default$16__T5')  # <T5>
    _copy$default$16__T6 = typing.TypeVar('_copy$default$16__T6')  # <T6>
    _copy$default$16__T7 = typing.TypeVar('_copy$default$16__T7')  # <T7>
    _copy$default$16__T8 = typing.TypeVar('_copy$default$16__T8')  # <T8>
    _copy$default$16__T9 = typing.TypeVar('_copy$default$16__T9')  # <T9>
    _copy$default$16__T10 = typing.TypeVar('_copy$default$16__T10')  # <T10>
    _copy$default$16__T11 = typing.TypeVar('_copy$default$16__T11')  # <T11>
    _copy$default$16__T12 = typing.TypeVar('_copy$default$16__T12')  # <T12>
    _copy$default$16__T13 = typing.TypeVar('_copy$default$16__T13')  # <T13>
    _copy$default$16__T14 = typing.TypeVar('_copy$default$16__T14')  # <T14>
    _copy$default$16__T15 = typing.TypeVar('_copy$default$16__T15')  # <T15>
    _copy$default$16__T16 = typing.TypeVar('_copy$default$16__T16')  # <T16>
    _copy$default$16__T17 = typing.TypeVar('_copy$default$16__T17')  # <T17>
    _copy$default$16__T18 = typing.TypeVar('_copy$default$16__T18')  # <T18>
    def copy$default$16(self) -> typing.Any: ...
    _copy$default$17__T1 = typing.TypeVar('_copy$default$17__T1')  # <T1>
    _copy$default$17__T2 = typing.TypeVar('_copy$default$17__T2')  # <T2>
    _copy$default$17__T3 = typing.TypeVar('_copy$default$17__T3')  # <T3>
    _copy$default$17__T4 = typing.TypeVar('_copy$default$17__T4')  # <T4>
    _copy$default$17__T5 = typing.TypeVar('_copy$default$17__T5')  # <T5>
    _copy$default$17__T6 = typing.TypeVar('_copy$default$17__T6')  # <T6>
    _copy$default$17__T7 = typing.TypeVar('_copy$default$17__T7')  # <T7>
    _copy$default$17__T8 = typing.TypeVar('_copy$default$17__T8')  # <T8>
    _copy$default$17__T9 = typing.TypeVar('_copy$default$17__T9')  # <T9>
    _copy$default$17__T10 = typing.TypeVar('_copy$default$17__T10')  # <T10>
    _copy$default$17__T11 = typing.TypeVar('_copy$default$17__T11')  # <T11>
    _copy$default$17__T12 = typing.TypeVar('_copy$default$17__T12')  # <T12>
    _copy$default$17__T13 = typing.TypeVar('_copy$default$17__T13')  # <T13>
    _copy$default$17__T14 = typing.TypeVar('_copy$default$17__T14')  # <T14>
    _copy$default$17__T15 = typing.TypeVar('_copy$default$17__T15')  # <T15>
    _copy$default$17__T16 = typing.TypeVar('_copy$default$17__T16')  # <T16>
    _copy$default$17__T17 = typing.TypeVar('_copy$default$17__T17')  # <T17>
    _copy$default$17__T18 = typing.TypeVar('_copy$default$17__T18')  # <T18>
    def copy$default$17(self) -> typing.Any: ...
    _copy$default$18__T1 = typing.TypeVar('_copy$default$18__T1')  # <T1>
    _copy$default$18__T2 = typing.TypeVar('_copy$default$18__T2')  # <T2>
    _copy$default$18__T3 = typing.TypeVar('_copy$default$18__T3')  # <T3>
    _copy$default$18__T4 = typing.TypeVar('_copy$default$18__T4')  # <T4>
    _copy$default$18__T5 = typing.TypeVar('_copy$default$18__T5')  # <T5>
    _copy$default$18__T6 = typing.TypeVar('_copy$default$18__T6')  # <T6>
    _copy$default$18__T7 = typing.TypeVar('_copy$default$18__T7')  # <T7>
    _copy$default$18__T8 = typing.TypeVar('_copy$default$18__T8')  # <T8>
    _copy$default$18__T9 = typing.TypeVar('_copy$default$18__T9')  # <T9>
    _copy$default$18__T10 = typing.TypeVar('_copy$default$18__T10')  # <T10>
    _copy$default$18__T11 = typing.TypeVar('_copy$default$18__T11')  # <T11>
    _copy$default$18__T12 = typing.TypeVar('_copy$default$18__T12')  # <T12>
    _copy$default$18__T13 = typing.TypeVar('_copy$default$18__T13')  # <T13>
    _copy$default$18__T14 = typing.TypeVar('_copy$default$18__T14')  # <T14>
    _copy$default$18__T15 = typing.TypeVar('_copy$default$18__T15')  # <T15>
    _copy$default$18__T16 = typing.TypeVar('_copy$default$18__T16')  # <T16>
    _copy$default$18__T17 = typing.TypeVar('_copy$default$18__T17')  # <T17>
    _copy$default$18__T18 = typing.TypeVar('_copy$default$18__T18')  # <T18>
    def copy$default$18(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    _copy$default$2__T9 = typing.TypeVar('_copy$default$2__T9')  # <T9>
    _copy$default$2__T10 = typing.TypeVar('_copy$default$2__T10')  # <T10>
    _copy$default$2__T11 = typing.TypeVar('_copy$default$2__T11')  # <T11>
    _copy$default$2__T12 = typing.TypeVar('_copy$default$2__T12')  # <T12>
    _copy$default$2__T13 = typing.TypeVar('_copy$default$2__T13')  # <T13>
    _copy$default$2__T14 = typing.TypeVar('_copy$default$2__T14')  # <T14>
    _copy$default$2__T15 = typing.TypeVar('_copy$default$2__T15')  # <T15>
    _copy$default$2__T16 = typing.TypeVar('_copy$default$2__T16')  # <T16>
    _copy$default$2__T17 = typing.TypeVar('_copy$default$2__T17')  # <T17>
    _copy$default$2__T18 = typing.TypeVar('_copy$default$2__T18')  # <T18>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    _copy$default$3__T9 = typing.TypeVar('_copy$default$3__T9')  # <T9>
    _copy$default$3__T10 = typing.TypeVar('_copy$default$3__T10')  # <T10>
    _copy$default$3__T11 = typing.TypeVar('_copy$default$3__T11')  # <T11>
    _copy$default$3__T12 = typing.TypeVar('_copy$default$3__T12')  # <T12>
    _copy$default$3__T13 = typing.TypeVar('_copy$default$3__T13')  # <T13>
    _copy$default$3__T14 = typing.TypeVar('_copy$default$3__T14')  # <T14>
    _copy$default$3__T15 = typing.TypeVar('_copy$default$3__T15')  # <T15>
    _copy$default$3__T16 = typing.TypeVar('_copy$default$3__T16')  # <T16>
    _copy$default$3__T17 = typing.TypeVar('_copy$default$3__T17')  # <T17>
    _copy$default$3__T18 = typing.TypeVar('_copy$default$3__T18')  # <T18>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    _copy$default$4__T9 = typing.TypeVar('_copy$default$4__T9')  # <T9>
    _copy$default$4__T10 = typing.TypeVar('_copy$default$4__T10')  # <T10>
    _copy$default$4__T11 = typing.TypeVar('_copy$default$4__T11')  # <T11>
    _copy$default$4__T12 = typing.TypeVar('_copy$default$4__T12')  # <T12>
    _copy$default$4__T13 = typing.TypeVar('_copy$default$4__T13')  # <T13>
    _copy$default$4__T14 = typing.TypeVar('_copy$default$4__T14')  # <T14>
    _copy$default$4__T15 = typing.TypeVar('_copy$default$4__T15')  # <T15>
    _copy$default$4__T16 = typing.TypeVar('_copy$default$4__T16')  # <T16>
    _copy$default$4__T17 = typing.TypeVar('_copy$default$4__T17')  # <T17>
    _copy$default$4__T18 = typing.TypeVar('_copy$default$4__T18')  # <T18>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    _copy$default$5__T9 = typing.TypeVar('_copy$default$5__T9')  # <T9>
    _copy$default$5__T10 = typing.TypeVar('_copy$default$5__T10')  # <T10>
    _copy$default$5__T11 = typing.TypeVar('_copy$default$5__T11')  # <T11>
    _copy$default$5__T12 = typing.TypeVar('_copy$default$5__T12')  # <T12>
    _copy$default$5__T13 = typing.TypeVar('_copy$default$5__T13')  # <T13>
    _copy$default$5__T14 = typing.TypeVar('_copy$default$5__T14')  # <T14>
    _copy$default$5__T15 = typing.TypeVar('_copy$default$5__T15')  # <T15>
    _copy$default$5__T16 = typing.TypeVar('_copy$default$5__T16')  # <T16>
    _copy$default$5__T17 = typing.TypeVar('_copy$default$5__T17')  # <T17>
    _copy$default$5__T18 = typing.TypeVar('_copy$default$5__T18')  # <T18>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    _copy$default$6__T9 = typing.TypeVar('_copy$default$6__T9')  # <T9>
    _copy$default$6__T10 = typing.TypeVar('_copy$default$6__T10')  # <T10>
    _copy$default$6__T11 = typing.TypeVar('_copy$default$6__T11')  # <T11>
    _copy$default$6__T12 = typing.TypeVar('_copy$default$6__T12')  # <T12>
    _copy$default$6__T13 = typing.TypeVar('_copy$default$6__T13')  # <T13>
    _copy$default$6__T14 = typing.TypeVar('_copy$default$6__T14')  # <T14>
    _copy$default$6__T15 = typing.TypeVar('_copy$default$6__T15')  # <T15>
    _copy$default$6__T16 = typing.TypeVar('_copy$default$6__T16')  # <T16>
    _copy$default$6__T17 = typing.TypeVar('_copy$default$6__T17')  # <T17>
    _copy$default$6__T18 = typing.TypeVar('_copy$default$6__T18')  # <T18>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    _copy$default$7__T9 = typing.TypeVar('_copy$default$7__T9')  # <T9>
    _copy$default$7__T10 = typing.TypeVar('_copy$default$7__T10')  # <T10>
    _copy$default$7__T11 = typing.TypeVar('_copy$default$7__T11')  # <T11>
    _copy$default$7__T12 = typing.TypeVar('_copy$default$7__T12')  # <T12>
    _copy$default$7__T13 = typing.TypeVar('_copy$default$7__T13')  # <T13>
    _copy$default$7__T14 = typing.TypeVar('_copy$default$7__T14')  # <T14>
    _copy$default$7__T15 = typing.TypeVar('_copy$default$7__T15')  # <T15>
    _copy$default$7__T16 = typing.TypeVar('_copy$default$7__T16')  # <T16>
    _copy$default$7__T17 = typing.TypeVar('_copy$default$7__T17')  # <T17>
    _copy$default$7__T18 = typing.TypeVar('_copy$default$7__T18')  # <T18>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    _copy$default$8__T9 = typing.TypeVar('_copy$default$8__T9')  # <T9>
    _copy$default$8__T10 = typing.TypeVar('_copy$default$8__T10')  # <T10>
    _copy$default$8__T11 = typing.TypeVar('_copy$default$8__T11')  # <T11>
    _copy$default$8__T12 = typing.TypeVar('_copy$default$8__T12')  # <T12>
    _copy$default$8__T13 = typing.TypeVar('_copy$default$8__T13')  # <T13>
    _copy$default$8__T14 = typing.TypeVar('_copy$default$8__T14')  # <T14>
    _copy$default$8__T15 = typing.TypeVar('_copy$default$8__T15')  # <T15>
    _copy$default$8__T16 = typing.TypeVar('_copy$default$8__T16')  # <T16>
    _copy$default$8__T17 = typing.TypeVar('_copy$default$8__T17')  # <T17>
    _copy$default$8__T18 = typing.TypeVar('_copy$default$8__T18')  # <T18>
    def copy$default$8(self) -> typing.Any: ...
    _copy$default$9__T1 = typing.TypeVar('_copy$default$9__T1')  # <T1>
    _copy$default$9__T2 = typing.TypeVar('_copy$default$9__T2')  # <T2>
    _copy$default$9__T3 = typing.TypeVar('_copy$default$9__T3')  # <T3>
    _copy$default$9__T4 = typing.TypeVar('_copy$default$9__T4')  # <T4>
    _copy$default$9__T5 = typing.TypeVar('_copy$default$9__T5')  # <T5>
    _copy$default$9__T6 = typing.TypeVar('_copy$default$9__T6')  # <T6>
    _copy$default$9__T7 = typing.TypeVar('_copy$default$9__T7')  # <T7>
    _copy$default$9__T8 = typing.TypeVar('_copy$default$9__T8')  # <T8>
    _copy$default$9__T9 = typing.TypeVar('_copy$default$9__T9')  # <T9>
    _copy$default$9__T10 = typing.TypeVar('_copy$default$9__T10')  # <T10>
    _copy$default$9__T11 = typing.TypeVar('_copy$default$9__T11')  # <T11>
    _copy$default$9__T12 = typing.TypeVar('_copy$default$9__T12')  # <T12>
    _copy$default$9__T13 = typing.TypeVar('_copy$default$9__T13')  # <T13>
    _copy$default$9__T14 = typing.TypeVar('_copy$default$9__T14')  # <T14>
    _copy$default$9__T15 = typing.TypeVar('_copy$default$9__T15')  # <T15>
    _copy$default$9__T16 = typing.TypeVar('_copy$default$9__T16')  # <T16>
    _copy$default$9__T17 = typing.TypeVar('_copy$default$9__T17')  # <T17>
    _copy$default$9__T18 = typing.TypeVar('_copy$default$9__T18')  # <T18>
    def copy$default$9(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    _unapply__T16 = typing.TypeVar('_unapply__T16')  # <T16>
    _unapply__T17 = typing.TypeVar('_unapply__T17')  # <T17>
    _unapply__T18 = typing.TypeVar('_unapply__T18')  # <T18>
    @staticmethod
    def unapply(x$0: 'Tuple18'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18]) -> Option['Tuple18'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18]]: ...

_Tuple19__T1 = typing.TypeVar('_Tuple19__T1')  # <T1>
_Tuple19__T2 = typing.TypeVar('_Tuple19__T2')  # <T2>
_Tuple19__T3 = typing.TypeVar('_Tuple19__T3')  # <T3>
_Tuple19__T4 = typing.TypeVar('_Tuple19__T4')  # <T4>
_Tuple19__T5 = typing.TypeVar('_Tuple19__T5')  # <T5>
_Tuple19__T6 = typing.TypeVar('_Tuple19__T6')  # <T6>
_Tuple19__T7 = typing.TypeVar('_Tuple19__T7')  # <T7>
_Tuple19__T8 = typing.TypeVar('_Tuple19__T8')  # <T8>
_Tuple19__T9 = typing.TypeVar('_Tuple19__T9')  # <T9>
_Tuple19__T10 = typing.TypeVar('_Tuple19__T10')  # <T10>
_Tuple19__T11 = typing.TypeVar('_Tuple19__T11')  # <T11>
_Tuple19__T12 = typing.TypeVar('_Tuple19__T12')  # <T12>
_Tuple19__T13 = typing.TypeVar('_Tuple19__T13')  # <T13>
_Tuple19__T14 = typing.TypeVar('_Tuple19__T14')  # <T14>
_Tuple19__T15 = typing.TypeVar('_Tuple19__T15')  # <T15>
_Tuple19__T16 = typing.TypeVar('_Tuple19__T16')  # <T16>
_Tuple19__T17 = typing.TypeVar('_Tuple19__T17')  # <T17>
_Tuple19__T18 = typing.TypeVar('_Tuple19__T18')  # <T18>
_Tuple19__T19 = typing.TypeVar('_Tuple19__T19')  # <T19>
class Tuple19(Product19[_Tuple19__T1, _Tuple19__T2, _Tuple19__T3, _Tuple19__T4, _Tuple19__T5, _Tuple19__T6, _Tuple19__T7, _Tuple19__T8, _Tuple19__T9, _Tuple19__T10, _Tuple19__T11, _Tuple19__T12, _Tuple19__T13, _Tuple19__T14, _Tuple19__T15, _Tuple19__T16, _Tuple19__T17, _Tuple19__T18, _Tuple19__T19], Serializable, typing.Generic[_Tuple19__T1, _Tuple19__T2, _Tuple19__T3, _Tuple19__T4, _Tuple19__T5, _Tuple19__T6, _Tuple19__T7, _Tuple19__T8, _Tuple19__T9, _Tuple19__T10, _Tuple19__T11, _Tuple19__T12, _Tuple19__T13, _Tuple19__T14, _Tuple19__T15, _Tuple19__T16, _Tuple19__T17, _Tuple19__T18, _Tuple19__T19]):
    def __init__(self, _1: _Tuple19__T1, _2: _Tuple19__T2, _3: _Tuple19__T3, _4: _Tuple19__T4, _5: _Tuple19__T5, _6: _Tuple19__T6, _7: _Tuple19__T7, _8: _Tuple19__T8, _9: _Tuple19__T9, _10: _Tuple19__T10, _11: _Tuple19__T11, _12: _Tuple19__T12, _13: _Tuple19__T13, _14: _Tuple19__T14, _15: _Tuple19__T15, _16: _Tuple19__T16, _17: _Tuple19__T17, _18: _Tuple19__T18, _19: _Tuple19__T19): ...
    def _1(self) -> _Tuple19__T1: ...
    def _10(self) -> _Tuple19__T10: ...
    def _11(self) -> _Tuple19__T11: ...
    def _12(self) -> _Tuple19__T12: ...
    def _13(self) -> _Tuple19__T13: ...
    def _14(self) -> _Tuple19__T14: ...
    def _15(self) -> _Tuple19__T15: ...
    def _16(self) -> _Tuple19__T16: ...
    def _17(self) -> _Tuple19__T17: ...
    def _18(self) -> _Tuple19__T18: ...
    def _19(self) -> _Tuple19__T19: ...
    def _2(self) -> _Tuple19__T2: ...
    def _3(self) -> _Tuple19__T3: ...
    def _4(self) -> _Tuple19__T4: ...
    def _5(self) -> _Tuple19__T5: ...
    def _6(self) -> _Tuple19__T6: ...
    def _7(self) -> _Tuple19__T7: ...
    def _8(self) -> _Tuple19__T8: ...
    def _9(self) -> _Tuple19__T9: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    _apply__T9 = typing.TypeVar('_apply__T9')  # <T9>
    _apply__T10 = typing.TypeVar('_apply__T10')  # <T10>
    _apply__T11 = typing.TypeVar('_apply__T11')  # <T11>
    _apply__T12 = typing.TypeVar('_apply__T12')  # <T12>
    _apply__T13 = typing.TypeVar('_apply__T13')  # <T13>
    _apply__T14 = typing.TypeVar('_apply__T14')  # <T14>
    _apply__T15 = typing.TypeVar('_apply__T15')  # <T15>
    _apply__T16 = typing.TypeVar('_apply__T16')  # <T16>
    _apply__T17 = typing.TypeVar('_apply__T17')  # <T17>
    _apply__T18 = typing.TypeVar('_apply__T18')  # <T18>
    _apply__T19 = typing.TypeVar('_apply__T19')  # <T19>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8, _9: _apply__T9, _10: _apply__T10, _11: _apply__T11, _12: _apply__T12, _13: _apply__T13, _14: _apply__T14, _15: _apply__T15, _16: _apply__T16, _17: _apply__T17, _18: _apply__T18, _19: _apply__T19) -> 'Tuple19'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8, _apply__T9, _apply__T10, _apply__T11, _apply__T12, _apply__T13, _apply__T14, _apply__T15, _apply__T16, _apply__T17, _apply__T18, _apply__T19]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    _copy__T9 = typing.TypeVar('_copy__T9')  # <T9>
    _copy__T10 = typing.TypeVar('_copy__T10')  # <T10>
    _copy__T11 = typing.TypeVar('_copy__T11')  # <T11>
    _copy__T12 = typing.TypeVar('_copy__T12')  # <T12>
    _copy__T13 = typing.TypeVar('_copy__T13')  # <T13>
    _copy__T14 = typing.TypeVar('_copy__T14')  # <T14>
    _copy__T15 = typing.TypeVar('_copy__T15')  # <T15>
    _copy__T16 = typing.TypeVar('_copy__T16')  # <T16>
    _copy__T17 = typing.TypeVar('_copy__T17')  # <T17>
    _copy__T18 = typing.TypeVar('_copy__T18')  # <T18>
    _copy__T19 = typing.TypeVar('_copy__T19')  # <T19>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any, _9: typing.Any, _10: typing.Any, _11: typing.Any, _12: typing.Any, _13: typing.Any, _14: typing.Any, _15: typing.Any, _16: typing.Any, _17: typing.Any, _18: typing.Any, _19: typing.Any) -> 'Tuple19'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    _copy$default$1__T9 = typing.TypeVar('_copy$default$1__T9')  # <T9>
    _copy$default$1__T10 = typing.TypeVar('_copy$default$1__T10')  # <T10>
    _copy$default$1__T11 = typing.TypeVar('_copy$default$1__T11')  # <T11>
    _copy$default$1__T12 = typing.TypeVar('_copy$default$1__T12')  # <T12>
    _copy$default$1__T13 = typing.TypeVar('_copy$default$1__T13')  # <T13>
    _copy$default$1__T14 = typing.TypeVar('_copy$default$1__T14')  # <T14>
    _copy$default$1__T15 = typing.TypeVar('_copy$default$1__T15')  # <T15>
    _copy$default$1__T16 = typing.TypeVar('_copy$default$1__T16')  # <T16>
    _copy$default$1__T17 = typing.TypeVar('_copy$default$1__T17')  # <T17>
    _copy$default$1__T18 = typing.TypeVar('_copy$default$1__T18')  # <T18>
    _copy$default$1__T19 = typing.TypeVar('_copy$default$1__T19')  # <T19>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$10__T1 = typing.TypeVar('_copy$default$10__T1')  # <T1>
    _copy$default$10__T2 = typing.TypeVar('_copy$default$10__T2')  # <T2>
    _copy$default$10__T3 = typing.TypeVar('_copy$default$10__T3')  # <T3>
    _copy$default$10__T4 = typing.TypeVar('_copy$default$10__T4')  # <T4>
    _copy$default$10__T5 = typing.TypeVar('_copy$default$10__T5')  # <T5>
    _copy$default$10__T6 = typing.TypeVar('_copy$default$10__T6')  # <T6>
    _copy$default$10__T7 = typing.TypeVar('_copy$default$10__T7')  # <T7>
    _copy$default$10__T8 = typing.TypeVar('_copy$default$10__T8')  # <T8>
    _copy$default$10__T9 = typing.TypeVar('_copy$default$10__T9')  # <T9>
    _copy$default$10__T10 = typing.TypeVar('_copy$default$10__T10')  # <T10>
    _copy$default$10__T11 = typing.TypeVar('_copy$default$10__T11')  # <T11>
    _copy$default$10__T12 = typing.TypeVar('_copy$default$10__T12')  # <T12>
    _copy$default$10__T13 = typing.TypeVar('_copy$default$10__T13')  # <T13>
    _copy$default$10__T14 = typing.TypeVar('_copy$default$10__T14')  # <T14>
    _copy$default$10__T15 = typing.TypeVar('_copy$default$10__T15')  # <T15>
    _copy$default$10__T16 = typing.TypeVar('_copy$default$10__T16')  # <T16>
    _copy$default$10__T17 = typing.TypeVar('_copy$default$10__T17')  # <T17>
    _copy$default$10__T18 = typing.TypeVar('_copy$default$10__T18')  # <T18>
    _copy$default$10__T19 = typing.TypeVar('_copy$default$10__T19')  # <T19>
    def copy$default$10(self) -> typing.Any: ...
    _copy$default$11__T1 = typing.TypeVar('_copy$default$11__T1')  # <T1>
    _copy$default$11__T2 = typing.TypeVar('_copy$default$11__T2')  # <T2>
    _copy$default$11__T3 = typing.TypeVar('_copy$default$11__T3')  # <T3>
    _copy$default$11__T4 = typing.TypeVar('_copy$default$11__T4')  # <T4>
    _copy$default$11__T5 = typing.TypeVar('_copy$default$11__T5')  # <T5>
    _copy$default$11__T6 = typing.TypeVar('_copy$default$11__T6')  # <T6>
    _copy$default$11__T7 = typing.TypeVar('_copy$default$11__T7')  # <T7>
    _copy$default$11__T8 = typing.TypeVar('_copy$default$11__T8')  # <T8>
    _copy$default$11__T9 = typing.TypeVar('_copy$default$11__T9')  # <T9>
    _copy$default$11__T10 = typing.TypeVar('_copy$default$11__T10')  # <T10>
    _copy$default$11__T11 = typing.TypeVar('_copy$default$11__T11')  # <T11>
    _copy$default$11__T12 = typing.TypeVar('_copy$default$11__T12')  # <T12>
    _copy$default$11__T13 = typing.TypeVar('_copy$default$11__T13')  # <T13>
    _copy$default$11__T14 = typing.TypeVar('_copy$default$11__T14')  # <T14>
    _copy$default$11__T15 = typing.TypeVar('_copy$default$11__T15')  # <T15>
    _copy$default$11__T16 = typing.TypeVar('_copy$default$11__T16')  # <T16>
    _copy$default$11__T17 = typing.TypeVar('_copy$default$11__T17')  # <T17>
    _copy$default$11__T18 = typing.TypeVar('_copy$default$11__T18')  # <T18>
    _copy$default$11__T19 = typing.TypeVar('_copy$default$11__T19')  # <T19>
    def copy$default$11(self) -> typing.Any: ...
    _copy$default$12__T1 = typing.TypeVar('_copy$default$12__T1')  # <T1>
    _copy$default$12__T2 = typing.TypeVar('_copy$default$12__T2')  # <T2>
    _copy$default$12__T3 = typing.TypeVar('_copy$default$12__T3')  # <T3>
    _copy$default$12__T4 = typing.TypeVar('_copy$default$12__T4')  # <T4>
    _copy$default$12__T5 = typing.TypeVar('_copy$default$12__T5')  # <T5>
    _copy$default$12__T6 = typing.TypeVar('_copy$default$12__T6')  # <T6>
    _copy$default$12__T7 = typing.TypeVar('_copy$default$12__T7')  # <T7>
    _copy$default$12__T8 = typing.TypeVar('_copy$default$12__T8')  # <T8>
    _copy$default$12__T9 = typing.TypeVar('_copy$default$12__T9')  # <T9>
    _copy$default$12__T10 = typing.TypeVar('_copy$default$12__T10')  # <T10>
    _copy$default$12__T11 = typing.TypeVar('_copy$default$12__T11')  # <T11>
    _copy$default$12__T12 = typing.TypeVar('_copy$default$12__T12')  # <T12>
    _copy$default$12__T13 = typing.TypeVar('_copy$default$12__T13')  # <T13>
    _copy$default$12__T14 = typing.TypeVar('_copy$default$12__T14')  # <T14>
    _copy$default$12__T15 = typing.TypeVar('_copy$default$12__T15')  # <T15>
    _copy$default$12__T16 = typing.TypeVar('_copy$default$12__T16')  # <T16>
    _copy$default$12__T17 = typing.TypeVar('_copy$default$12__T17')  # <T17>
    _copy$default$12__T18 = typing.TypeVar('_copy$default$12__T18')  # <T18>
    _copy$default$12__T19 = typing.TypeVar('_copy$default$12__T19')  # <T19>
    def copy$default$12(self) -> typing.Any: ...
    _copy$default$13__T1 = typing.TypeVar('_copy$default$13__T1')  # <T1>
    _copy$default$13__T2 = typing.TypeVar('_copy$default$13__T2')  # <T2>
    _copy$default$13__T3 = typing.TypeVar('_copy$default$13__T3')  # <T3>
    _copy$default$13__T4 = typing.TypeVar('_copy$default$13__T4')  # <T4>
    _copy$default$13__T5 = typing.TypeVar('_copy$default$13__T5')  # <T5>
    _copy$default$13__T6 = typing.TypeVar('_copy$default$13__T6')  # <T6>
    _copy$default$13__T7 = typing.TypeVar('_copy$default$13__T7')  # <T7>
    _copy$default$13__T8 = typing.TypeVar('_copy$default$13__T8')  # <T8>
    _copy$default$13__T9 = typing.TypeVar('_copy$default$13__T9')  # <T9>
    _copy$default$13__T10 = typing.TypeVar('_copy$default$13__T10')  # <T10>
    _copy$default$13__T11 = typing.TypeVar('_copy$default$13__T11')  # <T11>
    _copy$default$13__T12 = typing.TypeVar('_copy$default$13__T12')  # <T12>
    _copy$default$13__T13 = typing.TypeVar('_copy$default$13__T13')  # <T13>
    _copy$default$13__T14 = typing.TypeVar('_copy$default$13__T14')  # <T14>
    _copy$default$13__T15 = typing.TypeVar('_copy$default$13__T15')  # <T15>
    _copy$default$13__T16 = typing.TypeVar('_copy$default$13__T16')  # <T16>
    _copy$default$13__T17 = typing.TypeVar('_copy$default$13__T17')  # <T17>
    _copy$default$13__T18 = typing.TypeVar('_copy$default$13__T18')  # <T18>
    _copy$default$13__T19 = typing.TypeVar('_copy$default$13__T19')  # <T19>
    def copy$default$13(self) -> typing.Any: ...
    _copy$default$14__T1 = typing.TypeVar('_copy$default$14__T1')  # <T1>
    _copy$default$14__T2 = typing.TypeVar('_copy$default$14__T2')  # <T2>
    _copy$default$14__T3 = typing.TypeVar('_copy$default$14__T3')  # <T3>
    _copy$default$14__T4 = typing.TypeVar('_copy$default$14__T4')  # <T4>
    _copy$default$14__T5 = typing.TypeVar('_copy$default$14__T5')  # <T5>
    _copy$default$14__T6 = typing.TypeVar('_copy$default$14__T6')  # <T6>
    _copy$default$14__T7 = typing.TypeVar('_copy$default$14__T7')  # <T7>
    _copy$default$14__T8 = typing.TypeVar('_copy$default$14__T8')  # <T8>
    _copy$default$14__T9 = typing.TypeVar('_copy$default$14__T9')  # <T9>
    _copy$default$14__T10 = typing.TypeVar('_copy$default$14__T10')  # <T10>
    _copy$default$14__T11 = typing.TypeVar('_copy$default$14__T11')  # <T11>
    _copy$default$14__T12 = typing.TypeVar('_copy$default$14__T12')  # <T12>
    _copy$default$14__T13 = typing.TypeVar('_copy$default$14__T13')  # <T13>
    _copy$default$14__T14 = typing.TypeVar('_copy$default$14__T14')  # <T14>
    _copy$default$14__T15 = typing.TypeVar('_copy$default$14__T15')  # <T15>
    _copy$default$14__T16 = typing.TypeVar('_copy$default$14__T16')  # <T16>
    _copy$default$14__T17 = typing.TypeVar('_copy$default$14__T17')  # <T17>
    _copy$default$14__T18 = typing.TypeVar('_copy$default$14__T18')  # <T18>
    _copy$default$14__T19 = typing.TypeVar('_copy$default$14__T19')  # <T19>
    def copy$default$14(self) -> typing.Any: ...
    _copy$default$15__T1 = typing.TypeVar('_copy$default$15__T1')  # <T1>
    _copy$default$15__T2 = typing.TypeVar('_copy$default$15__T2')  # <T2>
    _copy$default$15__T3 = typing.TypeVar('_copy$default$15__T3')  # <T3>
    _copy$default$15__T4 = typing.TypeVar('_copy$default$15__T4')  # <T4>
    _copy$default$15__T5 = typing.TypeVar('_copy$default$15__T5')  # <T5>
    _copy$default$15__T6 = typing.TypeVar('_copy$default$15__T6')  # <T6>
    _copy$default$15__T7 = typing.TypeVar('_copy$default$15__T7')  # <T7>
    _copy$default$15__T8 = typing.TypeVar('_copy$default$15__T8')  # <T8>
    _copy$default$15__T9 = typing.TypeVar('_copy$default$15__T9')  # <T9>
    _copy$default$15__T10 = typing.TypeVar('_copy$default$15__T10')  # <T10>
    _copy$default$15__T11 = typing.TypeVar('_copy$default$15__T11')  # <T11>
    _copy$default$15__T12 = typing.TypeVar('_copy$default$15__T12')  # <T12>
    _copy$default$15__T13 = typing.TypeVar('_copy$default$15__T13')  # <T13>
    _copy$default$15__T14 = typing.TypeVar('_copy$default$15__T14')  # <T14>
    _copy$default$15__T15 = typing.TypeVar('_copy$default$15__T15')  # <T15>
    _copy$default$15__T16 = typing.TypeVar('_copy$default$15__T16')  # <T16>
    _copy$default$15__T17 = typing.TypeVar('_copy$default$15__T17')  # <T17>
    _copy$default$15__T18 = typing.TypeVar('_copy$default$15__T18')  # <T18>
    _copy$default$15__T19 = typing.TypeVar('_copy$default$15__T19')  # <T19>
    def copy$default$15(self) -> typing.Any: ...
    _copy$default$16__T1 = typing.TypeVar('_copy$default$16__T1')  # <T1>
    _copy$default$16__T2 = typing.TypeVar('_copy$default$16__T2')  # <T2>
    _copy$default$16__T3 = typing.TypeVar('_copy$default$16__T3')  # <T3>
    _copy$default$16__T4 = typing.TypeVar('_copy$default$16__T4')  # <T4>
    _copy$default$16__T5 = typing.TypeVar('_copy$default$16__T5')  # <T5>
    _copy$default$16__T6 = typing.TypeVar('_copy$default$16__T6')  # <T6>
    _copy$default$16__T7 = typing.TypeVar('_copy$default$16__T7')  # <T7>
    _copy$default$16__T8 = typing.TypeVar('_copy$default$16__T8')  # <T8>
    _copy$default$16__T9 = typing.TypeVar('_copy$default$16__T9')  # <T9>
    _copy$default$16__T10 = typing.TypeVar('_copy$default$16__T10')  # <T10>
    _copy$default$16__T11 = typing.TypeVar('_copy$default$16__T11')  # <T11>
    _copy$default$16__T12 = typing.TypeVar('_copy$default$16__T12')  # <T12>
    _copy$default$16__T13 = typing.TypeVar('_copy$default$16__T13')  # <T13>
    _copy$default$16__T14 = typing.TypeVar('_copy$default$16__T14')  # <T14>
    _copy$default$16__T15 = typing.TypeVar('_copy$default$16__T15')  # <T15>
    _copy$default$16__T16 = typing.TypeVar('_copy$default$16__T16')  # <T16>
    _copy$default$16__T17 = typing.TypeVar('_copy$default$16__T17')  # <T17>
    _copy$default$16__T18 = typing.TypeVar('_copy$default$16__T18')  # <T18>
    _copy$default$16__T19 = typing.TypeVar('_copy$default$16__T19')  # <T19>
    def copy$default$16(self) -> typing.Any: ...
    _copy$default$17__T1 = typing.TypeVar('_copy$default$17__T1')  # <T1>
    _copy$default$17__T2 = typing.TypeVar('_copy$default$17__T2')  # <T2>
    _copy$default$17__T3 = typing.TypeVar('_copy$default$17__T3')  # <T3>
    _copy$default$17__T4 = typing.TypeVar('_copy$default$17__T4')  # <T4>
    _copy$default$17__T5 = typing.TypeVar('_copy$default$17__T5')  # <T5>
    _copy$default$17__T6 = typing.TypeVar('_copy$default$17__T6')  # <T6>
    _copy$default$17__T7 = typing.TypeVar('_copy$default$17__T7')  # <T7>
    _copy$default$17__T8 = typing.TypeVar('_copy$default$17__T8')  # <T8>
    _copy$default$17__T9 = typing.TypeVar('_copy$default$17__T9')  # <T9>
    _copy$default$17__T10 = typing.TypeVar('_copy$default$17__T10')  # <T10>
    _copy$default$17__T11 = typing.TypeVar('_copy$default$17__T11')  # <T11>
    _copy$default$17__T12 = typing.TypeVar('_copy$default$17__T12')  # <T12>
    _copy$default$17__T13 = typing.TypeVar('_copy$default$17__T13')  # <T13>
    _copy$default$17__T14 = typing.TypeVar('_copy$default$17__T14')  # <T14>
    _copy$default$17__T15 = typing.TypeVar('_copy$default$17__T15')  # <T15>
    _copy$default$17__T16 = typing.TypeVar('_copy$default$17__T16')  # <T16>
    _copy$default$17__T17 = typing.TypeVar('_copy$default$17__T17')  # <T17>
    _copy$default$17__T18 = typing.TypeVar('_copy$default$17__T18')  # <T18>
    _copy$default$17__T19 = typing.TypeVar('_copy$default$17__T19')  # <T19>
    def copy$default$17(self) -> typing.Any: ...
    _copy$default$18__T1 = typing.TypeVar('_copy$default$18__T1')  # <T1>
    _copy$default$18__T2 = typing.TypeVar('_copy$default$18__T2')  # <T2>
    _copy$default$18__T3 = typing.TypeVar('_copy$default$18__T3')  # <T3>
    _copy$default$18__T4 = typing.TypeVar('_copy$default$18__T4')  # <T4>
    _copy$default$18__T5 = typing.TypeVar('_copy$default$18__T5')  # <T5>
    _copy$default$18__T6 = typing.TypeVar('_copy$default$18__T6')  # <T6>
    _copy$default$18__T7 = typing.TypeVar('_copy$default$18__T7')  # <T7>
    _copy$default$18__T8 = typing.TypeVar('_copy$default$18__T8')  # <T8>
    _copy$default$18__T9 = typing.TypeVar('_copy$default$18__T9')  # <T9>
    _copy$default$18__T10 = typing.TypeVar('_copy$default$18__T10')  # <T10>
    _copy$default$18__T11 = typing.TypeVar('_copy$default$18__T11')  # <T11>
    _copy$default$18__T12 = typing.TypeVar('_copy$default$18__T12')  # <T12>
    _copy$default$18__T13 = typing.TypeVar('_copy$default$18__T13')  # <T13>
    _copy$default$18__T14 = typing.TypeVar('_copy$default$18__T14')  # <T14>
    _copy$default$18__T15 = typing.TypeVar('_copy$default$18__T15')  # <T15>
    _copy$default$18__T16 = typing.TypeVar('_copy$default$18__T16')  # <T16>
    _copy$default$18__T17 = typing.TypeVar('_copy$default$18__T17')  # <T17>
    _copy$default$18__T18 = typing.TypeVar('_copy$default$18__T18')  # <T18>
    _copy$default$18__T19 = typing.TypeVar('_copy$default$18__T19')  # <T19>
    def copy$default$18(self) -> typing.Any: ...
    _copy$default$19__T1 = typing.TypeVar('_copy$default$19__T1')  # <T1>
    _copy$default$19__T2 = typing.TypeVar('_copy$default$19__T2')  # <T2>
    _copy$default$19__T3 = typing.TypeVar('_copy$default$19__T3')  # <T3>
    _copy$default$19__T4 = typing.TypeVar('_copy$default$19__T4')  # <T4>
    _copy$default$19__T5 = typing.TypeVar('_copy$default$19__T5')  # <T5>
    _copy$default$19__T6 = typing.TypeVar('_copy$default$19__T6')  # <T6>
    _copy$default$19__T7 = typing.TypeVar('_copy$default$19__T7')  # <T7>
    _copy$default$19__T8 = typing.TypeVar('_copy$default$19__T8')  # <T8>
    _copy$default$19__T9 = typing.TypeVar('_copy$default$19__T9')  # <T9>
    _copy$default$19__T10 = typing.TypeVar('_copy$default$19__T10')  # <T10>
    _copy$default$19__T11 = typing.TypeVar('_copy$default$19__T11')  # <T11>
    _copy$default$19__T12 = typing.TypeVar('_copy$default$19__T12')  # <T12>
    _copy$default$19__T13 = typing.TypeVar('_copy$default$19__T13')  # <T13>
    _copy$default$19__T14 = typing.TypeVar('_copy$default$19__T14')  # <T14>
    _copy$default$19__T15 = typing.TypeVar('_copy$default$19__T15')  # <T15>
    _copy$default$19__T16 = typing.TypeVar('_copy$default$19__T16')  # <T16>
    _copy$default$19__T17 = typing.TypeVar('_copy$default$19__T17')  # <T17>
    _copy$default$19__T18 = typing.TypeVar('_copy$default$19__T18')  # <T18>
    _copy$default$19__T19 = typing.TypeVar('_copy$default$19__T19')  # <T19>
    def copy$default$19(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    _copy$default$2__T9 = typing.TypeVar('_copy$default$2__T9')  # <T9>
    _copy$default$2__T10 = typing.TypeVar('_copy$default$2__T10')  # <T10>
    _copy$default$2__T11 = typing.TypeVar('_copy$default$2__T11')  # <T11>
    _copy$default$2__T12 = typing.TypeVar('_copy$default$2__T12')  # <T12>
    _copy$default$2__T13 = typing.TypeVar('_copy$default$2__T13')  # <T13>
    _copy$default$2__T14 = typing.TypeVar('_copy$default$2__T14')  # <T14>
    _copy$default$2__T15 = typing.TypeVar('_copy$default$2__T15')  # <T15>
    _copy$default$2__T16 = typing.TypeVar('_copy$default$2__T16')  # <T16>
    _copy$default$2__T17 = typing.TypeVar('_copy$default$2__T17')  # <T17>
    _copy$default$2__T18 = typing.TypeVar('_copy$default$2__T18')  # <T18>
    _copy$default$2__T19 = typing.TypeVar('_copy$default$2__T19')  # <T19>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    _copy$default$3__T9 = typing.TypeVar('_copy$default$3__T9')  # <T9>
    _copy$default$3__T10 = typing.TypeVar('_copy$default$3__T10')  # <T10>
    _copy$default$3__T11 = typing.TypeVar('_copy$default$3__T11')  # <T11>
    _copy$default$3__T12 = typing.TypeVar('_copy$default$3__T12')  # <T12>
    _copy$default$3__T13 = typing.TypeVar('_copy$default$3__T13')  # <T13>
    _copy$default$3__T14 = typing.TypeVar('_copy$default$3__T14')  # <T14>
    _copy$default$3__T15 = typing.TypeVar('_copy$default$3__T15')  # <T15>
    _copy$default$3__T16 = typing.TypeVar('_copy$default$3__T16')  # <T16>
    _copy$default$3__T17 = typing.TypeVar('_copy$default$3__T17')  # <T17>
    _copy$default$3__T18 = typing.TypeVar('_copy$default$3__T18')  # <T18>
    _copy$default$3__T19 = typing.TypeVar('_copy$default$3__T19')  # <T19>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    _copy$default$4__T9 = typing.TypeVar('_copy$default$4__T9')  # <T9>
    _copy$default$4__T10 = typing.TypeVar('_copy$default$4__T10')  # <T10>
    _copy$default$4__T11 = typing.TypeVar('_copy$default$4__T11')  # <T11>
    _copy$default$4__T12 = typing.TypeVar('_copy$default$4__T12')  # <T12>
    _copy$default$4__T13 = typing.TypeVar('_copy$default$4__T13')  # <T13>
    _copy$default$4__T14 = typing.TypeVar('_copy$default$4__T14')  # <T14>
    _copy$default$4__T15 = typing.TypeVar('_copy$default$4__T15')  # <T15>
    _copy$default$4__T16 = typing.TypeVar('_copy$default$4__T16')  # <T16>
    _copy$default$4__T17 = typing.TypeVar('_copy$default$4__T17')  # <T17>
    _copy$default$4__T18 = typing.TypeVar('_copy$default$4__T18')  # <T18>
    _copy$default$4__T19 = typing.TypeVar('_copy$default$4__T19')  # <T19>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    _copy$default$5__T9 = typing.TypeVar('_copy$default$5__T9')  # <T9>
    _copy$default$5__T10 = typing.TypeVar('_copy$default$5__T10')  # <T10>
    _copy$default$5__T11 = typing.TypeVar('_copy$default$5__T11')  # <T11>
    _copy$default$5__T12 = typing.TypeVar('_copy$default$5__T12')  # <T12>
    _copy$default$5__T13 = typing.TypeVar('_copy$default$5__T13')  # <T13>
    _copy$default$5__T14 = typing.TypeVar('_copy$default$5__T14')  # <T14>
    _copy$default$5__T15 = typing.TypeVar('_copy$default$5__T15')  # <T15>
    _copy$default$5__T16 = typing.TypeVar('_copy$default$5__T16')  # <T16>
    _copy$default$5__T17 = typing.TypeVar('_copy$default$5__T17')  # <T17>
    _copy$default$5__T18 = typing.TypeVar('_copy$default$5__T18')  # <T18>
    _copy$default$5__T19 = typing.TypeVar('_copy$default$5__T19')  # <T19>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    _copy$default$6__T9 = typing.TypeVar('_copy$default$6__T9')  # <T9>
    _copy$default$6__T10 = typing.TypeVar('_copy$default$6__T10')  # <T10>
    _copy$default$6__T11 = typing.TypeVar('_copy$default$6__T11')  # <T11>
    _copy$default$6__T12 = typing.TypeVar('_copy$default$6__T12')  # <T12>
    _copy$default$6__T13 = typing.TypeVar('_copy$default$6__T13')  # <T13>
    _copy$default$6__T14 = typing.TypeVar('_copy$default$6__T14')  # <T14>
    _copy$default$6__T15 = typing.TypeVar('_copy$default$6__T15')  # <T15>
    _copy$default$6__T16 = typing.TypeVar('_copy$default$6__T16')  # <T16>
    _copy$default$6__T17 = typing.TypeVar('_copy$default$6__T17')  # <T17>
    _copy$default$6__T18 = typing.TypeVar('_copy$default$6__T18')  # <T18>
    _copy$default$6__T19 = typing.TypeVar('_copy$default$6__T19')  # <T19>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    _copy$default$7__T9 = typing.TypeVar('_copy$default$7__T9')  # <T9>
    _copy$default$7__T10 = typing.TypeVar('_copy$default$7__T10')  # <T10>
    _copy$default$7__T11 = typing.TypeVar('_copy$default$7__T11')  # <T11>
    _copy$default$7__T12 = typing.TypeVar('_copy$default$7__T12')  # <T12>
    _copy$default$7__T13 = typing.TypeVar('_copy$default$7__T13')  # <T13>
    _copy$default$7__T14 = typing.TypeVar('_copy$default$7__T14')  # <T14>
    _copy$default$7__T15 = typing.TypeVar('_copy$default$7__T15')  # <T15>
    _copy$default$7__T16 = typing.TypeVar('_copy$default$7__T16')  # <T16>
    _copy$default$7__T17 = typing.TypeVar('_copy$default$7__T17')  # <T17>
    _copy$default$7__T18 = typing.TypeVar('_copy$default$7__T18')  # <T18>
    _copy$default$7__T19 = typing.TypeVar('_copy$default$7__T19')  # <T19>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    _copy$default$8__T9 = typing.TypeVar('_copy$default$8__T9')  # <T9>
    _copy$default$8__T10 = typing.TypeVar('_copy$default$8__T10')  # <T10>
    _copy$default$8__T11 = typing.TypeVar('_copy$default$8__T11')  # <T11>
    _copy$default$8__T12 = typing.TypeVar('_copy$default$8__T12')  # <T12>
    _copy$default$8__T13 = typing.TypeVar('_copy$default$8__T13')  # <T13>
    _copy$default$8__T14 = typing.TypeVar('_copy$default$8__T14')  # <T14>
    _copy$default$8__T15 = typing.TypeVar('_copy$default$8__T15')  # <T15>
    _copy$default$8__T16 = typing.TypeVar('_copy$default$8__T16')  # <T16>
    _copy$default$8__T17 = typing.TypeVar('_copy$default$8__T17')  # <T17>
    _copy$default$8__T18 = typing.TypeVar('_copy$default$8__T18')  # <T18>
    _copy$default$8__T19 = typing.TypeVar('_copy$default$8__T19')  # <T19>
    def copy$default$8(self) -> typing.Any: ...
    _copy$default$9__T1 = typing.TypeVar('_copy$default$9__T1')  # <T1>
    _copy$default$9__T2 = typing.TypeVar('_copy$default$9__T2')  # <T2>
    _copy$default$9__T3 = typing.TypeVar('_copy$default$9__T3')  # <T3>
    _copy$default$9__T4 = typing.TypeVar('_copy$default$9__T4')  # <T4>
    _copy$default$9__T5 = typing.TypeVar('_copy$default$9__T5')  # <T5>
    _copy$default$9__T6 = typing.TypeVar('_copy$default$9__T6')  # <T6>
    _copy$default$9__T7 = typing.TypeVar('_copy$default$9__T7')  # <T7>
    _copy$default$9__T8 = typing.TypeVar('_copy$default$9__T8')  # <T8>
    _copy$default$9__T9 = typing.TypeVar('_copy$default$9__T9')  # <T9>
    _copy$default$9__T10 = typing.TypeVar('_copy$default$9__T10')  # <T10>
    _copy$default$9__T11 = typing.TypeVar('_copy$default$9__T11')  # <T11>
    _copy$default$9__T12 = typing.TypeVar('_copy$default$9__T12')  # <T12>
    _copy$default$9__T13 = typing.TypeVar('_copy$default$9__T13')  # <T13>
    _copy$default$9__T14 = typing.TypeVar('_copy$default$9__T14')  # <T14>
    _copy$default$9__T15 = typing.TypeVar('_copy$default$9__T15')  # <T15>
    _copy$default$9__T16 = typing.TypeVar('_copy$default$9__T16')  # <T16>
    _copy$default$9__T17 = typing.TypeVar('_copy$default$9__T17')  # <T17>
    _copy$default$9__T18 = typing.TypeVar('_copy$default$9__T18')  # <T18>
    _copy$default$9__T19 = typing.TypeVar('_copy$default$9__T19')  # <T19>
    def copy$default$9(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    _unapply__T16 = typing.TypeVar('_unapply__T16')  # <T16>
    _unapply__T17 = typing.TypeVar('_unapply__T17')  # <T17>
    _unapply__T18 = typing.TypeVar('_unapply__T18')  # <T18>
    _unapply__T19 = typing.TypeVar('_unapply__T19')  # <T19>
    @staticmethod
    def unapply(x$0: 'Tuple19'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19]) -> Option['Tuple19'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19]]: ...

_Tuple2__T1 = typing.TypeVar('_Tuple2__T1')  # <T1>
_Tuple2__T2 = typing.TypeVar('_Tuple2__T2')  # <T2>
class Tuple2(Product2[_Tuple2__T1, _Tuple2__T2], Serializable, typing.Generic[_Tuple2__T1, _Tuple2__T2]):
    _1: typing.Any = ...
    _2: typing.Any = ...
    def __init__(self, _1: _Tuple2__T1, _2: _Tuple2__T2): ...
    def _1(self) -> _Tuple2__T1: ...
    def _1$mcC$sp(self) -> str: ...
    def _1$mcD$sp(self) -> float: ...
    def _1$mcI$sp(self) -> int: ...
    def _1$mcJ$sp(self) -> int: ...
    def _1$mcZ$sp(self) -> bool: ...
    def _2(self) -> _Tuple2__T2: ...
    def _2$mcC$sp(self) -> str: ...
    def _2$mcD$sp(self) -> float: ...
    def _2$mcI$sp(self) -> int: ...
    def _2$mcJ$sp(self) -> int: ...
    def _2$mcZ$sp(self) -> bool: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2) -> 'Tuple2'[_apply__T1, _apply__T2]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    def copy(self, _1: typing.Any, _2: typing.Any) -> 'Tuple2'[typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$1$mcC$sp__T1 = typing.TypeVar('_copy$default$1$mcC$sp__T1')  # <T1>
    _copy$default$1$mcC$sp__T2 = typing.TypeVar('_copy$default$1$mcC$sp__T2')  # <T2>
    def copy$default$1$mcC$sp(self) -> str: ...
    _copy$default$1$mcD$sp__T1 = typing.TypeVar('_copy$default$1$mcD$sp__T1')  # <T1>
    _copy$default$1$mcD$sp__T2 = typing.TypeVar('_copy$default$1$mcD$sp__T2')  # <T2>
    def copy$default$1$mcD$sp(self) -> float: ...
    _copy$default$1$mcI$sp__T1 = typing.TypeVar('_copy$default$1$mcI$sp__T1')  # <T1>
    _copy$default$1$mcI$sp__T2 = typing.TypeVar('_copy$default$1$mcI$sp__T2')  # <T2>
    def copy$default$1$mcI$sp(self) -> int: ...
    _copy$default$1$mcJ$sp__T1 = typing.TypeVar('_copy$default$1$mcJ$sp__T1')  # <T1>
    _copy$default$1$mcJ$sp__T2 = typing.TypeVar('_copy$default$1$mcJ$sp__T2')  # <T2>
    def copy$default$1$mcJ$sp(self) -> int: ...
    _copy$default$1$mcZ$sp__T1 = typing.TypeVar('_copy$default$1$mcZ$sp__T1')  # <T1>
    _copy$default$1$mcZ$sp__T2 = typing.TypeVar('_copy$default$1$mcZ$sp__T2')  # <T2>
    def copy$default$1$mcZ$sp(self) -> bool: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$2$mcC$sp__T1 = typing.TypeVar('_copy$default$2$mcC$sp__T1')  # <T1>
    _copy$default$2$mcC$sp__T2 = typing.TypeVar('_copy$default$2$mcC$sp__T2')  # <T2>
    def copy$default$2$mcC$sp(self) -> str: ...
    _copy$default$2$mcD$sp__T1 = typing.TypeVar('_copy$default$2$mcD$sp__T1')  # <T1>
    _copy$default$2$mcD$sp__T2 = typing.TypeVar('_copy$default$2$mcD$sp__T2')  # <T2>
    def copy$default$2$mcD$sp(self) -> float: ...
    _copy$default$2$mcI$sp__T1 = typing.TypeVar('_copy$default$2$mcI$sp__T1')  # <T1>
    _copy$default$2$mcI$sp__T2 = typing.TypeVar('_copy$default$2$mcI$sp__T2')  # <T2>
    def copy$default$2$mcI$sp(self) -> int: ...
    _copy$default$2$mcJ$sp__T1 = typing.TypeVar('_copy$default$2$mcJ$sp__T1')  # <T1>
    _copy$default$2$mcJ$sp__T2 = typing.TypeVar('_copy$default$2$mcJ$sp__T2')  # <T2>
    def copy$default$2$mcJ$sp(self) -> int: ...
    _copy$default$2$mcZ$sp__T1 = typing.TypeVar('_copy$default$2$mcZ$sp__T1')  # <T1>
    _copy$default$2$mcZ$sp__T2 = typing.TypeVar('_copy$default$2$mcZ$sp__T2')  # <T2>
    def copy$default$2$mcZ$sp(self) -> bool: ...
    def copy$mCCc$sp(self, _1: str, _2: str) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mCDc$sp(self, _1: str, _2: float) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mCIc$sp(self, _1: str, _2: int) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mCJc$sp(self, _1: str, _2: int) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mCZc$sp(self, _1: str, _2: bool) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mDCc$sp(self, _1: float, _2: str) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mDDc$sp(self, _1: float, _2: float) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mDIc$sp(self, _1: float, _2: int) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mDJc$sp(self, _1: float, _2: int) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mDZc$sp(self, _1: float, _2: bool) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mICc$sp(self, _1: int, _2: str) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mIDc$sp(self, _1: int, _2: float) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mIIc$sp(self, _1: int, _2: int) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mIJc$sp(self, _1: int, _2: int) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mIZc$sp(self, _1: int, _2: bool) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mJCc$sp(self, _1: int, _2: str) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mJDc$sp(self, _1: int, _2: float) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mJIc$sp(self, _1: int, _2: int) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mJJc$sp(self, _1: int, _2: int) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mJZc$sp(self, _1: int, _2: bool) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mZCc$sp(self, _1: bool, _2: str) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mZDc$sp(self, _1: bool, _2: float) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mZIc$sp(self, _1: bool, _2: int) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mZJc$sp(self, _1: bool, _2: int) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def copy$mZZc$sp(self, _1: bool, _2: bool) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def specInstance$(self) -> bool: ...
    def swap(self) -> 'Tuple2'[_Tuple2__T2, _Tuple2__T1]: ...
    def swap$mcCC$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcCD$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcCI$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcCJ$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcCZ$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcDC$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcDD$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcDI$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcDJ$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcDZ$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcIC$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcID$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcII$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcIJ$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcIZ$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcJC$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcJD$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcJI$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcJJ$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcJZ$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcZC$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcZD$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcZI$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcZJ$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def swap$mcZZ$sp(self) -> 'Tuple2'[typing.Any, typing.Any]: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    @staticmethod
    def unapply(x$0: 'Tuple2'[_unapply__T1, _unapply__T2]) -> Option['Tuple2'[_unapply__T1, _unapply__T2]]: ...

_Tuple20__T1 = typing.TypeVar('_Tuple20__T1')  # <T1>
_Tuple20__T2 = typing.TypeVar('_Tuple20__T2')  # <T2>
_Tuple20__T3 = typing.TypeVar('_Tuple20__T3')  # <T3>
_Tuple20__T4 = typing.TypeVar('_Tuple20__T4')  # <T4>
_Tuple20__T5 = typing.TypeVar('_Tuple20__T5')  # <T5>
_Tuple20__T6 = typing.TypeVar('_Tuple20__T6')  # <T6>
_Tuple20__T7 = typing.TypeVar('_Tuple20__T7')  # <T7>
_Tuple20__T8 = typing.TypeVar('_Tuple20__T8')  # <T8>
_Tuple20__T9 = typing.TypeVar('_Tuple20__T9')  # <T9>
_Tuple20__T10 = typing.TypeVar('_Tuple20__T10')  # <T10>
_Tuple20__T11 = typing.TypeVar('_Tuple20__T11')  # <T11>
_Tuple20__T12 = typing.TypeVar('_Tuple20__T12')  # <T12>
_Tuple20__T13 = typing.TypeVar('_Tuple20__T13')  # <T13>
_Tuple20__T14 = typing.TypeVar('_Tuple20__T14')  # <T14>
_Tuple20__T15 = typing.TypeVar('_Tuple20__T15')  # <T15>
_Tuple20__T16 = typing.TypeVar('_Tuple20__T16')  # <T16>
_Tuple20__T17 = typing.TypeVar('_Tuple20__T17')  # <T17>
_Tuple20__T18 = typing.TypeVar('_Tuple20__T18')  # <T18>
_Tuple20__T19 = typing.TypeVar('_Tuple20__T19')  # <T19>
_Tuple20__T20 = typing.TypeVar('_Tuple20__T20')  # <T20>
class Tuple20(Product20[_Tuple20__T1, _Tuple20__T2, _Tuple20__T3, _Tuple20__T4, _Tuple20__T5, _Tuple20__T6, _Tuple20__T7, _Tuple20__T8, _Tuple20__T9, _Tuple20__T10, _Tuple20__T11, _Tuple20__T12, _Tuple20__T13, _Tuple20__T14, _Tuple20__T15, _Tuple20__T16, _Tuple20__T17, _Tuple20__T18, _Tuple20__T19, _Tuple20__T20], Serializable, typing.Generic[_Tuple20__T1, _Tuple20__T2, _Tuple20__T3, _Tuple20__T4, _Tuple20__T5, _Tuple20__T6, _Tuple20__T7, _Tuple20__T8, _Tuple20__T9, _Tuple20__T10, _Tuple20__T11, _Tuple20__T12, _Tuple20__T13, _Tuple20__T14, _Tuple20__T15, _Tuple20__T16, _Tuple20__T17, _Tuple20__T18, _Tuple20__T19, _Tuple20__T20]):
    def __init__(self, _1: _Tuple20__T1, _2: _Tuple20__T2, _3: _Tuple20__T3, _4: _Tuple20__T4, _5: _Tuple20__T5, _6: _Tuple20__T6, _7: _Tuple20__T7, _8: _Tuple20__T8, _9: _Tuple20__T9, _10: _Tuple20__T10, _11: _Tuple20__T11, _12: _Tuple20__T12, _13: _Tuple20__T13, _14: _Tuple20__T14, _15: _Tuple20__T15, _16: _Tuple20__T16, _17: _Tuple20__T17, _18: _Tuple20__T18, _19: _Tuple20__T19, _20: _Tuple20__T20): ...
    def _1(self) -> _Tuple20__T1: ...
    def _10(self) -> _Tuple20__T10: ...
    def _11(self) -> _Tuple20__T11: ...
    def _12(self) -> _Tuple20__T12: ...
    def _13(self) -> _Tuple20__T13: ...
    def _14(self) -> _Tuple20__T14: ...
    def _15(self) -> _Tuple20__T15: ...
    def _16(self) -> _Tuple20__T16: ...
    def _17(self) -> _Tuple20__T17: ...
    def _18(self) -> _Tuple20__T18: ...
    def _19(self) -> _Tuple20__T19: ...
    def _2(self) -> _Tuple20__T2: ...
    def _20(self) -> _Tuple20__T20: ...
    def _3(self) -> _Tuple20__T3: ...
    def _4(self) -> _Tuple20__T4: ...
    def _5(self) -> _Tuple20__T5: ...
    def _6(self) -> _Tuple20__T6: ...
    def _7(self) -> _Tuple20__T7: ...
    def _8(self) -> _Tuple20__T8: ...
    def _9(self) -> _Tuple20__T9: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    _apply__T9 = typing.TypeVar('_apply__T9')  # <T9>
    _apply__T10 = typing.TypeVar('_apply__T10')  # <T10>
    _apply__T11 = typing.TypeVar('_apply__T11')  # <T11>
    _apply__T12 = typing.TypeVar('_apply__T12')  # <T12>
    _apply__T13 = typing.TypeVar('_apply__T13')  # <T13>
    _apply__T14 = typing.TypeVar('_apply__T14')  # <T14>
    _apply__T15 = typing.TypeVar('_apply__T15')  # <T15>
    _apply__T16 = typing.TypeVar('_apply__T16')  # <T16>
    _apply__T17 = typing.TypeVar('_apply__T17')  # <T17>
    _apply__T18 = typing.TypeVar('_apply__T18')  # <T18>
    _apply__T19 = typing.TypeVar('_apply__T19')  # <T19>
    _apply__T20 = typing.TypeVar('_apply__T20')  # <T20>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8, _9: _apply__T9, _10: _apply__T10, _11: _apply__T11, _12: _apply__T12, _13: _apply__T13, _14: _apply__T14, _15: _apply__T15, _16: _apply__T16, _17: _apply__T17, _18: _apply__T18, _19: _apply__T19, _20: _apply__T20) -> 'Tuple20'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8, _apply__T9, _apply__T10, _apply__T11, _apply__T12, _apply__T13, _apply__T14, _apply__T15, _apply__T16, _apply__T17, _apply__T18, _apply__T19, _apply__T20]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    _copy__T9 = typing.TypeVar('_copy__T9')  # <T9>
    _copy__T10 = typing.TypeVar('_copy__T10')  # <T10>
    _copy__T11 = typing.TypeVar('_copy__T11')  # <T11>
    _copy__T12 = typing.TypeVar('_copy__T12')  # <T12>
    _copy__T13 = typing.TypeVar('_copy__T13')  # <T13>
    _copy__T14 = typing.TypeVar('_copy__T14')  # <T14>
    _copy__T15 = typing.TypeVar('_copy__T15')  # <T15>
    _copy__T16 = typing.TypeVar('_copy__T16')  # <T16>
    _copy__T17 = typing.TypeVar('_copy__T17')  # <T17>
    _copy__T18 = typing.TypeVar('_copy__T18')  # <T18>
    _copy__T19 = typing.TypeVar('_copy__T19')  # <T19>
    _copy__T20 = typing.TypeVar('_copy__T20')  # <T20>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any, _9: typing.Any, _10: typing.Any, _11: typing.Any, _12: typing.Any, _13: typing.Any, _14: typing.Any, _15: typing.Any, _16: typing.Any, _17: typing.Any, _18: typing.Any, _19: typing.Any, _20: typing.Any) -> 'Tuple20'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    _copy$default$1__T9 = typing.TypeVar('_copy$default$1__T9')  # <T9>
    _copy$default$1__T10 = typing.TypeVar('_copy$default$1__T10')  # <T10>
    _copy$default$1__T11 = typing.TypeVar('_copy$default$1__T11')  # <T11>
    _copy$default$1__T12 = typing.TypeVar('_copy$default$1__T12')  # <T12>
    _copy$default$1__T13 = typing.TypeVar('_copy$default$1__T13')  # <T13>
    _copy$default$1__T14 = typing.TypeVar('_copy$default$1__T14')  # <T14>
    _copy$default$1__T15 = typing.TypeVar('_copy$default$1__T15')  # <T15>
    _copy$default$1__T16 = typing.TypeVar('_copy$default$1__T16')  # <T16>
    _copy$default$1__T17 = typing.TypeVar('_copy$default$1__T17')  # <T17>
    _copy$default$1__T18 = typing.TypeVar('_copy$default$1__T18')  # <T18>
    _copy$default$1__T19 = typing.TypeVar('_copy$default$1__T19')  # <T19>
    _copy$default$1__T20 = typing.TypeVar('_copy$default$1__T20')  # <T20>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$10__T1 = typing.TypeVar('_copy$default$10__T1')  # <T1>
    _copy$default$10__T2 = typing.TypeVar('_copy$default$10__T2')  # <T2>
    _copy$default$10__T3 = typing.TypeVar('_copy$default$10__T3')  # <T3>
    _copy$default$10__T4 = typing.TypeVar('_copy$default$10__T4')  # <T4>
    _copy$default$10__T5 = typing.TypeVar('_copy$default$10__T5')  # <T5>
    _copy$default$10__T6 = typing.TypeVar('_copy$default$10__T6')  # <T6>
    _copy$default$10__T7 = typing.TypeVar('_copy$default$10__T7')  # <T7>
    _copy$default$10__T8 = typing.TypeVar('_copy$default$10__T8')  # <T8>
    _copy$default$10__T9 = typing.TypeVar('_copy$default$10__T9')  # <T9>
    _copy$default$10__T10 = typing.TypeVar('_copy$default$10__T10')  # <T10>
    _copy$default$10__T11 = typing.TypeVar('_copy$default$10__T11')  # <T11>
    _copy$default$10__T12 = typing.TypeVar('_copy$default$10__T12')  # <T12>
    _copy$default$10__T13 = typing.TypeVar('_copy$default$10__T13')  # <T13>
    _copy$default$10__T14 = typing.TypeVar('_copy$default$10__T14')  # <T14>
    _copy$default$10__T15 = typing.TypeVar('_copy$default$10__T15')  # <T15>
    _copy$default$10__T16 = typing.TypeVar('_copy$default$10__T16')  # <T16>
    _copy$default$10__T17 = typing.TypeVar('_copy$default$10__T17')  # <T17>
    _copy$default$10__T18 = typing.TypeVar('_copy$default$10__T18')  # <T18>
    _copy$default$10__T19 = typing.TypeVar('_copy$default$10__T19')  # <T19>
    _copy$default$10__T20 = typing.TypeVar('_copy$default$10__T20')  # <T20>
    def copy$default$10(self) -> typing.Any: ...
    _copy$default$11__T1 = typing.TypeVar('_copy$default$11__T1')  # <T1>
    _copy$default$11__T2 = typing.TypeVar('_copy$default$11__T2')  # <T2>
    _copy$default$11__T3 = typing.TypeVar('_copy$default$11__T3')  # <T3>
    _copy$default$11__T4 = typing.TypeVar('_copy$default$11__T4')  # <T4>
    _copy$default$11__T5 = typing.TypeVar('_copy$default$11__T5')  # <T5>
    _copy$default$11__T6 = typing.TypeVar('_copy$default$11__T6')  # <T6>
    _copy$default$11__T7 = typing.TypeVar('_copy$default$11__T7')  # <T7>
    _copy$default$11__T8 = typing.TypeVar('_copy$default$11__T8')  # <T8>
    _copy$default$11__T9 = typing.TypeVar('_copy$default$11__T9')  # <T9>
    _copy$default$11__T10 = typing.TypeVar('_copy$default$11__T10')  # <T10>
    _copy$default$11__T11 = typing.TypeVar('_copy$default$11__T11')  # <T11>
    _copy$default$11__T12 = typing.TypeVar('_copy$default$11__T12')  # <T12>
    _copy$default$11__T13 = typing.TypeVar('_copy$default$11__T13')  # <T13>
    _copy$default$11__T14 = typing.TypeVar('_copy$default$11__T14')  # <T14>
    _copy$default$11__T15 = typing.TypeVar('_copy$default$11__T15')  # <T15>
    _copy$default$11__T16 = typing.TypeVar('_copy$default$11__T16')  # <T16>
    _copy$default$11__T17 = typing.TypeVar('_copy$default$11__T17')  # <T17>
    _copy$default$11__T18 = typing.TypeVar('_copy$default$11__T18')  # <T18>
    _copy$default$11__T19 = typing.TypeVar('_copy$default$11__T19')  # <T19>
    _copy$default$11__T20 = typing.TypeVar('_copy$default$11__T20')  # <T20>
    def copy$default$11(self) -> typing.Any: ...
    _copy$default$12__T1 = typing.TypeVar('_copy$default$12__T1')  # <T1>
    _copy$default$12__T2 = typing.TypeVar('_copy$default$12__T2')  # <T2>
    _copy$default$12__T3 = typing.TypeVar('_copy$default$12__T3')  # <T3>
    _copy$default$12__T4 = typing.TypeVar('_copy$default$12__T4')  # <T4>
    _copy$default$12__T5 = typing.TypeVar('_copy$default$12__T5')  # <T5>
    _copy$default$12__T6 = typing.TypeVar('_copy$default$12__T6')  # <T6>
    _copy$default$12__T7 = typing.TypeVar('_copy$default$12__T7')  # <T7>
    _copy$default$12__T8 = typing.TypeVar('_copy$default$12__T8')  # <T8>
    _copy$default$12__T9 = typing.TypeVar('_copy$default$12__T9')  # <T9>
    _copy$default$12__T10 = typing.TypeVar('_copy$default$12__T10')  # <T10>
    _copy$default$12__T11 = typing.TypeVar('_copy$default$12__T11')  # <T11>
    _copy$default$12__T12 = typing.TypeVar('_copy$default$12__T12')  # <T12>
    _copy$default$12__T13 = typing.TypeVar('_copy$default$12__T13')  # <T13>
    _copy$default$12__T14 = typing.TypeVar('_copy$default$12__T14')  # <T14>
    _copy$default$12__T15 = typing.TypeVar('_copy$default$12__T15')  # <T15>
    _copy$default$12__T16 = typing.TypeVar('_copy$default$12__T16')  # <T16>
    _copy$default$12__T17 = typing.TypeVar('_copy$default$12__T17')  # <T17>
    _copy$default$12__T18 = typing.TypeVar('_copy$default$12__T18')  # <T18>
    _copy$default$12__T19 = typing.TypeVar('_copy$default$12__T19')  # <T19>
    _copy$default$12__T20 = typing.TypeVar('_copy$default$12__T20')  # <T20>
    def copy$default$12(self) -> typing.Any: ...
    _copy$default$13__T1 = typing.TypeVar('_copy$default$13__T1')  # <T1>
    _copy$default$13__T2 = typing.TypeVar('_copy$default$13__T2')  # <T2>
    _copy$default$13__T3 = typing.TypeVar('_copy$default$13__T3')  # <T3>
    _copy$default$13__T4 = typing.TypeVar('_copy$default$13__T4')  # <T4>
    _copy$default$13__T5 = typing.TypeVar('_copy$default$13__T5')  # <T5>
    _copy$default$13__T6 = typing.TypeVar('_copy$default$13__T6')  # <T6>
    _copy$default$13__T7 = typing.TypeVar('_copy$default$13__T7')  # <T7>
    _copy$default$13__T8 = typing.TypeVar('_copy$default$13__T8')  # <T8>
    _copy$default$13__T9 = typing.TypeVar('_copy$default$13__T9')  # <T9>
    _copy$default$13__T10 = typing.TypeVar('_copy$default$13__T10')  # <T10>
    _copy$default$13__T11 = typing.TypeVar('_copy$default$13__T11')  # <T11>
    _copy$default$13__T12 = typing.TypeVar('_copy$default$13__T12')  # <T12>
    _copy$default$13__T13 = typing.TypeVar('_copy$default$13__T13')  # <T13>
    _copy$default$13__T14 = typing.TypeVar('_copy$default$13__T14')  # <T14>
    _copy$default$13__T15 = typing.TypeVar('_copy$default$13__T15')  # <T15>
    _copy$default$13__T16 = typing.TypeVar('_copy$default$13__T16')  # <T16>
    _copy$default$13__T17 = typing.TypeVar('_copy$default$13__T17')  # <T17>
    _copy$default$13__T18 = typing.TypeVar('_copy$default$13__T18')  # <T18>
    _copy$default$13__T19 = typing.TypeVar('_copy$default$13__T19')  # <T19>
    _copy$default$13__T20 = typing.TypeVar('_copy$default$13__T20')  # <T20>
    def copy$default$13(self) -> typing.Any: ...
    _copy$default$14__T1 = typing.TypeVar('_copy$default$14__T1')  # <T1>
    _copy$default$14__T2 = typing.TypeVar('_copy$default$14__T2')  # <T2>
    _copy$default$14__T3 = typing.TypeVar('_copy$default$14__T3')  # <T3>
    _copy$default$14__T4 = typing.TypeVar('_copy$default$14__T4')  # <T4>
    _copy$default$14__T5 = typing.TypeVar('_copy$default$14__T5')  # <T5>
    _copy$default$14__T6 = typing.TypeVar('_copy$default$14__T6')  # <T6>
    _copy$default$14__T7 = typing.TypeVar('_copy$default$14__T7')  # <T7>
    _copy$default$14__T8 = typing.TypeVar('_copy$default$14__T8')  # <T8>
    _copy$default$14__T9 = typing.TypeVar('_copy$default$14__T9')  # <T9>
    _copy$default$14__T10 = typing.TypeVar('_copy$default$14__T10')  # <T10>
    _copy$default$14__T11 = typing.TypeVar('_copy$default$14__T11')  # <T11>
    _copy$default$14__T12 = typing.TypeVar('_copy$default$14__T12')  # <T12>
    _copy$default$14__T13 = typing.TypeVar('_copy$default$14__T13')  # <T13>
    _copy$default$14__T14 = typing.TypeVar('_copy$default$14__T14')  # <T14>
    _copy$default$14__T15 = typing.TypeVar('_copy$default$14__T15')  # <T15>
    _copy$default$14__T16 = typing.TypeVar('_copy$default$14__T16')  # <T16>
    _copy$default$14__T17 = typing.TypeVar('_copy$default$14__T17')  # <T17>
    _copy$default$14__T18 = typing.TypeVar('_copy$default$14__T18')  # <T18>
    _copy$default$14__T19 = typing.TypeVar('_copy$default$14__T19')  # <T19>
    _copy$default$14__T20 = typing.TypeVar('_copy$default$14__T20')  # <T20>
    def copy$default$14(self) -> typing.Any: ...
    _copy$default$15__T1 = typing.TypeVar('_copy$default$15__T1')  # <T1>
    _copy$default$15__T2 = typing.TypeVar('_copy$default$15__T2')  # <T2>
    _copy$default$15__T3 = typing.TypeVar('_copy$default$15__T3')  # <T3>
    _copy$default$15__T4 = typing.TypeVar('_copy$default$15__T4')  # <T4>
    _copy$default$15__T5 = typing.TypeVar('_copy$default$15__T5')  # <T5>
    _copy$default$15__T6 = typing.TypeVar('_copy$default$15__T6')  # <T6>
    _copy$default$15__T7 = typing.TypeVar('_copy$default$15__T7')  # <T7>
    _copy$default$15__T8 = typing.TypeVar('_copy$default$15__T8')  # <T8>
    _copy$default$15__T9 = typing.TypeVar('_copy$default$15__T9')  # <T9>
    _copy$default$15__T10 = typing.TypeVar('_copy$default$15__T10')  # <T10>
    _copy$default$15__T11 = typing.TypeVar('_copy$default$15__T11')  # <T11>
    _copy$default$15__T12 = typing.TypeVar('_copy$default$15__T12')  # <T12>
    _copy$default$15__T13 = typing.TypeVar('_copy$default$15__T13')  # <T13>
    _copy$default$15__T14 = typing.TypeVar('_copy$default$15__T14')  # <T14>
    _copy$default$15__T15 = typing.TypeVar('_copy$default$15__T15')  # <T15>
    _copy$default$15__T16 = typing.TypeVar('_copy$default$15__T16')  # <T16>
    _copy$default$15__T17 = typing.TypeVar('_copy$default$15__T17')  # <T17>
    _copy$default$15__T18 = typing.TypeVar('_copy$default$15__T18')  # <T18>
    _copy$default$15__T19 = typing.TypeVar('_copy$default$15__T19')  # <T19>
    _copy$default$15__T20 = typing.TypeVar('_copy$default$15__T20')  # <T20>
    def copy$default$15(self) -> typing.Any: ...
    _copy$default$16__T1 = typing.TypeVar('_copy$default$16__T1')  # <T1>
    _copy$default$16__T2 = typing.TypeVar('_copy$default$16__T2')  # <T2>
    _copy$default$16__T3 = typing.TypeVar('_copy$default$16__T3')  # <T3>
    _copy$default$16__T4 = typing.TypeVar('_copy$default$16__T4')  # <T4>
    _copy$default$16__T5 = typing.TypeVar('_copy$default$16__T5')  # <T5>
    _copy$default$16__T6 = typing.TypeVar('_copy$default$16__T6')  # <T6>
    _copy$default$16__T7 = typing.TypeVar('_copy$default$16__T7')  # <T7>
    _copy$default$16__T8 = typing.TypeVar('_copy$default$16__T8')  # <T8>
    _copy$default$16__T9 = typing.TypeVar('_copy$default$16__T9')  # <T9>
    _copy$default$16__T10 = typing.TypeVar('_copy$default$16__T10')  # <T10>
    _copy$default$16__T11 = typing.TypeVar('_copy$default$16__T11')  # <T11>
    _copy$default$16__T12 = typing.TypeVar('_copy$default$16__T12')  # <T12>
    _copy$default$16__T13 = typing.TypeVar('_copy$default$16__T13')  # <T13>
    _copy$default$16__T14 = typing.TypeVar('_copy$default$16__T14')  # <T14>
    _copy$default$16__T15 = typing.TypeVar('_copy$default$16__T15')  # <T15>
    _copy$default$16__T16 = typing.TypeVar('_copy$default$16__T16')  # <T16>
    _copy$default$16__T17 = typing.TypeVar('_copy$default$16__T17')  # <T17>
    _copy$default$16__T18 = typing.TypeVar('_copy$default$16__T18')  # <T18>
    _copy$default$16__T19 = typing.TypeVar('_copy$default$16__T19')  # <T19>
    _copy$default$16__T20 = typing.TypeVar('_copy$default$16__T20')  # <T20>
    def copy$default$16(self) -> typing.Any: ...
    _copy$default$17__T1 = typing.TypeVar('_copy$default$17__T1')  # <T1>
    _copy$default$17__T2 = typing.TypeVar('_copy$default$17__T2')  # <T2>
    _copy$default$17__T3 = typing.TypeVar('_copy$default$17__T3')  # <T3>
    _copy$default$17__T4 = typing.TypeVar('_copy$default$17__T4')  # <T4>
    _copy$default$17__T5 = typing.TypeVar('_copy$default$17__T5')  # <T5>
    _copy$default$17__T6 = typing.TypeVar('_copy$default$17__T6')  # <T6>
    _copy$default$17__T7 = typing.TypeVar('_copy$default$17__T7')  # <T7>
    _copy$default$17__T8 = typing.TypeVar('_copy$default$17__T8')  # <T8>
    _copy$default$17__T9 = typing.TypeVar('_copy$default$17__T9')  # <T9>
    _copy$default$17__T10 = typing.TypeVar('_copy$default$17__T10')  # <T10>
    _copy$default$17__T11 = typing.TypeVar('_copy$default$17__T11')  # <T11>
    _copy$default$17__T12 = typing.TypeVar('_copy$default$17__T12')  # <T12>
    _copy$default$17__T13 = typing.TypeVar('_copy$default$17__T13')  # <T13>
    _copy$default$17__T14 = typing.TypeVar('_copy$default$17__T14')  # <T14>
    _copy$default$17__T15 = typing.TypeVar('_copy$default$17__T15')  # <T15>
    _copy$default$17__T16 = typing.TypeVar('_copy$default$17__T16')  # <T16>
    _copy$default$17__T17 = typing.TypeVar('_copy$default$17__T17')  # <T17>
    _copy$default$17__T18 = typing.TypeVar('_copy$default$17__T18')  # <T18>
    _copy$default$17__T19 = typing.TypeVar('_copy$default$17__T19')  # <T19>
    _copy$default$17__T20 = typing.TypeVar('_copy$default$17__T20')  # <T20>
    def copy$default$17(self) -> typing.Any: ...
    _copy$default$18__T1 = typing.TypeVar('_copy$default$18__T1')  # <T1>
    _copy$default$18__T2 = typing.TypeVar('_copy$default$18__T2')  # <T2>
    _copy$default$18__T3 = typing.TypeVar('_copy$default$18__T3')  # <T3>
    _copy$default$18__T4 = typing.TypeVar('_copy$default$18__T4')  # <T4>
    _copy$default$18__T5 = typing.TypeVar('_copy$default$18__T5')  # <T5>
    _copy$default$18__T6 = typing.TypeVar('_copy$default$18__T6')  # <T6>
    _copy$default$18__T7 = typing.TypeVar('_copy$default$18__T7')  # <T7>
    _copy$default$18__T8 = typing.TypeVar('_copy$default$18__T8')  # <T8>
    _copy$default$18__T9 = typing.TypeVar('_copy$default$18__T9')  # <T9>
    _copy$default$18__T10 = typing.TypeVar('_copy$default$18__T10')  # <T10>
    _copy$default$18__T11 = typing.TypeVar('_copy$default$18__T11')  # <T11>
    _copy$default$18__T12 = typing.TypeVar('_copy$default$18__T12')  # <T12>
    _copy$default$18__T13 = typing.TypeVar('_copy$default$18__T13')  # <T13>
    _copy$default$18__T14 = typing.TypeVar('_copy$default$18__T14')  # <T14>
    _copy$default$18__T15 = typing.TypeVar('_copy$default$18__T15')  # <T15>
    _copy$default$18__T16 = typing.TypeVar('_copy$default$18__T16')  # <T16>
    _copy$default$18__T17 = typing.TypeVar('_copy$default$18__T17')  # <T17>
    _copy$default$18__T18 = typing.TypeVar('_copy$default$18__T18')  # <T18>
    _copy$default$18__T19 = typing.TypeVar('_copy$default$18__T19')  # <T19>
    _copy$default$18__T20 = typing.TypeVar('_copy$default$18__T20')  # <T20>
    def copy$default$18(self) -> typing.Any: ...
    _copy$default$19__T1 = typing.TypeVar('_copy$default$19__T1')  # <T1>
    _copy$default$19__T2 = typing.TypeVar('_copy$default$19__T2')  # <T2>
    _copy$default$19__T3 = typing.TypeVar('_copy$default$19__T3')  # <T3>
    _copy$default$19__T4 = typing.TypeVar('_copy$default$19__T4')  # <T4>
    _copy$default$19__T5 = typing.TypeVar('_copy$default$19__T5')  # <T5>
    _copy$default$19__T6 = typing.TypeVar('_copy$default$19__T6')  # <T6>
    _copy$default$19__T7 = typing.TypeVar('_copy$default$19__T7')  # <T7>
    _copy$default$19__T8 = typing.TypeVar('_copy$default$19__T8')  # <T8>
    _copy$default$19__T9 = typing.TypeVar('_copy$default$19__T9')  # <T9>
    _copy$default$19__T10 = typing.TypeVar('_copy$default$19__T10')  # <T10>
    _copy$default$19__T11 = typing.TypeVar('_copy$default$19__T11')  # <T11>
    _copy$default$19__T12 = typing.TypeVar('_copy$default$19__T12')  # <T12>
    _copy$default$19__T13 = typing.TypeVar('_copy$default$19__T13')  # <T13>
    _copy$default$19__T14 = typing.TypeVar('_copy$default$19__T14')  # <T14>
    _copy$default$19__T15 = typing.TypeVar('_copy$default$19__T15')  # <T15>
    _copy$default$19__T16 = typing.TypeVar('_copy$default$19__T16')  # <T16>
    _copy$default$19__T17 = typing.TypeVar('_copy$default$19__T17')  # <T17>
    _copy$default$19__T18 = typing.TypeVar('_copy$default$19__T18')  # <T18>
    _copy$default$19__T19 = typing.TypeVar('_copy$default$19__T19')  # <T19>
    _copy$default$19__T20 = typing.TypeVar('_copy$default$19__T20')  # <T20>
    def copy$default$19(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    _copy$default$2__T9 = typing.TypeVar('_copy$default$2__T9')  # <T9>
    _copy$default$2__T10 = typing.TypeVar('_copy$default$2__T10')  # <T10>
    _copy$default$2__T11 = typing.TypeVar('_copy$default$2__T11')  # <T11>
    _copy$default$2__T12 = typing.TypeVar('_copy$default$2__T12')  # <T12>
    _copy$default$2__T13 = typing.TypeVar('_copy$default$2__T13')  # <T13>
    _copy$default$2__T14 = typing.TypeVar('_copy$default$2__T14')  # <T14>
    _copy$default$2__T15 = typing.TypeVar('_copy$default$2__T15')  # <T15>
    _copy$default$2__T16 = typing.TypeVar('_copy$default$2__T16')  # <T16>
    _copy$default$2__T17 = typing.TypeVar('_copy$default$2__T17')  # <T17>
    _copy$default$2__T18 = typing.TypeVar('_copy$default$2__T18')  # <T18>
    _copy$default$2__T19 = typing.TypeVar('_copy$default$2__T19')  # <T19>
    _copy$default$2__T20 = typing.TypeVar('_copy$default$2__T20')  # <T20>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$20__T1 = typing.TypeVar('_copy$default$20__T1')  # <T1>
    _copy$default$20__T2 = typing.TypeVar('_copy$default$20__T2')  # <T2>
    _copy$default$20__T3 = typing.TypeVar('_copy$default$20__T3')  # <T3>
    _copy$default$20__T4 = typing.TypeVar('_copy$default$20__T4')  # <T4>
    _copy$default$20__T5 = typing.TypeVar('_copy$default$20__T5')  # <T5>
    _copy$default$20__T6 = typing.TypeVar('_copy$default$20__T6')  # <T6>
    _copy$default$20__T7 = typing.TypeVar('_copy$default$20__T7')  # <T7>
    _copy$default$20__T8 = typing.TypeVar('_copy$default$20__T8')  # <T8>
    _copy$default$20__T9 = typing.TypeVar('_copy$default$20__T9')  # <T9>
    _copy$default$20__T10 = typing.TypeVar('_copy$default$20__T10')  # <T10>
    _copy$default$20__T11 = typing.TypeVar('_copy$default$20__T11')  # <T11>
    _copy$default$20__T12 = typing.TypeVar('_copy$default$20__T12')  # <T12>
    _copy$default$20__T13 = typing.TypeVar('_copy$default$20__T13')  # <T13>
    _copy$default$20__T14 = typing.TypeVar('_copy$default$20__T14')  # <T14>
    _copy$default$20__T15 = typing.TypeVar('_copy$default$20__T15')  # <T15>
    _copy$default$20__T16 = typing.TypeVar('_copy$default$20__T16')  # <T16>
    _copy$default$20__T17 = typing.TypeVar('_copy$default$20__T17')  # <T17>
    _copy$default$20__T18 = typing.TypeVar('_copy$default$20__T18')  # <T18>
    _copy$default$20__T19 = typing.TypeVar('_copy$default$20__T19')  # <T19>
    _copy$default$20__T20 = typing.TypeVar('_copy$default$20__T20')  # <T20>
    def copy$default$20(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    _copy$default$3__T9 = typing.TypeVar('_copy$default$3__T9')  # <T9>
    _copy$default$3__T10 = typing.TypeVar('_copy$default$3__T10')  # <T10>
    _copy$default$3__T11 = typing.TypeVar('_copy$default$3__T11')  # <T11>
    _copy$default$3__T12 = typing.TypeVar('_copy$default$3__T12')  # <T12>
    _copy$default$3__T13 = typing.TypeVar('_copy$default$3__T13')  # <T13>
    _copy$default$3__T14 = typing.TypeVar('_copy$default$3__T14')  # <T14>
    _copy$default$3__T15 = typing.TypeVar('_copy$default$3__T15')  # <T15>
    _copy$default$3__T16 = typing.TypeVar('_copy$default$3__T16')  # <T16>
    _copy$default$3__T17 = typing.TypeVar('_copy$default$3__T17')  # <T17>
    _copy$default$3__T18 = typing.TypeVar('_copy$default$3__T18')  # <T18>
    _copy$default$3__T19 = typing.TypeVar('_copy$default$3__T19')  # <T19>
    _copy$default$3__T20 = typing.TypeVar('_copy$default$3__T20')  # <T20>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    _copy$default$4__T9 = typing.TypeVar('_copy$default$4__T9')  # <T9>
    _copy$default$4__T10 = typing.TypeVar('_copy$default$4__T10')  # <T10>
    _copy$default$4__T11 = typing.TypeVar('_copy$default$4__T11')  # <T11>
    _copy$default$4__T12 = typing.TypeVar('_copy$default$4__T12')  # <T12>
    _copy$default$4__T13 = typing.TypeVar('_copy$default$4__T13')  # <T13>
    _copy$default$4__T14 = typing.TypeVar('_copy$default$4__T14')  # <T14>
    _copy$default$4__T15 = typing.TypeVar('_copy$default$4__T15')  # <T15>
    _copy$default$4__T16 = typing.TypeVar('_copy$default$4__T16')  # <T16>
    _copy$default$4__T17 = typing.TypeVar('_copy$default$4__T17')  # <T17>
    _copy$default$4__T18 = typing.TypeVar('_copy$default$4__T18')  # <T18>
    _copy$default$4__T19 = typing.TypeVar('_copy$default$4__T19')  # <T19>
    _copy$default$4__T20 = typing.TypeVar('_copy$default$4__T20')  # <T20>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    _copy$default$5__T9 = typing.TypeVar('_copy$default$5__T9')  # <T9>
    _copy$default$5__T10 = typing.TypeVar('_copy$default$5__T10')  # <T10>
    _copy$default$5__T11 = typing.TypeVar('_copy$default$5__T11')  # <T11>
    _copy$default$5__T12 = typing.TypeVar('_copy$default$5__T12')  # <T12>
    _copy$default$5__T13 = typing.TypeVar('_copy$default$5__T13')  # <T13>
    _copy$default$5__T14 = typing.TypeVar('_copy$default$5__T14')  # <T14>
    _copy$default$5__T15 = typing.TypeVar('_copy$default$5__T15')  # <T15>
    _copy$default$5__T16 = typing.TypeVar('_copy$default$5__T16')  # <T16>
    _copy$default$5__T17 = typing.TypeVar('_copy$default$5__T17')  # <T17>
    _copy$default$5__T18 = typing.TypeVar('_copy$default$5__T18')  # <T18>
    _copy$default$5__T19 = typing.TypeVar('_copy$default$5__T19')  # <T19>
    _copy$default$5__T20 = typing.TypeVar('_copy$default$5__T20')  # <T20>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    _copy$default$6__T9 = typing.TypeVar('_copy$default$6__T9')  # <T9>
    _copy$default$6__T10 = typing.TypeVar('_copy$default$6__T10')  # <T10>
    _copy$default$6__T11 = typing.TypeVar('_copy$default$6__T11')  # <T11>
    _copy$default$6__T12 = typing.TypeVar('_copy$default$6__T12')  # <T12>
    _copy$default$6__T13 = typing.TypeVar('_copy$default$6__T13')  # <T13>
    _copy$default$6__T14 = typing.TypeVar('_copy$default$6__T14')  # <T14>
    _copy$default$6__T15 = typing.TypeVar('_copy$default$6__T15')  # <T15>
    _copy$default$6__T16 = typing.TypeVar('_copy$default$6__T16')  # <T16>
    _copy$default$6__T17 = typing.TypeVar('_copy$default$6__T17')  # <T17>
    _copy$default$6__T18 = typing.TypeVar('_copy$default$6__T18')  # <T18>
    _copy$default$6__T19 = typing.TypeVar('_copy$default$6__T19')  # <T19>
    _copy$default$6__T20 = typing.TypeVar('_copy$default$6__T20')  # <T20>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    _copy$default$7__T9 = typing.TypeVar('_copy$default$7__T9')  # <T9>
    _copy$default$7__T10 = typing.TypeVar('_copy$default$7__T10')  # <T10>
    _copy$default$7__T11 = typing.TypeVar('_copy$default$7__T11')  # <T11>
    _copy$default$7__T12 = typing.TypeVar('_copy$default$7__T12')  # <T12>
    _copy$default$7__T13 = typing.TypeVar('_copy$default$7__T13')  # <T13>
    _copy$default$7__T14 = typing.TypeVar('_copy$default$7__T14')  # <T14>
    _copy$default$7__T15 = typing.TypeVar('_copy$default$7__T15')  # <T15>
    _copy$default$7__T16 = typing.TypeVar('_copy$default$7__T16')  # <T16>
    _copy$default$7__T17 = typing.TypeVar('_copy$default$7__T17')  # <T17>
    _copy$default$7__T18 = typing.TypeVar('_copy$default$7__T18')  # <T18>
    _copy$default$7__T19 = typing.TypeVar('_copy$default$7__T19')  # <T19>
    _copy$default$7__T20 = typing.TypeVar('_copy$default$7__T20')  # <T20>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    _copy$default$8__T9 = typing.TypeVar('_copy$default$8__T9')  # <T9>
    _copy$default$8__T10 = typing.TypeVar('_copy$default$8__T10')  # <T10>
    _copy$default$8__T11 = typing.TypeVar('_copy$default$8__T11')  # <T11>
    _copy$default$8__T12 = typing.TypeVar('_copy$default$8__T12')  # <T12>
    _copy$default$8__T13 = typing.TypeVar('_copy$default$8__T13')  # <T13>
    _copy$default$8__T14 = typing.TypeVar('_copy$default$8__T14')  # <T14>
    _copy$default$8__T15 = typing.TypeVar('_copy$default$8__T15')  # <T15>
    _copy$default$8__T16 = typing.TypeVar('_copy$default$8__T16')  # <T16>
    _copy$default$8__T17 = typing.TypeVar('_copy$default$8__T17')  # <T17>
    _copy$default$8__T18 = typing.TypeVar('_copy$default$8__T18')  # <T18>
    _copy$default$8__T19 = typing.TypeVar('_copy$default$8__T19')  # <T19>
    _copy$default$8__T20 = typing.TypeVar('_copy$default$8__T20')  # <T20>
    def copy$default$8(self) -> typing.Any: ...
    _copy$default$9__T1 = typing.TypeVar('_copy$default$9__T1')  # <T1>
    _copy$default$9__T2 = typing.TypeVar('_copy$default$9__T2')  # <T2>
    _copy$default$9__T3 = typing.TypeVar('_copy$default$9__T3')  # <T3>
    _copy$default$9__T4 = typing.TypeVar('_copy$default$9__T4')  # <T4>
    _copy$default$9__T5 = typing.TypeVar('_copy$default$9__T5')  # <T5>
    _copy$default$9__T6 = typing.TypeVar('_copy$default$9__T6')  # <T6>
    _copy$default$9__T7 = typing.TypeVar('_copy$default$9__T7')  # <T7>
    _copy$default$9__T8 = typing.TypeVar('_copy$default$9__T8')  # <T8>
    _copy$default$9__T9 = typing.TypeVar('_copy$default$9__T9')  # <T9>
    _copy$default$9__T10 = typing.TypeVar('_copy$default$9__T10')  # <T10>
    _copy$default$9__T11 = typing.TypeVar('_copy$default$9__T11')  # <T11>
    _copy$default$9__T12 = typing.TypeVar('_copy$default$9__T12')  # <T12>
    _copy$default$9__T13 = typing.TypeVar('_copy$default$9__T13')  # <T13>
    _copy$default$9__T14 = typing.TypeVar('_copy$default$9__T14')  # <T14>
    _copy$default$9__T15 = typing.TypeVar('_copy$default$9__T15')  # <T15>
    _copy$default$9__T16 = typing.TypeVar('_copy$default$9__T16')  # <T16>
    _copy$default$9__T17 = typing.TypeVar('_copy$default$9__T17')  # <T17>
    _copy$default$9__T18 = typing.TypeVar('_copy$default$9__T18')  # <T18>
    _copy$default$9__T19 = typing.TypeVar('_copy$default$9__T19')  # <T19>
    _copy$default$9__T20 = typing.TypeVar('_copy$default$9__T20')  # <T20>
    def copy$default$9(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    _unapply__T16 = typing.TypeVar('_unapply__T16')  # <T16>
    _unapply__T17 = typing.TypeVar('_unapply__T17')  # <T17>
    _unapply__T18 = typing.TypeVar('_unapply__T18')  # <T18>
    _unapply__T19 = typing.TypeVar('_unapply__T19')  # <T19>
    _unapply__T20 = typing.TypeVar('_unapply__T20')  # <T20>
    @staticmethod
    def unapply(x$0: 'Tuple20'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19, _unapply__T20]) -> Option['Tuple20'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19, _unapply__T20]]: ...

_Tuple21__T1 = typing.TypeVar('_Tuple21__T1')  # <T1>
_Tuple21__T2 = typing.TypeVar('_Tuple21__T2')  # <T2>
_Tuple21__T3 = typing.TypeVar('_Tuple21__T3')  # <T3>
_Tuple21__T4 = typing.TypeVar('_Tuple21__T4')  # <T4>
_Tuple21__T5 = typing.TypeVar('_Tuple21__T5')  # <T5>
_Tuple21__T6 = typing.TypeVar('_Tuple21__T6')  # <T6>
_Tuple21__T7 = typing.TypeVar('_Tuple21__T7')  # <T7>
_Tuple21__T8 = typing.TypeVar('_Tuple21__T8')  # <T8>
_Tuple21__T9 = typing.TypeVar('_Tuple21__T9')  # <T9>
_Tuple21__T10 = typing.TypeVar('_Tuple21__T10')  # <T10>
_Tuple21__T11 = typing.TypeVar('_Tuple21__T11')  # <T11>
_Tuple21__T12 = typing.TypeVar('_Tuple21__T12')  # <T12>
_Tuple21__T13 = typing.TypeVar('_Tuple21__T13')  # <T13>
_Tuple21__T14 = typing.TypeVar('_Tuple21__T14')  # <T14>
_Tuple21__T15 = typing.TypeVar('_Tuple21__T15')  # <T15>
_Tuple21__T16 = typing.TypeVar('_Tuple21__T16')  # <T16>
_Tuple21__T17 = typing.TypeVar('_Tuple21__T17')  # <T17>
_Tuple21__T18 = typing.TypeVar('_Tuple21__T18')  # <T18>
_Tuple21__T19 = typing.TypeVar('_Tuple21__T19')  # <T19>
_Tuple21__T20 = typing.TypeVar('_Tuple21__T20')  # <T20>
_Tuple21__T21 = typing.TypeVar('_Tuple21__T21')  # <T21>
class Tuple21(Product21[_Tuple21__T1, _Tuple21__T2, _Tuple21__T3, _Tuple21__T4, _Tuple21__T5, _Tuple21__T6, _Tuple21__T7, _Tuple21__T8, _Tuple21__T9, _Tuple21__T10, _Tuple21__T11, _Tuple21__T12, _Tuple21__T13, _Tuple21__T14, _Tuple21__T15, _Tuple21__T16, _Tuple21__T17, _Tuple21__T18, _Tuple21__T19, _Tuple21__T20, _Tuple21__T21], Serializable, typing.Generic[_Tuple21__T1, _Tuple21__T2, _Tuple21__T3, _Tuple21__T4, _Tuple21__T5, _Tuple21__T6, _Tuple21__T7, _Tuple21__T8, _Tuple21__T9, _Tuple21__T10, _Tuple21__T11, _Tuple21__T12, _Tuple21__T13, _Tuple21__T14, _Tuple21__T15, _Tuple21__T16, _Tuple21__T17, _Tuple21__T18, _Tuple21__T19, _Tuple21__T20, _Tuple21__T21]):
    def __init__(self, _1: _Tuple21__T1, _2: _Tuple21__T2, _3: _Tuple21__T3, _4: _Tuple21__T4, _5: _Tuple21__T5, _6: _Tuple21__T6, _7: _Tuple21__T7, _8: _Tuple21__T8, _9: _Tuple21__T9, _10: _Tuple21__T10, _11: _Tuple21__T11, _12: _Tuple21__T12, _13: _Tuple21__T13, _14: _Tuple21__T14, _15: _Tuple21__T15, _16: _Tuple21__T16, _17: _Tuple21__T17, _18: _Tuple21__T18, _19: _Tuple21__T19, _20: _Tuple21__T20, _21: _Tuple21__T21): ...
    def _1(self) -> _Tuple21__T1: ...
    def _10(self) -> _Tuple21__T10: ...
    def _11(self) -> _Tuple21__T11: ...
    def _12(self) -> _Tuple21__T12: ...
    def _13(self) -> _Tuple21__T13: ...
    def _14(self) -> _Tuple21__T14: ...
    def _15(self) -> _Tuple21__T15: ...
    def _16(self) -> _Tuple21__T16: ...
    def _17(self) -> _Tuple21__T17: ...
    def _18(self) -> _Tuple21__T18: ...
    def _19(self) -> _Tuple21__T19: ...
    def _2(self) -> _Tuple21__T2: ...
    def _20(self) -> _Tuple21__T20: ...
    def _21(self) -> _Tuple21__T21: ...
    def _3(self) -> _Tuple21__T3: ...
    def _4(self) -> _Tuple21__T4: ...
    def _5(self) -> _Tuple21__T5: ...
    def _6(self) -> _Tuple21__T6: ...
    def _7(self) -> _Tuple21__T7: ...
    def _8(self) -> _Tuple21__T8: ...
    def _9(self) -> _Tuple21__T9: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    _apply__T9 = typing.TypeVar('_apply__T9')  # <T9>
    _apply__T10 = typing.TypeVar('_apply__T10')  # <T10>
    _apply__T11 = typing.TypeVar('_apply__T11')  # <T11>
    _apply__T12 = typing.TypeVar('_apply__T12')  # <T12>
    _apply__T13 = typing.TypeVar('_apply__T13')  # <T13>
    _apply__T14 = typing.TypeVar('_apply__T14')  # <T14>
    _apply__T15 = typing.TypeVar('_apply__T15')  # <T15>
    _apply__T16 = typing.TypeVar('_apply__T16')  # <T16>
    _apply__T17 = typing.TypeVar('_apply__T17')  # <T17>
    _apply__T18 = typing.TypeVar('_apply__T18')  # <T18>
    _apply__T19 = typing.TypeVar('_apply__T19')  # <T19>
    _apply__T20 = typing.TypeVar('_apply__T20')  # <T20>
    _apply__T21 = typing.TypeVar('_apply__T21')  # <T21>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8, _9: _apply__T9, _10: _apply__T10, _11: _apply__T11, _12: _apply__T12, _13: _apply__T13, _14: _apply__T14, _15: _apply__T15, _16: _apply__T16, _17: _apply__T17, _18: _apply__T18, _19: _apply__T19, _20: _apply__T20, _21: _apply__T21) -> 'Tuple21'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8, _apply__T9, _apply__T10, _apply__T11, _apply__T12, _apply__T13, _apply__T14, _apply__T15, _apply__T16, _apply__T17, _apply__T18, _apply__T19, _apply__T20, _apply__T21]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    _copy__T9 = typing.TypeVar('_copy__T9')  # <T9>
    _copy__T10 = typing.TypeVar('_copy__T10')  # <T10>
    _copy__T11 = typing.TypeVar('_copy__T11')  # <T11>
    _copy__T12 = typing.TypeVar('_copy__T12')  # <T12>
    _copy__T13 = typing.TypeVar('_copy__T13')  # <T13>
    _copy__T14 = typing.TypeVar('_copy__T14')  # <T14>
    _copy__T15 = typing.TypeVar('_copy__T15')  # <T15>
    _copy__T16 = typing.TypeVar('_copy__T16')  # <T16>
    _copy__T17 = typing.TypeVar('_copy__T17')  # <T17>
    _copy__T18 = typing.TypeVar('_copy__T18')  # <T18>
    _copy__T19 = typing.TypeVar('_copy__T19')  # <T19>
    _copy__T20 = typing.TypeVar('_copy__T20')  # <T20>
    _copy__T21 = typing.TypeVar('_copy__T21')  # <T21>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any, _9: typing.Any, _10: typing.Any, _11: typing.Any, _12: typing.Any, _13: typing.Any, _14: typing.Any, _15: typing.Any, _16: typing.Any, _17: typing.Any, _18: typing.Any, _19: typing.Any, _20: typing.Any, _21: typing.Any) -> 'Tuple21'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    _copy$default$1__T9 = typing.TypeVar('_copy$default$1__T9')  # <T9>
    _copy$default$1__T10 = typing.TypeVar('_copy$default$1__T10')  # <T10>
    _copy$default$1__T11 = typing.TypeVar('_copy$default$1__T11')  # <T11>
    _copy$default$1__T12 = typing.TypeVar('_copy$default$1__T12')  # <T12>
    _copy$default$1__T13 = typing.TypeVar('_copy$default$1__T13')  # <T13>
    _copy$default$1__T14 = typing.TypeVar('_copy$default$1__T14')  # <T14>
    _copy$default$1__T15 = typing.TypeVar('_copy$default$1__T15')  # <T15>
    _copy$default$1__T16 = typing.TypeVar('_copy$default$1__T16')  # <T16>
    _copy$default$1__T17 = typing.TypeVar('_copy$default$1__T17')  # <T17>
    _copy$default$1__T18 = typing.TypeVar('_copy$default$1__T18')  # <T18>
    _copy$default$1__T19 = typing.TypeVar('_copy$default$1__T19')  # <T19>
    _copy$default$1__T20 = typing.TypeVar('_copy$default$1__T20')  # <T20>
    _copy$default$1__T21 = typing.TypeVar('_copy$default$1__T21')  # <T21>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$10__T1 = typing.TypeVar('_copy$default$10__T1')  # <T1>
    _copy$default$10__T2 = typing.TypeVar('_copy$default$10__T2')  # <T2>
    _copy$default$10__T3 = typing.TypeVar('_copy$default$10__T3')  # <T3>
    _copy$default$10__T4 = typing.TypeVar('_copy$default$10__T4')  # <T4>
    _copy$default$10__T5 = typing.TypeVar('_copy$default$10__T5')  # <T5>
    _copy$default$10__T6 = typing.TypeVar('_copy$default$10__T6')  # <T6>
    _copy$default$10__T7 = typing.TypeVar('_copy$default$10__T7')  # <T7>
    _copy$default$10__T8 = typing.TypeVar('_copy$default$10__T8')  # <T8>
    _copy$default$10__T9 = typing.TypeVar('_copy$default$10__T9')  # <T9>
    _copy$default$10__T10 = typing.TypeVar('_copy$default$10__T10')  # <T10>
    _copy$default$10__T11 = typing.TypeVar('_copy$default$10__T11')  # <T11>
    _copy$default$10__T12 = typing.TypeVar('_copy$default$10__T12')  # <T12>
    _copy$default$10__T13 = typing.TypeVar('_copy$default$10__T13')  # <T13>
    _copy$default$10__T14 = typing.TypeVar('_copy$default$10__T14')  # <T14>
    _copy$default$10__T15 = typing.TypeVar('_copy$default$10__T15')  # <T15>
    _copy$default$10__T16 = typing.TypeVar('_copy$default$10__T16')  # <T16>
    _copy$default$10__T17 = typing.TypeVar('_copy$default$10__T17')  # <T17>
    _copy$default$10__T18 = typing.TypeVar('_copy$default$10__T18')  # <T18>
    _copy$default$10__T19 = typing.TypeVar('_copy$default$10__T19')  # <T19>
    _copy$default$10__T20 = typing.TypeVar('_copy$default$10__T20')  # <T20>
    _copy$default$10__T21 = typing.TypeVar('_copy$default$10__T21')  # <T21>
    def copy$default$10(self) -> typing.Any: ...
    _copy$default$11__T1 = typing.TypeVar('_copy$default$11__T1')  # <T1>
    _copy$default$11__T2 = typing.TypeVar('_copy$default$11__T2')  # <T2>
    _copy$default$11__T3 = typing.TypeVar('_copy$default$11__T3')  # <T3>
    _copy$default$11__T4 = typing.TypeVar('_copy$default$11__T4')  # <T4>
    _copy$default$11__T5 = typing.TypeVar('_copy$default$11__T5')  # <T5>
    _copy$default$11__T6 = typing.TypeVar('_copy$default$11__T6')  # <T6>
    _copy$default$11__T7 = typing.TypeVar('_copy$default$11__T7')  # <T7>
    _copy$default$11__T8 = typing.TypeVar('_copy$default$11__T8')  # <T8>
    _copy$default$11__T9 = typing.TypeVar('_copy$default$11__T9')  # <T9>
    _copy$default$11__T10 = typing.TypeVar('_copy$default$11__T10')  # <T10>
    _copy$default$11__T11 = typing.TypeVar('_copy$default$11__T11')  # <T11>
    _copy$default$11__T12 = typing.TypeVar('_copy$default$11__T12')  # <T12>
    _copy$default$11__T13 = typing.TypeVar('_copy$default$11__T13')  # <T13>
    _copy$default$11__T14 = typing.TypeVar('_copy$default$11__T14')  # <T14>
    _copy$default$11__T15 = typing.TypeVar('_copy$default$11__T15')  # <T15>
    _copy$default$11__T16 = typing.TypeVar('_copy$default$11__T16')  # <T16>
    _copy$default$11__T17 = typing.TypeVar('_copy$default$11__T17')  # <T17>
    _copy$default$11__T18 = typing.TypeVar('_copy$default$11__T18')  # <T18>
    _copy$default$11__T19 = typing.TypeVar('_copy$default$11__T19')  # <T19>
    _copy$default$11__T20 = typing.TypeVar('_copy$default$11__T20')  # <T20>
    _copy$default$11__T21 = typing.TypeVar('_copy$default$11__T21')  # <T21>
    def copy$default$11(self) -> typing.Any: ...
    _copy$default$12__T1 = typing.TypeVar('_copy$default$12__T1')  # <T1>
    _copy$default$12__T2 = typing.TypeVar('_copy$default$12__T2')  # <T2>
    _copy$default$12__T3 = typing.TypeVar('_copy$default$12__T3')  # <T3>
    _copy$default$12__T4 = typing.TypeVar('_copy$default$12__T4')  # <T4>
    _copy$default$12__T5 = typing.TypeVar('_copy$default$12__T5')  # <T5>
    _copy$default$12__T6 = typing.TypeVar('_copy$default$12__T6')  # <T6>
    _copy$default$12__T7 = typing.TypeVar('_copy$default$12__T7')  # <T7>
    _copy$default$12__T8 = typing.TypeVar('_copy$default$12__T8')  # <T8>
    _copy$default$12__T9 = typing.TypeVar('_copy$default$12__T9')  # <T9>
    _copy$default$12__T10 = typing.TypeVar('_copy$default$12__T10')  # <T10>
    _copy$default$12__T11 = typing.TypeVar('_copy$default$12__T11')  # <T11>
    _copy$default$12__T12 = typing.TypeVar('_copy$default$12__T12')  # <T12>
    _copy$default$12__T13 = typing.TypeVar('_copy$default$12__T13')  # <T13>
    _copy$default$12__T14 = typing.TypeVar('_copy$default$12__T14')  # <T14>
    _copy$default$12__T15 = typing.TypeVar('_copy$default$12__T15')  # <T15>
    _copy$default$12__T16 = typing.TypeVar('_copy$default$12__T16')  # <T16>
    _copy$default$12__T17 = typing.TypeVar('_copy$default$12__T17')  # <T17>
    _copy$default$12__T18 = typing.TypeVar('_copy$default$12__T18')  # <T18>
    _copy$default$12__T19 = typing.TypeVar('_copy$default$12__T19')  # <T19>
    _copy$default$12__T20 = typing.TypeVar('_copy$default$12__T20')  # <T20>
    _copy$default$12__T21 = typing.TypeVar('_copy$default$12__T21')  # <T21>
    def copy$default$12(self) -> typing.Any: ...
    _copy$default$13__T1 = typing.TypeVar('_copy$default$13__T1')  # <T1>
    _copy$default$13__T2 = typing.TypeVar('_copy$default$13__T2')  # <T2>
    _copy$default$13__T3 = typing.TypeVar('_copy$default$13__T3')  # <T3>
    _copy$default$13__T4 = typing.TypeVar('_copy$default$13__T4')  # <T4>
    _copy$default$13__T5 = typing.TypeVar('_copy$default$13__T5')  # <T5>
    _copy$default$13__T6 = typing.TypeVar('_copy$default$13__T6')  # <T6>
    _copy$default$13__T7 = typing.TypeVar('_copy$default$13__T7')  # <T7>
    _copy$default$13__T8 = typing.TypeVar('_copy$default$13__T8')  # <T8>
    _copy$default$13__T9 = typing.TypeVar('_copy$default$13__T9')  # <T9>
    _copy$default$13__T10 = typing.TypeVar('_copy$default$13__T10')  # <T10>
    _copy$default$13__T11 = typing.TypeVar('_copy$default$13__T11')  # <T11>
    _copy$default$13__T12 = typing.TypeVar('_copy$default$13__T12')  # <T12>
    _copy$default$13__T13 = typing.TypeVar('_copy$default$13__T13')  # <T13>
    _copy$default$13__T14 = typing.TypeVar('_copy$default$13__T14')  # <T14>
    _copy$default$13__T15 = typing.TypeVar('_copy$default$13__T15')  # <T15>
    _copy$default$13__T16 = typing.TypeVar('_copy$default$13__T16')  # <T16>
    _copy$default$13__T17 = typing.TypeVar('_copy$default$13__T17')  # <T17>
    _copy$default$13__T18 = typing.TypeVar('_copy$default$13__T18')  # <T18>
    _copy$default$13__T19 = typing.TypeVar('_copy$default$13__T19')  # <T19>
    _copy$default$13__T20 = typing.TypeVar('_copy$default$13__T20')  # <T20>
    _copy$default$13__T21 = typing.TypeVar('_copy$default$13__T21')  # <T21>
    def copy$default$13(self) -> typing.Any: ...
    _copy$default$14__T1 = typing.TypeVar('_copy$default$14__T1')  # <T1>
    _copy$default$14__T2 = typing.TypeVar('_copy$default$14__T2')  # <T2>
    _copy$default$14__T3 = typing.TypeVar('_copy$default$14__T3')  # <T3>
    _copy$default$14__T4 = typing.TypeVar('_copy$default$14__T4')  # <T4>
    _copy$default$14__T5 = typing.TypeVar('_copy$default$14__T5')  # <T5>
    _copy$default$14__T6 = typing.TypeVar('_copy$default$14__T6')  # <T6>
    _copy$default$14__T7 = typing.TypeVar('_copy$default$14__T7')  # <T7>
    _copy$default$14__T8 = typing.TypeVar('_copy$default$14__T8')  # <T8>
    _copy$default$14__T9 = typing.TypeVar('_copy$default$14__T9')  # <T9>
    _copy$default$14__T10 = typing.TypeVar('_copy$default$14__T10')  # <T10>
    _copy$default$14__T11 = typing.TypeVar('_copy$default$14__T11')  # <T11>
    _copy$default$14__T12 = typing.TypeVar('_copy$default$14__T12')  # <T12>
    _copy$default$14__T13 = typing.TypeVar('_copy$default$14__T13')  # <T13>
    _copy$default$14__T14 = typing.TypeVar('_copy$default$14__T14')  # <T14>
    _copy$default$14__T15 = typing.TypeVar('_copy$default$14__T15')  # <T15>
    _copy$default$14__T16 = typing.TypeVar('_copy$default$14__T16')  # <T16>
    _copy$default$14__T17 = typing.TypeVar('_copy$default$14__T17')  # <T17>
    _copy$default$14__T18 = typing.TypeVar('_copy$default$14__T18')  # <T18>
    _copy$default$14__T19 = typing.TypeVar('_copy$default$14__T19')  # <T19>
    _copy$default$14__T20 = typing.TypeVar('_copy$default$14__T20')  # <T20>
    _copy$default$14__T21 = typing.TypeVar('_copy$default$14__T21')  # <T21>
    def copy$default$14(self) -> typing.Any: ...
    _copy$default$15__T1 = typing.TypeVar('_copy$default$15__T1')  # <T1>
    _copy$default$15__T2 = typing.TypeVar('_copy$default$15__T2')  # <T2>
    _copy$default$15__T3 = typing.TypeVar('_copy$default$15__T3')  # <T3>
    _copy$default$15__T4 = typing.TypeVar('_copy$default$15__T4')  # <T4>
    _copy$default$15__T5 = typing.TypeVar('_copy$default$15__T5')  # <T5>
    _copy$default$15__T6 = typing.TypeVar('_copy$default$15__T6')  # <T6>
    _copy$default$15__T7 = typing.TypeVar('_copy$default$15__T7')  # <T7>
    _copy$default$15__T8 = typing.TypeVar('_copy$default$15__T8')  # <T8>
    _copy$default$15__T9 = typing.TypeVar('_copy$default$15__T9')  # <T9>
    _copy$default$15__T10 = typing.TypeVar('_copy$default$15__T10')  # <T10>
    _copy$default$15__T11 = typing.TypeVar('_copy$default$15__T11')  # <T11>
    _copy$default$15__T12 = typing.TypeVar('_copy$default$15__T12')  # <T12>
    _copy$default$15__T13 = typing.TypeVar('_copy$default$15__T13')  # <T13>
    _copy$default$15__T14 = typing.TypeVar('_copy$default$15__T14')  # <T14>
    _copy$default$15__T15 = typing.TypeVar('_copy$default$15__T15')  # <T15>
    _copy$default$15__T16 = typing.TypeVar('_copy$default$15__T16')  # <T16>
    _copy$default$15__T17 = typing.TypeVar('_copy$default$15__T17')  # <T17>
    _copy$default$15__T18 = typing.TypeVar('_copy$default$15__T18')  # <T18>
    _copy$default$15__T19 = typing.TypeVar('_copy$default$15__T19')  # <T19>
    _copy$default$15__T20 = typing.TypeVar('_copy$default$15__T20')  # <T20>
    _copy$default$15__T21 = typing.TypeVar('_copy$default$15__T21')  # <T21>
    def copy$default$15(self) -> typing.Any: ...
    _copy$default$16__T1 = typing.TypeVar('_copy$default$16__T1')  # <T1>
    _copy$default$16__T2 = typing.TypeVar('_copy$default$16__T2')  # <T2>
    _copy$default$16__T3 = typing.TypeVar('_copy$default$16__T3')  # <T3>
    _copy$default$16__T4 = typing.TypeVar('_copy$default$16__T4')  # <T4>
    _copy$default$16__T5 = typing.TypeVar('_copy$default$16__T5')  # <T5>
    _copy$default$16__T6 = typing.TypeVar('_copy$default$16__T6')  # <T6>
    _copy$default$16__T7 = typing.TypeVar('_copy$default$16__T7')  # <T7>
    _copy$default$16__T8 = typing.TypeVar('_copy$default$16__T8')  # <T8>
    _copy$default$16__T9 = typing.TypeVar('_copy$default$16__T9')  # <T9>
    _copy$default$16__T10 = typing.TypeVar('_copy$default$16__T10')  # <T10>
    _copy$default$16__T11 = typing.TypeVar('_copy$default$16__T11')  # <T11>
    _copy$default$16__T12 = typing.TypeVar('_copy$default$16__T12')  # <T12>
    _copy$default$16__T13 = typing.TypeVar('_copy$default$16__T13')  # <T13>
    _copy$default$16__T14 = typing.TypeVar('_copy$default$16__T14')  # <T14>
    _copy$default$16__T15 = typing.TypeVar('_copy$default$16__T15')  # <T15>
    _copy$default$16__T16 = typing.TypeVar('_copy$default$16__T16')  # <T16>
    _copy$default$16__T17 = typing.TypeVar('_copy$default$16__T17')  # <T17>
    _copy$default$16__T18 = typing.TypeVar('_copy$default$16__T18')  # <T18>
    _copy$default$16__T19 = typing.TypeVar('_copy$default$16__T19')  # <T19>
    _copy$default$16__T20 = typing.TypeVar('_copy$default$16__T20')  # <T20>
    _copy$default$16__T21 = typing.TypeVar('_copy$default$16__T21')  # <T21>
    def copy$default$16(self) -> typing.Any: ...
    _copy$default$17__T1 = typing.TypeVar('_copy$default$17__T1')  # <T1>
    _copy$default$17__T2 = typing.TypeVar('_copy$default$17__T2')  # <T2>
    _copy$default$17__T3 = typing.TypeVar('_copy$default$17__T3')  # <T3>
    _copy$default$17__T4 = typing.TypeVar('_copy$default$17__T4')  # <T4>
    _copy$default$17__T5 = typing.TypeVar('_copy$default$17__T5')  # <T5>
    _copy$default$17__T6 = typing.TypeVar('_copy$default$17__T6')  # <T6>
    _copy$default$17__T7 = typing.TypeVar('_copy$default$17__T7')  # <T7>
    _copy$default$17__T8 = typing.TypeVar('_copy$default$17__T8')  # <T8>
    _copy$default$17__T9 = typing.TypeVar('_copy$default$17__T9')  # <T9>
    _copy$default$17__T10 = typing.TypeVar('_copy$default$17__T10')  # <T10>
    _copy$default$17__T11 = typing.TypeVar('_copy$default$17__T11')  # <T11>
    _copy$default$17__T12 = typing.TypeVar('_copy$default$17__T12')  # <T12>
    _copy$default$17__T13 = typing.TypeVar('_copy$default$17__T13')  # <T13>
    _copy$default$17__T14 = typing.TypeVar('_copy$default$17__T14')  # <T14>
    _copy$default$17__T15 = typing.TypeVar('_copy$default$17__T15')  # <T15>
    _copy$default$17__T16 = typing.TypeVar('_copy$default$17__T16')  # <T16>
    _copy$default$17__T17 = typing.TypeVar('_copy$default$17__T17')  # <T17>
    _copy$default$17__T18 = typing.TypeVar('_copy$default$17__T18')  # <T18>
    _copy$default$17__T19 = typing.TypeVar('_copy$default$17__T19')  # <T19>
    _copy$default$17__T20 = typing.TypeVar('_copy$default$17__T20')  # <T20>
    _copy$default$17__T21 = typing.TypeVar('_copy$default$17__T21')  # <T21>
    def copy$default$17(self) -> typing.Any: ...
    _copy$default$18__T1 = typing.TypeVar('_copy$default$18__T1')  # <T1>
    _copy$default$18__T2 = typing.TypeVar('_copy$default$18__T2')  # <T2>
    _copy$default$18__T3 = typing.TypeVar('_copy$default$18__T3')  # <T3>
    _copy$default$18__T4 = typing.TypeVar('_copy$default$18__T4')  # <T4>
    _copy$default$18__T5 = typing.TypeVar('_copy$default$18__T5')  # <T5>
    _copy$default$18__T6 = typing.TypeVar('_copy$default$18__T6')  # <T6>
    _copy$default$18__T7 = typing.TypeVar('_copy$default$18__T7')  # <T7>
    _copy$default$18__T8 = typing.TypeVar('_copy$default$18__T8')  # <T8>
    _copy$default$18__T9 = typing.TypeVar('_copy$default$18__T9')  # <T9>
    _copy$default$18__T10 = typing.TypeVar('_copy$default$18__T10')  # <T10>
    _copy$default$18__T11 = typing.TypeVar('_copy$default$18__T11')  # <T11>
    _copy$default$18__T12 = typing.TypeVar('_copy$default$18__T12')  # <T12>
    _copy$default$18__T13 = typing.TypeVar('_copy$default$18__T13')  # <T13>
    _copy$default$18__T14 = typing.TypeVar('_copy$default$18__T14')  # <T14>
    _copy$default$18__T15 = typing.TypeVar('_copy$default$18__T15')  # <T15>
    _copy$default$18__T16 = typing.TypeVar('_copy$default$18__T16')  # <T16>
    _copy$default$18__T17 = typing.TypeVar('_copy$default$18__T17')  # <T17>
    _copy$default$18__T18 = typing.TypeVar('_copy$default$18__T18')  # <T18>
    _copy$default$18__T19 = typing.TypeVar('_copy$default$18__T19')  # <T19>
    _copy$default$18__T20 = typing.TypeVar('_copy$default$18__T20')  # <T20>
    _copy$default$18__T21 = typing.TypeVar('_copy$default$18__T21')  # <T21>
    def copy$default$18(self) -> typing.Any: ...
    _copy$default$19__T1 = typing.TypeVar('_copy$default$19__T1')  # <T1>
    _copy$default$19__T2 = typing.TypeVar('_copy$default$19__T2')  # <T2>
    _copy$default$19__T3 = typing.TypeVar('_copy$default$19__T3')  # <T3>
    _copy$default$19__T4 = typing.TypeVar('_copy$default$19__T4')  # <T4>
    _copy$default$19__T5 = typing.TypeVar('_copy$default$19__T5')  # <T5>
    _copy$default$19__T6 = typing.TypeVar('_copy$default$19__T6')  # <T6>
    _copy$default$19__T7 = typing.TypeVar('_copy$default$19__T7')  # <T7>
    _copy$default$19__T8 = typing.TypeVar('_copy$default$19__T8')  # <T8>
    _copy$default$19__T9 = typing.TypeVar('_copy$default$19__T9')  # <T9>
    _copy$default$19__T10 = typing.TypeVar('_copy$default$19__T10')  # <T10>
    _copy$default$19__T11 = typing.TypeVar('_copy$default$19__T11')  # <T11>
    _copy$default$19__T12 = typing.TypeVar('_copy$default$19__T12')  # <T12>
    _copy$default$19__T13 = typing.TypeVar('_copy$default$19__T13')  # <T13>
    _copy$default$19__T14 = typing.TypeVar('_copy$default$19__T14')  # <T14>
    _copy$default$19__T15 = typing.TypeVar('_copy$default$19__T15')  # <T15>
    _copy$default$19__T16 = typing.TypeVar('_copy$default$19__T16')  # <T16>
    _copy$default$19__T17 = typing.TypeVar('_copy$default$19__T17')  # <T17>
    _copy$default$19__T18 = typing.TypeVar('_copy$default$19__T18')  # <T18>
    _copy$default$19__T19 = typing.TypeVar('_copy$default$19__T19')  # <T19>
    _copy$default$19__T20 = typing.TypeVar('_copy$default$19__T20')  # <T20>
    _copy$default$19__T21 = typing.TypeVar('_copy$default$19__T21')  # <T21>
    def copy$default$19(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    _copy$default$2__T9 = typing.TypeVar('_copy$default$2__T9')  # <T9>
    _copy$default$2__T10 = typing.TypeVar('_copy$default$2__T10')  # <T10>
    _copy$default$2__T11 = typing.TypeVar('_copy$default$2__T11')  # <T11>
    _copy$default$2__T12 = typing.TypeVar('_copy$default$2__T12')  # <T12>
    _copy$default$2__T13 = typing.TypeVar('_copy$default$2__T13')  # <T13>
    _copy$default$2__T14 = typing.TypeVar('_copy$default$2__T14')  # <T14>
    _copy$default$2__T15 = typing.TypeVar('_copy$default$2__T15')  # <T15>
    _copy$default$2__T16 = typing.TypeVar('_copy$default$2__T16')  # <T16>
    _copy$default$2__T17 = typing.TypeVar('_copy$default$2__T17')  # <T17>
    _copy$default$2__T18 = typing.TypeVar('_copy$default$2__T18')  # <T18>
    _copy$default$2__T19 = typing.TypeVar('_copy$default$2__T19')  # <T19>
    _copy$default$2__T20 = typing.TypeVar('_copy$default$2__T20')  # <T20>
    _copy$default$2__T21 = typing.TypeVar('_copy$default$2__T21')  # <T21>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$20__T1 = typing.TypeVar('_copy$default$20__T1')  # <T1>
    _copy$default$20__T2 = typing.TypeVar('_copy$default$20__T2')  # <T2>
    _copy$default$20__T3 = typing.TypeVar('_copy$default$20__T3')  # <T3>
    _copy$default$20__T4 = typing.TypeVar('_copy$default$20__T4')  # <T4>
    _copy$default$20__T5 = typing.TypeVar('_copy$default$20__T5')  # <T5>
    _copy$default$20__T6 = typing.TypeVar('_copy$default$20__T6')  # <T6>
    _copy$default$20__T7 = typing.TypeVar('_copy$default$20__T7')  # <T7>
    _copy$default$20__T8 = typing.TypeVar('_copy$default$20__T8')  # <T8>
    _copy$default$20__T9 = typing.TypeVar('_copy$default$20__T9')  # <T9>
    _copy$default$20__T10 = typing.TypeVar('_copy$default$20__T10')  # <T10>
    _copy$default$20__T11 = typing.TypeVar('_copy$default$20__T11')  # <T11>
    _copy$default$20__T12 = typing.TypeVar('_copy$default$20__T12')  # <T12>
    _copy$default$20__T13 = typing.TypeVar('_copy$default$20__T13')  # <T13>
    _copy$default$20__T14 = typing.TypeVar('_copy$default$20__T14')  # <T14>
    _copy$default$20__T15 = typing.TypeVar('_copy$default$20__T15')  # <T15>
    _copy$default$20__T16 = typing.TypeVar('_copy$default$20__T16')  # <T16>
    _copy$default$20__T17 = typing.TypeVar('_copy$default$20__T17')  # <T17>
    _copy$default$20__T18 = typing.TypeVar('_copy$default$20__T18')  # <T18>
    _copy$default$20__T19 = typing.TypeVar('_copy$default$20__T19')  # <T19>
    _copy$default$20__T20 = typing.TypeVar('_copy$default$20__T20')  # <T20>
    _copy$default$20__T21 = typing.TypeVar('_copy$default$20__T21')  # <T21>
    def copy$default$20(self) -> typing.Any: ...
    _copy$default$21__T1 = typing.TypeVar('_copy$default$21__T1')  # <T1>
    _copy$default$21__T2 = typing.TypeVar('_copy$default$21__T2')  # <T2>
    _copy$default$21__T3 = typing.TypeVar('_copy$default$21__T3')  # <T3>
    _copy$default$21__T4 = typing.TypeVar('_copy$default$21__T4')  # <T4>
    _copy$default$21__T5 = typing.TypeVar('_copy$default$21__T5')  # <T5>
    _copy$default$21__T6 = typing.TypeVar('_copy$default$21__T6')  # <T6>
    _copy$default$21__T7 = typing.TypeVar('_copy$default$21__T7')  # <T7>
    _copy$default$21__T8 = typing.TypeVar('_copy$default$21__T8')  # <T8>
    _copy$default$21__T9 = typing.TypeVar('_copy$default$21__T9')  # <T9>
    _copy$default$21__T10 = typing.TypeVar('_copy$default$21__T10')  # <T10>
    _copy$default$21__T11 = typing.TypeVar('_copy$default$21__T11')  # <T11>
    _copy$default$21__T12 = typing.TypeVar('_copy$default$21__T12')  # <T12>
    _copy$default$21__T13 = typing.TypeVar('_copy$default$21__T13')  # <T13>
    _copy$default$21__T14 = typing.TypeVar('_copy$default$21__T14')  # <T14>
    _copy$default$21__T15 = typing.TypeVar('_copy$default$21__T15')  # <T15>
    _copy$default$21__T16 = typing.TypeVar('_copy$default$21__T16')  # <T16>
    _copy$default$21__T17 = typing.TypeVar('_copy$default$21__T17')  # <T17>
    _copy$default$21__T18 = typing.TypeVar('_copy$default$21__T18')  # <T18>
    _copy$default$21__T19 = typing.TypeVar('_copy$default$21__T19')  # <T19>
    _copy$default$21__T20 = typing.TypeVar('_copy$default$21__T20')  # <T20>
    _copy$default$21__T21 = typing.TypeVar('_copy$default$21__T21')  # <T21>
    def copy$default$21(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    _copy$default$3__T9 = typing.TypeVar('_copy$default$3__T9')  # <T9>
    _copy$default$3__T10 = typing.TypeVar('_copy$default$3__T10')  # <T10>
    _copy$default$3__T11 = typing.TypeVar('_copy$default$3__T11')  # <T11>
    _copy$default$3__T12 = typing.TypeVar('_copy$default$3__T12')  # <T12>
    _copy$default$3__T13 = typing.TypeVar('_copy$default$3__T13')  # <T13>
    _copy$default$3__T14 = typing.TypeVar('_copy$default$3__T14')  # <T14>
    _copy$default$3__T15 = typing.TypeVar('_copy$default$3__T15')  # <T15>
    _copy$default$3__T16 = typing.TypeVar('_copy$default$3__T16')  # <T16>
    _copy$default$3__T17 = typing.TypeVar('_copy$default$3__T17')  # <T17>
    _copy$default$3__T18 = typing.TypeVar('_copy$default$3__T18')  # <T18>
    _copy$default$3__T19 = typing.TypeVar('_copy$default$3__T19')  # <T19>
    _copy$default$3__T20 = typing.TypeVar('_copy$default$3__T20')  # <T20>
    _copy$default$3__T21 = typing.TypeVar('_copy$default$3__T21')  # <T21>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    _copy$default$4__T9 = typing.TypeVar('_copy$default$4__T9')  # <T9>
    _copy$default$4__T10 = typing.TypeVar('_copy$default$4__T10')  # <T10>
    _copy$default$4__T11 = typing.TypeVar('_copy$default$4__T11')  # <T11>
    _copy$default$4__T12 = typing.TypeVar('_copy$default$4__T12')  # <T12>
    _copy$default$4__T13 = typing.TypeVar('_copy$default$4__T13')  # <T13>
    _copy$default$4__T14 = typing.TypeVar('_copy$default$4__T14')  # <T14>
    _copy$default$4__T15 = typing.TypeVar('_copy$default$4__T15')  # <T15>
    _copy$default$4__T16 = typing.TypeVar('_copy$default$4__T16')  # <T16>
    _copy$default$4__T17 = typing.TypeVar('_copy$default$4__T17')  # <T17>
    _copy$default$4__T18 = typing.TypeVar('_copy$default$4__T18')  # <T18>
    _copy$default$4__T19 = typing.TypeVar('_copy$default$4__T19')  # <T19>
    _copy$default$4__T20 = typing.TypeVar('_copy$default$4__T20')  # <T20>
    _copy$default$4__T21 = typing.TypeVar('_copy$default$4__T21')  # <T21>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    _copy$default$5__T9 = typing.TypeVar('_copy$default$5__T9')  # <T9>
    _copy$default$5__T10 = typing.TypeVar('_copy$default$5__T10')  # <T10>
    _copy$default$5__T11 = typing.TypeVar('_copy$default$5__T11')  # <T11>
    _copy$default$5__T12 = typing.TypeVar('_copy$default$5__T12')  # <T12>
    _copy$default$5__T13 = typing.TypeVar('_copy$default$5__T13')  # <T13>
    _copy$default$5__T14 = typing.TypeVar('_copy$default$5__T14')  # <T14>
    _copy$default$5__T15 = typing.TypeVar('_copy$default$5__T15')  # <T15>
    _copy$default$5__T16 = typing.TypeVar('_copy$default$5__T16')  # <T16>
    _copy$default$5__T17 = typing.TypeVar('_copy$default$5__T17')  # <T17>
    _copy$default$5__T18 = typing.TypeVar('_copy$default$5__T18')  # <T18>
    _copy$default$5__T19 = typing.TypeVar('_copy$default$5__T19')  # <T19>
    _copy$default$5__T20 = typing.TypeVar('_copy$default$5__T20')  # <T20>
    _copy$default$5__T21 = typing.TypeVar('_copy$default$5__T21')  # <T21>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    _copy$default$6__T9 = typing.TypeVar('_copy$default$6__T9')  # <T9>
    _copy$default$6__T10 = typing.TypeVar('_copy$default$6__T10')  # <T10>
    _copy$default$6__T11 = typing.TypeVar('_copy$default$6__T11')  # <T11>
    _copy$default$6__T12 = typing.TypeVar('_copy$default$6__T12')  # <T12>
    _copy$default$6__T13 = typing.TypeVar('_copy$default$6__T13')  # <T13>
    _copy$default$6__T14 = typing.TypeVar('_copy$default$6__T14')  # <T14>
    _copy$default$6__T15 = typing.TypeVar('_copy$default$6__T15')  # <T15>
    _copy$default$6__T16 = typing.TypeVar('_copy$default$6__T16')  # <T16>
    _copy$default$6__T17 = typing.TypeVar('_copy$default$6__T17')  # <T17>
    _copy$default$6__T18 = typing.TypeVar('_copy$default$6__T18')  # <T18>
    _copy$default$6__T19 = typing.TypeVar('_copy$default$6__T19')  # <T19>
    _copy$default$6__T20 = typing.TypeVar('_copy$default$6__T20')  # <T20>
    _copy$default$6__T21 = typing.TypeVar('_copy$default$6__T21')  # <T21>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    _copy$default$7__T9 = typing.TypeVar('_copy$default$7__T9')  # <T9>
    _copy$default$7__T10 = typing.TypeVar('_copy$default$7__T10')  # <T10>
    _copy$default$7__T11 = typing.TypeVar('_copy$default$7__T11')  # <T11>
    _copy$default$7__T12 = typing.TypeVar('_copy$default$7__T12')  # <T12>
    _copy$default$7__T13 = typing.TypeVar('_copy$default$7__T13')  # <T13>
    _copy$default$7__T14 = typing.TypeVar('_copy$default$7__T14')  # <T14>
    _copy$default$7__T15 = typing.TypeVar('_copy$default$7__T15')  # <T15>
    _copy$default$7__T16 = typing.TypeVar('_copy$default$7__T16')  # <T16>
    _copy$default$7__T17 = typing.TypeVar('_copy$default$7__T17')  # <T17>
    _copy$default$7__T18 = typing.TypeVar('_copy$default$7__T18')  # <T18>
    _copy$default$7__T19 = typing.TypeVar('_copy$default$7__T19')  # <T19>
    _copy$default$7__T20 = typing.TypeVar('_copy$default$7__T20')  # <T20>
    _copy$default$7__T21 = typing.TypeVar('_copy$default$7__T21')  # <T21>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    _copy$default$8__T9 = typing.TypeVar('_copy$default$8__T9')  # <T9>
    _copy$default$8__T10 = typing.TypeVar('_copy$default$8__T10')  # <T10>
    _copy$default$8__T11 = typing.TypeVar('_copy$default$8__T11')  # <T11>
    _copy$default$8__T12 = typing.TypeVar('_copy$default$8__T12')  # <T12>
    _copy$default$8__T13 = typing.TypeVar('_copy$default$8__T13')  # <T13>
    _copy$default$8__T14 = typing.TypeVar('_copy$default$8__T14')  # <T14>
    _copy$default$8__T15 = typing.TypeVar('_copy$default$8__T15')  # <T15>
    _copy$default$8__T16 = typing.TypeVar('_copy$default$8__T16')  # <T16>
    _copy$default$8__T17 = typing.TypeVar('_copy$default$8__T17')  # <T17>
    _copy$default$8__T18 = typing.TypeVar('_copy$default$8__T18')  # <T18>
    _copy$default$8__T19 = typing.TypeVar('_copy$default$8__T19')  # <T19>
    _copy$default$8__T20 = typing.TypeVar('_copy$default$8__T20')  # <T20>
    _copy$default$8__T21 = typing.TypeVar('_copy$default$8__T21')  # <T21>
    def copy$default$8(self) -> typing.Any: ...
    _copy$default$9__T1 = typing.TypeVar('_copy$default$9__T1')  # <T1>
    _copy$default$9__T2 = typing.TypeVar('_copy$default$9__T2')  # <T2>
    _copy$default$9__T3 = typing.TypeVar('_copy$default$9__T3')  # <T3>
    _copy$default$9__T4 = typing.TypeVar('_copy$default$9__T4')  # <T4>
    _copy$default$9__T5 = typing.TypeVar('_copy$default$9__T5')  # <T5>
    _copy$default$9__T6 = typing.TypeVar('_copy$default$9__T6')  # <T6>
    _copy$default$9__T7 = typing.TypeVar('_copy$default$9__T7')  # <T7>
    _copy$default$9__T8 = typing.TypeVar('_copy$default$9__T8')  # <T8>
    _copy$default$9__T9 = typing.TypeVar('_copy$default$9__T9')  # <T9>
    _copy$default$9__T10 = typing.TypeVar('_copy$default$9__T10')  # <T10>
    _copy$default$9__T11 = typing.TypeVar('_copy$default$9__T11')  # <T11>
    _copy$default$9__T12 = typing.TypeVar('_copy$default$9__T12')  # <T12>
    _copy$default$9__T13 = typing.TypeVar('_copy$default$9__T13')  # <T13>
    _copy$default$9__T14 = typing.TypeVar('_copy$default$9__T14')  # <T14>
    _copy$default$9__T15 = typing.TypeVar('_copy$default$9__T15')  # <T15>
    _copy$default$9__T16 = typing.TypeVar('_copy$default$9__T16')  # <T16>
    _copy$default$9__T17 = typing.TypeVar('_copy$default$9__T17')  # <T17>
    _copy$default$9__T18 = typing.TypeVar('_copy$default$9__T18')  # <T18>
    _copy$default$9__T19 = typing.TypeVar('_copy$default$9__T19')  # <T19>
    _copy$default$9__T20 = typing.TypeVar('_copy$default$9__T20')  # <T20>
    _copy$default$9__T21 = typing.TypeVar('_copy$default$9__T21')  # <T21>
    def copy$default$9(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    _unapply__T16 = typing.TypeVar('_unapply__T16')  # <T16>
    _unapply__T17 = typing.TypeVar('_unapply__T17')  # <T17>
    _unapply__T18 = typing.TypeVar('_unapply__T18')  # <T18>
    _unapply__T19 = typing.TypeVar('_unapply__T19')  # <T19>
    _unapply__T20 = typing.TypeVar('_unapply__T20')  # <T20>
    _unapply__T21 = typing.TypeVar('_unapply__T21')  # <T21>
    @staticmethod
    def unapply(x$0: 'Tuple21'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19, _unapply__T20, _unapply__T21]) -> Option['Tuple21'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19, _unapply__T20, _unapply__T21]]: ...

_Tuple22__T1 = typing.TypeVar('_Tuple22__T1')  # <T1>
_Tuple22__T2 = typing.TypeVar('_Tuple22__T2')  # <T2>
_Tuple22__T3 = typing.TypeVar('_Tuple22__T3')  # <T3>
_Tuple22__T4 = typing.TypeVar('_Tuple22__T4')  # <T4>
_Tuple22__T5 = typing.TypeVar('_Tuple22__T5')  # <T5>
_Tuple22__T6 = typing.TypeVar('_Tuple22__T6')  # <T6>
_Tuple22__T7 = typing.TypeVar('_Tuple22__T7')  # <T7>
_Tuple22__T8 = typing.TypeVar('_Tuple22__T8')  # <T8>
_Tuple22__T9 = typing.TypeVar('_Tuple22__T9')  # <T9>
_Tuple22__T10 = typing.TypeVar('_Tuple22__T10')  # <T10>
_Tuple22__T11 = typing.TypeVar('_Tuple22__T11')  # <T11>
_Tuple22__T12 = typing.TypeVar('_Tuple22__T12')  # <T12>
_Tuple22__T13 = typing.TypeVar('_Tuple22__T13')  # <T13>
_Tuple22__T14 = typing.TypeVar('_Tuple22__T14')  # <T14>
_Tuple22__T15 = typing.TypeVar('_Tuple22__T15')  # <T15>
_Tuple22__T16 = typing.TypeVar('_Tuple22__T16')  # <T16>
_Tuple22__T17 = typing.TypeVar('_Tuple22__T17')  # <T17>
_Tuple22__T18 = typing.TypeVar('_Tuple22__T18')  # <T18>
_Tuple22__T19 = typing.TypeVar('_Tuple22__T19')  # <T19>
_Tuple22__T20 = typing.TypeVar('_Tuple22__T20')  # <T20>
_Tuple22__T21 = typing.TypeVar('_Tuple22__T21')  # <T21>
_Tuple22__T22 = typing.TypeVar('_Tuple22__T22')  # <T22>
class Tuple22(Product22[_Tuple22__T1, _Tuple22__T2, _Tuple22__T3, _Tuple22__T4, _Tuple22__T5, _Tuple22__T6, _Tuple22__T7, _Tuple22__T8, _Tuple22__T9, _Tuple22__T10, _Tuple22__T11, _Tuple22__T12, _Tuple22__T13, _Tuple22__T14, _Tuple22__T15, _Tuple22__T16, _Tuple22__T17, _Tuple22__T18, _Tuple22__T19, _Tuple22__T20, _Tuple22__T21, _Tuple22__T22], Serializable, typing.Generic[_Tuple22__T1, _Tuple22__T2, _Tuple22__T3, _Tuple22__T4, _Tuple22__T5, _Tuple22__T6, _Tuple22__T7, _Tuple22__T8, _Tuple22__T9, _Tuple22__T10, _Tuple22__T11, _Tuple22__T12, _Tuple22__T13, _Tuple22__T14, _Tuple22__T15, _Tuple22__T16, _Tuple22__T17, _Tuple22__T18, _Tuple22__T19, _Tuple22__T20, _Tuple22__T21, _Tuple22__T22]):
    def __init__(self, _1: _Tuple22__T1, _2: _Tuple22__T2, _3: _Tuple22__T3, _4: _Tuple22__T4, _5: _Tuple22__T5, _6: _Tuple22__T6, _7: _Tuple22__T7, _8: _Tuple22__T8, _9: _Tuple22__T9, _10: _Tuple22__T10, _11: _Tuple22__T11, _12: _Tuple22__T12, _13: _Tuple22__T13, _14: _Tuple22__T14, _15: _Tuple22__T15, _16: _Tuple22__T16, _17: _Tuple22__T17, _18: _Tuple22__T18, _19: _Tuple22__T19, _20: _Tuple22__T20, _21: _Tuple22__T21, _22: _Tuple22__T22): ...
    def _1(self) -> _Tuple22__T1: ...
    def _10(self) -> _Tuple22__T10: ...
    def _11(self) -> _Tuple22__T11: ...
    def _12(self) -> _Tuple22__T12: ...
    def _13(self) -> _Tuple22__T13: ...
    def _14(self) -> _Tuple22__T14: ...
    def _15(self) -> _Tuple22__T15: ...
    def _16(self) -> _Tuple22__T16: ...
    def _17(self) -> _Tuple22__T17: ...
    def _18(self) -> _Tuple22__T18: ...
    def _19(self) -> _Tuple22__T19: ...
    def _2(self) -> _Tuple22__T2: ...
    def _20(self) -> _Tuple22__T20: ...
    def _21(self) -> _Tuple22__T21: ...
    def _22(self) -> _Tuple22__T22: ...
    def _3(self) -> _Tuple22__T3: ...
    def _4(self) -> _Tuple22__T4: ...
    def _5(self) -> _Tuple22__T5: ...
    def _6(self) -> _Tuple22__T6: ...
    def _7(self) -> _Tuple22__T7: ...
    def _8(self) -> _Tuple22__T8: ...
    def _9(self) -> _Tuple22__T9: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    _apply__T9 = typing.TypeVar('_apply__T9')  # <T9>
    _apply__T10 = typing.TypeVar('_apply__T10')  # <T10>
    _apply__T11 = typing.TypeVar('_apply__T11')  # <T11>
    _apply__T12 = typing.TypeVar('_apply__T12')  # <T12>
    _apply__T13 = typing.TypeVar('_apply__T13')  # <T13>
    _apply__T14 = typing.TypeVar('_apply__T14')  # <T14>
    _apply__T15 = typing.TypeVar('_apply__T15')  # <T15>
    _apply__T16 = typing.TypeVar('_apply__T16')  # <T16>
    _apply__T17 = typing.TypeVar('_apply__T17')  # <T17>
    _apply__T18 = typing.TypeVar('_apply__T18')  # <T18>
    _apply__T19 = typing.TypeVar('_apply__T19')  # <T19>
    _apply__T20 = typing.TypeVar('_apply__T20')  # <T20>
    _apply__T21 = typing.TypeVar('_apply__T21')  # <T21>
    _apply__T22 = typing.TypeVar('_apply__T22')  # <T22>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8, _9: _apply__T9, _10: _apply__T10, _11: _apply__T11, _12: _apply__T12, _13: _apply__T13, _14: _apply__T14, _15: _apply__T15, _16: _apply__T16, _17: _apply__T17, _18: _apply__T18, _19: _apply__T19, _20: _apply__T20, _21: _apply__T21, _22: _apply__T22) -> 'Tuple22'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8, _apply__T9, _apply__T10, _apply__T11, _apply__T12, _apply__T13, _apply__T14, _apply__T15, _apply__T16, _apply__T17, _apply__T18, _apply__T19, _apply__T20, _apply__T21, _apply__T22]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    _copy__T9 = typing.TypeVar('_copy__T9')  # <T9>
    _copy__T10 = typing.TypeVar('_copy__T10')  # <T10>
    _copy__T11 = typing.TypeVar('_copy__T11')  # <T11>
    _copy__T12 = typing.TypeVar('_copy__T12')  # <T12>
    _copy__T13 = typing.TypeVar('_copy__T13')  # <T13>
    _copy__T14 = typing.TypeVar('_copy__T14')  # <T14>
    _copy__T15 = typing.TypeVar('_copy__T15')  # <T15>
    _copy__T16 = typing.TypeVar('_copy__T16')  # <T16>
    _copy__T17 = typing.TypeVar('_copy__T17')  # <T17>
    _copy__T18 = typing.TypeVar('_copy__T18')  # <T18>
    _copy__T19 = typing.TypeVar('_copy__T19')  # <T19>
    _copy__T20 = typing.TypeVar('_copy__T20')  # <T20>
    _copy__T21 = typing.TypeVar('_copy__T21')  # <T21>
    _copy__T22 = typing.TypeVar('_copy__T22')  # <T22>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any, _9: typing.Any, _10: typing.Any, _11: typing.Any, _12: typing.Any, _13: typing.Any, _14: typing.Any, _15: typing.Any, _16: typing.Any, _17: typing.Any, _18: typing.Any, _19: typing.Any, _20: typing.Any, _21: typing.Any, _22: typing.Any) -> 'Tuple22'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    _copy$default$1__T9 = typing.TypeVar('_copy$default$1__T9')  # <T9>
    _copy$default$1__T10 = typing.TypeVar('_copy$default$1__T10')  # <T10>
    _copy$default$1__T11 = typing.TypeVar('_copy$default$1__T11')  # <T11>
    _copy$default$1__T12 = typing.TypeVar('_copy$default$1__T12')  # <T12>
    _copy$default$1__T13 = typing.TypeVar('_copy$default$1__T13')  # <T13>
    _copy$default$1__T14 = typing.TypeVar('_copy$default$1__T14')  # <T14>
    _copy$default$1__T15 = typing.TypeVar('_copy$default$1__T15')  # <T15>
    _copy$default$1__T16 = typing.TypeVar('_copy$default$1__T16')  # <T16>
    _copy$default$1__T17 = typing.TypeVar('_copy$default$1__T17')  # <T17>
    _copy$default$1__T18 = typing.TypeVar('_copy$default$1__T18')  # <T18>
    _copy$default$1__T19 = typing.TypeVar('_copy$default$1__T19')  # <T19>
    _copy$default$1__T20 = typing.TypeVar('_copy$default$1__T20')  # <T20>
    _copy$default$1__T21 = typing.TypeVar('_copy$default$1__T21')  # <T21>
    _copy$default$1__T22 = typing.TypeVar('_copy$default$1__T22')  # <T22>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$10__T1 = typing.TypeVar('_copy$default$10__T1')  # <T1>
    _copy$default$10__T2 = typing.TypeVar('_copy$default$10__T2')  # <T2>
    _copy$default$10__T3 = typing.TypeVar('_copy$default$10__T3')  # <T3>
    _copy$default$10__T4 = typing.TypeVar('_copy$default$10__T4')  # <T4>
    _copy$default$10__T5 = typing.TypeVar('_copy$default$10__T5')  # <T5>
    _copy$default$10__T6 = typing.TypeVar('_copy$default$10__T6')  # <T6>
    _copy$default$10__T7 = typing.TypeVar('_copy$default$10__T7')  # <T7>
    _copy$default$10__T8 = typing.TypeVar('_copy$default$10__T8')  # <T8>
    _copy$default$10__T9 = typing.TypeVar('_copy$default$10__T9')  # <T9>
    _copy$default$10__T10 = typing.TypeVar('_copy$default$10__T10')  # <T10>
    _copy$default$10__T11 = typing.TypeVar('_copy$default$10__T11')  # <T11>
    _copy$default$10__T12 = typing.TypeVar('_copy$default$10__T12')  # <T12>
    _copy$default$10__T13 = typing.TypeVar('_copy$default$10__T13')  # <T13>
    _copy$default$10__T14 = typing.TypeVar('_copy$default$10__T14')  # <T14>
    _copy$default$10__T15 = typing.TypeVar('_copy$default$10__T15')  # <T15>
    _copy$default$10__T16 = typing.TypeVar('_copy$default$10__T16')  # <T16>
    _copy$default$10__T17 = typing.TypeVar('_copy$default$10__T17')  # <T17>
    _copy$default$10__T18 = typing.TypeVar('_copy$default$10__T18')  # <T18>
    _copy$default$10__T19 = typing.TypeVar('_copy$default$10__T19')  # <T19>
    _copy$default$10__T20 = typing.TypeVar('_copy$default$10__T20')  # <T20>
    _copy$default$10__T21 = typing.TypeVar('_copy$default$10__T21')  # <T21>
    _copy$default$10__T22 = typing.TypeVar('_copy$default$10__T22')  # <T22>
    def copy$default$10(self) -> typing.Any: ...
    _copy$default$11__T1 = typing.TypeVar('_copy$default$11__T1')  # <T1>
    _copy$default$11__T2 = typing.TypeVar('_copy$default$11__T2')  # <T2>
    _copy$default$11__T3 = typing.TypeVar('_copy$default$11__T3')  # <T3>
    _copy$default$11__T4 = typing.TypeVar('_copy$default$11__T4')  # <T4>
    _copy$default$11__T5 = typing.TypeVar('_copy$default$11__T5')  # <T5>
    _copy$default$11__T6 = typing.TypeVar('_copy$default$11__T6')  # <T6>
    _copy$default$11__T7 = typing.TypeVar('_copy$default$11__T7')  # <T7>
    _copy$default$11__T8 = typing.TypeVar('_copy$default$11__T8')  # <T8>
    _copy$default$11__T9 = typing.TypeVar('_copy$default$11__T9')  # <T9>
    _copy$default$11__T10 = typing.TypeVar('_copy$default$11__T10')  # <T10>
    _copy$default$11__T11 = typing.TypeVar('_copy$default$11__T11')  # <T11>
    _copy$default$11__T12 = typing.TypeVar('_copy$default$11__T12')  # <T12>
    _copy$default$11__T13 = typing.TypeVar('_copy$default$11__T13')  # <T13>
    _copy$default$11__T14 = typing.TypeVar('_copy$default$11__T14')  # <T14>
    _copy$default$11__T15 = typing.TypeVar('_copy$default$11__T15')  # <T15>
    _copy$default$11__T16 = typing.TypeVar('_copy$default$11__T16')  # <T16>
    _copy$default$11__T17 = typing.TypeVar('_copy$default$11__T17')  # <T17>
    _copy$default$11__T18 = typing.TypeVar('_copy$default$11__T18')  # <T18>
    _copy$default$11__T19 = typing.TypeVar('_copy$default$11__T19')  # <T19>
    _copy$default$11__T20 = typing.TypeVar('_copy$default$11__T20')  # <T20>
    _copy$default$11__T21 = typing.TypeVar('_copy$default$11__T21')  # <T21>
    _copy$default$11__T22 = typing.TypeVar('_copy$default$11__T22')  # <T22>
    def copy$default$11(self) -> typing.Any: ...
    _copy$default$12__T1 = typing.TypeVar('_copy$default$12__T1')  # <T1>
    _copy$default$12__T2 = typing.TypeVar('_copy$default$12__T2')  # <T2>
    _copy$default$12__T3 = typing.TypeVar('_copy$default$12__T3')  # <T3>
    _copy$default$12__T4 = typing.TypeVar('_copy$default$12__T4')  # <T4>
    _copy$default$12__T5 = typing.TypeVar('_copy$default$12__T5')  # <T5>
    _copy$default$12__T6 = typing.TypeVar('_copy$default$12__T6')  # <T6>
    _copy$default$12__T7 = typing.TypeVar('_copy$default$12__T7')  # <T7>
    _copy$default$12__T8 = typing.TypeVar('_copy$default$12__T8')  # <T8>
    _copy$default$12__T9 = typing.TypeVar('_copy$default$12__T9')  # <T9>
    _copy$default$12__T10 = typing.TypeVar('_copy$default$12__T10')  # <T10>
    _copy$default$12__T11 = typing.TypeVar('_copy$default$12__T11')  # <T11>
    _copy$default$12__T12 = typing.TypeVar('_copy$default$12__T12')  # <T12>
    _copy$default$12__T13 = typing.TypeVar('_copy$default$12__T13')  # <T13>
    _copy$default$12__T14 = typing.TypeVar('_copy$default$12__T14')  # <T14>
    _copy$default$12__T15 = typing.TypeVar('_copy$default$12__T15')  # <T15>
    _copy$default$12__T16 = typing.TypeVar('_copy$default$12__T16')  # <T16>
    _copy$default$12__T17 = typing.TypeVar('_copy$default$12__T17')  # <T17>
    _copy$default$12__T18 = typing.TypeVar('_copy$default$12__T18')  # <T18>
    _copy$default$12__T19 = typing.TypeVar('_copy$default$12__T19')  # <T19>
    _copy$default$12__T20 = typing.TypeVar('_copy$default$12__T20')  # <T20>
    _copy$default$12__T21 = typing.TypeVar('_copy$default$12__T21')  # <T21>
    _copy$default$12__T22 = typing.TypeVar('_copy$default$12__T22')  # <T22>
    def copy$default$12(self) -> typing.Any: ...
    _copy$default$13__T1 = typing.TypeVar('_copy$default$13__T1')  # <T1>
    _copy$default$13__T2 = typing.TypeVar('_copy$default$13__T2')  # <T2>
    _copy$default$13__T3 = typing.TypeVar('_copy$default$13__T3')  # <T3>
    _copy$default$13__T4 = typing.TypeVar('_copy$default$13__T4')  # <T4>
    _copy$default$13__T5 = typing.TypeVar('_copy$default$13__T5')  # <T5>
    _copy$default$13__T6 = typing.TypeVar('_copy$default$13__T6')  # <T6>
    _copy$default$13__T7 = typing.TypeVar('_copy$default$13__T7')  # <T7>
    _copy$default$13__T8 = typing.TypeVar('_copy$default$13__T8')  # <T8>
    _copy$default$13__T9 = typing.TypeVar('_copy$default$13__T9')  # <T9>
    _copy$default$13__T10 = typing.TypeVar('_copy$default$13__T10')  # <T10>
    _copy$default$13__T11 = typing.TypeVar('_copy$default$13__T11')  # <T11>
    _copy$default$13__T12 = typing.TypeVar('_copy$default$13__T12')  # <T12>
    _copy$default$13__T13 = typing.TypeVar('_copy$default$13__T13')  # <T13>
    _copy$default$13__T14 = typing.TypeVar('_copy$default$13__T14')  # <T14>
    _copy$default$13__T15 = typing.TypeVar('_copy$default$13__T15')  # <T15>
    _copy$default$13__T16 = typing.TypeVar('_copy$default$13__T16')  # <T16>
    _copy$default$13__T17 = typing.TypeVar('_copy$default$13__T17')  # <T17>
    _copy$default$13__T18 = typing.TypeVar('_copy$default$13__T18')  # <T18>
    _copy$default$13__T19 = typing.TypeVar('_copy$default$13__T19')  # <T19>
    _copy$default$13__T20 = typing.TypeVar('_copy$default$13__T20')  # <T20>
    _copy$default$13__T21 = typing.TypeVar('_copy$default$13__T21')  # <T21>
    _copy$default$13__T22 = typing.TypeVar('_copy$default$13__T22')  # <T22>
    def copy$default$13(self) -> typing.Any: ...
    _copy$default$14__T1 = typing.TypeVar('_copy$default$14__T1')  # <T1>
    _copy$default$14__T2 = typing.TypeVar('_copy$default$14__T2')  # <T2>
    _copy$default$14__T3 = typing.TypeVar('_copy$default$14__T3')  # <T3>
    _copy$default$14__T4 = typing.TypeVar('_copy$default$14__T4')  # <T4>
    _copy$default$14__T5 = typing.TypeVar('_copy$default$14__T5')  # <T5>
    _copy$default$14__T6 = typing.TypeVar('_copy$default$14__T6')  # <T6>
    _copy$default$14__T7 = typing.TypeVar('_copy$default$14__T7')  # <T7>
    _copy$default$14__T8 = typing.TypeVar('_copy$default$14__T8')  # <T8>
    _copy$default$14__T9 = typing.TypeVar('_copy$default$14__T9')  # <T9>
    _copy$default$14__T10 = typing.TypeVar('_copy$default$14__T10')  # <T10>
    _copy$default$14__T11 = typing.TypeVar('_copy$default$14__T11')  # <T11>
    _copy$default$14__T12 = typing.TypeVar('_copy$default$14__T12')  # <T12>
    _copy$default$14__T13 = typing.TypeVar('_copy$default$14__T13')  # <T13>
    _copy$default$14__T14 = typing.TypeVar('_copy$default$14__T14')  # <T14>
    _copy$default$14__T15 = typing.TypeVar('_copy$default$14__T15')  # <T15>
    _copy$default$14__T16 = typing.TypeVar('_copy$default$14__T16')  # <T16>
    _copy$default$14__T17 = typing.TypeVar('_copy$default$14__T17')  # <T17>
    _copy$default$14__T18 = typing.TypeVar('_copy$default$14__T18')  # <T18>
    _copy$default$14__T19 = typing.TypeVar('_copy$default$14__T19')  # <T19>
    _copy$default$14__T20 = typing.TypeVar('_copy$default$14__T20')  # <T20>
    _copy$default$14__T21 = typing.TypeVar('_copy$default$14__T21')  # <T21>
    _copy$default$14__T22 = typing.TypeVar('_copy$default$14__T22')  # <T22>
    def copy$default$14(self) -> typing.Any: ...
    _copy$default$15__T1 = typing.TypeVar('_copy$default$15__T1')  # <T1>
    _copy$default$15__T2 = typing.TypeVar('_copy$default$15__T2')  # <T2>
    _copy$default$15__T3 = typing.TypeVar('_copy$default$15__T3')  # <T3>
    _copy$default$15__T4 = typing.TypeVar('_copy$default$15__T4')  # <T4>
    _copy$default$15__T5 = typing.TypeVar('_copy$default$15__T5')  # <T5>
    _copy$default$15__T6 = typing.TypeVar('_copy$default$15__T6')  # <T6>
    _copy$default$15__T7 = typing.TypeVar('_copy$default$15__T7')  # <T7>
    _copy$default$15__T8 = typing.TypeVar('_copy$default$15__T8')  # <T8>
    _copy$default$15__T9 = typing.TypeVar('_copy$default$15__T9')  # <T9>
    _copy$default$15__T10 = typing.TypeVar('_copy$default$15__T10')  # <T10>
    _copy$default$15__T11 = typing.TypeVar('_copy$default$15__T11')  # <T11>
    _copy$default$15__T12 = typing.TypeVar('_copy$default$15__T12')  # <T12>
    _copy$default$15__T13 = typing.TypeVar('_copy$default$15__T13')  # <T13>
    _copy$default$15__T14 = typing.TypeVar('_copy$default$15__T14')  # <T14>
    _copy$default$15__T15 = typing.TypeVar('_copy$default$15__T15')  # <T15>
    _copy$default$15__T16 = typing.TypeVar('_copy$default$15__T16')  # <T16>
    _copy$default$15__T17 = typing.TypeVar('_copy$default$15__T17')  # <T17>
    _copy$default$15__T18 = typing.TypeVar('_copy$default$15__T18')  # <T18>
    _copy$default$15__T19 = typing.TypeVar('_copy$default$15__T19')  # <T19>
    _copy$default$15__T20 = typing.TypeVar('_copy$default$15__T20')  # <T20>
    _copy$default$15__T21 = typing.TypeVar('_copy$default$15__T21')  # <T21>
    _copy$default$15__T22 = typing.TypeVar('_copy$default$15__T22')  # <T22>
    def copy$default$15(self) -> typing.Any: ...
    _copy$default$16__T1 = typing.TypeVar('_copy$default$16__T1')  # <T1>
    _copy$default$16__T2 = typing.TypeVar('_copy$default$16__T2')  # <T2>
    _copy$default$16__T3 = typing.TypeVar('_copy$default$16__T3')  # <T3>
    _copy$default$16__T4 = typing.TypeVar('_copy$default$16__T4')  # <T4>
    _copy$default$16__T5 = typing.TypeVar('_copy$default$16__T5')  # <T5>
    _copy$default$16__T6 = typing.TypeVar('_copy$default$16__T6')  # <T6>
    _copy$default$16__T7 = typing.TypeVar('_copy$default$16__T7')  # <T7>
    _copy$default$16__T8 = typing.TypeVar('_copy$default$16__T8')  # <T8>
    _copy$default$16__T9 = typing.TypeVar('_copy$default$16__T9')  # <T9>
    _copy$default$16__T10 = typing.TypeVar('_copy$default$16__T10')  # <T10>
    _copy$default$16__T11 = typing.TypeVar('_copy$default$16__T11')  # <T11>
    _copy$default$16__T12 = typing.TypeVar('_copy$default$16__T12')  # <T12>
    _copy$default$16__T13 = typing.TypeVar('_copy$default$16__T13')  # <T13>
    _copy$default$16__T14 = typing.TypeVar('_copy$default$16__T14')  # <T14>
    _copy$default$16__T15 = typing.TypeVar('_copy$default$16__T15')  # <T15>
    _copy$default$16__T16 = typing.TypeVar('_copy$default$16__T16')  # <T16>
    _copy$default$16__T17 = typing.TypeVar('_copy$default$16__T17')  # <T17>
    _copy$default$16__T18 = typing.TypeVar('_copy$default$16__T18')  # <T18>
    _copy$default$16__T19 = typing.TypeVar('_copy$default$16__T19')  # <T19>
    _copy$default$16__T20 = typing.TypeVar('_copy$default$16__T20')  # <T20>
    _copy$default$16__T21 = typing.TypeVar('_copy$default$16__T21')  # <T21>
    _copy$default$16__T22 = typing.TypeVar('_copy$default$16__T22')  # <T22>
    def copy$default$16(self) -> typing.Any: ...
    _copy$default$17__T1 = typing.TypeVar('_copy$default$17__T1')  # <T1>
    _copy$default$17__T2 = typing.TypeVar('_copy$default$17__T2')  # <T2>
    _copy$default$17__T3 = typing.TypeVar('_copy$default$17__T3')  # <T3>
    _copy$default$17__T4 = typing.TypeVar('_copy$default$17__T4')  # <T4>
    _copy$default$17__T5 = typing.TypeVar('_copy$default$17__T5')  # <T5>
    _copy$default$17__T6 = typing.TypeVar('_copy$default$17__T6')  # <T6>
    _copy$default$17__T7 = typing.TypeVar('_copy$default$17__T7')  # <T7>
    _copy$default$17__T8 = typing.TypeVar('_copy$default$17__T8')  # <T8>
    _copy$default$17__T9 = typing.TypeVar('_copy$default$17__T9')  # <T9>
    _copy$default$17__T10 = typing.TypeVar('_copy$default$17__T10')  # <T10>
    _copy$default$17__T11 = typing.TypeVar('_copy$default$17__T11')  # <T11>
    _copy$default$17__T12 = typing.TypeVar('_copy$default$17__T12')  # <T12>
    _copy$default$17__T13 = typing.TypeVar('_copy$default$17__T13')  # <T13>
    _copy$default$17__T14 = typing.TypeVar('_copy$default$17__T14')  # <T14>
    _copy$default$17__T15 = typing.TypeVar('_copy$default$17__T15')  # <T15>
    _copy$default$17__T16 = typing.TypeVar('_copy$default$17__T16')  # <T16>
    _copy$default$17__T17 = typing.TypeVar('_copy$default$17__T17')  # <T17>
    _copy$default$17__T18 = typing.TypeVar('_copy$default$17__T18')  # <T18>
    _copy$default$17__T19 = typing.TypeVar('_copy$default$17__T19')  # <T19>
    _copy$default$17__T20 = typing.TypeVar('_copy$default$17__T20')  # <T20>
    _copy$default$17__T21 = typing.TypeVar('_copy$default$17__T21')  # <T21>
    _copy$default$17__T22 = typing.TypeVar('_copy$default$17__T22')  # <T22>
    def copy$default$17(self) -> typing.Any: ...
    _copy$default$18__T1 = typing.TypeVar('_copy$default$18__T1')  # <T1>
    _copy$default$18__T2 = typing.TypeVar('_copy$default$18__T2')  # <T2>
    _copy$default$18__T3 = typing.TypeVar('_copy$default$18__T3')  # <T3>
    _copy$default$18__T4 = typing.TypeVar('_copy$default$18__T4')  # <T4>
    _copy$default$18__T5 = typing.TypeVar('_copy$default$18__T5')  # <T5>
    _copy$default$18__T6 = typing.TypeVar('_copy$default$18__T6')  # <T6>
    _copy$default$18__T7 = typing.TypeVar('_copy$default$18__T7')  # <T7>
    _copy$default$18__T8 = typing.TypeVar('_copy$default$18__T8')  # <T8>
    _copy$default$18__T9 = typing.TypeVar('_copy$default$18__T9')  # <T9>
    _copy$default$18__T10 = typing.TypeVar('_copy$default$18__T10')  # <T10>
    _copy$default$18__T11 = typing.TypeVar('_copy$default$18__T11')  # <T11>
    _copy$default$18__T12 = typing.TypeVar('_copy$default$18__T12')  # <T12>
    _copy$default$18__T13 = typing.TypeVar('_copy$default$18__T13')  # <T13>
    _copy$default$18__T14 = typing.TypeVar('_copy$default$18__T14')  # <T14>
    _copy$default$18__T15 = typing.TypeVar('_copy$default$18__T15')  # <T15>
    _copy$default$18__T16 = typing.TypeVar('_copy$default$18__T16')  # <T16>
    _copy$default$18__T17 = typing.TypeVar('_copy$default$18__T17')  # <T17>
    _copy$default$18__T18 = typing.TypeVar('_copy$default$18__T18')  # <T18>
    _copy$default$18__T19 = typing.TypeVar('_copy$default$18__T19')  # <T19>
    _copy$default$18__T20 = typing.TypeVar('_copy$default$18__T20')  # <T20>
    _copy$default$18__T21 = typing.TypeVar('_copy$default$18__T21')  # <T21>
    _copy$default$18__T22 = typing.TypeVar('_copy$default$18__T22')  # <T22>
    def copy$default$18(self) -> typing.Any: ...
    _copy$default$19__T1 = typing.TypeVar('_copy$default$19__T1')  # <T1>
    _copy$default$19__T2 = typing.TypeVar('_copy$default$19__T2')  # <T2>
    _copy$default$19__T3 = typing.TypeVar('_copy$default$19__T3')  # <T3>
    _copy$default$19__T4 = typing.TypeVar('_copy$default$19__T4')  # <T4>
    _copy$default$19__T5 = typing.TypeVar('_copy$default$19__T5')  # <T5>
    _copy$default$19__T6 = typing.TypeVar('_copy$default$19__T6')  # <T6>
    _copy$default$19__T7 = typing.TypeVar('_copy$default$19__T7')  # <T7>
    _copy$default$19__T8 = typing.TypeVar('_copy$default$19__T8')  # <T8>
    _copy$default$19__T9 = typing.TypeVar('_copy$default$19__T9')  # <T9>
    _copy$default$19__T10 = typing.TypeVar('_copy$default$19__T10')  # <T10>
    _copy$default$19__T11 = typing.TypeVar('_copy$default$19__T11')  # <T11>
    _copy$default$19__T12 = typing.TypeVar('_copy$default$19__T12')  # <T12>
    _copy$default$19__T13 = typing.TypeVar('_copy$default$19__T13')  # <T13>
    _copy$default$19__T14 = typing.TypeVar('_copy$default$19__T14')  # <T14>
    _copy$default$19__T15 = typing.TypeVar('_copy$default$19__T15')  # <T15>
    _copy$default$19__T16 = typing.TypeVar('_copy$default$19__T16')  # <T16>
    _copy$default$19__T17 = typing.TypeVar('_copy$default$19__T17')  # <T17>
    _copy$default$19__T18 = typing.TypeVar('_copy$default$19__T18')  # <T18>
    _copy$default$19__T19 = typing.TypeVar('_copy$default$19__T19')  # <T19>
    _copy$default$19__T20 = typing.TypeVar('_copy$default$19__T20')  # <T20>
    _copy$default$19__T21 = typing.TypeVar('_copy$default$19__T21')  # <T21>
    _copy$default$19__T22 = typing.TypeVar('_copy$default$19__T22')  # <T22>
    def copy$default$19(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    _copy$default$2__T9 = typing.TypeVar('_copy$default$2__T9')  # <T9>
    _copy$default$2__T10 = typing.TypeVar('_copy$default$2__T10')  # <T10>
    _copy$default$2__T11 = typing.TypeVar('_copy$default$2__T11')  # <T11>
    _copy$default$2__T12 = typing.TypeVar('_copy$default$2__T12')  # <T12>
    _copy$default$2__T13 = typing.TypeVar('_copy$default$2__T13')  # <T13>
    _copy$default$2__T14 = typing.TypeVar('_copy$default$2__T14')  # <T14>
    _copy$default$2__T15 = typing.TypeVar('_copy$default$2__T15')  # <T15>
    _copy$default$2__T16 = typing.TypeVar('_copy$default$2__T16')  # <T16>
    _copy$default$2__T17 = typing.TypeVar('_copy$default$2__T17')  # <T17>
    _copy$default$2__T18 = typing.TypeVar('_copy$default$2__T18')  # <T18>
    _copy$default$2__T19 = typing.TypeVar('_copy$default$2__T19')  # <T19>
    _copy$default$2__T20 = typing.TypeVar('_copy$default$2__T20')  # <T20>
    _copy$default$2__T21 = typing.TypeVar('_copy$default$2__T21')  # <T21>
    _copy$default$2__T22 = typing.TypeVar('_copy$default$2__T22')  # <T22>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$20__T1 = typing.TypeVar('_copy$default$20__T1')  # <T1>
    _copy$default$20__T2 = typing.TypeVar('_copy$default$20__T2')  # <T2>
    _copy$default$20__T3 = typing.TypeVar('_copy$default$20__T3')  # <T3>
    _copy$default$20__T4 = typing.TypeVar('_copy$default$20__T4')  # <T4>
    _copy$default$20__T5 = typing.TypeVar('_copy$default$20__T5')  # <T5>
    _copy$default$20__T6 = typing.TypeVar('_copy$default$20__T6')  # <T6>
    _copy$default$20__T7 = typing.TypeVar('_copy$default$20__T7')  # <T7>
    _copy$default$20__T8 = typing.TypeVar('_copy$default$20__T8')  # <T8>
    _copy$default$20__T9 = typing.TypeVar('_copy$default$20__T9')  # <T9>
    _copy$default$20__T10 = typing.TypeVar('_copy$default$20__T10')  # <T10>
    _copy$default$20__T11 = typing.TypeVar('_copy$default$20__T11')  # <T11>
    _copy$default$20__T12 = typing.TypeVar('_copy$default$20__T12')  # <T12>
    _copy$default$20__T13 = typing.TypeVar('_copy$default$20__T13')  # <T13>
    _copy$default$20__T14 = typing.TypeVar('_copy$default$20__T14')  # <T14>
    _copy$default$20__T15 = typing.TypeVar('_copy$default$20__T15')  # <T15>
    _copy$default$20__T16 = typing.TypeVar('_copy$default$20__T16')  # <T16>
    _copy$default$20__T17 = typing.TypeVar('_copy$default$20__T17')  # <T17>
    _copy$default$20__T18 = typing.TypeVar('_copy$default$20__T18')  # <T18>
    _copy$default$20__T19 = typing.TypeVar('_copy$default$20__T19')  # <T19>
    _copy$default$20__T20 = typing.TypeVar('_copy$default$20__T20')  # <T20>
    _copy$default$20__T21 = typing.TypeVar('_copy$default$20__T21')  # <T21>
    _copy$default$20__T22 = typing.TypeVar('_copy$default$20__T22')  # <T22>
    def copy$default$20(self) -> typing.Any: ...
    _copy$default$21__T1 = typing.TypeVar('_copy$default$21__T1')  # <T1>
    _copy$default$21__T2 = typing.TypeVar('_copy$default$21__T2')  # <T2>
    _copy$default$21__T3 = typing.TypeVar('_copy$default$21__T3')  # <T3>
    _copy$default$21__T4 = typing.TypeVar('_copy$default$21__T4')  # <T4>
    _copy$default$21__T5 = typing.TypeVar('_copy$default$21__T5')  # <T5>
    _copy$default$21__T6 = typing.TypeVar('_copy$default$21__T6')  # <T6>
    _copy$default$21__T7 = typing.TypeVar('_copy$default$21__T7')  # <T7>
    _copy$default$21__T8 = typing.TypeVar('_copy$default$21__T8')  # <T8>
    _copy$default$21__T9 = typing.TypeVar('_copy$default$21__T9')  # <T9>
    _copy$default$21__T10 = typing.TypeVar('_copy$default$21__T10')  # <T10>
    _copy$default$21__T11 = typing.TypeVar('_copy$default$21__T11')  # <T11>
    _copy$default$21__T12 = typing.TypeVar('_copy$default$21__T12')  # <T12>
    _copy$default$21__T13 = typing.TypeVar('_copy$default$21__T13')  # <T13>
    _copy$default$21__T14 = typing.TypeVar('_copy$default$21__T14')  # <T14>
    _copy$default$21__T15 = typing.TypeVar('_copy$default$21__T15')  # <T15>
    _copy$default$21__T16 = typing.TypeVar('_copy$default$21__T16')  # <T16>
    _copy$default$21__T17 = typing.TypeVar('_copy$default$21__T17')  # <T17>
    _copy$default$21__T18 = typing.TypeVar('_copy$default$21__T18')  # <T18>
    _copy$default$21__T19 = typing.TypeVar('_copy$default$21__T19')  # <T19>
    _copy$default$21__T20 = typing.TypeVar('_copy$default$21__T20')  # <T20>
    _copy$default$21__T21 = typing.TypeVar('_copy$default$21__T21')  # <T21>
    _copy$default$21__T22 = typing.TypeVar('_copy$default$21__T22')  # <T22>
    def copy$default$21(self) -> typing.Any: ...
    _copy$default$22__T1 = typing.TypeVar('_copy$default$22__T1')  # <T1>
    _copy$default$22__T2 = typing.TypeVar('_copy$default$22__T2')  # <T2>
    _copy$default$22__T3 = typing.TypeVar('_copy$default$22__T3')  # <T3>
    _copy$default$22__T4 = typing.TypeVar('_copy$default$22__T4')  # <T4>
    _copy$default$22__T5 = typing.TypeVar('_copy$default$22__T5')  # <T5>
    _copy$default$22__T6 = typing.TypeVar('_copy$default$22__T6')  # <T6>
    _copy$default$22__T7 = typing.TypeVar('_copy$default$22__T7')  # <T7>
    _copy$default$22__T8 = typing.TypeVar('_copy$default$22__T8')  # <T8>
    _copy$default$22__T9 = typing.TypeVar('_copy$default$22__T9')  # <T9>
    _copy$default$22__T10 = typing.TypeVar('_copy$default$22__T10')  # <T10>
    _copy$default$22__T11 = typing.TypeVar('_copy$default$22__T11')  # <T11>
    _copy$default$22__T12 = typing.TypeVar('_copy$default$22__T12')  # <T12>
    _copy$default$22__T13 = typing.TypeVar('_copy$default$22__T13')  # <T13>
    _copy$default$22__T14 = typing.TypeVar('_copy$default$22__T14')  # <T14>
    _copy$default$22__T15 = typing.TypeVar('_copy$default$22__T15')  # <T15>
    _copy$default$22__T16 = typing.TypeVar('_copy$default$22__T16')  # <T16>
    _copy$default$22__T17 = typing.TypeVar('_copy$default$22__T17')  # <T17>
    _copy$default$22__T18 = typing.TypeVar('_copy$default$22__T18')  # <T18>
    _copy$default$22__T19 = typing.TypeVar('_copy$default$22__T19')  # <T19>
    _copy$default$22__T20 = typing.TypeVar('_copy$default$22__T20')  # <T20>
    _copy$default$22__T21 = typing.TypeVar('_copy$default$22__T21')  # <T21>
    _copy$default$22__T22 = typing.TypeVar('_copy$default$22__T22')  # <T22>
    def copy$default$22(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    _copy$default$3__T9 = typing.TypeVar('_copy$default$3__T9')  # <T9>
    _copy$default$3__T10 = typing.TypeVar('_copy$default$3__T10')  # <T10>
    _copy$default$3__T11 = typing.TypeVar('_copy$default$3__T11')  # <T11>
    _copy$default$3__T12 = typing.TypeVar('_copy$default$3__T12')  # <T12>
    _copy$default$3__T13 = typing.TypeVar('_copy$default$3__T13')  # <T13>
    _copy$default$3__T14 = typing.TypeVar('_copy$default$3__T14')  # <T14>
    _copy$default$3__T15 = typing.TypeVar('_copy$default$3__T15')  # <T15>
    _copy$default$3__T16 = typing.TypeVar('_copy$default$3__T16')  # <T16>
    _copy$default$3__T17 = typing.TypeVar('_copy$default$3__T17')  # <T17>
    _copy$default$3__T18 = typing.TypeVar('_copy$default$3__T18')  # <T18>
    _copy$default$3__T19 = typing.TypeVar('_copy$default$3__T19')  # <T19>
    _copy$default$3__T20 = typing.TypeVar('_copy$default$3__T20')  # <T20>
    _copy$default$3__T21 = typing.TypeVar('_copy$default$3__T21')  # <T21>
    _copy$default$3__T22 = typing.TypeVar('_copy$default$3__T22')  # <T22>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    _copy$default$4__T9 = typing.TypeVar('_copy$default$4__T9')  # <T9>
    _copy$default$4__T10 = typing.TypeVar('_copy$default$4__T10')  # <T10>
    _copy$default$4__T11 = typing.TypeVar('_copy$default$4__T11')  # <T11>
    _copy$default$4__T12 = typing.TypeVar('_copy$default$4__T12')  # <T12>
    _copy$default$4__T13 = typing.TypeVar('_copy$default$4__T13')  # <T13>
    _copy$default$4__T14 = typing.TypeVar('_copy$default$4__T14')  # <T14>
    _copy$default$4__T15 = typing.TypeVar('_copy$default$4__T15')  # <T15>
    _copy$default$4__T16 = typing.TypeVar('_copy$default$4__T16')  # <T16>
    _copy$default$4__T17 = typing.TypeVar('_copy$default$4__T17')  # <T17>
    _copy$default$4__T18 = typing.TypeVar('_copy$default$4__T18')  # <T18>
    _copy$default$4__T19 = typing.TypeVar('_copy$default$4__T19')  # <T19>
    _copy$default$4__T20 = typing.TypeVar('_copy$default$4__T20')  # <T20>
    _copy$default$4__T21 = typing.TypeVar('_copy$default$4__T21')  # <T21>
    _copy$default$4__T22 = typing.TypeVar('_copy$default$4__T22')  # <T22>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    _copy$default$5__T9 = typing.TypeVar('_copy$default$5__T9')  # <T9>
    _copy$default$5__T10 = typing.TypeVar('_copy$default$5__T10')  # <T10>
    _copy$default$5__T11 = typing.TypeVar('_copy$default$5__T11')  # <T11>
    _copy$default$5__T12 = typing.TypeVar('_copy$default$5__T12')  # <T12>
    _copy$default$5__T13 = typing.TypeVar('_copy$default$5__T13')  # <T13>
    _copy$default$5__T14 = typing.TypeVar('_copy$default$5__T14')  # <T14>
    _copy$default$5__T15 = typing.TypeVar('_copy$default$5__T15')  # <T15>
    _copy$default$5__T16 = typing.TypeVar('_copy$default$5__T16')  # <T16>
    _copy$default$5__T17 = typing.TypeVar('_copy$default$5__T17')  # <T17>
    _copy$default$5__T18 = typing.TypeVar('_copy$default$5__T18')  # <T18>
    _copy$default$5__T19 = typing.TypeVar('_copy$default$5__T19')  # <T19>
    _copy$default$5__T20 = typing.TypeVar('_copy$default$5__T20')  # <T20>
    _copy$default$5__T21 = typing.TypeVar('_copy$default$5__T21')  # <T21>
    _copy$default$5__T22 = typing.TypeVar('_copy$default$5__T22')  # <T22>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    _copy$default$6__T9 = typing.TypeVar('_copy$default$6__T9')  # <T9>
    _copy$default$6__T10 = typing.TypeVar('_copy$default$6__T10')  # <T10>
    _copy$default$6__T11 = typing.TypeVar('_copy$default$6__T11')  # <T11>
    _copy$default$6__T12 = typing.TypeVar('_copy$default$6__T12')  # <T12>
    _copy$default$6__T13 = typing.TypeVar('_copy$default$6__T13')  # <T13>
    _copy$default$6__T14 = typing.TypeVar('_copy$default$6__T14')  # <T14>
    _copy$default$6__T15 = typing.TypeVar('_copy$default$6__T15')  # <T15>
    _copy$default$6__T16 = typing.TypeVar('_copy$default$6__T16')  # <T16>
    _copy$default$6__T17 = typing.TypeVar('_copy$default$6__T17')  # <T17>
    _copy$default$6__T18 = typing.TypeVar('_copy$default$6__T18')  # <T18>
    _copy$default$6__T19 = typing.TypeVar('_copy$default$6__T19')  # <T19>
    _copy$default$6__T20 = typing.TypeVar('_copy$default$6__T20')  # <T20>
    _copy$default$6__T21 = typing.TypeVar('_copy$default$6__T21')  # <T21>
    _copy$default$6__T22 = typing.TypeVar('_copy$default$6__T22')  # <T22>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    _copy$default$7__T9 = typing.TypeVar('_copy$default$7__T9')  # <T9>
    _copy$default$7__T10 = typing.TypeVar('_copy$default$7__T10')  # <T10>
    _copy$default$7__T11 = typing.TypeVar('_copy$default$7__T11')  # <T11>
    _copy$default$7__T12 = typing.TypeVar('_copy$default$7__T12')  # <T12>
    _copy$default$7__T13 = typing.TypeVar('_copy$default$7__T13')  # <T13>
    _copy$default$7__T14 = typing.TypeVar('_copy$default$7__T14')  # <T14>
    _copy$default$7__T15 = typing.TypeVar('_copy$default$7__T15')  # <T15>
    _copy$default$7__T16 = typing.TypeVar('_copy$default$7__T16')  # <T16>
    _copy$default$7__T17 = typing.TypeVar('_copy$default$7__T17')  # <T17>
    _copy$default$7__T18 = typing.TypeVar('_copy$default$7__T18')  # <T18>
    _copy$default$7__T19 = typing.TypeVar('_copy$default$7__T19')  # <T19>
    _copy$default$7__T20 = typing.TypeVar('_copy$default$7__T20')  # <T20>
    _copy$default$7__T21 = typing.TypeVar('_copy$default$7__T21')  # <T21>
    _copy$default$7__T22 = typing.TypeVar('_copy$default$7__T22')  # <T22>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    _copy$default$8__T9 = typing.TypeVar('_copy$default$8__T9')  # <T9>
    _copy$default$8__T10 = typing.TypeVar('_copy$default$8__T10')  # <T10>
    _copy$default$8__T11 = typing.TypeVar('_copy$default$8__T11')  # <T11>
    _copy$default$8__T12 = typing.TypeVar('_copy$default$8__T12')  # <T12>
    _copy$default$8__T13 = typing.TypeVar('_copy$default$8__T13')  # <T13>
    _copy$default$8__T14 = typing.TypeVar('_copy$default$8__T14')  # <T14>
    _copy$default$8__T15 = typing.TypeVar('_copy$default$8__T15')  # <T15>
    _copy$default$8__T16 = typing.TypeVar('_copy$default$8__T16')  # <T16>
    _copy$default$8__T17 = typing.TypeVar('_copy$default$8__T17')  # <T17>
    _copy$default$8__T18 = typing.TypeVar('_copy$default$8__T18')  # <T18>
    _copy$default$8__T19 = typing.TypeVar('_copy$default$8__T19')  # <T19>
    _copy$default$8__T20 = typing.TypeVar('_copy$default$8__T20')  # <T20>
    _copy$default$8__T21 = typing.TypeVar('_copy$default$8__T21')  # <T21>
    _copy$default$8__T22 = typing.TypeVar('_copy$default$8__T22')  # <T22>
    def copy$default$8(self) -> typing.Any: ...
    _copy$default$9__T1 = typing.TypeVar('_copy$default$9__T1')  # <T1>
    _copy$default$9__T2 = typing.TypeVar('_copy$default$9__T2')  # <T2>
    _copy$default$9__T3 = typing.TypeVar('_copy$default$9__T3')  # <T3>
    _copy$default$9__T4 = typing.TypeVar('_copy$default$9__T4')  # <T4>
    _copy$default$9__T5 = typing.TypeVar('_copy$default$9__T5')  # <T5>
    _copy$default$9__T6 = typing.TypeVar('_copy$default$9__T6')  # <T6>
    _copy$default$9__T7 = typing.TypeVar('_copy$default$9__T7')  # <T7>
    _copy$default$9__T8 = typing.TypeVar('_copy$default$9__T8')  # <T8>
    _copy$default$9__T9 = typing.TypeVar('_copy$default$9__T9')  # <T9>
    _copy$default$9__T10 = typing.TypeVar('_copy$default$9__T10')  # <T10>
    _copy$default$9__T11 = typing.TypeVar('_copy$default$9__T11')  # <T11>
    _copy$default$9__T12 = typing.TypeVar('_copy$default$9__T12')  # <T12>
    _copy$default$9__T13 = typing.TypeVar('_copy$default$9__T13')  # <T13>
    _copy$default$9__T14 = typing.TypeVar('_copy$default$9__T14')  # <T14>
    _copy$default$9__T15 = typing.TypeVar('_copy$default$9__T15')  # <T15>
    _copy$default$9__T16 = typing.TypeVar('_copy$default$9__T16')  # <T16>
    _copy$default$9__T17 = typing.TypeVar('_copy$default$9__T17')  # <T17>
    _copy$default$9__T18 = typing.TypeVar('_copy$default$9__T18')  # <T18>
    _copy$default$9__T19 = typing.TypeVar('_copy$default$9__T19')  # <T19>
    _copy$default$9__T20 = typing.TypeVar('_copy$default$9__T20')  # <T20>
    _copy$default$9__T21 = typing.TypeVar('_copy$default$9__T21')  # <T21>
    _copy$default$9__T22 = typing.TypeVar('_copy$default$9__T22')  # <T22>
    def copy$default$9(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    _unapply__T10 = typing.TypeVar('_unapply__T10')  # <T10>
    _unapply__T11 = typing.TypeVar('_unapply__T11')  # <T11>
    _unapply__T12 = typing.TypeVar('_unapply__T12')  # <T12>
    _unapply__T13 = typing.TypeVar('_unapply__T13')  # <T13>
    _unapply__T14 = typing.TypeVar('_unapply__T14')  # <T14>
    _unapply__T15 = typing.TypeVar('_unapply__T15')  # <T15>
    _unapply__T16 = typing.TypeVar('_unapply__T16')  # <T16>
    _unapply__T17 = typing.TypeVar('_unapply__T17')  # <T17>
    _unapply__T18 = typing.TypeVar('_unapply__T18')  # <T18>
    _unapply__T19 = typing.TypeVar('_unapply__T19')  # <T19>
    _unapply__T20 = typing.TypeVar('_unapply__T20')  # <T20>
    _unapply__T21 = typing.TypeVar('_unapply__T21')  # <T21>
    _unapply__T22 = typing.TypeVar('_unapply__T22')  # <T22>
    @staticmethod
    def unapply(x$0: 'Tuple22'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19, _unapply__T20, _unapply__T21, _unapply__T22]) -> Option['Tuple22'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9, _unapply__T10, _unapply__T11, _unapply__T12, _unapply__T13, _unapply__T14, _unapply__T15, _unapply__T16, _unapply__T17, _unapply__T18, _unapply__T19, _unapply__T20, _unapply__T21, _unapply__T22]]: ...

_Tuple3__T1 = typing.TypeVar('_Tuple3__T1')  # <T1>
_Tuple3__T2 = typing.TypeVar('_Tuple3__T2')  # <T2>
_Tuple3__T3 = typing.TypeVar('_Tuple3__T3')  # <T3>
class Tuple3(Product3[_Tuple3__T1, _Tuple3__T2, _Tuple3__T3], Serializable, typing.Generic[_Tuple3__T1, _Tuple3__T2, _Tuple3__T3]):
    def __init__(self, _1: _Tuple3__T1, _2: _Tuple3__T2, _3: _Tuple3__T3): ...
    def _1(self) -> _Tuple3__T1: ...
    def _2(self) -> _Tuple3__T2: ...
    def _3(self) -> _Tuple3__T3: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3) -> 'Tuple3'[_apply__T1, _apply__T2, _apply__T3]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any) -> 'Tuple3'[typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    def copy$default$3(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    @staticmethod
    def unapply(x$0: 'Tuple3'[_unapply__T1, _unapply__T2, _unapply__T3]) -> Option['Tuple3'[_unapply__T1, _unapply__T2, _unapply__T3]]: ...

_Tuple4__T1 = typing.TypeVar('_Tuple4__T1')  # <T1>
_Tuple4__T2 = typing.TypeVar('_Tuple4__T2')  # <T2>
_Tuple4__T3 = typing.TypeVar('_Tuple4__T3')  # <T3>
_Tuple4__T4 = typing.TypeVar('_Tuple4__T4')  # <T4>
class Tuple4(Product4[_Tuple4__T1, _Tuple4__T2, _Tuple4__T3, _Tuple4__T4], Serializable, typing.Generic[_Tuple4__T1, _Tuple4__T2, _Tuple4__T3, _Tuple4__T4]):
    def __init__(self, _1: _Tuple4__T1, _2: _Tuple4__T2, _3: _Tuple4__T3, _4: _Tuple4__T4): ...
    def _1(self) -> _Tuple4__T1: ...
    def _2(self) -> _Tuple4__T2: ...
    def _3(self) -> _Tuple4__T3: ...
    def _4(self) -> _Tuple4__T4: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4) -> 'Tuple4'[_apply__T1, _apply__T2, _apply__T3, _apply__T4]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any) -> 'Tuple4'[typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    def copy$default$4(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    @staticmethod
    def unapply(x$0: 'Tuple4'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4]) -> Option['Tuple4'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4]]: ...

_Tuple5__T1 = typing.TypeVar('_Tuple5__T1')  # <T1>
_Tuple5__T2 = typing.TypeVar('_Tuple5__T2')  # <T2>
_Tuple5__T3 = typing.TypeVar('_Tuple5__T3')  # <T3>
_Tuple5__T4 = typing.TypeVar('_Tuple5__T4')  # <T4>
_Tuple5__T5 = typing.TypeVar('_Tuple5__T5')  # <T5>
class Tuple5(Product5[_Tuple5__T1, _Tuple5__T2, _Tuple5__T3, _Tuple5__T4, _Tuple5__T5], Serializable, typing.Generic[_Tuple5__T1, _Tuple5__T2, _Tuple5__T3, _Tuple5__T4, _Tuple5__T5]):
    def __init__(self, _1: _Tuple5__T1, _2: _Tuple5__T2, _3: _Tuple5__T3, _4: _Tuple5__T4, _5: _Tuple5__T5): ...
    def _1(self) -> _Tuple5__T1: ...
    def _2(self) -> _Tuple5__T2: ...
    def _3(self) -> _Tuple5__T3: ...
    def _4(self) -> _Tuple5__T4: ...
    def _5(self) -> _Tuple5__T5: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5) -> 'Tuple5'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any) -> 'Tuple5'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    def copy$default$5(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    @staticmethod
    def unapply(x$0: 'Tuple5'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5]) -> Option['Tuple5'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5]]: ...

_Tuple6__T1 = typing.TypeVar('_Tuple6__T1')  # <T1>
_Tuple6__T2 = typing.TypeVar('_Tuple6__T2')  # <T2>
_Tuple6__T3 = typing.TypeVar('_Tuple6__T3')  # <T3>
_Tuple6__T4 = typing.TypeVar('_Tuple6__T4')  # <T4>
_Tuple6__T5 = typing.TypeVar('_Tuple6__T5')  # <T5>
_Tuple6__T6 = typing.TypeVar('_Tuple6__T6')  # <T6>
class Tuple6(Product6[_Tuple6__T1, _Tuple6__T2, _Tuple6__T3, _Tuple6__T4, _Tuple6__T5, _Tuple6__T6], Serializable, typing.Generic[_Tuple6__T1, _Tuple6__T2, _Tuple6__T3, _Tuple6__T4, _Tuple6__T5, _Tuple6__T6]):
    def __init__(self, _1: _Tuple6__T1, _2: _Tuple6__T2, _3: _Tuple6__T3, _4: _Tuple6__T4, _5: _Tuple6__T5, _6: _Tuple6__T6): ...
    def _1(self) -> _Tuple6__T1: ...
    def _2(self) -> _Tuple6__T2: ...
    def _3(self) -> _Tuple6__T3: ...
    def _4(self) -> _Tuple6__T4: ...
    def _5(self) -> _Tuple6__T5: ...
    def _6(self) -> _Tuple6__T6: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6) -> 'Tuple6'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any) -> 'Tuple6'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    def copy$default$6(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    @staticmethod
    def unapply(x$0: 'Tuple6'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6]) -> Option['Tuple6'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6]]: ...

_Tuple7__T1 = typing.TypeVar('_Tuple7__T1')  # <T1>
_Tuple7__T2 = typing.TypeVar('_Tuple7__T2')  # <T2>
_Tuple7__T3 = typing.TypeVar('_Tuple7__T3')  # <T3>
_Tuple7__T4 = typing.TypeVar('_Tuple7__T4')  # <T4>
_Tuple7__T5 = typing.TypeVar('_Tuple7__T5')  # <T5>
_Tuple7__T6 = typing.TypeVar('_Tuple7__T6')  # <T6>
_Tuple7__T7 = typing.TypeVar('_Tuple7__T7')  # <T7>
class Tuple7(Product7[_Tuple7__T1, _Tuple7__T2, _Tuple7__T3, _Tuple7__T4, _Tuple7__T5, _Tuple7__T6, _Tuple7__T7], Serializable, typing.Generic[_Tuple7__T1, _Tuple7__T2, _Tuple7__T3, _Tuple7__T4, _Tuple7__T5, _Tuple7__T6, _Tuple7__T7]):
    def __init__(self, _1: _Tuple7__T1, _2: _Tuple7__T2, _3: _Tuple7__T3, _4: _Tuple7__T4, _5: _Tuple7__T5, _6: _Tuple7__T6, _7: _Tuple7__T7): ...
    def _1(self) -> _Tuple7__T1: ...
    def _2(self) -> _Tuple7__T2: ...
    def _3(self) -> _Tuple7__T3: ...
    def _4(self) -> _Tuple7__T4: ...
    def _5(self) -> _Tuple7__T5: ...
    def _6(self) -> _Tuple7__T6: ...
    def _7(self) -> _Tuple7__T7: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7) -> 'Tuple7'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any) -> 'Tuple7'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    def copy$default$7(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    @staticmethod
    def unapply(x$0: 'Tuple7'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7]) -> Option['Tuple7'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7]]: ...

_Tuple8__T1 = typing.TypeVar('_Tuple8__T1')  # <T1>
_Tuple8__T2 = typing.TypeVar('_Tuple8__T2')  # <T2>
_Tuple8__T3 = typing.TypeVar('_Tuple8__T3')  # <T3>
_Tuple8__T4 = typing.TypeVar('_Tuple8__T4')  # <T4>
_Tuple8__T5 = typing.TypeVar('_Tuple8__T5')  # <T5>
_Tuple8__T6 = typing.TypeVar('_Tuple8__T6')  # <T6>
_Tuple8__T7 = typing.TypeVar('_Tuple8__T7')  # <T7>
_Tuple8__T8 = typing.TypeVar('_Tuple8__T8')  # <T8>
class Tuple8(Product8[_Tuple8__T1, _Tuple8__T2, _Tuple8__T3, _Tuple8__T4, _Tuple8__T5, _Tuple8__T6, _Tuple8__T7, _Tuple8__T8], Serializable, typing.Generic[_Tuple8__T1, _Tuple8__T2, _Tuple8__T3, _Tuple8__T4, _Tuple8__T5, _Tuple8__T6, _Tuple8__T7, _Tuple8__T8]):
    def __init__(self, _1: _Tuple8__T1, _2: _Tuple8__T2, _3: _Tuple8__T3, _4: _Tuple8__T4, _5: _Tuple8__T5, _6: _Tuple8__T6, _7: _Tuple8__T7, _8: _Tuple8__T8): ...
    def _1(self) -> _Tuple8__T1: ...
    def _2(self) -> _Tuple8__T2: ...
    def _3(self) -> _Tuple8__T3: ...
    def _4(self) -> _Tuple8__T4: ...
    def _5(self) -> _Tuple8__T5: ...
    def _6(self) -> _Tuple8__T6: ...
    def _7(self) -> _Tuple8__T7: ...
    def _8(self) -> _Tuple8__T8: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8) -> 'Tuple8'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any) -> 'Tuple8'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    def copy$default$8(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    @staticmethod
    def unapply(x$0: 'Tuple8'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8]) -> Option['Tuple8'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8]]: ...

_Tuple9__T1 = typing.TypeVar('_Tuple9__T1')  # <T1>
_Tuple9__T2 = typing.TypeVar('_Tuple9__T2')  # <T2>
_Tuple9__T3 = typing.TypeVar('_Tuple9__T3')  # <T3>
_Tuple9__T4 = typing.TypeVar('_Tuple9__T4')  # <T4>
_Tuple9__T5 = typing.TypeVar('_Tuple9__T5')  # <T5>
_Tuple9__T6 = typing.TypeVar('_Tuple9__T6')  # <T6>
_Tuple9__T7 = typing.TypeVar('_Tuple9__T7')  # <T7>
_Tuple9__T8 = typing.TypeVar('_Tuple9__T8')  # <T8>
_Tuple9__T9 = typing.TypeVar('_Tuple9__T9')  # <T9>
class Tuple9(Product9[_Tuple9__T1, _Tuple9__T2, _Tuple9__T3, _Tuple9__T4, _Tuple9__T5, _Tuple9__T6, _Tuple9__T7, _Tuple9__T8, _Tuple9__T9], Serializable, typing.Generic[_Tuple9__T1, _Tuple9__T2, _Tuple9__T3, _Tuple9__T4, _Tuple9__T5, _Tuple9__T6, _Tuple9__T7, _Tuple9__T8, _Tuple9__T9]):
    def __init__(self, _1: _Tuple9__T1, _2: _Tuple9__T2, _3: _Tuple9__T3, _4: _Tuple9__T4, _5: _Tuple9__T5, _6: _Tuple9__T6, _7: _Tuple9__T7, _8: _Tuple9__T8, _9: _Tuple9__T9): ...
    def _1(self) -> _Tuple9__T1: ...
    def _2(self) -> _Tuple9__T2: ...
    def _3(self) -> _Tuple9__T3: ...
    def _4(self) -> _Tuple9__T4: ...
    def _5(self) -> _Tuple9__T5: ...
    def _6(self) -> _Tuple9__T6: ...
    def _7(self) -> _Tuple9__T7: ...
    def _8(self) -> _Tuple9__T8: ...
    def _9(self) -> _Tuple9__T9: ...
    _apply__T1 = typing.TypeVar('_apply__T1')  # <T1>
    _apply__T2 = typing.TypeVar('_apply__T2')  # <T2>
    _apply__T3 = typing.TypeVar('_apply__T3')  # <T3>
    _apply__T4 = typing.TypeVar('_apply__T4')  # <T4>
    _apply__T5 = typing.TypeVar('_apply__T5')  # <T5>
    _apply__T6 = typing.TypeVar('_apply__T6')  # <T6>
    _apply__T7 = typing.TypeVar('_apply__T7')  # <T7>
    _apply__T8 = typing.TypeVar('_apply__T8')  # <T8>
    _apply__T9 = typing.TypeVar('_apply__T9')  # <T9>
    @staticmethod
    def apply(_1: _apply__T1, _2: _apply__T2, _3: _apply__T3, _4: _apply__T4, _5: _apply__T5, _6: _apply__T6, _7: _apply__T7, _8: _apply__T8, _9: _apply__T9) -> 'Tuple9'[_apply__T1, _apply__T2, _apply__T3, _apply__T4, _apply__T5, _apply__T6, _apply__T7, _apply__T8, _apply__T9]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__T1 = typing.TypeVar('_copy__T1')  # <T1>
    _copy__T2 = typing.TypeVar('_copy__T2')  # <T2>
    _copy__T3 = typing.TypeVar('_copy__T3')  # <T3>
    _copy__T4 = typing.TypeVar('_copy__T4')  # <T4>
    _copy__T5 = typing.TypeVar('_copy__T5')  # <T5>
    _copy__T6 = typing.TypeVar('_copy__T6')  # <T6>
    _copy__T7 = typing.TypeVar('_copy__T7')  # <T7>
    _copy__T8 = typing.TypeVar('_copy__T8')  # <T8>
    _copy__T9 = typing.TypeVar('_copy__T9')  # <T9>
    def copy(self, _1: typing.Any, _2: typing.Any, _3: typing.Any, _4: typing.Any, _5: typing.Any, _6: typing.Any, _7: typing.Any, _8: typing.Any, _9: typing.Any) -> 'Tuple9'[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]: ...
    _copy$default$1__T1 = typing.TypeVar('_copy$default$1__T1')  # <T1>
    _copy$default$1__T2 = typing.TypeVar('_copy$default$1__T2')  # <T2>
    _copy$default$1__T3 = typing.TypeVar('_copy$default$1__T3')  # <T3>
    _copy$default$1__T4 = typing.TypeVar('_copy$default$1__T4')  # <T4>
    _copy$default$1__T5 = typing.TypeVar('_copy$default$1__T5')  # <T5>
    _copy$default$1__T6 = typing.TypeVar('_copy$default$1__T6')  # <T6>
    _copy$default$1__T7 = typing.TypeVar('_copy$default$1__T7')  # <T7>
    _copy$default$1__T8 = typing.TypeVar('_copy$default$1__T8')  # <T8>
    _copy$default$1__T9 = typing.TypeVar('_copy$default$1__T9')  # <T9>
    def copy$default$1(self) -> typing.Any: ...
    _copy$default$2__T1 = typing.TypeVar('_copy$default$2__T1')  # <T1>
    _copy$default$2__T2 = typing.TypeVar('_copy$default$2__T2')  # <T2>
    _copy$default$2__T3 = typing.TypeVar('_copy$default$2__T3')  # <T3>
    _copy$default$2__T4 = typing.TypeVar('_copy$default$2__T4')  # <T4>
    _copy$default$2__T5 = typing.TypeVar('_copy$default$2__T5')  # <T5>
    _copy$default$2__T6 = typing.TypeVar('_copy$default$2__T6')  # <T6>
    _copy$default$2__T7 = typing.TypeVar('_copy$default$2__T7')  # <T7>
    _copy$default$2__T8 = typing.TypeVar('_copy$default$2__T8')  # <T8>
    _copy$default$2__T9 = typing.TypeVar('_copy$default$2__T9')  # <T9>
    def copy$default$2(self) -> typing.Any: ...
    _copy$default$3__T1 = typing.TypeVar('_copy$default$3__T1')  # <T1>
    _copy$default$3__T2 = typing.TypeVar('_copy$default$3__T2')  # <T2>
    _copy$default$3__T3 = typing.TypeVar('_copy$default$3__T3')  # <T3>
    _copy$default$3__T4 = typing.TypeVar('_copy$default$3__T4')  # <T4>
    _copy$default$3__T5 = typing.TypeVar('_copy$default$3__T5')  # <T5>
    _copy$default$3__T6 = typing.TypeVar('_copy$default$3__T6')  # <T6>
    _copy$default$3__T7 = typing.TypeVar('_copy$default$3__T7')  # <T7>
    _copy$default$3__T8 = typing.TypeVar('_copy$default$3__T8')  # <T8>
    _copy$default$3__T9 = typing.TypeVar('_copy$default$3__T9')  # <T9>
    def copy$default$3(self) -> typing.Any: ...
    _copy$default$4__T1 = typing.TypeVar('_copy$default$4__T1')  # <T1>
    _copy$default$4__T2 = typing.TypeVar('_copy$default$4__T2')  # <T2>
    _copy$default$4__T3 = typing.TypeVar('_copy$default$4__T3')  # <T3>
    _copy$default$4__T4 = typing.TypeVar('_copy$default$4__T4')  # <T4>
    _copy$default$4__T5 = typing.TypeVar('_copy$default$4__T5')  # <T5>
    _copy$default$4__T6 = typing.TypeVar('_copy$default$4__T6')  # <T6>
    _copy$default$4__T7 = typing.TypeVar('_copy$default$4__T7')  # <T7>
    _copy$default$4__T8 = typing.TypeVar('_copy$default$4__T8')  # <T8>
    _copy$default$4__T9 = typing.TypeVar('_copy$default$4__T9')  # <T9>
    def copy$default$4(self) -> typing.Any: ...
    _copy$default$5__T1 = typing.TypeVar('_copy$default$5__T1')  # <T1>
    _copy$default$5__T2 = typing.TypeVar('_copy$default$5__T2')  # <T2>
    _copy$default$5__T3 = typing.TypeVar('_copy$default$5__T3')  # <T3>
    _copy$default$5__T4 = typing.TypeVar('_copy$default$5__T4')  # <T4>
    _copy$default$5__T5 = typing.TypeVar('_copy$default$5__T5')  # <T5>
    _copy$default$5__T6 = typing.TypeVar('_copy$default$5__T6')  # <T6>
    _copy$default$5__T7 = typing.TypeVar('_copy$default$5__T7')  # <T7>
    _copy$default$5__T8 = typing.TypeVar('_copy$default$5__T8')  # <T8>
    _copy$default$5__T9 = typing.TypeVar('_copy$default$5__T9')  # <T9>
    def copy$default$5(self) -> typing.Any: ...
    _copy$default$6__T1 = typing.TypeVar('_copy$default$6__T1')  # <T1>
    _copy$default$6__T2 = typing.TypeVar('_copy$default$6__T2')  # <T2>
    _copy$default$6__T3 = typing.TypeVar('_copy$default$6__T3')  # <T3>
    _copy$default$6__T4 = typing.TypeVar('_copy$default$6__T4')  # <T4>
    _copy$default$6__T5 = typing.TypeVar('_copy$default$6__T5')  # <T5>
    _copy$default$6__T6 = typing.TypeVar('_copy$default$6__T6')  # <T6>
    _copy$default$6__T7 = typing.TypeVar('_copy$default$6__T7')  # <T7>
    _copy$default$6__T8 = typing.TypeVar('_copy$default$6__T8')  # <T8>
    _copy$default$6__T9 = typing.TypeVar('_copy$default$6__T9')  # <T9>
    def copy$default$6(self) -> typing.Any: ...
    _copy$default$7__T1 = typing.TypeVar('_copy$default$7__T1')  # <T1>
    _copy$default$7__T2 = typing.TypeVar('_copy$default$7__T2')  # <T2>
    _copy$default$7__T3 = typing.TypeVar('_copy$default$7__T3')  # <T3>
    _copy$default$7__T4 = typing.TypeVar('_copy$default$7__T4')  # <T4>
    _copy$default$7__T5 = typing.TypeVar('_copy$default$7__T5')  # <T5>
    _copy$default$7__T6 = typing.TypeVar('_copy$default$7__T6')  # <T6>
    _copy$default$7__T7 = typing.TypeVar('_copy$default$7__T7')  # <T7>
    _copy$default$7__T8 = typing.TypeVar('_copy$default$7__T8')  # <T8>
    _copy$default$7__T9 = typing.TypeVar('_copy$default$7__T9')  # <T9>
    def copy$default$7(self) -> typing.Any: ...
    _copy$default$8__T1 = typing.TypeVar('_copy$default$8__T1')  # <T1>
    _copy$default$8__T2 = typing.TypeVar('_copy$default$8__T2')  # <T2>
    _copy$default$8__T3 = typing.TypeVar('_copy$default$8__T3')  # <T3>
    _copy$default$8__T4 = typing.TypeVar('_copy$default$8__T4')  # <T4>
    _copy$default$8__T5 = typing.TypeVar('_copy$default$8__T5')  # <T5>
    _copy$default$8__T6 = typing.TypeVar('_copy$default$8__T6')  # <T6>
    _copy$default$8__T7 = typing.TypeVar('_copy$default$8__T7')  # <T7>
    _copy$default$8__T8 = typing.TypeVar('_copy$default$8__T8')  # <T8>
    _copy$default$8__T9 = typing.TypeVar('_copy$default$8__T9')  # <T9>
    def copy$default$8(self) -> typing.Any: ...
    _copy$default$9__T1 = typing.TypeVar('_copy$default$9__T1')  # <T1>
    _copy$default$9__T2 = typing.TypeVar('_copy$default$9__T2')  # <T2>
    _copy$default$9__T3 = typing.TypeVar('_copy$default$9__T3')  # <T3>
    _copy$default$9__T4 = typing.TypeVar('_copy$default$9__T4')  # <T4>
    _copy$default$9__T5 = typing.TypeVar('_copy$default$9__T5')  # <T5>
    _copy$default$9__T6 = typing.TypeVar('_copy$default$9__T6')  # <T6>
    _copy$default$9__T7 = typing.TypeVar('_copy$default$9__T7')  # <T7>
    _copy$default$9__T8 = typing.TypeVar('_copy$default$9__T8')  # <T8>
    _copy$default$9__T9 = typing.TypeVar('_copy$default$9__T9')  # <T9>
    def copy$default$9(self) -> typing.Any: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, n: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> str: ...
    def toString(self) -> str: ...
    _unapply__T1 = typing.TypeVar('_unapply__T1')  # <T1>
    _unapply__T2 = typing.TypeVar('_unapply__T2')  # <T2>
    _unapply__T3 = typing.TypeVar('_unapply__T3')  # <T3>
    _unapply__T4 = typing.TypeVar('_unapply__T4')  # <T4>
    _unapply__T5 = typing.TypeVar('_unapply__T5')  # <T5>
    _unapply__T6 = typing.TypeVar('_unapply__T6')  # <T6>
    _unapply__T7 = typing.TypeVar('_unapply__T7')  # <T7>
    _unapply__T8 = typing.TypeVar('_unapply__T8')  # <T8>
    _unapply__T9 = typing.TypeVar('_unapply__T9')  # <T9>
    @staticmethod
    def unapply(x$0: 'Tuple9'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9]) -> Option['Tuple9'[_unapply__T1, _unapply__T2, _unapply__T3, _unapply__T4, _unapply__T5, _unapply__T6, _unapply__T7, _unapply__T8, _unapply__T9]]: ...

class AnyValCompanion(scala.Specializable): ...

class Enumeration(Serializable):
    serialVersionUID: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, initial: int): ...
    def ValueOrdering(self) -> 'Enumeration.ValueOrdering.': ...
    def apply(self, x: int) -> 'Enumeration.Value': ...
    def maxId(self) -> int: ...
    def nextId(self) -> int: ...
    def nextId_$eq(self, x$1: int) -> None: ...
    def nextName(self) -> scala.collection.Iterator[str]: ...
    def nextName_$eq(self, x$1: scala.collection.Iterator[str]) -> None: ...
    def readResolve(self) -> typing.Any: ...
    def scala$Enumeration$$bottomId(self) -> int: ...
    def scala$Enumeration$$bottomId_$eq(self, x$1: int) -> None: ...
    def scala$Enumeration$$nameOf(self, i: int) -> str: ...
    def scala$Enumeration$$nextNameOrNull(self) -> str: ...
    def scala$Enumeration$$topId(self) -> int: ...
    def scala$Enumeration$$topId_$eq(self, x$1: int) -> None: ...
    def scala$Enumeration$$vmap(self) -> scala.collection.mutable.Map[typing.Any, 'Enumeration.Value']: ...
    def scala$Enumeration$$vsetDefined_$eq(self, x$1: bool) -> None: ...
    def toString(self) -> str: ...
    def values(self) -> 'Enumeration.ValueSet': ...
    def withName(self, s: str) -> 'Enumeration.Value': ...
    class Val(scala.Enumeration.Value):
        serialVersionUID: typing.ClassVar[int] = ...
        @typing.overload
        def __init__(self, $outer: 'Enumeration'): ...
        @typing.overload
        def __init__(self, $outer: 'Enumeration', i: int): ...
        @typing.overload
        def __init__(self, $outer: 'Enumeration', i: int, name: str): ...
        @typing.overload
        def __init__(self, $outer: 'Enumeration', name: str): ...
        def id(self) -> int: ...
        def readResolve(self) -> typing.Any: ...
        def toString(self) -> str: ...
    class Value(scala.math.Ordered['Enumeration.Value'], Serializable):
        serialVersionUID: typing.ClassVar[int] = ...
        $outer: 'Enumeration' = ...
        def __init__(self, $outer: 'Enumeration'): ...
        def $greater(self, that: typing.Any) -> bool: ...
        def $greater$eq(self, that: typing.Any) -> bool: ...
        def $less(self, that: typing.Any) -> bool: ...
        def $less$eq(self, that: typing.Any) -> bool: ...
        def $plus(self, v: 'Enumeration.Value') -> 'Enumeration.ValueSet': ...
        def compare(self, that: 'Enumeration.Value') -> int: ...
        def compareTo(self, that: typing.Any) -> int: ...
        def equals(self, other: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def id(self) -> int: ...
        def scala$Enumeration$$outerEnum(self) -> 'Enumeration': ...
    class ValueOrdering$(scala.math.Ordering['Enumeration.Value']):
        def __init__(self, $outer: 'Enumeration'): ...
        def compare(self, x: 'Enumeration.Value', y: 'Enumeration.Value') -> int: ...
        def equiv(self, x: typing.Any, y: typing.Any) -> bool: ...
        def gt(self, x: typing.Any, y: typing.Any) -> bool: ...
        def gteq(self, x: typing.Any, y: typing.Any) -> bool: ...
        def lt(self, x: typing.Any, y: typing.Any) -> bool: ...
        def lteq(self, x: typing.Any, y: typing.Any) -> bool: ...
        def max(self, x: typing.Any, y: typing.Any) -> typing.Any: ...
        def min(self, x: typing.Any, y: typing.Any) -> typing.Any: ...
        def mkOrderingOps(self, lhs: typing.Any) -> scala.math.Ordering.Ops: ...
        _on__U = typing.TypeVar('_on__U')  # <U>
        def on(self, f: Function1[_on__U, 'Enumeration.Value']) -> scala.math.Ordering[_on__U]: ...
        def reverse(self) -> scala.math.Ordering['Enumeration.Value']: ...
        def tryCompare(self, x: typing.Any, y: typing.Any) -> Some: ...
    class ValueSet(scala.collection.AbstractSet['Enumeration.Value'], scala.collection.immutable.SortedSet['Enumeration.Value'], Serializable):
        $outer: 'Enumeration' = ...
        def __init__(self, $outer: 'Enumeration', nnIds: scala.collection.immutable.BitSet): ...
        @typing.overload
        def $minus(self, value: 'Enumeration.Value') -> 'Enumeration.ValueSet': ...
        @typing.overload
        def $minus(self, elem1: typing.Any, elem2: typing.Any, elems: scala.collection.Seq) -> scala.collection.generic.Subtractable: ...
        @typing.overload
        def $plus(self, value: 'Enumeration.Value') -> 'Enumeration.ValueSet': ...
        @typing.overload
        def $plus(self, elem1: typing.Any, elem2: typing.Any, elems: scala.collection.Seq[typing.Any]) -> scala.collection.Set[typing.Any]: ...
        def apply(self, elem: typing.Any) -> bool: ...
        def companion(self) -> scala.collection.generic.GenericCompanion[scala.collection.immutable.Set]: ...
        def compare(self, k0: typing.Any, k1: typing.Any) -> int: ...
        def contains(self, v: 'Enumeration.Value') -> bool: ...
        def diff(self, that: scala.collection.GenSet[typing.Any]) -> scala.collection.Set[typing.Any]: ...
        def empty(self) -> 'Enumeration.ValueSet': ...
        def firstKey(self) -> typing.Any: ...
        _groupBy__K = typing.TypeVar('_groupBy__K')  # <K>
        def groupBy(self, f: Function1[typing.Any, _groupBy__K]) -> scala.collection.immutable.Map[_groupBy__K, scala.collection.Traversable[typing.Any]]: ...
        def hasAll(self, j: scala.collection.Iterator['Enumeration.Value']) -> bool: ...
        def iterator(self) -> scala.collection.Iterator['Enumeration.Value']: ...
        def iteratorFrom(self, start: typing.Any) -> scala.collection.Iterator: ...
        def keySet(self) -> scala.collection.SortedSet: ...
        def keysIteratorFrom(self, start: 'Enumeration.Value') -> scala.collection.Iterator['Enumeration.Value']: ...
        def lastKey(self) -> typing.Any: ...
        def ordering(self) -> scala.math.Ordering['Enumeration.Value']: ...
        def parCombiner(self) -> scala.collection.parallel.Combiner['Enumeration.Value', scala.collection.parallel.immutable.ParSet['Enumeration.Value']]: ...
        def range(self, from_: typing.Any, until: typing.Any) -> scala.collection.SortedSet: ...
        def rangeImpl(self, from_: Option['Enumeration.Value'], until: Option['Enumeration.Value']) -> 'Enumeration.ValueSet': ...
        def repr(self) -> typing.Any: ...
        def seq(self) -> scala.collection.immutable.Set['Enumeration.Value']: ...
        def stringPrefix(self) -> str: ...
        def subsetOf(self, that: scala.collection.GenSet['Enumeration.Value']) -> bool: ...
        def thisCollection(self) -> scala.collection.Iterable[typing.Any]: ...
        _to_0__Col = typing.TypeVar('_to_0__Col')  # <Col>
        @typing.overload
        def to(self, cbf: scala.collection.generic.CanBuildFrom[scala.runtime.Nothing., typing.Any, _to_0__Col]) -> _to_0__Col: ...
        @typing.overload
        def to(self, to: typing.Any) -> scala.collection.generic.Sorted: ...
        def toBitMask(self) -> typing.List[int]: ...
        def toCollection(self, repr: typing.Any) -> scala.collection.Iterable: ...
        def toIterable(self) -> scala.collection.Iterable[typing.Any]: ...
        def toSeq(self) -> scala.collection.Seq[typing.Any]: ...
        _toSet__B = typing.TypeVar('_toSet__B')  # <B>
        def toSet(self) -> scala.collection.immutable.Set[_toSet__B]: ...
        def toTraversable(self) -> scala.collection.Traversable[typing.Any]: ...
        def union(self, that: scala.collection.GenSet[typing.Any]) -> scala.collection.Set[typing.Any]: ...
        def until(self, until: typing.Any) -> scala.collection.SortedSet: ...
        @typing.overload
        def view(self) -> scala.collection.IterableView[typing.Any, scala.collection.Iterable[typing.Any]]: ...
        @typing.overload
        def view(self, from_: int, until: int) -> scala.collection.IterableView[typing.Any, scala.collection.Iterable[typing.Any]]: ...
    class ValueSet$(Serializable):
        def __init__(self, $outer: 'Enumeration'): ...
        def apply(self, elems: scala.collection.Seq['Enumeration.Value']) -> 'Enumeration.ValueSet': ...
        def canBuildFrom(self) -> scala.collection.generic.CanBuildFrom['Enumeration.ValueSet', 'Enumeration.Value', 'Enumeration.ValueSet']: ...
        def empty(self) -> 'Enumeration.ValueSet': ...
        def fromBitMask(self, elems: typing.List[int]) -> 'Enumeration.ValueSet': ...
        def newBuilder(self) -> scala.collection.mutable.Builder['Enumeration.Value', 'Enumeration.ValueSet']: ...

_PartialFunction__AndThen__A = typing.TypeVar('_PartialFunction__AndThen__A')  # <A>
_PartialFunction__AndThen__B = typing.TypeVar('_PartialFunction__AndThen__B')  # <B>
_PartialFunction__AndThen__C = typing.TypeVar('_PartialFunction__AndThen__C')  # <C>
_PartialFunction__Lifted__A = typing.TypeVar('_PartialFunction__Lifted__A')  # <A>
_PartialFunction__Lifted__B = typing.TypeVar('_PartialFunction__Lifted__B')  # <B>
_PartialFunction__OrElse__A = typing.TypeVar('_PartialFunction__OrElse__A')  # <A>
_PartialFunction__OrElse__B = typing.TypeVar('_PartialFunction__OrElse__B')  # <B>
_PartialFunction__Unlifted__A = typing.TypeVar('_PartialFunction__Unlifted__A')  # <A>
_PartialFunction__Unlifted__B = typing.TypeVar('_PartialFunction__Unlifted__B')  # <B>
_PartialFunction__A = typing.TypeVar('_PartialFunction__A')  # <A>
_PartialFunction__B = typing.TypeVar('_PartialFunction__B')  # <B>
class PartialFunction(Function1[_PartialFunction__A, _PartialFunction__B], typing.Generic[_PartialFunction__A, _PartialFunction__B]):
    @staticmethod
    def $init$($this: 'PartialFunction') -> None: ...
    _andThen_0__A = typing.TypeVar('_andThen_0__A')  # <A>
    _andThen_1__C = typing.TypeVar('_andThen_1__C')  # <C>
    @typing.overload
    def andThen(self, g: Function1[typing.Any, typing.Any]) -> Function1[typing.Any, typing.Any]: ...
    @typing.overload
    def andThen(self, k: Function1[_PartialFunction__B, _andThen_1__C]) -> 'PartialFunction'[_PartialFunction__A, _andThen_1__C]: ...
    _applyOrElse__A1 = typing.TypeVar('_applyOrElse__A1')  # <A1>
    _applyOrElse__B1 = typing.TypeVar('_applyOrElse__B1')  # <B1>
    def applyOrElse(self, x: _applyOrElse__A1, default: Function1[_applyOrElse__A1, _applyOrElse__B1]) -> _applyOrElse__B1: ...
    _cond__T = typing.TypeVar('_cond__T')  # <T>
    @staticmethod
    def cond(x: _cond__T, pf: 'PartialFunction'[_cond__T, typing.Any]) -> bool: ...
    _condOpt__T = typing.TypeVar('_condOpt__T')  # <T>
    _condOpt__U = typing.TypeVar('_condOpt__U')  # <U>
    @staticmethod
    def condOpt(x: _condOpt__T, pf: 'PartialFunction'[_condOpt__T, _condOpt__U]) -> Option[_condOpt__U]: ...
    _empty__A = typing.TypeVar('_empty__A')  # <A>
    _empty__B = typing.TypeVar('_empty__B')  # <B>
    @staticmethod
    def empty() -> 'PartialFunction'[_empty__A, _empty__B]: ...
    def isDefinedAt(self, x: _PartialFunction__A) -> bool: ...
    def lift(self) -> Function1[_PartialFunction__A, Option[_PartialFunction__B]]: ...
    _orElse__A1 = typing.TypeVar('_orElse__A1')  # <A1>
    _orElse__B1 = typing.TypeVar('_orElse__B1')  # <B1>
    def orElse(self, that: 'PartialFunction'[_orElse__A1, _orElse__B1]) -> 'PartialFunction'[_orElse__A1, _orElse__B1]: ...
    _runWith__U = typing.TypeVar('_runWith__U')  # <U>
    def runWith(self, action: Function1[_PartialFunction__B, _runWith__U]) -> Function1[_PartialFunction__A, typing.Any]: ...
    def toString(self) -> str: ...
    class AndThen(scala.PartialFunction[_PartialFunction__AndThen__A, _PartialFunction__AndThen__C], Serializable, typing.Generic[_PartialFunction__AndThen__A, _PartialFunction__AndThen__B, _PartialFunction__AndThen__C]):
        def __init__(self, pf: 'PartialFunction'[_PartialFunction__AndThen__A, _PartialFunction__AndThen__B], k: Function1[_PartialFunction__AndThen__B, _PartialFunction__AndThen__C]): ...
        _andThen__C = typing.TypeVar('_andThen__C')  # <C>
        def andThen(self, k: Function1[typing.Any, typing.Any]) -> 'PartialFunction'[_PartialFunction__AndThen__A, typing.Any]: ...
        def apply(self, x: _PartialFunction__AndThen__A) -> _PartialFunction__AndThen__C: ...
        def apply$mcDD$sp(self, v1: float) -> float: ...
        def apply$mcDF$sp(self, v1: float) -> float: ...
        def apply$mcDI$sp(self, v1: int) -> float: ...
        def apply$mcDJ$sp(self, v1: int) -> float: ...
        def apply$mcFD$sp(self, v1: float) -> float: ...
        def apply$mcFF$sp(self, v1: float) -> float: ...
        def apply$mcFI$sp(self, v1: int) -> float: ...
        def apply$mcFJ$sp(self, v1: int) -> float: ...
        def apply$mcID$sp(self, v1: float) -> int: ...
        def apply$mcIF$sp(self, v1: float) -> int: ...
        def apply$mcII$sp(self, v1: int) -> int: ...
        def apply$mcIJ$sp(self, v1: int) -> int: ...
        def apply$mcJD$sp(self, v1: float) -> int: ...
        def apply$mcJF$sp(self, v1: float) -> int: ...
        def apply$mcJI$sp(self, v1: int) -> int: ...
        def apply$mcJJ$sp(self, v1: int) -> int: ...
        def apply$mcVD$sp(self, v1: float) -> None: ...
        def apply$mcVF$sp(self, v1: float) -> None: ...
        def apply$mcVI$sp(self, v1: int) -> None: ...
        def apply$mcVJ$sp(self, v1: int) -> None: ...
        def apply$mcZD$sp(self, v1: float) -> bool: ...
        def apply$mcZF$sp(self, v1: float) -> bool: ...
        def apply$mcZI$sp(self, v1: int) -> bool: ...
        def apply$mcZJ$sp(self, v1: int) -> bool: ...
        _applyOrElse__A1 = typing.TypeVar('_applyOrElse__A1')  # <A1>
        _applyOrElse__C1 = typing.TypeVar('_applyOrElse__C1')  # <C1>
        def applyOrElse(self, x: _applyOrElse__A1, default: Function1[_applyOrElse__A1, _applyOrElse__C1]) -> _applyOrElse__C1: ...
        _compose__A = typing.TypeVar('_compose__A')  # <A>
        def compose(self, g: Function1[typing.Any, typing.Any]) -> Function1[typing.Any, _PartialFunction__AndThen__C]: ...
        def isDefinedAt(self, x: _PartialFunction__AndThen__A) -> bool: ...
        def lift(self) -> Function1[_PartialFunction__AndThen__A, Option[_PartialFunction__AndThen__C]]: ...
        _orElse__A1 = typing.TypeVar('_orElse__A1')  # <A1>
        _orElse__B1 = typing.TypeVar('_orElse__B1')  # <B1>
        def orElse(self, that: 'PartialFunction'[_orElse__A1, _orElse__B1]) -> 'PartialFunction'[_orElse__A1, _orElse__B1]: ...
        _runWith__U = typing.TypeVar('_runWith__U')  # <U>
        def runWith(self, action: Function1[_PartialFunction__AndThen__C, _runWith__U]) -> Function1[_PartialFunction__AndThen__A, typing.Any]: ...
        def toString(self) -> str: ...
    class Lifted(scala.runtime.AbstractFunction1[_PartialFunction__Lifted__A, Option[_PartialFunction__Lifted__B]], Serializable, typing.Generic[_PartialFunction__Lifted__A, _PartialFunction__Lifted__B]):
        def __init__(self, pf: 'PartialFunction'[_PartialFunction__Lifted__A, _PartialFunction__Lifted__B]): ...
        def apply(self, x: _PartialFunction__Lifted__A) -> Option[_PartialFunction__Lifted__B]: ...
        def pf(self) -> 'PartialFunction'[_PartialFunction__Lifted__A, _PartialFunction__Lifted__B]: ...
    class OrElse(scala.runtime.AbstractPartialFunction[_PartialFunction__OrElse__A, _PartialFunction__OrElse__B], Serializable, typing.Generic[_PartialFunction__OrElse__A, _PartialFunction__OrElse__B]):
        def __init__(self, f1: 'PartialFunction'[_PartialFunction__OrElse__A, _PartialFunction__OrElse__B], f2: 'PartialFunction'[_PartialFunction__OrElse__A, _PartialFunction__OrElse__B]): ...
        _andThen__C = typing.TypeVar('_andThen__C')  # <C>
        def andThen(self, k: Function1[_PartialFunction__OrElse__B, _andThen__C]) -> 'PartialFunction.OrElse'[_PartialFunction__OrElse__A, _andThen__C]: ...
        def apply(self, x: _PartialFunction__OrElse__A) -> _PartialFunction__OrElse__B: ...
        _applyOrElse__A1 = typing.TypeVar('_applyOrElse__A1')  # <A1>
        _applyOrElse__B1 = typing.TypeVar('_applyOrElse__B1')  # <B1>
        def applyOrElse(self, x: _applyOrElse__A1, default: Function1[_applyOrElse__A1, _applyOrElse__B1]) -> _applyOrElse__B1: ...
        def isDefinedAt(self, x: _PartialFunction__OrElse__A) -> bool: ...
        _orElse__A1 = typing.TypeVar('_orElse__A1')  # <A1>
        _orElse__B1 = typing.TypeVar('_orElse__B1')  # <B1>
        def orElse(self, that: 'PartialFunction'[_orElse__A1, _orElse__B1]) -> 'PartialFunction.OrElse'[_orElse__A1, _orElse__B1]: ...
    class Unlifted(scala.runtime.AbstractPartialFunction[_PartialFunction__Unlifted__A, _PartialFunction__Unlifted__B], Serializable, typing.Generic[_PartialFunction__Unlifted__A, _PartialFunction__Unlifted__B]):
        def __init__(self, f: Function1[_PartialFunction__Unlifted__A, Option[_PartialFunction__Unlifted__B]]): ...
        _applyOrElse__A1 = typing.TypeVar('_applyOrElse__A1')  # <A1>
        _applyOrElse__B1 = typing.TypeVar('_applyOrElse__B1')  # <B1>
        def applyOrElse(self, x: _applyOrElse__A1, default: Function1[_applyOrElse__A1, _applyOrElse__B1]) -> _applyOrElse__B1: ...
        def isDefinedAt(self, x: _PartialFunction__Unlifted__A) -> bool: ...
        def lift(self) -> Function1[_PartialFunction__Unlifted__A, Option[_PartialFunction__Unlifted__B]]: ...

_Proxy__Typed__T = typing.TypeVar('_Proxy__Typed__T')  # <T>
class Proxy:
    @staticmethod
    def $init$($this: 'Proxy') -> None: ...
    def equals(self, that: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def self(self) -> typing.Any: ...
    def toString(self) -> str: ...
    class Typed(scala.Proxy, typing.Generic[_Proxy__Typed__T]):
        def equals(self, that: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def self(self) -> _Proxy__Typed__T: ...
        def toString(self) -> str: ...

_Specializable__Group__T = typing.TypeVar('_Specializable__Group__T')  # <T>
class Specializable:
    @staticmethod
    def AllNumeric() -> 'Specializable.Group'[Tuple7['Byte.', 'Short.', 'Int.', 'Long.', 'Char.', 'Float.', 'Double.']]: ...
    @staticmethod
    def BestOfBreed() -> 'Specializable.Group'[Tuple5['Int.', 'Double.', 'Boolean.', 'Unit.', 'Specializable']]: ...
    @staticmethod
    def Bits32AndUp() -> 'Specializable.Group'[Tuple4['Int.', 'Long.', 'Float.', 'Double.']]: ...
    @staticmethod
    def Everything() -> 'Specializable.Group'[Tuple10['Byte.', 'Short.', 'Int.', 'Long.', 'Char.', 'Float.', 'Double.', 'Boolean.', 'Unit.', 'Specializable']]: ...
    @staticmethod
    def Integral() -> 'Specializable.Group'[Tuple5['Byte.', 'Short.', 'Int.', 'Long.', 'Char.']]: ...
    @staticmethod
    def Primitives() -> 'Specializable.Group'[Tuple9['Byte.', 'Short.', 'Int.', 'Long.', 'Char.', 'Float.', 'Double.', 'Boolean.', 'Unit.']]: ...
    class Group(scala.Specializable.SpecializedGroup, typing.Generic[_Specializable__Group__T]):
        def __init__(self, value: _Specializable__Group__T): ...
    class SpecializedGroup: ...

class languageFeature:
    class dynamics: ...
    class dynamics$(scala.languageFeature.dynamics):
        MODULE$: typing.ClassVar['languageFeature.dynamics.'] = ...
        def __init__(self): ...
    class existentials: ...
    class existentials$(scala.languageFeature.existentials):
        MODULE$: typing.ClassVar['languageFeature.existentials.'] = ...
        def __init__(self): ...
    class experimental$:
        MODULE$: typing.ClassVar['languageFeature.experimental.'] = ...
        def __init__(self): ...
        class macros: ...
        class macros$(scala.languageFeature.experimental.macros):
            MODULE$: typing.ClassVar['languageFeature.experimental.macros.'] = ...
            def __init__(self): ...
    class higherKinds: ...
    class higherKinds$(scala.languageFeature.higherKinds):
        MODULE$: typing.ClassVar['languageFeature.higherKinds.'] = ...
        def __init__(self): ...
    class implicitConversions: ...
    class implicitConversions$(scala.languageFeature.implicitConversions):
        MODULE$: typing.ClassVar['languageFeature.implicitConversions.'] = ...
        def __init__(self): ...
    class postfixOps: ...
    class postfixOps$(scala.languageFeature.postfixOps):
        MODULE$: typing.ClassVar['languageFeature.postfixOps.'] = ...
        def __init__(self): ...
    class reflectiveCalls: ...
    class reflectiveCalls$(scala.languageFeature.reflectiveCalls):
        MODULE$: typing.ClassVar['languageFeature.reflectiveCalls.'] = ...
        def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scala")``.

    AnyVal: typing.Type[AnyVal]
    AnyValCompanion: typing.Type[AnyValCompanion]
    App: typing.Type[App]
    Array: typing.Type[Array]
    Boolean: typing.Type[Boolean]
    Byte: typing.Type[Byte]
    Char: typing.Type[Char]
    Cloneable: typing.Type[Cloneable]
    Console: typing.Type[Console]
    DelayedInit: typing.Type[DelayedInit]
    DeprecatedConsole: typing.Type[DeprecatedConsole]
    DeprecatedPredef: typing.Type[DeprecatedPredef]
    Double: typing.Type[Double]
    Dynamic: typing.Type[Dynamic]
    Enumeration: typing.Type[Enumeration]
    Equals: typing.Type[Equals]
    FallbackArrayBuilding: typing.Type[FallbackArrayBuilding]
    Float: typing.Type[Float]
    Function: typing.Type[Function]
    Function0: typing.Type[Function0]
    Function1: typing.Type[Function1]
    Function10: typing.Type[Function10]
    Function11: typing.Type[Function11]
    Function12: typing.Type[Function12]
    Function13: typing.Type[Function13]
    Function14: typing.Type[Function14]
    Function15: typing.Type[Function15]
    Function16: typing.Type[Function16]
    Function17: typing.Type[Function17]
    Function18: typing.Type[Function18]
    Function19: typing.Type[Function19]
    Function2: typing.Type[Function2]
    Function20: typing.Type[Function20]
    Function21: typing.Type[Function21]
    Function22: typing.Type[Function22]
    Function3: typing.Type[Function3]
    Function4: typing.Type[Function4]
    Function5: typing.Type[Function5]
    Function6: typing.Type[Function6]
    Function7: typing.Type[Function7]
    Function8: typing.Type[Function8]
    Function9: typing.Type[Function9]
    Immutable: typing.Type[Immutable]
    Int: typing.Type[Int]
    Long: typing.Type[Long]
    LowPriorityImplicits: typing.Type[LowPriorityImplicits]
    MatchError: typing.Type[MatchError]
    Mutable: typing.Type[Mutable]
    None: typing.Type[None]
    NotImplementedError: typing.Type[NotImplementedError]
    NotNull: typing.Type[NotNull]
    Option: typing.Type[Option]
    PartialFunction: typing.Type[PartialFunction]
    Predef: typing.Type[Predef]
    Product: typing.Type[Product]
    Product1: typing.Type[Product1]
    Product10: typing.Type[Product10]
    Product11: typing.Type[Product11]
    Product12: typing.Type[Product12]
    Product13: typing.Type[Product13]
    Product14: typing.Type[Product14]
    Product15: typing.Type[Product15]
    Product16: typing.Type[Product16]
    Product17: typing.Type[Product17]
    Product18: typing.Type[Product18]
    Product19: typing.Type[Product19]
    Product2: typing.Type[Product2]
    Product20: typing.Type[Product20]
    Product21: typing.Type[Product21]
    Product22: typing.Type[Product22]
    Product3: typing.Type[Product3]
    Product4: typing.Type[Product4]
    Product5: typing.Type[Product5]
    Product6: typing.Type[Product6]
    Product7: typing.Type[Product7]
    Product8: typing.Type[Product8]
    Product9: typing.Type[Product9]
    Proxy: typing.Type[Proxy]
    Responder: typing.Type[Responder]
    ScalaReflectionException: typing.Type[ScalaReflectionException]
    SerialVersionUID: typing.Type[SerialVersionUID]
    Serializable: typing.Type[Serializable]
    Short: typing.Type[Short]
    Some: typing.Type[Some]
    Specializable: typing.Type[Specializable]
    StringContext: typing.Type[StringContext]
    Symbol: typing.Type[Symbol]
    Tuple1: typing.Type[Tuple1]
    Tuple10: typing.Type[Tuple10]
    Tuple11: typing.Type[Tuple11]
    Tuple12: typing.Type[Tuple12]
    Tuple13: typing.Type[Tuple13]
    Tuple14: typing.Type[Tuple14]
    Tuple15: typing.Type[Tuple15]
    Tuple16: typing.Type[Tuple16]
    Tuple17: typing.Type[Tuple17]
    Tuple18: typing.Type[Tuple18]
    Tuple19: typing.Type[Tuple19]
    Tuple2: typing.Type[Tuple2]
    Tuple20: typing.Type[Tuple20]
    Tuple21: typing.Type[Tuple21]
    Tuple22: typing.Type[Tuple22]
    Tuple3: typing.Type[Tuple3]
    Tuple4: typing.Type[Tuple4]
    Tuple5: typing.Type[Tuple5]
    Tuple6: typing.Type[Tuple6]
    Tuple7: typing.Type[Tuple7]
    Tuple8: typing.Type[Tuple8]
    Tuple9: typing.Type[Tuple9]
    UninitializedError: typing.Type[UninitializedError]
    UninitializedFieldError: typing.Type[UninitializedFieldError]
    UniquenessCache: typing.Type[UniquenessCache]
    Unit: typing.Type[Unit]
    deprecated: typing.Type[deprecated]
    deprecatedInheritance: typing.Type[deprecatedInheritance]
    deprecatedName: typing.Type[deprecatedName]
    deprecatedOverriding: typing.Type[deprecatedOverriding]
    inline: typing.Type[inline]
    language: typing.Type[language]
    languageFeature: typing.Type[languageFeature]
    native: typing.Type[native]
    noinline: typing.Type[noinline]
    package: typing.Type[package]
    remote: typing.Type[remote]
    specialized: typing.Type[specialized]
    throws: typing.Type[throws]
    transient: typing.Type[transient]
    unchecked: typing.Type[unchecked]
    volatile: typing.Type[volatile]
    annotation: scala.annotation.__module_protocol__
    beans: scala.beans.__module_protocol__
    collection: scala.collection.__module_protocol__
    compat: scala.compat.__module_protocol__
    concurrent: scala.concurrent.__module_protocol__
    io: scala.io.__module_protocol__
    math: scala.math.__module_protocol__
    ref: scala.ref.__module_protocol__
    reflect: scala.reflect.__module_protocol__
    runtime: scala.runtime.__module_protocol__
    sys: scala.sys.__module_protocol__
    text: scala.text.__module_protocol__
    util: scala.util.__module_protocol__
