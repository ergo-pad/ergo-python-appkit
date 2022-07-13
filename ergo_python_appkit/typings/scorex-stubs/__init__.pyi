import scorex.crypto
import scorex.util
import scorex.utils
import typing


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scorex")``.

    crypto: scorex.crypto.__module_protocol__
    util: scorex.util.__module_protocol__
    utils: scorex.utils.__module_protocol__
