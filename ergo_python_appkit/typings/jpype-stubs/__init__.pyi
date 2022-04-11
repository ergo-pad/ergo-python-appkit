import types
import typing

import java
import org
import scala
import special


@typing.overload
def JPackage(__package_name: typing.Literal['java']) -> java.__module_protocol__: ...


@typing.overload
def JPackage(__package_name: typing.Literal['org']) -> org.__module_protocol__: ...


@typing.overload
def JPackage(__package_name: typing.Literal['scala']) -> scala.__module_protocol__: ...


@typing.overload
def JPackage(__package_name: typing.Literal['special']) -> special.__module_protocol__: ...


def JPackage(__package_name) -> types.ModuleType: ...

