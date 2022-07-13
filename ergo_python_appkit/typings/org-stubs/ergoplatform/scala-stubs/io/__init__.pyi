import java.io
import java.lang
import java.net
import java.nio.charset
import jpype.protocol
import scala
import scala.collection
import scala.collection.generic
import scala.collection.immutable
import scala.collection.mutable
import scala.math
import scala.reflect
import scala.runtime
import typing



class AnsiColor:
    @staticmethod
    def $init$($this: 'AnsiColor') -> None: ...
    def BLACK(self) -> java.lang.String: ...
    def BLACK_B(self) -> java.lang.String: ...
    def BLINK(self) -> java.lang.String: ...
    def BLUE(self) -> java.lang.String: ...
    def BLUE_B(self) -> java.lang.String: ...
    def BOLD(self) -> java.lang.String: ...
    def CYAN(self) -> java.lang.String: ...
    def CYAN_B(self) -> java.lang.String: ...
    def GREEN(self) -> java.lang.String: ...
    def GREEN_B(self) -> java.lang.String: ...
    def INVISIBLE(self) -> java.lang.String: ...
    def MAGENTA(self) -> java.lang.String: ...
    def MAGENTA_B(self) -> java.lang.String: ...
    def RED(self) -> java.lang.String: ...
    def RED_B(self) -> java.lang.String: ...
    def RESET(self) -> java.lang.String: ...
    def REVERSED(self) -> java.lang.String: ...
    def UNDERLINED(self) -> java.lang.String: ...
    def WHITE(self) -> java.lang.String: ...
    def WHITE_B(self) -> java.lang.String: ...
    def YELLOW(self) -> java.lang.String: ...
    def YELLOW_B(self) -> java.lang.String: ...

class Codec:
    def __init__(self, charSet: java.nio.charset.Charset): ...
    @staticmethod
    def ISO8859() -> 'Codec': ...
    @staticmethod
    def UTF8() -> 'Codec': ...
    @typing.overload
    @staticmethod
    def apply(encoding: typing.Union[java.lang.String, str]) -> 'Codec': ...
    @typing.overload
    @staticmethod
    def apply(charSet: java.nio.charset.Charset) -> 'Codec': ...
    @typing.overload
    @staticmethod
    def apply(decoder: java.nio.charset.CharsetDecoder) -> 'Codec': ...
    def charSet(self) -> java.nio.charset.Charset: ...
    @staticmethod
    def charset2codec(c: java.nio.charset.Charset) -> 'Codec': ...
    def decoder(self) -> java.nio.charset.CharsetDecoder: ...
    @staticmethod
    def decoder2codec(cd: java.nio.charset.CharsetDecoder) -> 'Codec': ...
    def decodingReplaceWith(self, newReplacement: typing.Union[java.lang.String, str]) -> 'Codec': ...
    @staticmethod
    def default() -> 'Codec': ...
    @staticmethod
    def defaultCharsetCodec() -> 'Codec': ...
    def encoder(self) -> java.nio.charset.CharsetEncoder: ...
    def encodingReplaceWith(self, newReplacement: typing.List[int]) -> 'Codec': ...
    @staticmethod
    def fallbackSystemCodec() -> 'Codec': ...
    @staticmethod
    def fileEncodingCodec() -> 'Codec': ...
    @typing.overload
    @staticmethod
    def fromUTF8(bytes: typing.List[int]) -> typing.List[str]: ...
    @typing.overload
    @staticmethod
    def fromUTF8(bytes: typing.List[int], offset: int, len: int) -> typing.List[str]: ...
    def name(self) -> java.lang.String: ...
    def onCodingException(self, handler: scala.Function1[java.nio.charset.CharacterCodingException, typing.Any]) -> 'Codec': ...
    def onMalformedInput(self, newAction: java.nio.charset.CodingErrorAction) -> 'Codec': ...
    def onUnmappableCharacter(self, newAction: java.nio.charset.CodingErrorAction) -> 'Codec': ...
    @staticmethod
    def string2codec(s: typing.Union[java.lang.String, str]) -> 'Codec': ...
    def toString(self) -> java.lang.String: ...
    @typing.overload
    @staticmethod
    def toUTF8(chars: typing.List[str], offset: int, len: int) -> typing.List[int]: ...
    @typing.overload
    @staticmethod
    def toUTF8(cs: typing.Union[java.lang.CharSequence, str]) -> typing.List[int]: ...
    def wrap(self, body: scala.Function0[typing.Any]) -> int: ...

