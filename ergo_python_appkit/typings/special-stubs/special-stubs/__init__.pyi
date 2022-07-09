import special.collection
import special.sigma
import typing


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("special")``.

    collection: special.collection.__module_protocol__
    sigma: special.sigma.__module_protocol__
