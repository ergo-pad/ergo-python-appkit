import java.lang
import okhttp3
import typing



class ApiKeyAuth(okhttp3.Interceptor):
    def __init__(self, string: typing.Union[java.lang.String, str], string2: typing.Union[java.lang.String, str]): ...
    def getApiKey(self) -> java.lang.String: ...
    def getLocation(self) -> java.lang.String: ...
    def getParamName(self) -> java.lang.String: ...
    def intercept(self, chain: okhttp3.Interceptor.Chain) -> okhttp3.Response: ...
    def setApiKey(self, string: typing.Union[java.lang.String, str]) -> None: ...

class HttpBasicAuth(okhttp3.Interceptor):
    def __init__(self): ...
    def getPassword(self) -> java.lang.String: ...
    def getUsername(self) -> java.lang.String: ...
    def intercept(self, chain: okhttp3.Interceptor.Chain) -> okhttp3.Response: ...
    def setCredentials(self, string: typing.Union[java.lang.String, str], string2: typing.Union[java.lang.String, str]) -> None: ...
    def setPassword(self, string: typing.Union[java.lang.String, str]) -> None: ...
    def setUsername(self, string: typing.Union[java.lang.String, str]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.ergoplatform.explorer.client.auth")``.

    ApiKeyAuth: typing.Type[ApiKeyAuth]
    HttpBasicAuth: typing.Type[HttpBasicAuth]
