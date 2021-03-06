import java.lang
import scala
import scala.collection
import scala.collection.immutable
import scala.collection.mutable
import scala.math
import scala.runtime
import scala.util
import scorex.crypto.hash
import typing



class BlockchainSimulator:
    @staticmethod
    def PubKeyLength() -> int: ...
    @staticmethod
    def currentGodBalance() -> int: ...
    @staticmethod
    def currentGodBalance_$eq(x$1: int) -> None: ...
    @staticmethod
    def delayedInit(body: scala.Function0[scala.runtime.BoxedUnit]) -> None: ...
    @staticmethod
    def emptyState() -> 'SparseMerkleTree'[typing.List[int]]: ...
    @staticmethod
    def executionStart() -> int: ...
    @staticmethod
    def godAccount() -> typing.List[int]: ...
    @staticmethod
    def godBalance() -> int: ...
    @staticmethod
    def godProof() -> 'SparseMerkleProof'[typing.List[int]]: ...
    @staticmethod
    def godProof_$eq(x$1: 'SparseMerkleProof'[typing.List[int]]) -> None: ...
    @staticmethod
    def godProofs() -> scala.collection.Seq['SparseMerkleProof'[typing.List[int]]]: ...
    @staticmethod
    def height() -> int: ...
    @staticmethod
    def hf() -> scorex.crypto.hash.CryptographicHash[typing.List[int]]: ...
    @staticmethod
    def initialState() -> 'SparseMerkleTree'[typing.List[int]]: ...
    @staticmethod
    def main(args: typing.List[java.lang.String]) -> None: ...
    @staticmethod
    def maxTxsCacheSize() -> int: ...
    @staticmethod
    def numOfBlocks() -> int: ...
    @staticmethod
    def txAmount() -> int: ...
    @staticmethod
    def txsCache() -> scala.collection.mutable.ArrayBuffer[scala.runtime.Nothing.]: ...
    @staticmethod
    def txsPerBlock() -> int: ...
    class Block(scala.Product, scala.Serializable):
        def __init__(self, transactions: scala.collection.Seq['BlockchainSimulator.Transaction']): ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def copy(self, transactions: scala.collection.Seq['BlockchainSimulator.Transaction']) -> 'BlockchainSimulator.Block': ...
        def copy$default$1(self) -> scala.collection.Seq['BlockchainSimulator.Transaction']: ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> java.lang.String: ...
        def toString(self) -> java.lang.String: ...
        def transactions(self) -> scala.collection.Seq['BlockchainSimulator.Transaction']: ...
    class Block$(scala.runtime.AbstractFunction1[scala.collection.Seq['BlockchainSimulator.Transaction'], 'BlockchainSimulator.Block'], scala.Serializable):
        MODULE$: typing.ClassVar['BlockchainSimulator.Block.'] = ...
        def __init__(self): ...
        def apply(self, transactions: scala.collection.Seq['BlockchainSimulator.Transaction']) -> 'BlockchainSimulator.Block': ...
        def toString(self) -> java.lang.String: ...
        def unapply(self, x$0: 'BlockchainSimulator.Block') -> scala.Option[scala.collection.Seq['BlockchainSimulator.Transaction']]: ...
    class Transaction(scala.Product, scala.Serializable):
        def __init__(self, amount: int, sender: typing.List[int], recipient: typing.List[int], coinBalance: int, coinProof: 'SparseMerkleProof'[typing.List[int]]): ...
        def amount(self) -> int: ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def coinBalance(self) -> int: ...
        def coinProof(self) -> 'SparseMerkleProof'[typing.List[int]]: ...
        def copy(self, amount: int, sender: typing.List[int], recipient: typing.List[int], coinBalance: int, coinProof: 'SparseMerkleProof'[typing.List[int]]) -> 'BlockchainSimulator.Transaction': ...
        def copy$default$1(self) -> int: ...
        def copy$default$2(self) -> typing.List[int]: ...
        def copy$default$3(self) -> typing.List[int]: ...
        def copy$default$4(self) -> int: ...
        def copy$default$5(self) -> 'SparseMerkleProof'[typing.List[int]]: ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> java.lang.String: ...
        def recipient(self) -> typing.List[int]: ...
        def sender(self) -> typing.List[int]: ...
        def toString(self) -> java.lang.String: ...
    class Transaction$(scala.Serializable):
        MODULE$: typing.ClassVar['BlockchainSimulator.Transaction.'] = ...
        def __init__(self): ...
        def apply(self, amount: int, sender: typing.List[int], recipient: typing.List[int], coinBalance: int, coinProof: 'SparseMerkleProof'[typing.List[int]]) -> 'BlockchainSimulator.Transaction': ...
        def coinBytes(self, pubKey: typing.List[int], balance: int) -> scala.Some[typing.List[int]]: ...
        def process(self, tx: 'BlockchainSimulator.Transaction', state: 'SparseMerkleTree'[typing.List[int]]) -> scala.util.Try[scala.Tuple2['SparseMerkleTree'[typing.List[int]], scala.collection.Seq['SparseMerkleProof'[typing.List[int]]]]]: ...
        def unapply(self, x$0: 'BlockchainSimulator.Transaction') -> scala.Option[scala.Tuple5[typing.Any, typing.List[int], typing.List[int], typing.Any, 'SparseMerkleProof'[typing.List[int]]]]: ...

