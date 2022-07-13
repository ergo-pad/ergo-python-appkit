import java.lang
import org.ergoplatform
import org.ergoplatform.wallet.boxes
import scala
import scala.collection
import scala.collection.immutable
import scala.util
import special.collection
import typing



class TransactionBuilder:
    @staticmethod
    def buildUnsignedTx(inputs: scala.collection.IndexedSeq[org.ergoplatform.ErgoBox], dataInputs: scala.collection.IndexedSeq[org.ergoplatform.DataInput], outputCandidates: scala.collection.Seq[org.ergoplatform.ErgoBoxCandidate], currentHeight: int, createFeeOutput: scala.Option[typing.Any], changeAddress: org.ergoplatform.ErgoAddress, minChangeValue: int, minerRewardDelay: int, burnTokens: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any], boxSelector: org.ergoplatform.wallet.boxes.BoxSelector) -> scala.util.Try[org.ergoplatform.UnsignedErgoLikeTransaction]: ...
    @staticmethod
    def buildUnsignedTx$default$10() -> org.ergoplatform.wallet.boxes.BoxSelector: ...
    @staticmethod
    def buildUnsignedTx$default$9() -> scala.collection.immutable.Map[java.lang.String, typing.Any]: ...
    @staticmethod
    def collTokensToMap(tokens: special.collection.Coll[scala.Tuple2[typing.List[int], typing.Any]]) -> scala.collection.immutable.Map[java.lang.String, typing.Any]: ...
    @staticmethod
    def collectOutputTokens(outputCandidates: scala.collection.Seq[org.ergoplatform.ErgoBoxCandidate]) -> scala.collection.immutable.Map[java.lang.String, typing.Any]: ...
    @staticmethod
    def tokensMapToColl(tokens: scala.collection.immutable.Map[typing.Union[java.lang.String, str], typing.Any]) -> special.collection.Coll[scala.Tuple2[typing.List[int], typing.Any]]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.ergoplatform.wallet.transactions")``.

    TransactionBuilder: typing.Type[TransactionBuilder]
