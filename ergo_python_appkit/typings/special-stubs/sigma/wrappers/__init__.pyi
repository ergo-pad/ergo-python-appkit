import special.wrappers
import typing



class WrappersModule(special.wrappers.WrappersModule): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("special.sigma.wrappers")``.

    WrappersModule: typing.Type[WrappersModule]
