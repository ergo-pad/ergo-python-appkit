import org.ergoplatform.wallet.protocol.context
import typing



class Constants:
    @staticmethod
    def BlocksPerDay() -> int: ...
    @staticmethod
    def BlocksPerHour() -> int: ...
    @staticmethod
    def BlocksPerMonth() -> int: ...
    @staticmethod
    def BlocksPerWeek() -> int: ...
    @staticmethod
    def BlocksPerYear() -> int: ...
    @staticmethod
    def HashLength() -> int: ...
    @staticmethod
    def StorageContractCost() -> int: ...
    @staticmethod
    def StorageIndexVarId() -> int: ...
    @staticmethod
    def StoragePeriod() -> int: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.ergoplatform.wallet.protocol")``.

    Constants: typing.Type[Constants]
    context: org.ergoplatform.wallet.protocol.context.__module_protocol__