_Node__D = typing.TypeVar('_Node__D', bound=typing.List[int])  # <D>
class Node(typing.Generic[_Node__D]):
    def hash(self) -> _Node__D: ...
    def isNull(self) -> bool: ...

class OpsBenchmark:
    @staticmethod
    def bSize() -> int: ...
    @staticmethod
    def delayedInit(body: scala.Function0[scala.runtime.BoxedUnit]) -> None: ...
    @staticmethod
    def executionStart() -> int: ...
    @staticmethod
    def height() -> int: ...
    @staticmethod
    def hf() -> scorex.crypto.hash.CryptographicHash[typing.List[int]]: ...
    @staticmethod
    def main(args: typing.List[java.lang.String]) -> None: ...
    @staticmethod
    def proof() -> 'SparseMerkleProof'[typing.List[int]]: ...
    @staticmethod
    def proof_$eq(x$1: 'SparseMerkleProof'[typing.List[int]]) -> None: ...
    @staticmethod
    def tb() -> int: ...
    @staticmethod
    def tb0() -> int: ...
    @staticmethod
    def te() -> int: ...
    @staticmethod
    def te0() -> int: ...
    @staticmethod
    def tp() -> int: ...
    @staticmethod
    def tp0() -> int: ...
    @staticmethod
    def tree() -> 'SparseMerkleTree'[typing.List[int]]: ...
    @staticmethod
    def tree_$eq(x$1: 'SparseMerkleTree'[typing.List[int]]) -> None: ...
    @staticmethod
    def tu() -> int: ...
    @staticmethod
    def tv() -> int: ...
    @staticmethod
    def tv0() -> int: ...

