import java.lang
import scala
import scala.collection
import sigmastate
import sigmastate.serialization
import sigmastate.utils
import typing



_QuadrupleSerializer__S1 = typing.TypeVar('_QuadrupleSerializer__S1', bound=sigmastate.SType)  # <S1>
_QuadrupleSerializer__S2 = typing.TypeVar('_QuadrupleSerializer__S2', bound=sigmastate.SType)  # <S2>
_QuadrupleSerializer__S3 = typing.TypeVar('_QuadrupleSerializer__S3', bound=sigmastate.SType)  # <S3>
_QuadrupleSerializer__S4 = typing.TypeVar('_QuadrupleSerializer__S4', bound=sigmastate.SType)  # <S4>
class QuadrupleSerializer(sigmastate.serialization.ValueSerializer[sigmastate.Quadruple[_QuadrupleSerializer__S1, _QuadrupleSerializer__S2, _QuadrupleSerializer__S3, _QuadrupleSerializer__S4]], scala.Product, scala.Serializable, typing.Generic[_QuadrupleSerializer__S1, _QuadrupleSerializer__S2, _QuadrupleSerializer__S3, _QuadrupleSerializer__S4]):
    def __init__(self, opDesc: sigmastate.QuadrupleCompanion, cons: scala.Function3[sigmastate.Values.Value[_QuadrupleSerializer__S1], sigmastate.Values.Value[_QuadrupleSerializer__S2], sigmastate.Values.Value[_QuadrupleSerializer__S3], sigmastate.Values.Value[_QuadrupleSerializer__S4]]): ...
    _apply__S1 = typing.TypeVar('_apply__S1', bound=sigmastate.SType)  # <S1>
    _apply__S2 = typing.TypeVar('_apply__S2', bound=sigmastate.SType)  # <S2>
    _apply__S3 = typing.TypeVar('_apply__S3', bound=sigmastate.SType)  # <S3>
    _apply__S4 = typing.TypeVar('_apply__S4', bound=sigmastate.SType)  # <S4>
    @staticmethod
    def apply(opDesc: sigmastate.QuadrupleCompanion, cons: scala.Function3[sigmastate.Values.Value[_apply__S1], sigmastate.Values.Value[_apply__S2], sigmastate.Values.Value[_apply__S3], sigmastate.Values.Value[_apply__S4]]) -> 'QuadrupleSerializer'[_apply__S1, _apply__S2, _apply__S3, _apply__S4]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    def cons(self) -> scala.Function3[sigmastate.Values.Value[_QuadrupleSerializer__S1], sigmastate.Values.Value[_QuadrupleSerializer__S2], sigmastate.Values.Value[_QuadrupleSerializer__S3], sigmastate.Values.Value[_QuadrupleSerializer__S4]]: ...
    _copy__S1 = typing.TypeVar('_copy__S1', bound=sigmastate.SType)  # <S1>
    _copy__S2 = typing.TypeVar('_copy__S2', bound=sigmastate.SType)  # <S2>
    _copy__S3 = typing.TypeVar('_copy__S3', bound=sigmastate.SType)  # <S3>
    _copy__S4 = typing.TypeVar('_copy__S4', bound=sigmastate.SType)  # <S4>
    def copy(self, opDesc: sigmastate.QuadrupleCompanion, cons: scala.Function3[sigmastate.Values.Value[sigmastate.SType], sigmastate.Values.Value[sigmastate.SType], sigmastate.Values.Value[sigmastate.SType], sigmastate.Values.Value[sigmastate.SType]]) -> 'QuadrupleSerializer'[sigmastate.SType, sigmastate.SType, sigmastate.SType, sigmastate.SType]: ...
    _copy$default$1__S1 = typing.TypeVar('_copy$default$1__S1', bound=sigmastate.SType)  # <S1>
    _copy$default$1__S2 = typing.TypeVar('_copy$default$1__S2', bound=sigmastate.SType)  # <S2>
    _copy$default$1__S3 = typing.TypeVar('_copy$default$1__S3', bound=sigmastate.SType)  # <S3>
    _copy$default$1__S4 = typing.TypeVar('_copy$default$1__S4', bound=sigmastate.SType)  # <S4>
    def copy$default$1(self) -> sigmastate.QuadrupleCompanion: ...
    _copy$default$2__S1 = typing.TypeVar('_copy$default$2__S1', bound=sigmastate.SType)  # <S1>
    _copy$default$2__S2 = typing.TypeVar('_copy$default$2__S2', bound=sigmastate.SType)  # <S2>
    _copy$default$2__S3 = typing.TypeVar('_copy$default$2__S3', bound=sigmastate.SType)  # <S3>
    _copy$default$2__S4 = typing.TypeVar('_copy$default$2__S4', bound=sigmastate.SType)  # <S4>
    def copy$default$2(self) -> scala.Function3[sigmastate.Values.Value[sigmastate.SType], sigmastate.Values.Value[sigmastate.SType], sigmastate.Values.Value[sigmastate.SType], sigmastate.Values.Value[sigmastate.SType]]: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def firstInfo(self) -> sigmastate.utils.SigmaByteWriter.DataInfo[sigmastate.Values.Value[sigmastate.SType]]: ...
    def hashCode(self) -> int: ...
    def opDesc(self) -> sigmastate.QuadrupleCompanion: ...
    def parse(self, r: sigmastate.utils.SigmaByteReader) -> sigmastate.Values.Value[_QuadrupleSerializer__S4]: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> java.lang.String: ...
    def secondInfo(self) -> sigmastate.utils.SigmaByteWriter.DataInfo[sigmastate.Values.Value[sigmastate.SType]]: ...
    def serialize(self, obj: sigmastate.Quadruple[_QuadrupleSerializer__S1, _QuadrupleSerializer__S2, _QuadrupleSerializer__S3, _QuadrupleSerializer__S4], w: sigmastate.utils.SigmaByteWriter) -> None: ...
    def thirdInfo(self) -> sigmastate.utils.SigmaByteWriter.DataInfo[sigmastate.Values.Value[sigmastate.SType]]: ...
    def toString(self) -> java.lang.String: ...
    _unapply__S1 = typing.TypeVar('_unapply__S1', bound=sigmastate.SType)  # <S1>
    _unapply__S2 = typing.TypeVar('_unapply__S2', bound=sigmastate.SType)  # <S2>
    _unapply__S3 = typing.TypeVar('_unapply__S3', bound=sigmastate.SType)  # <S3>
    _unapply__S4 = typing.TypeVar('_unapply__S4', bound=sigmastate.SType)  # <S4>
    @staticmethod
    def unapply(x$0: 'QuadrupleSerializer'[_unapply__S1, _unapply__S2, _unapply__S3, _unapply__S4]) -> scala.Option[scala.Tuple2[sigmastate.QuadrupleCompanion, scala.Function3[sigmastate.Values.Value[_unapply__S1], sigmastate.Values.Value[_unapply__S2], sigmastate.Values.Value[_unapply__S3], sigmastate.Values.Value[_unapply__S4]]]]: ...

