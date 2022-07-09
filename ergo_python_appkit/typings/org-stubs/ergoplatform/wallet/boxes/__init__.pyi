import java.lang
import org
import org.ergoplatform
import scala
import scala.collection
import scala.collection.immutable
import scala.collection.mutable
import scala.runtime
import scala.util
import scorex.util.serialization
import typing



_BoxSelector__BoxSelectionResult__T = typing.TypeVar('_BoxSelector__BoxSelectionResult__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
class BoxSelector:
    @staticmethod
    def $init$($this: 'BoxSelector') -> None: ...
    @staticmethod
    def MinBoxValue() -> int: ...
    @staticmethod
    def ScanDepthFactor() -> int: ...
    _select_0__T = typing.TypeVar('_select_0__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
    _select_1__T = typing.TypeVar('_select_1__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
    @typing.overload
    def select(self, inputBoxes: scala.collection.Iterator[_select_0__T], filterFn: scala.Function1[_select_0__T, typing.Any], targetBalance: int, targetAssets: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> scala.util.Either['BoxSelector.BoxSelectionError', 'BoxSelector.BoxSelectionResult'[_select_0__T]]: ...
    @typing.overload
    def select(self, inputBoxes: scala.collection.Iterator[_select_1__T], targetBalance: int, targetAssets: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> scala.util.Either['BoxSelector.BoxSelectionError', 'BoxSelector.BoxSelectionResult'[_select_1__T]]: ...
    class BoxSelectionError:
        def message(self) -> java.lang.String: ...
    class BoxSelectionResult(scala.Product, scala.Serializable, typing.Generic[_BoxSelector__BoxSelectionResult__T]):
        def __init__(self, boxes: scala.collection.Seq[_BoxSelector__BoxSelectionResult__T], changeBoxes: scala.collection.Seq[org.ergoplatform.ErgoBoxAssets]): ...
        def boxes(self) -> scala.collection.Seq[_BoxSelector__BoxSelectionResult__T]: ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def changeBoxes(self) -> scala.collection.Seq[org.ergoplatform.ErgoBoxAssets]: ...
        _copy__T = typing.TypeVar('_copy__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
        def copy(self, boxes: scala.collection.Seq[org.ergoplatform.ErgoBoxAssets], changeBoxes: scala.collection.Seq[org.ergoplatform.ErgoBoxAssets]) -> 'BoxSelector.BoxSelectionResult'[org.ergoplatform.ErgoBoxAssets]: ...
        _copy$default$1__T = typing.TypeVar('_copy$default$1__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
        def copy$default$1(self) -> scala.collection.Seq[org.ergoplatform.ErgoBoxAssets]: ...
        _copy$default$2__T = typing.TypeVar('_copy$default$2__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
        def copy$default$2(self) -> scala.collection.Seq[org.ergoplatform.ErgoBoxAssets]: ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> java.lang.String: ...
        def toString(self) -> java.lang.String: ...
    class BoxSelectionResult$(scala.Serializable):
        MODULE$: typing.ClassVar['BoxSelector.BoxSelectionResult.'] = ...
        def __init__(self): ...
        _apply__T = typing.TypeVar('_apply__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
        def apply(self, boxes: scala.collection.Seq[_apply__T], changeBoxes: scala.collection.Seq[org.ergoplatform.ErgoBoxAssets]) -> 'BoxSelector.BoxSelectionResult'[_apply__T]: ...
        def toString(self) -> java.lang.String: ...
        _unapply__T = typing.TypeVar('_unapply__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
        def unapply(self, x$0: 'BoxSelector.BoxSelectionResult'[_unapply__T]) -> scala.Option[scala.Tuple2[scala.collection.Seq[_unapply__T], scala.collection.Seq[org.ergoplatform.ErgoBoxAssets]]]: ...

class ErgoBoxAssetExtractor:
    @staticmethod
    def MaxAssetsPerBox() -> int: ...
    @staticmethod
    def extractAssets(boxes: scala.collection.IndexedSeq[org.ergoplatform.ErgoBoxCandidate]) -> scala.util.Try[scala.Tuple2[scala.collection.immutable.Map[scala.collection.Seq[typing.Any], typing.Any], typing.Any]]: ...
    @staticmethod
    def extractTotalAssetsAccessCost(inputBoxes: scala.collection.IndexedSeq[org.ergoplatform.ErgoBoxCandidate], outputBoxes: scala.collection.IndexedSeq[org.ergoplatform.ErgoBoxCandidate], tokenAccessCost: int) -> scala.util.Try[typing.Any]: ...
    @staticmethod
    def totalAssetsAccessCost(inAssetsNum: int, inAssetsSize: int, outAssetsNum: int, outAssetsSize: int, tokenAccessCost: int) -> int: ...

class ErgoBoxSerializer:
    @staticmethod
    def parse(r: scorex.util.serialization.Reader) -> org.ergoplatform.ErgoBox: ...
    @staticmethod
    def parseBytes(bytes: typing.List[int]) -> typing.Any: ...
    @staticmethod
    def parseBytesTry(bytes: typing.List[int]) -> scala.util.Try[org.ergoplatform.ErgoBox]: ...
    @staticmethod
    def parseTry(r: scorex.util.serialization.Reader) -> scala.util.Try[org.ergoplatform.ErgoBox]: ...
    @staticmethod
    def serialize(box: org.ergoplatform.ErgoBox, w: scorex.util.serialization.Writer) -> None: ...
    @staticmethod
    def toBytes(obj: typing.Any) -> typing.List[int]: ...

class TrackedBox(org.ergoplatform.ErgoBoxAssets, scala.Product, scala.Serializable):
    def __init__(self, creationTxId: typing.Union[java.lang.String, str], creationOutIndex: int, inclusionHeightOpt: scala.Option[typing.Any], spendingTxIdOpt: scala.Option[typing.Union[java.lang.String, str]], spendingHeightOpt: scala.Option[typing.Any], box: org.ergoplatform.ErgoBox, scans: scala.collection.immutable.Set[typing.Any]): ...
    @typing.overload
    @staticmethod
    def apply(creationTxId: typing.Union[java.lang.String, str], creationOutIndex: int, inclusionHeightOpt: scala.Option[typing.Any], spendingTxIdOpt: scala.Option[typing.Union[java.lang.String, str]], spendingHeightOpt: scala.Option[typing.Any], box: org.ergoplatform.ErgoBox, scans: scala.collection.immutable.Set[typing.Any]) -> 'TrackedBox': ...
    @typing.overload
    @staticmethod
    def apply(box: org.ergoplatform.ErgoBox, inclusionHeight: int, scans: scala.collection.immutable.Set[typing.Any]) -> 'TrackedBox': ...
    @typing.overload
    @staticmethod
    def apply(creationTx: org.ergoplatform.ErgoLikeTransaction, creationOutIndex: int, creationHeight: scala.Option[typing.Any], box: org.ergoplatform.ErgoBox, appStatuses: scala.collection.immutable.Set[typing.Any]) -> 'TrackedBox': ...
    def box(self) -> org.ergoplatform.ErgoBox: ...
    def boxId(self) -> java.lang.String: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    def chainStatus(self) -> 'ChainStatus': ...
    def copy(self, creationTxId: typing.Union[java.lang.String, str], creationOutIndex: int, inclusionHeightOpt: scala.Option[typing.Any], spendingTxIdOpt: scala.Option[typing.Union[java.lang.String, str]], spendingHeightOpt: scala.Option[typing.Any], box: org.ergoplatform.ErgoBox, scans: scala.collection.immutable.Set[typing.Any]) -> 'TrackedBox': ...
    def copy$default$1(self) -> java.lang.String: ...
    def copy$default$2(self) -> int: ...
    def copy$default$3(self) -> scala.Option[typing.Any]: ...
    def copy$default$4(self) -> scala.Option[java.lang.String]: ...
    def copy$default$5(self) -> scala.Option[typing.Any]: ...
    def copy$default$6(self) -> org.ergoplatform.ErgoBox: ...
    def copy$default$7(self) -> scala.collection.immutable.Set[typing.Any]: ...
    def creationChainStatus(self) -> 'ChainStatus': ...
    def creationOutIndex(self) -> int: ...
    def creationTxId(self) -> java.lang.String: ...
    def equals(self, obj: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def inclusionHeightOpt(self) -> scala.Option[typing.Any]: ...
    def isSpent(self) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> java.lang.String: ...
    def scans(self) -> scala.collection.immutable.Set[typing.Any]: ...
    def spendingChainStatus(self) -> 'ChainStatus': ...
    def spendingHeightOpt(self) -> scala.Option[typing.Any]: ...
    def spendingStatus(self) -> 'SpendingStatus': ...
    def spendingTxIdOpt(self) -> scala.Option[java.lang.String]: ...
    def toString(self) -> java.lang.String: ...
    def tokens(self) -> scala.collection.immutable.Map[java.lang.String, typing.Any]: ...
    @staticmethod
    def unapply(x$0: 'TrackedBox') -> scala.Option[scala.Tuple7[java.lang.String, typing.Any, scala.Option[typing.Any], scala.Option[java.lang.String], scala.Option[typing.Any], org.ergoplatform.ErgoBox, scala.collection.immutable.Set[typing.Any]]]: ...
    def value(self) -> int: ...

class TrackedBoxSerializer:
    @staticmethod
    def parse(r: scorex.util.serialization.Reader) -> TrackedBox: ...
    @staticmethod
    def parseBytes(bytes: typing.List[int]) -> typing.Any: ...
    @staticmethod
    def parseBytesTry(bytes: typing.List[int]) -> scala.util.Try[TrackedBox]: ...
    @staticmethod
    def parseTry(r: scorex.util.serialization.Reader) -> scala.util.Try[TrackedBox]: ...
    @staticmethod
    def serialize(obj: TrackedBox, w: scorex.util.serialization.Writer) -> None: ...
    @staticmethod
    def toBytes(obj: typing.Any) -> typing.List[int]: ...

class DefaultBoxSelector:
    @staticmethod
    def formChangeBoxes(foundBalance: int, targetBalance: int, foundBoxAssets: scala.collection.mutable.Map[typing.Union[java.lang.String, str], typing.Any], targetBoxAssets: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> scala.util.Either[BoxSelector.BoxSelectionError, scala.collection.Seq[org.ergoplatform.ErgoBoxAssets]]: ...
    _select_0__T = typing.TypeVar('_select_0__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
    _select_1__T = typing.TypeVar('_select_1__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
    @typing.overload
    @staticmethod
    def select(inputBoxes: scala.collection.Iterator[_select_0__T], targetBalance: int, targetAssets: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> scala.util.Either[BoxSelector.BoxSelectionError, BoxSelector.BoxSelectionResult[_select_0__T]]: ...
    @typing.overload
    @staticmethod
    def select(inputBoxes: scala.collection.Iterator[_select_1__T], externalFilter: scala.Function1[_select_1__T, typing.Any], targetBalance: int, targetAssets: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> scala.util.Either[BoxSelector.BoxSelectionError, BoxSelector.BoxSelectionResult[_select_1__T]]: ...
    class NotEnoughCoinsForChangeBoxesError(BoxSelector.BoxSelectionError, scala.Product, scala.Serializable):
        def __init__(self, message: typing.Union[java.lang.String, str]): ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def copy(self, message: typing.Union[java.lang.String, str]) -> 'DefaultBoxSelector.NotEnoughCoinsForChangeBoxesError': ...
        def copy$default$1(self) -> java.lang.String: ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def message(self) -> java.lang.String: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> java.lang.String: ...
        def toString(self) -> java.lang.String: ...
    class NotEnoughCoinsForChangeBoxesError$(scala.runtime.AbstractFunction1[java.lang.String, 'DefaultBoxSelector.NotEnoughCoinsForChangeBoxesError'], scala.Serializable):
        MODULE$: typing.ClassVar['DefaultBoxSelector.NotEnoughCoinsForChangeBoxesError.'] = ...
        def __init__(self): ...
        def apply(self, message: typing.Union[java.lang.String, str]) -> 'DefaultBoxSelector.NotEnoughCoinsForChangeBoxesError': ...
        def toString(self) -> java.lang.String: ...
        def unapply(self, x$0: 'DefaultBoxSelector.NotEnoughCoinsForChangeBoxesError') -> scala.Option[java.lang.String]: ...
    class NotEnoughErgsError(BoxSelector.BoxSelectionError, scala.Product, scala.Serializable):
        def __init__(self, message: typing.Union[java.lang.String, str], balanceFound: int): ...
        def balanceFound(self) -> int: ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def copy(self, message: typing.Union[java.lang.String, str], balanceFound: int) -> 'DefaultBoxSelector.NotEnoughErgsError': ...
        def copy$default$1(self) -> java.lang.String: ...
        def copy$default$2(self) -> int: ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def message(self) -> java.lang.String: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> java.lang.String: ...
        def toString(self) -> java.lang.String: ...
    class NotEnoughErgsError$(scala.runtime.AbstractFunction2[java.lang.String, typing.Any, 'DefaultBoxSelector.NotEnoughErgsError'], scala.Serializable):
        MODULE$: typing.ClassVar['DefaultBoxSelector.NotEnoughErgsError.'] = ...
        def __init__(self): ...
        def apply(self, message: typing.Union[java.lang.String, str], balanceFound: int) -> 'DefaultBoxSelector.NotEnoughErgsError': ...
        def toString(self) -> java.lang.String: ...
        def unapply(self, x$0: 'DefaultBoxSelector.NotEnoughErgsError') -> scala.Option[scala.Tuple2[java.lang.String, typing.Any]]: ...
    class NotEnoughTokensError(BoxSelector.BoxSelectionError, scala.Product, scala.Serializable):
        def __init__(self, message: typing.Union[java.lang.String, str], tokensFound: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]): ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def copy(self, message: typing.Union[java.lang.String, str], tokensFound: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> 'DefaultBoxSelector.NotEnoughTokensError': ...
        def copy$default$1(self) -> java.lang.String: ...
        def copy$default$2(self) -> scala.collection.immutable.Map[java.lang.String, typing.Any]: ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def message(self) -> java.lang.String: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> java.lang.String: ...
        def toString(self) -> java.lang.String: ...
        def tokensFound(self) -> scala.collection.immutable.Map[java.lang.String, typing.Any]: ...
    class NotEnoughTokensError$(scala.runtime.AbstractFunction2[java.lang.String, scala.collection.immutable.Map[java.lang.String, typing.Any], 'DefaultBoxSelector.NotEnoughTokensError'], scala.Serializable):
        MODULE$: typing.ClassVar['DefaultBoxSelector.NotEnoughTokensError.'] = ...
        def __init__(self): ...
        def apply(self, message: typing.Union[java.lang.String, str], tokensFound: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> 'DefaultBoxSelector.NotEnoughTokensError': ...
        def toString(self) -> java.lang.String: ...
        def unapply(self, x$0: 'DefaultBoxSelector.NotEnoughTokensError') -> scala.Option[scala.Tuple2[java.lang.String, scala.collection.immutable.Map[java.lang.String, typing.Any]]]: ...

class ReplaceCompactCollectBoxSelector(BoxSelector):
    def __init__(self, maxInputs: int, optimalInputs: int): ...
    _calcChange__T = typing.TypeVar('_calcChange__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
    def calcChange(self, boxes: scala.collection.Seq[_calcChange__T], targetBalance: int, targetAssets: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> scala.util.Either[BoxSelector.BoxSelectionError, scala.collection.Seq[org.ergoplatform.ErgoBoxAssets]]: ...
    _collectDust__T = typing.TypeVar('_collectDust__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
    def collectDust(self, bsr: BoxSelector.BoxSelectionResult[_collectDust__T], tail: scala.collection.Seq[_collectDust__T], targetBalance: int, targetAssets: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> scala.util.Either[BoxSelector.BoxSelectionError, BoxSelector.BoxSelectionResult[_collectDust__T]]: ...
    _compress__T = typing.TypeVar('_compress__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
    def compress(self, bsr: BoxSelector.BoxSelectionResult[_compress__T], targetBalance: int, targetAssets: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> scala.util.Either[BoxSelector.BoxSelectionError, BoxSelector.BoxSelectionResult[_compress__T]]: ...
    _replace__T = typing.TypeVar('_replace__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
    def replace(self, bsr: BoxSelector.BoxSelectionResult[_replace__T], tail: scala.collection.Seq[_replace__T], targetBalance: int, targetAssets: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> scala.util.Either[BoxSelector.BoxSelectionError, BoxSelector.BoxSelectionResult[_replace__T]]: ...
    _select_0__T = typing.TypeVar('_select_0__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
    _select_1__T = typing.TypeVar('_select_1__T', bound=org.ergoplatform.ErgoBoxAssets)  # <T>
    @typing.overload
    def select(self, inputBoxes: scala.collection.Iterator[_select_0__T], targetBalance: int, targetAssets: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> scala.util.Either[BoxSelector.BoxSelectionError, BoxSelector.BoxSelectionResult[_select_0__T]]: ...
    @typing.overload
    def select(self, inputBoxes: scala.collection.Iterator[_select_1__T], filterFn: scala.Function1[_select_1__T, typing.Any], targetBalance: int, targetAssets: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> scala.util.Either[BoxSelector.BoxSelectionError, BoxSelector.BoxSelectionResult[_select_1__T]]: ...
    class MaxInputsExceededError(BoxSelector.BoxSelectionError, scala.Product, scala.Serializable):
        def __init__(self, message: typing.Union[java.lang.String, str]): ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def copy(self, message: typing.Union[java.lang.String, str]) -> 'ReplaceCompactCollectBoxSelector.MaxInputsExceededError': ...
        def copy$default$1(self) -> java.lang.String: ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def message(self) -> java.lang.String: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> java.lang.String: ...
        def toString(self) -> java.lang.String: ...
    class MaxInputsExceededError$(scala.runtime.AbstractFunction1[java.lang.String, 'ReplaceCompactCollectBoxSelector.MaxInputsExceededError'], scala.Serializable):
        MODULE$: typing.ClassVar['ReplaceCompactCollectBoxSelector.MaxInputsExceededError.'] = ...
        def __init__(self): ...
        def apply(self, message: typing.Union[java.lang.String, str]) -> 'ReplaceCompactCollectBoxSelector.MaxInputsExceededError': ...
        def toString(self) -> java.lang.String: ...
        def unapply(self, x$0: 'ReplaceCompactCollectBoxSelector.MaxInputsExceededError') -> scala.Option[java.lang.String]: ...

class ChainStatus:
    def __init__(self, onChain: bool): ...
    def onChain(self) -> bool: ...
    class OffChain$(org.ergoplatform.wallet.boxes.ChainStatus, scala.Product, scala.Serializable):
        MODULE$: typing.ClassVar['ChainStatus.OffChain.'] = ...
        def __init__(self): ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> java.lang.String: ...
        def toString(self) -> java.lang.String: ...
    class OnChain$(org.ergoplatform.wallet.boxes.ChainStatus, scala.Product, scala.Serializable):
        MODULE$: typing.ClassVar['ChainStatus.OnChain.'] = ...
        def __init__(self): ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> java.lang.String: ...
        def toString(self) -> java.lang.String: ...

class SpendingStatus:
    def __init__(self, spent: bool): ...
    def spent(self) -> bool: ...
    class Spent$(org.ergoplatform.wallet.boxes.SpendingStatus, scala.Product, scala.Serializable):
        MODULE$: typing.ClassVar['SpendingStatus.Spent.'] = ...
        def __init__(self): ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> java.lang.String: ...
        def toString(self) -> java.lang.String: ...
    class Unspent$(org.ergoplatform.wallet.boxes.SpendingStatus, scala.Product, scala.Serializable):
        MODULE$: typing.ClassVar['SpendingStatus.Unspent.'] = ...
        def __init__(self): ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> java.lang.String: ...
        def toString(self) -> java.lang.String: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.ergoplatform.wallet.boxes")``.

    BoxSelector: typing.Type[BoxSelector]
    ChainStatus: typing.Type[ChainStatus]
    DefaultBoxSelector: typing.Type[DefaultBoxSelector]
    ErgoBoxAssetExtractor: typing.Type[ErgoBoxAssetExtractor]
    ErgoBoxSerializer: typing.Type[ErgoBoxSerializer]
    ReplaceCompactCollectBoxSelector: typing.Type[ReplaceCompactCollectBoxSelector]
    SpendingStatus: typing.Type[SpendingStatus]
    TrackedBox: typing.Type[TrackedBox]
    TrackedBoxSerializer: typing.Type[TrackedBoxSerializer]