class LowPriorityCodecImplicits:
    @staticmethod
    def $init$($this: 'LowPriorityCodecImplicits') -> None: ...
    def fallbackSystemCodec(self) -> Codec: ...

class Position:
    def __init__(self): ...
    def COLUMN_BITS(self) -> int: ...
    def COLUMN_MASK(self) -> int: ...
    def LINE_BITS(self) -> int: ...
    def LINE_MASK(self) -> int: ...
    def checkInput(self, line: int, column: int) -> None: ...
    def column(self, pos: int) -> int: ...
    def encode(self, line: int, column: int) -> int: ...
    def line(self, pos: int) -> int: ...
    @typing.overload
    def toString(self) -> java.lang.String: ...
    @typing.overload
    def toString(self, pos: int) -> java.lang.String: ...

class StdIn:
    @staticmethod
    def $init$($this: 'StdIn') -> None: ...
    def readBoolean(self) -> bool: ...
    def readByte(self) -> int: ...
    def readChar(self) -> str: ...
    def readDouble(self) -> float: ...
    def readFloat(self) -> float: ...
    def readInt(self) -> int: ...
    @typing.overload
    def readLine(self) -> java.lang.String: ...
    @typing.overload
    def readLine(self, text: typing.Union[java.lang.String, str], args: scala.collection.Seq[typing.Any]) -> java.lang.String: ...
    def readLong(self) -> int: ...
    def readShort(self) -> int: ...
    def readf(self, format: typing.Union[java.lang.String, str]) -> scala.collection.immutable.List[typing.Any]: ...
    def readf1(self, format: typing.Union[java.lang.String, str]) -> typing.Any: ...
    def readf2(self, format: typing.Union[java.lang.String, str]) -> scala.Tuple2[typing.Any, typing.Any]: ...
    def readf3(self, format: typing.Union[java.lang.String, str]) -> scala.Tuple3[typing.Any, typing.Any, typing.Any]: ...

