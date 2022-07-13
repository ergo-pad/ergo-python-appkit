import java.lang
import scala
import scala.collection
import scala.util
import scorex.crypto.hash
import scorex.util
import sigmastate
import special.collection
import typing



class ErgoAlgos(scorex.util.ScorexEncoding):
    @staticmethod
    def $init$($this: 'ErgoAlgos') -> None: ...
    def decode(self, str: typing.Union[java.lang.String, str]) -> scala.util.Try[typing.List[int]]: ...
    def decodeUnsafe(self, str: typing.Union[java.lang.String, str]) -> typing.List[int]: ...
    @typing.overload
    def encode(self, bytes: typing.List[int]) -> java.lang.String: ...
    @typing.overload
    def encode(self, bytes: special.collection.Coll[typing.Any]) -> java.lang.String: ...
    def hash(self) -> scorex.crypto.hash.Blake2b256.: ...
    def org$ergoplatform$settings$ErgoAlgos$_setter_$hash_$eq(self, x$1: scorex.crypto.hash.Blake2b256.) -> None: ...

class MonetarySettings(scala.Product, scala.Serializable):
    def __init__(self, fixedRatePeriod: int, epochLength: int, fixedRate: int, oneEpochReduction: int, minerRewardDelay: int, foundersInitialReward: int): ...
    @staticmethod
    def $lessinit$greater$default$1() -> int: ...
    @staticmethod
    def $lessinit$greater$default$2() -> int: ...
    @staticmethod
    def $lessinit$greater$default$3() -> int: ...
    @staticmethod
    def $lessinit$greater$default$4() -> int: ...
    @staticmethod
    def $lessinit$greater$default$5() -> int: ...
    @staticmethod
    def $lessinit$greater$default$6() -> int: ...
    @staticmethod
    def apply(fixedRatePeriod: int, epochLength: int, fixedRate: int, oneEpochReduction: int, minerRewardDelay: int, foundersInitialReward: int) -> 'MonetarySettings': ...
    @staticmethod
    def apply$default$1() -> int: ...
    @staticmethod
    def apply$default$2() -> int: ...
    @staticmethod
    def apply$default$3() -> int: ...
    @staticmethod
    def apply$default$4() -> int: ...
    @staticmethod
    def apply$default$5() -> int: ...
    @staticmethod
    def apply$default$6() -> int: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    def copy(self, fixedRatePeriod: int, epochLength: int, fixedRate: int, oneEpochReduction: int, minerRewardDelay: int, foundersInitialReward: int) -> 'MonetarySettings': ...
    def copy$default$1(self) -> int: ...
    def copy$default$2(self) -> int: ...
    def copy$default$3(self) -> int: ...
    def copy$default$4(self) -> int: ...
    def copy$default$5(self) -> int: ...
    def copy$default$6(self) -> int: ...
    @staticmethod
    def curried() -> scala.Function1[typing.Any, scala.Function1[typing.Any, scala.Function1[typing.Any, scala.Function1[typing.Any, scala.Function1[typing.Any, scala.Function1[typing.Any, 'MonetarySettings']]]]]]: ...
    def emissionBoxProposition(self) -> sigmastate.Values.ErgoTree: ...
    def epochLength(self) -> int: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def feeProposition(self) -> sigmastate.Values.ErgoTree: ...
    def feePropositionBytes(self) -> typing.List[int]: ...
    def fixedRate(self) -> int: ...
    def fixedRatePeriod(self) -> int: ...
    def foundersBoxProposition(self) -> sigmastate.Values.ErgoTree: ...
    def foundersInitialReward(self) -> int: ...
    def hashCode(self) -> int: ...
    def minerRewardDelay(self) -> int: ...
    def oneEpochReduction(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    @staticmethod
    def tupled() -> scala.Function1[scala.Tuple6[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any], 'MonetarySettings']: ...
    @staticmethod
    def unapply(x$0: 'MonetarySettings') -> scala.Option[scala.Tuple6[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.ergoplatform.settings")``.

    ErgoAlgos: typing.Type[ErgoAlgos]
    MonetarySettings: typing.Type[MonetarySettings]
