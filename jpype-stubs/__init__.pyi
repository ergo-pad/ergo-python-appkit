import types
import typing

import io_


@typing.overload
def JPackage(__package_name: typing.Literal['io']) -> io_.__module_protocol__: ...


def JPackage(__package_name) -> types.ModuleType: ...

