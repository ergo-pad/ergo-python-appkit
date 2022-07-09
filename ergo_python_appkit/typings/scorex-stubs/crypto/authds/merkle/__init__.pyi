import java.lang
import scala
import scala.collection
import scala.collection.immutable
import scala.collection.mutable
import scorex.crypto.authds.merkle.sparse
import scorex.crypto.hash
import scorex.util
import scorex.util.encode
import typing



_MerkleProof__D = typing.TypeVar('_MerkleProof__D', bound=typing.List[int])  # <D>
class MerkleProof(scorex.util.ScorexEncoding, scala.Product, scala.Serializable, typing.Generic[_MerkleProof__D]):
    def __init__(self, leafData: typing.List[int], levels: scala.collection.Seq[scala.Tuple2[typing.List[int], typing.Any]], hf: scorex.crypto.hash.CryptographicHash[_MerkleProof__D]): ...
    @staticmethod
    def LeftSide() -> int: ...
    @staticmethod
    def RightSide() -> int: ...
    _apply__D = typing.TypeVar('_apply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def apply(leafData: typing.List[int], levels: scala.collection.Seq[scala.Tuple2[typing.List[int], typing.Any]], hf: scorex.crypto.hash.CryptographicHash[_apply__D]) -> 'MerkleProof'[_apply__D]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__D = typing.TypeVar('_copy__D', bound=typing.List[int])  # <D>
    def copy(self, leafData: typing.List[int], levels: scala.collection.Seq[scala.Tuple2[typing.List[int], typing.Any]], hf: scorex.crypto.hash.CryptographicHash[typing.List[int]]) -> 'MerkleProof'[typing.List[int]]: ...
    _copy$default$1__D = typing.TypeVar('_copy$default$1__D', bound=typing.List[int])  # <D>
    def copy$default$1(self) -> typing.List[int]: ...
    _copy$default$2__D = typing.TypeVar('_copy$default$2__D', bound=typing.List[int])  # <D>
    def copy$default$2(self) -> scala.collection.Seq[scala.Tuple2[typing.List[int], typing.Any]]: ...
    def encoder(self) -> scorex.util.encode.BytesEncoder: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def hf(self) -> scorex.crypto.hash.CryptographicHash[_MerkleProof__D]: ...
    def leafData(self) -> typing.List[int]: ...
    def levels(self) -> scala.collection.Seq[scala.Tuple2[typing.List[int], typing.Any]]: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> java.lang.String: ...
    def scorex$util$ScorexEncoding$_setter_$encoder_$eq(self, x$1: scorex.util.encode.BytesEncoder) -> None: ...
    def toString(self) -> java.lang.String: ...
    _unapply__D = typing.TypeVar('_unapply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def unapply(x$0: 'MerkleProof'[_unapply__D]) -> scala.Option[scala.Tuple2[typing.List[int], scala.collection.Seq[scala.Tuple2[typing.List[int], typing.Any]]]]: ...
    def valid(self, expectedRootHash: typing.List[int]) -> bool: ...

_MerkleTree__D = typing.TypeVar('_MerkleTree__D', bound=typing.List[int])  # <D>
class MerkleTree(scala.Product, scala.Serializable, typing.Generic[_MerkleTree__D]):
    def __init__(self, topNode: 'Node'[_MerkleTree__D], elementsHashIndex: scala.collection.immutable.Map[scala.collection.mutable.WrappedArray.ofByte, typing.Any]): ...
    @staticmethod
    def InternalNodePrefix() -> int: ...
    @staticmethod
    def LeafPrefix() -> int: ...
    _apply_0__D = typing.TypeVar('_apply_0__D', bound=typing.List[int])  # <D>
    _apply_1__D = typing.TypeVar('_apply_1__D', bound=typing.List[int])  # <D>
    @typing.overload
    @staticmethod
    def apply(payload: scala.collection.Seq[typing.List[int]], hf: scorex.crypto.hash.CryptographicHash[_apply_0__D]) -> 'MerkleTree'[_apply_0__D]: ...
    @typing.overload
    @staticmethod
    def apply(topNode: 'Node'[_apply_1__D], elementsHashIndex: scala.collection.immutable.Map[scala.collection.mutable.WrappedArray.ofByte, typing.Any]) -> 'MerkleTree'[_apply_1__D]: ...
    _calcTopNode__D = typing.TypeVar('_calcTopNode__D', bound=typing.List[int])  # <D>
    @staticmethod
    def calcTopNode(nodes: scala.collection.Seq['Node'[_calcTopNode__D]], hf: scorex.crypto.hash.CryptographicHash[_calcTopNode__D]) -> 'Node'[_calcTopNode__D]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__D = typing.TypeVar('_copy__D', bound=typing.List[int])  # <D>
    def copy(self, topNode: 'Node'[typing.List[int]], elementsHashIndex: scala.collection.immutable.Map[scala.collection.mutable.WrappedArray.ofByte, typing.Any]) -> 'MerkleTree'[typing.List[int]]: ...
    _copy$default$1__D = typing.TypeVar('_copy$default$1__D', bound=typing.List[int])  # <D>
    def copy$default$1(self) -> 'Node'[typing.List[int]]: ...
    _copy$default$2__D = typing.TypeVar('_copy$default$2__D', bound=typing.List[int])  # <D>
    def copy$default$2(self) -> scala.collection.immutable.Map[scala.collection.mutable.WrappedArray.ofByte, typing.Any]: ...
    def elementsHashIndex(self) -> scala.collection.immutable.Map[scala.collection.mutable.WrappedArray.ofByte, typing.Any]: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def length(self) -> int: ...
    def lengthWithEmptyLeafs(self) -> int: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> java.lang.String: ...
    def proofByElement(self, element: 'Leaf'[_MerkleTree__D]) -> scala.Option[MerkleProof[_MerkleTree__D]]: ...
    def proofByElementHash(self, hash: _MerkleTree__D) -> scala.Option[MerkleProof[_MerkleTree__D]]: ...
    def proofByIndex(self, index: int) -> scala.Option[MerkleProof[_MerkleTree__D]]: ...
    def rootHash(self) -> _MerkleTree__D: ...
    def toString(self) -> java.lang.String: ...
    def topNode(self) -> 'Node'[_MerkleTree__D]: ...
    _unapply__D = typing.TypeVar('_unapply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def unapply(x$0: 'MerkleTree'[_unapply__D]) -> scala.Option[scala.Tuple2['Node'[_unapply__D], scala.collection.immutable.Map[scala.collection.mutable.WrappedArray.ofByte, typing.Any]]]: ...

_Node__D = typing.TypeVar('_Node__D', bound=typing.List[int])  # <D>
class Node(scorex.util.ScorexEncoding, typing.Generic[_Node__D]):
    def hash(self) -> _Node__D: ...

_EmptyNode__D = typing.TypeVar('_EmptyNode__D', bound=typing.List[int])  # <D>
class EmptyNode(Node[_EmptyNode__D], scala.Product, scala.Serializable, typing.Generic[_EmptyNode__D]):
    def __init__(self, hf: scorex.crypto.hash.CryptographicHash[_EmptyNode__D]): ...
    _apply__D = typing.TypeVar('_apply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def apply(hf: scorex.crypto.hash.CryptographicHash[_apply__D]) -> 'EmptyNode'[_apply__D]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__D = typing.TypeVar('_copy__D', bound=typing.List[int])  # <D>
    def copy(self, hf: scorex.crypto.hash.CryptographicHash[typing.List[int]]) -> 'EmptyNode'[typing.List[int]]: ...
    def encoder(self) -> scorex.util.encode.BytesEncoder: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hash(self) -> _EmptyNode__D: ...
    def hashCode(self) -> int: ...
    def hf(self) -> scorex.crypto.hash.CryptographicHash[_EmptyNode__D]: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> java.lang.String: ...
    def scorex$util$ScorexEncoding$_setter_$encoder_$eq(self, x$1: scorex.util.encode.BytesEncoder) -> None: ...
    def toString(self) -> java.lang.String: ...
    _unapply__D = typing.TypeVar('_unapply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def unapply(x$0: 'EmptyNode'[_unapply__D]) -> bool: ...

_EmptyRootNode__D = typing.TypeVar('_EmptyRootNode__D', bound=typing.List[int])  # <D>
class EmptyRootNode(Node[_EmptyRootNode__D], scala.Product, scala.Serializable, typing.Generic[_EmptyRootNode__D]):
    def __init__(self, hf: scorex.crypto.hash.CryptographicHash[_EmptyRootNode__D]): ...
    _apply__D = typing.TypeVar('_apply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def apply(hf: scorex.crypto.hash.CryptographicHash[_apply__D]) -> 'EmptyRootNode'[_apply__D]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__D = typing.TypeVar('_copy__D', bound=typing.List[int])  # <D>
    def copy(self, hf: scorex.crypto.hash.CryptographicHash[typing.List[int]]) -> 'EmptyRootNode'[typing.List[int]]: ...
    def encoder(self) -> scorex.util.encode.BytesEncoder: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hash(self) -> _EmptyRootNode__D: ...
    def hashCode(self) -> int: ...
    def hf(self) -> scorex.crypto.hash.CryptographicHash[_EmptyRootNode__D]: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> java.lang.String: ...
    def scorex$util$ScorexEncoding$_setter_$encoder_$eq(self, x$1: scorex.util.encode.BytesEncoder) -> None: ...
    def toString(self) -> java.lang.String: ...
    _unapply__D = typing.TypeVar('_unapply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def unapply(x$0: 'EmptyRootNode'[_unapply__D]) -> bool: ...

_InternalNode__D = typing.TypeVar('_InternalNode__D', bound=typing.List[int])  # <D>
class InternalNode(Node[_InternalNode__D], scala.Product, scala.Serializable, typing.Generic[_InternalNode__D]):
    def __init__(self, left: Node[_InternalNode__D], right: Node[_InternalNode__D], hf: scorex.crypto.hash.CryptographicHash[_InternalNode__D]): ...
    _apply__D = typing.TypeVar('_apply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def apply(left: Node[_apply__D], right: Node[_apply__D], hf: scorex.crypto.hash.CryptographicHash[_apply__D]) -> 'InternalNode'[_apply__D]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__D = typing.TypeVar('_copy__D', bound=typing.List[int])  # <D>
    def copy(self, left: Node[typing.List[int]], right: Node[typing.List[int]], hf: scorex.crypto.hash.CryptographicHash[typing.List[int]]) -> 'InternalNode'[typing.List[int]]: ...
    _copy$default$1__D = typing.TypeVar('_copy$default$1__D', bound=typing.List[int])  # <D>
    def copy$default$1(self) -> Node[typing.List[int]]: ...
    _copy$default$2__D = typing.TypeVar('_copy$default$2__D', bound=typing.List[int])  # <D>
    def copy$default$2(self) -> Node[typing.List[int]]: ...
    def encoder(self) -> scorex.util.encode.BytesEncoder: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hash(self) -> _InternalNode__D: ...
    def hashCode(self) -> int: ...
    def hf(self) -> scorex.crypto.hash.CryptographicHash[_InternalNode__D]: ...
    def left(self) -> Node[_InternalNode__D]: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> java.lang.String: ...
    def right(self) -> Node[_InternalNode__D]: ...
    def scorex$util$ScorexEncoding$_setter_$encoder_$eq(self, x$1: scorex.util.encode.BytesEncoder) -> None: ...
    def toString(self) -> java.lang.String: ...
    _unapply__D = typing.TypeVar('_unapply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def unapply(x$0: 'InternalNode'[_unapply__D]) -> scala.Option[scala.Tuple2[Node[_unapply__D], Node[_unapply__D]]]: ...

_Leaf__D = typing.TypeVar('_Leaf__D', bound=typing.List[int])  # <D>
class Leaf(Node[_Leaf__D], scala.Product, scala.Serializable, typing.Generic[_Leaf__D]):
    def __init__(self, data: typing.List[int], hf: scorex.crypto.hash.CryptographicHash[_Leaf__D]): ...
    _apply__D = typing.TypeVar('_apply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def apply(data: typing.List[int], hf: scorex.crypto.hash.CryptographicHash[_apply__D]) -> 'Leaf'[_apply__D]: ...
    def canEqual(self, x$1: typing.Any) -> bool: ...
    _copy__D = typing.TypeVar('_copy__D', bound=typing.List[int])  # <D>
    def copy(self, data: typing.List[int], hf: scorex.crypto.hash.CryptographicHash[typing.List[int]]) -> 'Leaf'[typing.List[int]]: ...
    _copy$default$1__D = typing.TypeVar('_copy$default$1__D', bound=typing.List[int])  # <D>
    def copy$default$1(self) -> typing.List[int]: ...
    def data(self) -> typing.List[int]: ...
    def encoder(self) -> scorex.util.encode.BytesEncoder: ...
    def equals(self, x$1: typing.Any) -> bool: ...
    def hash(self) -> _Leaf__D: ...
    def hashCode(self) -> int: ...
    def hf(self) -> scorex.crypto.hash.CryptographicHash[_Leaf__D]: ...
    def productArity(self) -> int: ...
    def productElement(self, x$1: int) -> typing.Any: ...
    def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
    def productPrefix(self) -> java.lang.String: ...
    def scorex$util$ScorexEncoding$_setter_$encoder_$eq(self, x$1: scorex.util.encode.BytesEncoder) -> None: ...
    def toString(self) -> java.lang.String: ...
    _unapply__D = typing.TypeVar('_unapply__D', bound=typing.List[int])  # <D>
    @staticmethod
    def unapply(x$0: 'Leaf'[_unapply__D]) -> scala.Option[typing.List[int]]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scorex.crypto.authds.merkle")``.

    EmptyNode: typing.Type[EmptyNode]
    EmptyRootNode: typing.Type[EmptyRootNode]
    InternalNode: typing.Type[InternalNode]
    Leaf: typing.Type[Leaf]
    MerkleProof: typing.Type[MerkleProof]
    MerkleTree: typing.Type[MerkleTree]
    Node: typing.Type[Node]
    sparse: scorex.crypto.authds.merkle.sparse.__module_protocol__