class BufferedSource(scala.io.Source):
    @typing.overload
    def __init__(self, inputStream: java.io.InputStream, bufferSize: int, codec: Codec): ...
    @typing.overload
    def __init__(self, inputStream: java.io.InputStream, codec: Codec): ...
    def bufferedReader(self) -> java.io.BufferedReader: ...
    def codec(self) -> Codec: ...
    def getLines(self) -> scala.collection.Iterator[java.lang.String]: ...
    def iter(self) -> scala.collection.Iterator[typing.Any]: ...
    @typing.overload
    def mkString(self) -> java.lang.String: ...
    @typing.overload
    def mkString(self, sep: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    @typing.overload
    def mkString(self, start: typing.Union[java.lang.String, str], sep: typing.Union[java.lang.String, str], end: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    def reader(self) -> java.io.InputStreamReader: ...
    def scala$io$BufferedSource$$decachedReader(self) -> java.io.BufferedReader: ...
    class BufferedLineIterator(scala.collection.AbstractIterator[java.lang.String]):
        $outer: 'BufferedSource' = ...
        def __init__(self, $outer: 'BufferedSource'): ...
        def hasNext(self) -> bool: ...
        def next(self) -> java.lang.String: ...
        def nextLine(self) -> java.lang.String: ...
        def nextLine_$eq(self, x$1: typing.Union[java.lang.String, str]) -> None: ...

class Source(scala.collection.Iterator[typing.Any], java.io.Closeable):
    def __init__(self): ...
    _$colon$bslash__B = typing.TypeVar('_$colon$bslash__B')  # <B>
    def $colon$bslash(self, z: _.colon.bslash__B, op: scala.Function2[typing.Any, _.colon.bslash__B, _.colon.bslash__B]) -> _.colon.bslash__B: ...
    _$div$colon__B = typing.TypeVar('_$div$colon__B')  # <B>
    def $div$colon(self, z: _.div.colon__B, op: scala.Function2[_.div.colon__B, typing.Any, _.div.colon__B]) -> _.div.colon__B: ...
    _$plus$plus__B = typing.TypeVar('_$plus$plus__B')  # <B>
    def $plus$plus(self, that: scala.Function0[scala.collection.GenTraversableOnce[_.plus.plus__B]]) -> scala.collection.Iterator[_.plus.plus__B]: ...
    @staticmethod
    def DefaultBufSize() -> int: ...
    def NoPositioner(self) -> 'Source.NoPositioner.': ...
    def RelaxedPosition(self) -> 'Source.RelaxedPosition.': ...
    def RelaxedPositioner(self) -> 'Source.RelaxedPositioner.': ...
    @typing.overload
    def addString(self, b: scala.collection.mutable.StringBuilder) -> scala.collection.mutable.StringBuilder: ...
    @typing.overload
    def addString(self, b: scala.collection.mutable.StringBuilder, sep: typing.Union[java.lang.String, str]) -> scala.collection.mutable.StringBuilder: ...
    @typing.overload
    def addString(self, b: scala.collection.mutable.StringBuilder, start: typing.Union[java.lang.String, str], sep: typing.Union[java.lang.String, str], end: typing.Union[java.lang.String, str]) -> scala.collection.mutable.StringBuilder: ...
    _aggregate__B = typing.TypeVar('_aggregate__B')  # <B>
    def aggregate(self, z: scala.Function0[_aggregate__B], seqop: scala.Function2[_aggregate__B, typing.Any, _aggregate__B], combop: scala.Function2[_aggregate__B, _aggregate__B, _aggregate__B]) -> _aggregate__B: ...
    def buffered(self) -> scala.collection.BufferedIterator[typing.Any]: ...
    def ch(self) -> str: ...
    def close(self) -> None: ...
    _collect__B = typing.TypeVar('_collect__B')  # <B>
    def collect(self, pf: scala.PartialFunction[typing.Any, _collect__B]) -> scala.collection.Iterator[_collect__B]: ...
    _collectFirst__B = typing.TypeVar('_collectFirst__B')  # <B>
    def collectFirst(self, pf: scala.PartialFunction[typing.Any, _collectFirst__B]) -> scala.Option[_collectFirst__B]: ...
    def contains(self, elem: typing.Any) -> bool: ...
    _copyToArray_0__B = typing.TypeVar('_copyToArray_0__B')  # <B>
    _copyToArray_1__B = typing.TypeVar('_copyToArray_1__B')  # <B>
    _copyToArray_2__B = typing.TypeVar('_copyToArray_2__B')  # <B>
    @typing.overload
    def copyToArray(self, xs: typing.Any) -> None: ...
    @typing.overload
    def copyToArray(self, xs: typing.Any, start: int) -> None: ...
    @typing.overload
    def copyToArray(self, xs: typing.Any, start: int, len: int) -> None: ...
    _copyToBuffer__B = typing.TypeVar('_copyToBuffer__B')  # <B>
    def copyToBuffer(self, dest: scala.collection.mutable.Buffer[_copyToBuffer__B]) -> None: ...
    _corresponds__B = typing.TypeVar('_corresponds__B')  # <B>
    def corresponds(self, that: scala.collection.GenTraversableOnce[_corresponds__B], p: scala.Function2[typing.Any, _corresponds__B, typing.Any]) -> bool: ...
    def count(self, p: scala.Function1[typing.Any, typing.Any]) -> int: ...
    @staticmethod
    def createBufferedSource(inputStream: java.io.InputStream, bufferSize: int, reset: scala.Function0['Source'], close: scala.Function0[scala.runtime.BoxedUnit], codec: Codec) -> BufferedSource: ...
    @staticmethod
    def createBufferedSource$default$2() -> int: ...
    @staticmethod
    def createBufferedSource$default$3() -> scala.Function0['Source']: ...
    @staticmethod
    def createBufferedSource$default$4() -> scala.Function0[scala.runtime.BoxedUnit]: ...
    def descr(self) -> java.lang.String: ...
    def descr_$eq(self, x$1: typing.Union[java.lang.String, str]) -> None: ...
    def drop(self, n: int) -> scala.collection.Iterator[typing.Any]: ...
    def dropWhile(self, p: scala.Function1[typing.Any, typing.Any]) -> scala.collection.Iterator[typing.Any]: ...
    def duplicate(self) -> scala.Tuple2[scala.collection.Iterator[typing.Any], scala.collection.Iterator[typing.Any]]: ...
    def exists(self, p: scala.Function1[typing.Any, typing.Any]) -> bool: ...
    def filter(self, p: scala.Function1[typing.Any, typing.Any]) -> scala.collection.Iterator[typing.Any]: ...
    def filterNot(self, p: scala.Function1[typing.Any, typing.Any]) -> scala.collection.Iterator[typing.Any]: ...
    def find(self, p: scala.Function1[typing.Any, typing.Any]) -> scala.Option[typing.Any]: ...
    _flatMap__B = typing.TypeVar('_flatMap__B')  # <B>
    def flatMap(self, f: scala.Function1[typing.Any, scala.collection.GenTraversableOnce[_flatMap__B]]) -> scala.collection.Iterator[_flatMap__B]: ...
    _fold__A1 = typing.TypeVar('_fold__A1')  # <A1>
    def fold(self, z: _fold__A1, op: scala.Function2[_fold__A1, _fold__A1, _fold__A1]) -> _fold__A1: ...
    _foldLeft__B = typing.TypeVar('_foldLeft__B')  # <B>
    def foldLeft(self, z: _foldLeft__B, op: scala.Function2[_foldLeft__B, typing.Any, _foldLeft__B]) -> _foldLeft__B: ...
    _foldRight__B = typing.TypeVar('_foldRight__B')  # <B>
    def foldRight(self, z: _foldRight__B, op: scala.Function2[typing.Any, _foldRight__B, _foldRight__B]) -> _foldRight__B: ...
    def forall(self, p: scala.Function1[typing.Any, typing.Any]) -> bool: ...
    _foreach__U = typing.TypeVar('_foreach__U')  # <U>
    def foreach(self, f: scala.Function1[typing.Any, _foreach__U]) -> None: ...
    @typing.overload
    @staticmethod
    def fromBytes(bytes: typing.List[int], enc: typing.Union[java.lang.String, str]) -> 'Source': ...
    @typing.overload
    @staticmethod
    def fromBytes(bytes: typing.List[int], codec: Codec) -> 'Source': ...
    @staticmethod
    def fromChar(c: str) -> 'Source': ...
    @staticmethod
    def fromChars(chars: typing.List[str]) -> 'Source': ...
    @typing.overload
    @staticmethod
    def fromFile(file: typing.Union[java.io.File, jpype.protocol.SupportsPath], bufferSize: int, codec: Codec) -> BufferedSource: ...
    @typing.overload
    @staticmethod
    def fromFile(file: typing.Union[java.io.File, jpype.protocol.SupportsPath], enc: typing.Union[java.lang.String, str]) -> BufferedSource: ...
    @typing.overload
    @staticmethod
    def fromFile(file: typing.Union[java.io.File, jpype.protocol.SupportsPath], enc: typing.Union[java.lang.String, str], bufferSize: int) -> BufferedSource: ...
    @typing.overload
    @staticmethod
    def fromFile(file: typing.Union[java.io.File, jpype.protocol.SupportsPath], codec: Codec) -> BufferedSource: ...
    @typing.overload
    @staticmethod
    def fromFile(name: typing.Union[java.lang.String, str], enc: typing.Union[java.lang.String, str]) -> BufferedSource: ...
    @typing.overload
    @staticmethod
    def fromFile(name: typing.Union[java.lang.String, str], codec: Codec) -> BufferedSource: ...
    @typing.overload
    @staticmethod
    def fromFile(uri: java.net.URI, enc: typing.Union[java.lang.String, str]) -> BufferedSource: ...
    @typing.overload
    @staticmethod
    def fromFile(uri: java.net.URI, codec: Codec) -> BufferedSource: ...
    @typing.overload
    @staticmethod
    def fromInputStream(is_: java.io.InputStream, enc: typing.Union[java.lang.String, str]) -> BufferedSource: ...
    @typing.overload
    @staticmethod
    def fromInputStream(is_: java.io.InputStream, codec: Codec) -> BufferedSource: ...
    @staticmethod
    def fromIterable(iterable: scala.collection.Iterable[typing.Any]) -> 'Source': ...
    @staticmethod
    def fromRawBytes(bytes: typing.List[int]) -> 'Source': ...
    @staticmethod
    def fromResource(resource: typing.Union[java.lang.String, str], classLoader: java.lang.ClassLoader, codec: Codec) -> BufferedSource: ...
    @staticmethod
    def fromResource$default$2() -> java.lang.ClassLoader: ...
    @staticmethod
    def fromString(s: typing.Union[java.lang.String, str]) -> 'Source': ...
    @staticmethod
    def fromURI(uri: java.net.URI, codec: Codec) -> BufferedSource: ...
    @typing.overload
    @staticmethod
    def fromURL(s: typing.Union[java.lang.String, str], enc: typing.Union[java.lang.String, str]) -> BufferedSource: ...
    @typing.overload
    @staticmethod
    def fromURL(s: typing.Union[java.lang.String, str], codec: Codec) -> BufferedSource: ...
    @typing.overload
    @staticmethod
    def fromURL(url: java.net.URL, enc: typing.Union[java.lang.String, str]) -> BufferedSource: ...
    @typing.overload
    @staticmethod
    def fromURL(url: java.net.URL, codec: Codec) -> BufferedSource: ...
    def getLines(self) -> scala.collection.Iterator[java.lang.String]: ...
    _grouped__B = typing.TypeVar('_grouped__B')  # <B>
    def grouped(self, size: int) -> scala.collection.Iterator.GroupedIterator[_grouped__B]: ...
    def hasDefiniteSize(self) -> bool: ...
    def hasNext(self) -> bool: ...
    _indexOf_0__B = typing.TypeVar('_indexOf_0__B')  # <B>
    _indexOf_1__B = typing.TypeVar('_indexOf_1__B')  # <B>
    @typing.overload
    def indexOf(self, elem: _indexOf_0__B) -> int: ...
    @typing.overload
    def indexOf(self, elem: _indexOf_1__B, from_: int) -> int: ...
    @typing.overload
    def indexWhere(self, p: scala.Function1[typing.Any, typing.Any]) -> int: ...
    @typing.overload
    def indexWhere(self, p: scala.Function1[typing.Any, typing.Any], from_: int) -> int: ...
    def isEmpty(self) -> bool: ...
    def isTraversableAgain(self) -> bool: ...
    def iter(self) -> scala.collection.Iterator[typing.Any]: ...
    def length(self) -> int: ...
    _map__B = typing.TypeVar('_map__B')  # <B>
    def map(self, f: scala.Function1[typing.Any, _map__B]) -> scala.collection.Iterator[_map__B]: ...
    def max(self, cmp: scala.math.Ordering) -> typing.Any: ...
    def maxBy(self, f: scala.Function1, cmp: scala.math.Ordering) -> typing.Any: ...
    def min(self, cmp: scala.math.Ordering) -> typing.Any: ...
    def minBy(self, f: scala.Function1, cmp: scala.math.Ordering) -> typing.Any: ...
    @typing.overload
    def mkString(self) -> java.lang.String: ...
    @typing.overload
    def mkString(self, sep: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    @typing.overload
    def mkString(self, start: typing.Union[java.lang.String, str], sep: typing.Union[java.lang.String, str], end: typing.Union[java.lang.String, str]) -> java.lang.String: ...
    def nerrors(self) -> int: ...
    def nerrors_$eq(self, x$1: int) -> None: ...
    def next(self) -> str: ...
    def nonEmpty(self) -> bool: ...
    def nwarnings(self) -> int: ...
    def nwarnings_$eq(self, x$1: int) -> None: ...
    _padTo__A1 = typing.TypeVar('_padTo__A1')  # <A1>
    def padTo(self, len: int, elem: _padTo__A1) -> scala.collection.Iterator[_padTo__A1]: ...
    def partition(self, p: scala.Function1[typing.Any, typing.Any]) -> scala.Tuple2[scala.collection.Iterator[typing.Any], scala.collection.Iterator[typing.Any]]: ...
    _patch__B = typing.TypeVar('_patch__B')  # <B>
    def patch(self, from_: int, patchElems: scala.collection.Iterator[_patch__B], replaced: int) -> scala.collection.Iterator[_patch__B]: ...
    def pos(self) -> int: ...
    _product__B = typing.TypeVar('_product__B')  # <B>
    def product(self, num: scala.math.Numeric[_product__B]) -> _product__B: ...
    _reduce__A1 = typing.TypeVar('_reduce__A1')  # <A1>
    def reduce(self, op: scala.Function2[_reduce__A1, _reduce__A1, _reduce__A1]) -> _reduce__A1: ...
    _reduceLeft__B = typing.TypeVar('_reduceLeft__B')  # <B>
    def reduceLeft(self, op: scala.Function2[_reduceLeft__B, typing.Any, _reduceLeft__B]) -> _reduceLeft__B: ...
    _reduceLeftOption__B = typing.TypeVar('_reduceLeftOption__B')  # <B>
    def reduceLeftOption(self, op: scala.Function2[_reduceLeftOption__B, typing.Any, _reduceLeftOption__B]) -> scala.Option[_reduceLeftOption__B]: ...
    _reduceOption__A1 = typing.TypeVar('_reduceOption__A1')  # <A1>
    def reduceOption(self, op: scala.Function2[_reduceOption__A1, _reduceOption__A1, _reduceOption__A1]) -> scala.Option[_reduceOption__A1]: ...
    _reduceRight__B = typing.TypeVar('_reduceRight__B')  # <B>
    def reduceRight(self, op: scala.Function2[typing.Any, _reduceRight__B, _reduceRight__B]) -> _reduceRight__B: ...
    _reduceRightOption__B = typing.TypeVar('_reduceRightOption__B')  # <B>
    def reduceRightOption(self, op: scala.Function2[typing.Any, _reduceRightOption__B, _reduceRightOption__B]) -> scala.Option[_reduceRightOption__B]: ...
    def report(self, pos: int, msg: typing.Union[java.lang.String, str], out: java.io.PrintStream) -> None: ...
    def reportError(self, pos: int, msg: typing.Union[java.lang.String, str], out: java.io.PrintStream) -> None: ...
    def reportError$default$3(self) -> java.io.PrintStream: ...
    def reportWarning(self, pos: int, msg: typing.Union[java.lang.String, str], out: java.io.PrintStream) -> None: ...
    def reportWarning$default$3(self) -> java.io.PrintStream: ...
    def reset(self) -> 'Source': ...
    def reversed(self) -> scala.collection.immutable.List[typing.Any]: ...
    def sameElements(self, that: scala.collection.Iterator[typing.Any]) -> bool: ...
    _scanLeft__B = typing.TypeVar('_scanLeft__B')  # <B>
    def scanLeft(self, z: _scanLeft__B, op: scala.Function2[_scanLeft__B, typing.Any, _scanLeft__B]) -> scala.collection.Iterator[_scanLeft__B]: ...
    _scanRight__B = typing.TypeVar('_scanRight__B')  # <B>
    def scanRight(self, z: _scanRight__B, op: scala.Function2[typing.Any, _scanRight__B, _scanRight__B]) -> scala.collection.Iterator[_scanRight__B]: ...
    def seq(self) -> scala.collection.Iterator[typing.Any]: ...
    def size(self) -> int: ...
    def sizeHintIfCheap(self) -> int: ...
    def slice(self, from_: int, until: int) -> scala.collection.Iterator[typing.Any]: ...
    def sliceIterator(self, from_: int, until: int) -> scala.collection.Iterator[typing.Any]: ...
    _sliding__B = typing.TypeVar('_sliding__B')  # <B>
    def sliding(self, size: int, step: int) -> scala.collection.Iterator.GroupedIterator[_sliding__B]: ...
    _sliding$default$2__B = typing.TypeVar('_sliding$default$2__B')  # <B>
    def sliding$default$2(self) -> int: ...
    def span(self, p: scala.Function1[typing.Any, typing.Any]) -> scala.Tuple2[scala.collection.Iterator[typing.Any], scala.collection.Iterator[typing.Any]]: ...
    @staticmethod
    def stdin() -> BufferedSource: ...
    _sum__B = typing.TypeVar('_sum__B')  # <B>
    def sum(self, num: scala.math.Numeric[_sum__B]) -> _sum__B: ...
    def take(self, n: int) -> scala.collection.Iterator[typing.Any]: ...
    def takeWhile(self, p: scala.Function1[typing.Any, typing.Any]) -> scala.collection.Iterator[typing.Any]: ...
    _to__Col = typing.TypeVar('_to__Col')  # <Col>
    def to(self, cbf: scala.collection.generic.CanBuildFrom[scala.runtime.Nothing., typing.Any, _to__Col]) -> _to__Col: ...
    _toArray__B = typing.TypeVar('_toArray__B')  # <B>
    def toArray(self, evidence$1: scala.reflect.ClassTag[_toArray__B]) -> typing.Any: ...
    _toBuffer__B = typing.TypeVar('_toBuffer__B')  # <B>
    def toBuffer(self) -> scala.collection.mutable.Buffer[_toBuffer__B]: ...
    def toIndexedSeq(self) -> scala.collection.immutable.IndexedSeq[typing.Any]: ...
    def toIterable(self) -> scala.collection.Iterable[typing.Any]: ...
    def toIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def toList(self) -> scala.collection.immutable.List[typing.Any]: ...
    _toMap__T = typing.TypeVar('_toMap__T')  # <T>
    _toMap__U = typing.TypeVar('_toMap__U')  # <U>
    def toMap(self, ev: scala.Predef..less.colon.less[typing.Any, scala.Tuple2[_toMap__T, _toMap__U]]) -> scala.collection.immutable.Map[_toMap__T, _toMap__U]: ...
    def toSeq(self) -> scala.collection.Seq[typing.Any]: ...
    _toSet__B = typing.TypeVar('_toSet__B')  # <B>
    def toSet(self) -> scala.collection.immutable.Set[_toSet__B]: ...
    def toStream(self) -> scala.collection.immutable.Stream[typing.Any]: ...
    def toString(self) -> java.lang.String: ...
    def toTraversable(self) -> scala.collection.Traversable[typing.Any]: ...
    def toVector(self) -> scala.collection.immutable.Vector[typing.Any]: ...
    def withClose(self, f: scala.Function0[scala.runtime.BoxedUnit]) -> 'Source': ...
    def withDescription(self, text: typing.Union[java.lang.String, str]) -> 'Source': ...
    def withFilter(self, p: scala.Function1[typing.Any, typing.Any]) -> scala.collection.Iterator[typing.Any]: ...
    @typing.overload
    def withPositioning(self, on: bool) -> 'Source': ...
    @typing.overload
    def withPositioning(self, pos: 'Source.Positioner') -> 'Source': ...
    def withReset(self, f: scala.Function0['Source']) -> 'Source': ...
    _zip__B = typing.TypeVar('_zip__B')  # <B>
    def zip(self, that: scala.collection.Iterator[_zip__B]) -> scala.collection.Iterator[scala.Tuple2[typing.Any, _zip__B]]: ...
    _zipAll__B = typing.TypeVar('_zipAll__B')  # <B>
    _zipAll__A1 = typing.TypeVar('_zipAll__A1')  # <A1>
    _zipAll__B1 = typing.TypeVar('_zipAll__B1')  # <B1>
    def zipAll(self, that: scala.collection.Iterator[_zipAll__B], thisElem: _zipAll__A1, thatElem: _zipAll__B1) -> scala.collection.Iterator[scala.Tuple2[_zipAll__A1, _zipAll__B1]]: ...
    def zipWithIndex(self) -> scala.collection.Iterator[scala.Tuple2[typing.Any, typing.Any]]: ...
    class LineIterator(scala.collection.AbstractIterator[java.lang.String]):
        $outer: 'Source' = ...
        def __init__(self, $outer: 'Source'): ...
        def getc(self) -> bool: ...
        def hasNext(self) -> bool: ...
        def isNewline(self, ch: str) -> bool: ...
        def iter(self) -> scala.collection.BufferedIterator[typing.Any]: ...
        def next(self) -> java.lang.String: ...
    class NoPositioner$(scala.io.Source.Positioner):
        def __init__(self, $outer: 'Source'): ...
        def next(self) -> str: ...
    class Positioner:
        $outer: 'Source' = ...
        @typing.overload
        def __init__(self, $outer: 'Source'): ...
        @typing.overload
        def __init__(self, $outer: 'Source', encoder: Position): ...
        def ccol(self) -> int: ...
        def ccol_$eq(self, x$1: int) -> None: ...
        def ch(self) -> str: ...
        def ch_$eq(self, x$1: str) -> None: ...
        def cline(self) -> int: ...
        def cline_$eq(self, x$1: int) -> None: ...
        def next(self) -> str: ...
        def pos(self) -> int: ...
        def pos_$eq(self, x$1: int) -> None: ...
        def tabinc(self) -> int: ...
        def tabinc_$eq(self, x$1: int) -> None: ...
    class RelaxedPosition$(Position):
        def __init__(self, $outer: 'Source'): ...
        def checkInput(self, line: int, column: int) -> None: ...
    class RelaxedPositioner$(scala.io.Source.Positioner):
        def __init__(self, $outer: 'Source'): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scala.io")``.

    AnsiColor: typing.Type[AnsiColor]
    BufferedSource: typing.Type[BufferedSource]
    Codec: typing.Type[Codec]
    LowPriorityCodecImplicits: typing.Type[LowPriorityCodecImplicits]
    Position: typing.Type[Position]
    Source: typing.Type[Source]
    StdIn: typing.Type[StdIn]
