import scala.reflect.api
import scala.reflect.macros
import typing



class Context(scala.reflect.macros.Aliases, scala.reflect.macros.Enclosures, scala.reflect.macros.Names, scala.reflect.macros.Reifiers, scala.reflect.macros.FrontEnds, scala.reflect.macros.Infrastructure, scala.reflect.macros.Typers, scala.reflect.macros.Parsers, scala.reflect.macros.Evals, scala.reflect.macros.ExprUtils, scala.reflect.macros.Internals):
    def mirror(self) -> scala.reflect.api.Mirror: ...
    def prefix(self) -> scala.reflect.api.Exprs.Expr[typing.Any]: ...
    def universe(self) -> scala.reflect.macros.Universe: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scala.reflect.macros.blackbox")``.

    Context: typing.Type[Context]
