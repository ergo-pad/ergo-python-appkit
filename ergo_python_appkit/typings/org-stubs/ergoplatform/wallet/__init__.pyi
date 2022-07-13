import java.lang
import org.ergoplatform
import org.ergoplatform.wallet.boxes
import org.ergoplatform.wallet.crypto
import org.ergoplatform.wallet.interface4j
import org.ergoplatform.wallet.interpreter
import org.ergoplatform.wallet.mnemonic
import org.ergoplatform.wallet.protocol
import org.ergoplatform.wallet.secrets
import org.ergoplatform.wallet.serialization
import org.ergoplatform.wallet.settings
import org.ergoplatform.wallet.transactions
import org.ergoplatform.wallet.utils
import scala
import scala.collection
import scala.collection.immutable
import scala.collection.mutable
import scala.math
import scala.util
import supertagged
import typing



class AssetUtils:
    @staticmethod
    def mergeAssets(initialMap: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any], maps: scala.collection.Seq[scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]]) -> scala.collection.immutable.Map[java.lang.String, typing.Any]: ...
    @staticmethod
    def mergeAssetsMut(into: scala.collection.mutable.Map[typing.Union[java.lang.String, str], typing.Any], from_: scala.collection.Seq[scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]]) -> None: ...
    @staticmethod
    def subtractAssets(initialMap: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any], subtractor: scala.collection.Seq[scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]]) -> scala.collection.immutable.Map[java.lang.String, typing.Any]: ...
    @staticmethod
    def subtractAssetsMut(from_: scala.collection.mutable.Map[typing.Union[java.lang.String, str], typing.Any], subtractor: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> None: ...

class Constants:
    @staticmethod
    def BitcoinSeed() -> typing.List[int]: ...
    @staticmethod
    def CoinType() -> int: ...
    @staticmethod
    def Encoding() -> java.lang.String: ...
    @staticmethod
    def MaxAssetsPerBox() -> int: ...
    @staticmethod
    def MiningScanId() -> int: ...
    @staticmethod
    def ModifierIdLength() -> int: ...
    @staticmethod
    def PaymentsScanId() -> int: ...
    @staticmethod
    def SecretKeyLength() -> int: ...
    @staticmethod
    def eip3DerivationPath() -> org.ergoplatform.wallet.secrets.DerivationPath: ...
    @staticmethod
    def preEip3DerivationPath() -> org.ergoplatform.wallet.secrets.DerivationPath: ...
    class ScanId$(supertagged.package.TaggedType[typing.Any]):
        MODULE$: typing.ClassVar['Constants.ScanId.'] = ...
        def __init__(self): ...
        _$at$at__TagIn = typing.TypeVar('_$at$at__TagIn')  # <TagIn>
        _$at$at__Sub = typing.TypeVar('_$at$at__Sub')  # <Sub>
        _$at$at__C = typing.TypeVar('_$at$at__C')  # <C>
        def $at$at(self, c: _.at.at__C, tagger: supertagged.package.Tagger[_.at.at__TagIn, typing.Any, supertagged.package.TaggedType, _.at.at__Sub, _.at.at__C]) -> typing.Any: ...
        _$bang$at$at__TagIn = typing.TypeVar('_$bang$at$at__TagIn')  # <TagIn>
        _$bang$at$at__Sub = typing.TypeVar('_$bang$at$at__Sub')  # <Sub>
        _$bang$at$at__C = typing.TypeVar('_$bang$at$at__C')  # <C>
        def $bang$at$at(self, c: _.bang.at.at__C, tagger: supertagged.package.Tagger[_.bang.at.at__TagIn, typing.Any, supertagged.package.TaggedType, _.bang.at.at__Sub, _.bang.at.at__C]) -> typing.Any: ...
        _apply__TagIn = typing.TypeVar('_apply__TagIn')  # <TagIn>
        _apply__Sub = typing.TypeVar('_apply__Sub')  # <Sub>
        _apply__C = typing.TypeVar('_apply__C')  # <C>
        def apply(self, c: _apply__C, tagger: supertagged.package.Tagger[_apply__TagIn, typing.Any, supertagged.package.TaggedType, _apply__Sub, _apply__C]) -> typing.Any: ...
        _ordering__U = typing.TypeVar('_ordering__U')  # <U>
        def ordering(self, origin: scala.math.Ordering[typing.Any]) -> scala.math.Ordering[typing.Any]: ...
        def raw(self, c: typing.Any) -> typing.Any: ...
        _untag__TagIn = typing.TypeVar('_untag__TagIn')  # <TagIn>
        _untag__Sub = typing.TypeVar('_untag__Sub')  # <Sub>
        _untag__C = typing.TypeVar('_untag__C')  # <C>
        def untag(self, c: _untag__C, tagger: supertagged.package.Tagger[_untag__TagIn, typing.Any, supertagged.package.TaggedType, _untag__Sub, _untag__C]) -> typing.Any: ...

_Utils__EitherOpsFor211__A = typing.TypeVar('_Utils__EitherOpsFor211__A')  # <A>
_Utils__EitherOpsFor211__B = typing.TypeVar('_Utils__EitherOpsFor211__B')  # <B>
class Utils:
    @staticmethod
    def paymentTransaction(recipientAddress: org.ergoplatform.ErgoAddress, changeAddress: org.ergoplatform.ErgoAddress, transferAmt: int, feeAmt: int, changeAmt: int, inputIds: typing.List[java.lang.String], currentHeight: int) -> org.ergoplatform.UnsignedErgoLikeTransaction: ...
    class EitherOpsFor211(typing.Generic[_Utils__EitherOpsFor211__A, _Utils__EitherOpsFor211__B]):
        def __init__(self, source: scala.util.Either[_Utils__EitherOpsFor211__A, _Utils__EitherOpsFor211__B]): ...
        def equals(self, x$1: typing.Any) -> bool: ...
        _flatMapRight__A1 = typing.TypeVar('_flatMapRight__A1')  # <A1>
        _flatMapRight__B1 = typing.TypeVar('_flatMapRight__B1')  # <B1>
        def flatMapRight(self, f: scala.Function1[_Utils__EitherOpsFor211__B, scala.util.Either[_flatMapRight__A1, _flatMapRight__B1]]) -> scala.util.Either[_flatMapRight__A1, _flatMapRight__B1]: ...
        def hashCode(self) -> int: ...
        _mapRight__B1 = typing.TypeVar('_mapRight__B1')  # <B1>
        def mapRight(self, f: scala.Function1[_Utils__EitherOpsFor211__B, _mapRight__B1]) -> scala.util.Either[_Utils__EitherOpsFor211__A, _mapRight__B1]: ...
        def source(self) -> scala.util.Either[_Utils__EitherOpsFor211__A, _Utils__EitherOpsFor211__B]: ...
    class EitherOpsFor211$:
        MODULE$: typing.ClassVar['Utils.EitherOpsFor211.'] = ...
        def __init__(self): ...
        _equals$extension__A = typing.TypeVar('_equals$extension__A')  # <A>
        _equals$extension__B = typing.TypeVar('_equals$extension__B')  # <B>
        def equals$extension(self, $this: scala.util.Either[_equals.extension__A, _equals.extension__B], x$1: typing.Any) -> bool: ...
        _flatMapRight$extension__A1 = typing.TypeVar('_flatMapRight$extension__A1')  # <A1>
        _flatMapRight$extension__B1 = typing.TypeVar('_flatMapRight$extension__B1')  # <B1>
        _flatMapRight$extension__A = typing.TypeVar('_flatMapRight$extension__A')  # <A>
        _flatMapRight$extension__B = typing.TypeVar('_flatMapRight$extension__B')  # <B>
        def flatMapRight$extension(self, $this: scala.util.Either[_flatMapRight.extension__A, _flatMapRight.extension__B], f: scala.Function1[_flatMapRight.extension__B, scala.util.Either[_flatMapRight.extension__A1, _flatMapRight.extension__B1]]) -> scala.util.Either[_flatMapRight.extension__A1, _flatMapRight.extension__B1]: ...
        _hashCode$extension__A = typing.TypeVar('_hashCode$extension__A')  # <A>
        _hashCode$extension__B = typing.TypeVar('_hashCode$extension__B')  # <B>
        def hashCode$extension(self, $this: scala.util.Either[_hashCode.extension__A, _hashCode.extension__B]) -> int: ...
        _mapRight$extension__B1 = typing.TypeVar('_mapRight$extension__B1')  # <B1>
        _mapRight$extension__A = typing.TypeVar('_mapRight$extension__A')  # <A>
        _mapRight$extension__B = typing.TypeVar('_mapRight$extension__B')  # <B>
        def mapRight$extension(self, $this: scala.util.Either[_mapRight.extension__A, _mapRight.extension__B], f: scala.Function1[_mapRight.extension__B, _mapRight.extension__B1]) -> scala.util.Either[_mapRight.extension__A, _mapRight.extension__B1]: ...

class package: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.ergoplatform.wallet")``.

    AssetUtils: typing.Type[AssetUtils]
    Constants: typing.Type[Constants]
    Utils: typing.Type[Utils]
    package: typing.Type[package]
    boxes: org.ergoplatform.wallet.boxes.__module_protocol__
    crypto: org.ergoplatform.wallet.crypto.__module_protocol__
    interface4j: org.ergoplatform.wallet.interface4j.__module_protocol__
    interpreter: org.ergoplatform.wallet.interpreter.__module_protocol__
    mnemonic: org.ergoplatform.wallet.mnemonic.__module_protocol__
    protocol: org.ergoplatform.wallet.protocol.__module_protocol__
    secrets: org.ergoplatform.wallet.secrets.__module_protocol__
    serialization: org.ergoplatform.wallet.serialization.__module_protocol__
    settings: org.ergoplatform.wallet.settings.__module_protocol__
    transactions: org.ergoplatform.wallet.transactions.__module_protocol__
    utils: org.ergoplatform.wallet.utils.__module_protocol__