_SparseMerkleProof__D = typing.TypeVar('_SparseMerkleProof__D', bound=typing.List[int])  # <D>
class SparseMerkleProof(scala.Product, scala.Serializable, typing.Generic[_SparseMerkleProof__D]):
    def __init__(self, idx: scala.math.BigInt, leafDataOpt: scala.Option[typing.List[int]], levels: scala.collection.immutable.Vector[scala.Option[_SparseMerkleProof__D]]): ...
    _apply__D = typing.TypeVar('_apply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def apply(idx: scala.math.BigInt, leafDataOpt: scala.Option[typing.List[int]], levels: scala.collection.immutable.Vector[scala.Option[_apply__D]]) -> 'SparseMerkleProof'[_apply__D]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__D = typing.TypeVar('_copy__D', bound=typing.List[int])  # <D>
    def copy(self, idx: scala.math.BigInt, leafDataOpt: scala.Option[typing.List[int]], levels: scala.collection.immutable.Vector[scala.Option[typing.List[int]]]) -> 'SparseMerkleProof'[typing.List[int]]: ...
    _copy$default$1__D = typing.TypeVar('_copy$default$1__D', bound=typing.List[int])  # <D>
    def copy$default$1(self) -> scala.math.BigInt: ...
    _copy$default$2__D = typing.TypeVar('_copy$default$2__D', bound=typing.List[int])  # <D>
    def copy$default$2(self) -> scala.Option[typing.List[int]]: ...
    _copy$default$3__D = typing.TypeVar('_copy$default$3__D', bound=typing.List[int])  # <D>
    def copy$default$3(self) -> scala.collection.immutable.Vector[scala.Option[typing.List[int]]]: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def idx(self) -> scala.math.BigInt: ...
    def leafDataOpt(self) -> scala.Option[typing.List[int]]: ...
    def levels(self) -> scala.collection.immutable.Vector[scala.Option[_SparseMerkleProof__D]]: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> java.lang.String: ...
    def propagateChanges(self, leafDataOpt: scala.Option[typing.List[int]], hf: scorex.crypto.hash.CryptographicHash[_SparseMerkleProof__D]) -> scala.Tuple2[scala.Option[_SparseMerkleProof__D], scala.collection.immutable.Vector[scala.Option[_SparseMerkleProof__D]]]: ...
    def toString(self) -> java.lang.String: ...
    _unapply__D = typing.TypeVar('_unapply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def unapply(x$0: 'SparseMerkleProof'[_unapply__D]) -> scala.Option[scala.Tuple3[scala.math.BigInt, scala.Option[typing.List[int]], scala.collection.immutable.Vector[scala.Option[_unapply__D]]]]: ...
    @typing.overload
    def valid(self, expectedRootHash: scala.Option[_SparseMerkleProof__D], height: int, hf: scorex.crypto.hash.CryptographicHash[_SparseMerkleProof__D]) -> bool: ...
    @typing.overload
    def valid(self, tree: 'SparseMerkleTree'[_SparseMerkleProof__D], hf: scorex.crypto.hash.CryptographicHash[_SparseMerkleProof__D]) -> bool: ...

_SparseMerkleTree__D = typing.TypeVar('_SparseMerkleTree__D', bound=typing.List[int])  # <D>
class SparseMerkleTree(typing.Generic[_SparseMerkleTree__D]):
    def __init__(self, rootDigest: scala.Option[_SparseMerkleTree__D], height: int, lastProof: SparseMerkleProof[_SparseMerkleTree__D], hf: scorex.crypto.hash.CryptographicHash[_SparseMerkleTree__D]): ...
    _emptyTree__D = typing.TypeVar('_emptyTree__D', bound=typing.List[int])  # <D>
    @staticmethod
    def emptyTree(height: int, hf: scorex.crypto.hash.CryptographicHash[_emptyTree__D]) -> 'SparseMerkleTree'[_emptyTree__D]: ...
    def height(self) -> int: ...
    @staticmethod
    def indexToBits(idx: scala.math.BigInt, height: int) -> scala.collection.immutable.IndexedSeq[typing.Any]: ...
    @staticmethod
    def indexToBitsReverse(idx: scala.math.BigInt, height: int) -> scala.collection.immutable.IndexedSeq[typing.Any]: ...
    def lastIndex(self) -> scala.math.BigInt: ...
    def lastProof(self) -> SparseMerkleProof[_SparseMerkleTree__D]: ...
    @staticmethod
    def passAllFilterFn() -> scala.Function2[scala.math.BigInt, scala.Option[typing.List[int]], typing.Any]: ...
    def rootDigest(self) -> scala.Option[_SparseMerkleTree__D]: ...
    def update(self, proof: SparseMerkleProof[_SparseMerkleTree__D], newLeafData: scala.Option[typing.List[int]], proofsToUpdate: scala.collection.Seq[SparseMerkleProof[_SparseMerkleTree__D]], filterFn: scala.Function2[scala.math.BigInt, scala.Option[typing.List[int]], typing.Any]) -> scala.util.Try[scala.Tuple2['SparseMerkleTree'[_SparseMerkleTree__D], scala.collection.Seq[SparseMerkleProof[_SparseMerkleTree__D]]]]: ...
    def update$default$3(self) -> scala.collection.Seq[SparseMerkleProof[_SparseMerkleTree__D]]: ...
    def update$default$4(self) -> scala.Function2[scala.math.BigInt, scala.Option[typing.List[int]], typing.Any]: ...
    _zeroProof__D = typing.TypeVar('_zeroProof__D', bound=typing.List[int])  # <D>
    @staticmethod
    def zeroProof(height: int) -> SparseMerkleProof[_zeroProof__D]: ...

_InternalNode__D = typing.TypeVar('_InternalNode__D', bound=typing.List[int])  # <D>
class InternalNode(Node[_InternalNode__D], scala.Product, scala.Serializable, typing.Generic[_InternalNode__D]):
    def __init__(self, left: scala.Option[Node[_InternalNode__D]], right: scala.Option[Node[_InternalNode__D]], hf: scorex.crypto.hash.CryptographicHash[_InternalNode__D]): ...
    _apply__D = typing.TypeVar('_apply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def apply(left: scala.Option[Node[_apply__D]], right: scala.Option[Node[_apply__D]], hf: scorex.crypto.hash.CryptographicHash[_apply__D]) -> 'InternalNode'[_apply__D]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__D = typing.TypeVar('_copy__D', bound=typing.List[int])  # <D>
    def copy(self, left: scala.Option[Node[typing.List[int]]], right: scala.Option[Node[typing.List[int]]], hf: scorex.crypto.hash.CryptographicHash[typing.List[int]]) -> 'InternalNode'[typing.List[int]]: ...
    _copy$default$1__D = typing.TypeVar('_copy$default$1__D', bound=typing.List[int])  # <D>
    def copy$default$1(self) -> scala.Option[Node[typing.List[int]]]: ...
    _copy$default$2__D = typing.TypeVar('_copy$default$2__D', bound=typing.List[int])  # <D>
    def copy$default$2(self) -> scala.Option[Node[typing.List[int]]]: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hash(self) -> _InternalNode__D: ...
    def hashCode(self) -> int: ...
    def hf(self) -> scorex.crypto.hash.CryptographicHash[_InternalNode__D]: ...
    def isNull(self) -> bool: ...
    def left(self) -> scala.Option[Node[_InternalNode__D]]: ...
    def leftHash(self) -> typing.List[int]: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> java.lang.String: ...
    def right(self) -> scala.Option[Node[_InternalNode__D]]: ...
    def rightHash(self) -> typing.List[int]: ...
    def toString(self) -> java.lang.String: ...
    _unapply__D = typing.TypeVar('_unapply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def unapply(x$0: 'InternalNode'[_unapply__D]) -> scala.Option[scala.Tuple2[scala.Option[Node[_unapply__D]], scala.Option[Node[_unapply__D]]]]: ...

_Leaf__D = typing.TypeVar('_Leaf__D', bound=typing.List[int])  # <D>
class Leaf(Node[_Leaf__D], scala.Product, scala.Serializable, typing.Generic[_Leaf__D]):
    def __init__(self, idx: scala.math.BigInt, data: typing.List[int], hf: scorex.crypto.hash.CryptographicHash[_Leaf__D]): ...
    _apply__D = typing.TypeVar('_apply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def apply(idx: scala.math.BigInt, data: typing.List[int], hf: scorex.crypto.hash.CryptographicHash[_apply__D]) -> 'Leaf'[_apply__D]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__D = typing.TypeVar('_copy__D', bound=typing.List[int])  # <D>
    def copy(self, idx: scala.math.BigInt, data: typing.List[int], hf: scorex.crypto.hash.CryptographicHash[typing.List[int]]) -> 'Leaf'[typing.List[int]]: ...
    _copy$default$1__D = typing.TypeVar('_copy$default$1__D', bound=typing.List[int])  # <D>
    def copy$default$1(self) -> scala.math.BigInt: ...
    _copy$default$2__D = typing.TypeVar('_copy$default$2__D', bound=typing.List[int])  # <D>
    def copy$default$2(self) -> typing.List[int]: ...
    def data(self) -> typing.List[int]: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hash(self) -> _Leaf__D: ...
    def hashCode(self) -> int: ...
    def hf(self) -> scorex.crypto.hash.CryptographicHash[_Leaf__D]: ...
    def idx(self) -> scala.math.BigInt: ...
    def isNull(self) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    _unapply__D = typing.TypeVar('_unapply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def unapply(x$0: 'Leaf'[_unapply__D]) -> scala.Option[scala.Tuple2[scala.math.BigInt, typing.List[int]]]: ...

_LeafHash__D = typing.TypeVar('_LeafHash__D', bound=typing.List[int])  # <D>
class LeafHash(Node[_LeafHash__D], scala.Product, scala.Serializable, typing.Generic[_LeafHash__D]):
    def __init__(self, hash: _LeafHash__D): ...
    _apply__D = typing.TypeVar('_apply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def apply(hash: _apply__D) -> 'LeafHash'[_apply__D]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__D = typing.TypeVar('_copy__D', bound=typing.List[int])  # <D>
    def copy(self, hash: typing.List[int]) -> 'LeafHash'[typing.List[int]]: ...
    _copy$default$1__D = typing.TypeVar('_copy$default$1__D', bound=typing.List[int])  # <D>
    def copy$default$1(self) -> typing.List[int]: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hash(self) -> _LeafHash__D: ...
    def hashCode(self) -> int: ...
    def isNull(self) -> bool: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> java.lang.String: ...
    def toString(self) -> java.lang.String: ...
    _unapply__D = typing.TypeVar('_unapply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def unapply(x$0: 'LeafHash'[_unapply__D]) -> scala.Option[_unapply__D]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scorex.crypto.authds.merkle.sparse")``.

    BlockchainSimulator: typing.Type[BlockchainSimulator]
    InternalNode: typing.Type[InternalNode]
    Leaf: typing.Type[Leaf]
    LeafHash: typing.Type[LeafHash]
    Node: typing.Type[Node]
    OpsBenchmark: typing.Type[OpsBenchmark]
    SparseMerkleProof: typing.Type[SparseMerkleProof]
    SparseMerkleTree: typing.Type[SparseMerkleTree]
