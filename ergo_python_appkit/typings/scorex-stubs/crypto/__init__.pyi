import scorex.crypto.authds
import scorex.crypto.encode
import scorex.crypto.hash
import scorex.crypto.signatures
import typing


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("scorex.crypto")``.

    authds: scorex.crypto.authds.__module_protocol__
    encode: scorex.crypto.encode.__module_protocol__
    hash: scorex.crypto.hash.__module_protocol__
    signatures: scorex.crypto.signatures.__module_protocol__