_Relation2Serializer__S1 = typing.TypeVar('_Relation2Serializer__S1', bound=sigmastate.SType)  # <S1>
_Relation2Serializer__S2 = typing.TypeVar('_Relation2Serializer__S2', bound=sigmastate.SType)  # <S2>
_Relation2Serializer__R = typing.TypeVar('_Relation2Serializer__R', bound=sigmastate.Values.Value)  # <R>
class Relation2Serializer(sigmastate.serialization.ValueSerializer[_Relation2Serializer__R], scala.Product, scala.Serializable, typing.Generic[_Relation2Serializer__S1, _Relation2Serializer__S2, _Relation2Serializer__R]):
    def __init__(self, opDesc: sigmastate.RelationCompanion, constructor: scala.Function2[sigmastate.Values.Value[_Relation2Serializer__S1], sigmastate.Values.Value[_Relation2Serializer__S2], sigmastate.Values.Value[sigmastate.SBoolean.]]): ...
    _apply__S1 = typing.TypeVar('_apply__S1', bound=sigmastate.SType)  # <S1>
    _apply__S2 = typing.TypeVar('_apply__S2', bound=sigmastate.SType)  # <S2>
    _apply__R = typing.TypeVar('_apply__R', bound=sigmastate.Values.Value)  # <R>
    @staticmethod
    def apply(opDesc: sigmastate.RelationCompanion, constructor: scala.Function2[sigmastate.Values.Value[_apply__S1], sigmastate.Values.Value[_apply__S2], sigmastate.Values.Value[sigmastate.SBoolean.]]) -> 'Relation2Serializer'[_apply__S1, _apply__S2, _apply__R]: ...
    def bitsInfo(self) -> sigmastate.utils.SigmaByteWriter.DataInfo[sigmastate.utils.SigmaByteWriter.Bits]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    def constructor(self) -> scala.Function2[sigmastate.Values.Value[_Relation2Serializer__S1], sigmastate.Values.Value[_Relation2Serializer__S2], sigmastate.Values.Value[sigmastate.SBoolean.]]: ...
    _copy__S1 = typing.TypeVar('_copy__S1', bound=sigmastate.SType)  # <S1>
    _copy__S2 = typing.TypeVar('_copy__S2', bound=sigmastate.SType)  # <S2>
    _copy__R = typing.TypeVar('_copy__R', bound=sigmastate.Values.Value)  # <R>
    def copy(self, opDesc: sigmastate.RelationCompanion, constructor: scala.Function2[sigmastate.Values.Value[sigmastate.SType], sigmastate.Values.Value[sigmastate.SType], sigmastate.Values.Value[sigmastate.SBoolean.]]) -> 'Relation2Serializer'[sigmastate.SType, sigmastate.SType, sigmastate.Values.Value]: ...
    _copy$default$1__S1 = typing.TypeVar('_copy$default$1__S1', bound=sigmastate.SType)  # <S1>
    _copy$default$1__S2 = typing.TypeVar('_copy$default$1__S2', bound=sigmastate.SType)  # <S2>
    _copy$default$1__R = typing.TypeVar('_copy$default$1__R', bound=sigmastate.Values.Value)  # <R>
    def copy$default$1(self) -> sigmastate.RelationCompanion: ...
    _copy$default$2__S1 = typing.TypeVar('_copy$default$2__S1', bound=sigmastate.SType)  # <S1>
    _copy$default$2__S2 = typing.TypeVar('_copy$default$2__S2', bound=sigmastate.SType)  # <S2>
    _copy$default$2__R = typing.TypeVar('_copy$default$2__R', bound=sigmastate.Values.Value)  # <R>
    def copy$default$2(self) -> scala.Function2[sigmastate.Values.Value[sigmastate.SType], sigmastate.Values.Value[sigmastate.SType], sigmastate.Values.Value[sigmastate.SBoolean.]]: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def leftArgInfo(self) -> sigmastate.utils.SigmaByteWriter.DataInfo[sigmastate.Values.Value[sigmastate.SType]]: ...
    def opCodeInfo(self) -> sigmastate.utils.SigmaByteWriter.DataInfo[typing.Any]: ...
    def opDesc(self) -> sigmastate.RelationCompanion: ...
    def parse(self, r: sigmastate.utils.SigmaByteReader) -> _Relation2Serializer__R: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> java.lang.String: ...
    def rightArgInfo(self) -> sigmastate.utils.SigmaByteWriter.DataInfo[sigmastate.Values.Value[sigmastate.SType]]: ...
    def serialize(self, obj: _Relation2Serializer__R, w: sigmastate.utils.SigmaByteWriter) -> None: ...
    def toString(self) -> java.lang.String: ...
    _unapply__S1 = typing.TypeVar('_unapply__S1', bound=sigmastate.SType)  # <S1>
    _unapply__S2 = typing.TypeVar('_unapply__S2', bound=sigmastate.SType)  # <S2>
    _unapply__R = typing.TypeVar('_unapply__R', bound=sigmastate.Values.Value)  # <R>
    @staticmethod
    def unapply(x$0: 'Relation2Serializer'[_unapply__S1, _unapply__S2, _unapply__R]) -> scala.Option[scala.Tuple2[sigmastate.RelationCompanion, scala.Function2[sigmastate.Values.Value[_unapply__S1], sigmastate.Values.Value[_unapply__S2], sigmastate.Values.Value[sigmastate.SBoolean.]]]]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("sigmastate.serialization.trees")``.

    QuadrupleSerializer: typing.Type[QuadrupleSerializer]
    Relation2Serializer: typing.Type[Relation2Serializer]