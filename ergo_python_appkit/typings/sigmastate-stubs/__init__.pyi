import sigmastate.Values
import sigmastate.basics
import sigmastate.interpreter
import sigmastate.lang
import sigmastate.serialization
import sigmastate.utils
import typing


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("sigmastate")``.

    Values: sigmastate.Values.__module_protocol__
    basics: sigmastate.basics.__module_protocol__
    interpreter: sigmastate.interpreter.__module_protocol__
    lang: sigmastate.lang.__module_protocol__
    serialization: sigmastate.serialization.__module_protocol__
    utils: sigmastate.utils.__module_protocol__
