import java.lang
import scala
import scala.collection
import scala.collection.immutable
import scala.reflect.api
import scala.reflect.macros.blackbox
import scala.runtime
import typing



class Context(scala.reflect.macros.blackbox.Context):
    @staticmethod
    def $init$($this: 'Context') -> None: ...
    def enclosingImplicits(self) -> scala.collection.immutable.List['Context.ImplicitCandidate']: ...
    def enclosingMacros(self) -> scala.collection.immutable.List['Context']: ...
    def openImplicits(self) -> scala.collection.immutable.List['Context.ImplicitCandidate']: ...
    def openMacros(self) -> scala.collection.immutable.List['Context']: ...
    class ImplicitCandidate(scala.Product, scala.Serializable):
        $outer: 'Context' = ...
        def __init__(self, $outer: 'Context', pre: scala.reflect.api.Types.TypeApi, sym: scala.reflect.api.Symbols.SymbolApi, pt: scala.reflect.api.Types.TypeApi, tree: scala.reflect.api.Trees.TreeApi): ...
        def canEqual(self, x$1: typing.Any) -> bool: ...
        def copy(self, pre: scala.reflect.api.Types.TypeApi, sym: scala.reflect.api.Symbols.SymbolApi, pt: scala.reflect.api.Types.TypeApi, tree: scala.reflect.api.Trees.TreeApi) -> 'Context.ImplicitCandidate': ...
        def copy$default$1(self) -> scala.reflect.api.Types.TypeApi: ...
        def copy$default$2(self) -> scala.reflect.api.Symbols.SymbolApi: ...
        def copy$default$3(self) -> scala.reflect.api.Types.TypeApi: ...
        def copy$default$4(self) -> scala.reflect.api.Trees.TreeApi: ...
        def equals(self, x$1: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def pre(self) -> scala.reflect.api.Types.TypeApi: ...
        def productArity(self) -> int: ...
        def productElement(self, x$1: int) -> typing.Any: ...
        def productIterator(self) -> scala.collection.Iterator[typing.Any]: ...
        def productPrefix(self) -> java.lang.String: ...
        def pt(self) -> scala.reflect.api.Types.TypeApi: ...
        def sym(self) -> scala.reflect.api.Symbols.SymbolApi: ...
        def toString(self) -> java.lang.String: ...
        def tree(self) -> scala.reflect.api.Trees.TreeApi: ...
    class ImplicitCandidate$(scala.runtime.AbstractFunction4[scala.reflect.api.Types.TypeApi, scala.reflect.api.Symbols.SymbolApi, scala.reflect.api.Types.TypeApi, scala.reflect.api.Trees.TreeApi, 'Context.ImplicitCandidate'], scala.Serializable):
        def __init__(self, $outer: 'Context'): ...
        def apply(self, pre: scala.reflect.api.Types.TypeApi, sym: scala.reflect.api.Symbols.SymbolApi, pt: scala.reflect.api.Types.TypeApi, tree: scala.reflect.api.Trees.TreeApi) -> 'Context.ImplicitCandidate': ...
        def toString(self) -> java.lang.String: ...
        def unapply(self, x$0: 'Context.ImplicitCandidate') -> scala.Option[scala.Tuple4[scala.reflect.api.Types.TypeApi, scala.reflect.api.Symbols.SymbolApi, scala.reflect.api.Types.TypeApi, scala.reflect.api.Trees.TreeApi]]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scala.reflect.macros.whitebox")``.

    Context: typing.Type[Context]
