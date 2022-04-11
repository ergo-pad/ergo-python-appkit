import com.google.gson
import com.google.gson.stream
import datetime
import java.net
import java.sql
import java.text
import java.time
import java.time.format
import java.util
import okhttp3
import org
import org.ergoplatform.explorer.client.auth
import org.ergoplatform.explorer.client.model
import retrofit2
import typing



class DefaultApi:
    def getApiV1AddressesP1BalanceConfirmed(self, string: str, integer: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.Balance]: ...
    def getApiV1AddressesP1BalanceTotal(self, string: str) -> retrofit2.Call[org.ergoplatform.explorer.client.model.TotalBalance]: ...
    def getApiV1AddressesP1Transactions(self, string: str, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.Items[org.ergoplatform.explorer.client.model.TransactionInfo]]: ...
    def getApiV1Assets(self, integer: int, integer2: int, string: str, boolean: bool) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ItemsA]: ...
    def getApiV1AssetsSearchBytokenid(self, string: str, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ItemsA]: ...
    def getApiV1Blocks(self, integer: int, integer2: int, string: str, string2: str) -> retrofit2.Call[org.ergoplatform.explorer.client.model.Items[org.ergoplatform.explorer.client.model.BlockInfo]]: ...
    def getApiV1BlocksP1(self, string: str) -> retrofit2.Call[org.ergoplatform.explorer.client.model.BlockSummary]: ...
    def getApiV1BoxesByaddressP1(self, string: str, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ItemsA]: ...
    def getApiV1BoxesByergotreeP1(self, string: str, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ItemsA]: ...
    def getApiV1BoxesByergotreetemplatehashP1(self, string: str, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ItemsA]: ...
    def getApiV1BoxesByergotreetemplatehashP1Stream(self, string: str, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ListOutputInfo]: ...
    def getApiV1BoxesBytokenidP1(self, string: str, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ItemsA]: ...
    def getApiV1BoxesP1(self, string: str) -> retrofit2.Call[org.ergoplatform.explorer.client.model.OutputInfo]: ...
    def getApiV1BoxesUnspentByaddressP1(self, string: str, integer: int, integer2: int, string2: str) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ItemsA]: ...
    def getApiV1BoxesUnspentByergotreeP1(self, string: str, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ItemsA]: ...
    def getApiV1BoxesUnspentByergotreetemplatehashP1(self, string: str, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ItemsA]: ...
    def getApiV1BoxesUnspentByergotreetemplatehashP1Stream(self, string: str, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ListOutputInfo]: ...
    def getApiV1BoxesUnspentBylastepochsStream(self, integer: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ListOutputInfo]: ...
    def getApiV1BoxesUnspentBytokenidP1(self, string: str, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ItemsA]: ...
    def getApiV1BoxesUnspentStream(self, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ListOutputInfo]: ...
    def getApiV1EpochsParams(self) -> retrofit2.Call[org.ergoplatform.explorer.client.model.EpochParameters]: ...
    def getApiV1MempoolTransactionsByaddressP1(self, string: str, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.Items[org.ergoplatform.explorer.client.model.TransactionInfo]]: ...
    def getApiV1Tokens(self, integer: int, integer2: int, string: str, boolean: bool) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ItemsA]: ...
    def getApiV1TokensP1(self, string: str) -> retrofit2.Call[org.ergoplatform.explorer.client.model.TokenInfo]: ...
    def getApiV1TokensSearch(self, string: str, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ItemsA]: ...
    def getApiV1TransactionsByinputsscripttemplatehashP1(self, string: str, integer: int, integer2: int, string2: str) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ItemsA]: ...
    def getApiV1TransactionsP1(self, string: str) -> retrofit2.Call[org.ergoplatform.explorer.client.model.TransactionInfo]: ...
    def postApiV1BoxesSearch(self, boxQuery: org.ergoplatform.explorer.client.model.BoxQuery, integer: int, integer2: int) -> retrofit2.Call[org.ergoplatform.explorer.client.model.ItemsA]: ...

class ExplorerApiClient:
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str): ...
    @typing.overload
    def __init__(self, string: str, stringArray: typing.List[str]): ...
    @typing.overload
    def __init__(self, string: str, proxy: java.net.Proxy): ...
    def addAuthorization(self, string: str, interceptor: okhttp3.Interceptor) -> 'ExplorerApiClient': ...
    def addAuthsToOkBuilder(self, builder: okhttp3.OkHttpClient.Builder) -> None: ...
    def configureFromOkclient(self, okHttpClient: okhttp3.OkHttpClient) -> None: ...
    def createDefaultAdapter(self) -> None: ...
    _createService__S = typing.TypeVar('_createService__S')  # <S>
    def createService(self, class_: typing.Type[_createService__S]) -> _createService__S: ...
    def getAdapterBuilder(self) -> retrofit2.Retrofit.Builder: ...
    def getApiAuthorizations(self) -> java.util.Map[str, okhttp3.Interceptor]: ...
    def getOkBuilder(self) -> okhttp3.OkHttpClient.Builder: ...
    def setAccessToken(self, string: str) -> 'ExplorerApiClient': ...
    def setAdapterBuilder(self, builder: retrofit2.Retrofit.Builder) -> 'ExplorerApiClient': ...
    def setApiAuthorizations(self, map: typing.Union[java.util.Map[str, okhttp3.Interceptor], typing.Mapping[str, okhttp3.Interceptor]]) -> 'ExplorerApiClient': ...
    def setApiKey(self, string: str) -> 'ExplorerApiClient': ...
    def setCredentials(self, string: str, string2: str) -> 'ExplorerApiClient': ...
    def setDateFormat(self, dateFormat: java.text.DateFormat) -> 'ExplorerApiClient': ...
    def setLocalDateFormat(self, dateTimeFormatter: java.time.format.DateTimeFormatter) -> 'ExplorerApiClient': ...
    def setOffsetDateTimeFormat(self, dateTimeFormatter: java.time.format.DateTimeFormatter) -> 'ExplorerApiClient': ...
    def setSqlDateFormat(self, dateFormat: java.text.DateFormat) -> 'ExplorerApiClient': ...

class JSON:
    def __init__(self): ...
    @staticmethod
    def createGson() -> com.google.gson.GsonBuilder: ...
    def getGson(self) -> com.google.gson.Gson: ...
    def setDateFormat(self, dateFormat: java.text.DateFormat) -> 'JSON': ...
    def setGson(self, gson: com.google.gson.Gson) -> 'JSON': ...
    def setLocalDateFormat(self, dateTimeFormatter: java.time.format.DateTimeFormatter) -> 'JSON': ...
    def setOffsetDateTimeFormat(self, dateTimeFormatter: java.time.format.DateTimeFormatter) -> 'JSON': ...
    def setSqlDateFormat(self, dateFormat: java.text.DateFormat) -> 'JSON': ...
    class DateTypeAdapter(com.google.gson.TypeAdapter[java.util.Date]):
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, dateFormat: java.text.DateFormat): ...
        def read(self, jsonReader: com.google.gson.stream.JsonReader) -> java.util.Date: ...
        def setFormat(self, dateFormat: java.text.DateFormat) -> None: ...
        def write(self, jsonWriter: com.google.gson.stream.JsonWriter, date: java.util.Date) -> None: ...
    class LocalDateTypeAdapter(com.google.gson.TypeAdapter[java.time.LocalDate]):
        @typing.overload
        def __init__(self, jSON: 'JSON'): ...
        @typing.overload
        def __init__(self, jSON: 'JSON', dateTimeFormatter: java.time.format.DateTimeFormatter): ...
        def read(self, jsonReader: com.google.gson.stream.JsonReader) -> java.time.LocalDate: ...
        def setFormat(self, dateTimeFormatter: java.time.format.DateTimeFormatter) -> None: ...
        def write(self, jsonWriter: com.google.gson.stream.JsonWriter, localDate: java.time.LocalDate) -> None: ...
    class OffsetDateTimeTypeAdapter(com.google.gson.TypeAdapter[java.time.OffsetDateTime]):
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, dateTimeFormatter: java.time.format.DateTimeFormatter): ...
        def read(self, jsonReader: com.google.gson.stream.JsonReader) -> java.time.OffsetDateTime: ...
        def setFormat(self, dateTimeFormatter: java.time.format.DateTimeFormatter) -> None: ...
        def write(self, jsonWriter: com.google.gson.stream.JsonWriter, offsetDateTime: java.time.OffsetDateTime) -> None: ...
    class SqlDateTypeAdapter(com.google.gson.TypeAdapter[java.sql.Date]):
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, dateFormat: java.text.DateFormat): ...
        def read(self, jsonReader: com.google.gson.stream.JsonReader) -> java.sql.Date: ...
        def setFormat(self, dateFormat: java.text.DateFormat) -> None: ...
        def write(self, jsonWriter: com.google.gson.stream.JsonWriter, date: typing.Union[java.sql.Date, datetime.date]) -> None: ...

class StringUtil:
    def __init__(self): ...
    @staticmethod
    def containsIgnoreCase(stringArray: typing.List[str], string2: str) -> bool: ...
    @staticmethod
    def join(stringArray: typing.List[str], string2: str) -> str: ...

class CollectionFormats:
    def __init__(self): ...
    class CSVParams:
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, stringArray: typing.List[str]): ...
        @typing.overload
        def __init__(self, list: java.util.List[str]): ...
        def getParams(self) -> java.util.List[str]: ...
        def setParams(self, list: java.util.List[str]) -> None: ...
        def toString(self) -> str: ...
    class PIPESParams(org.ergoplatform.explorer.client.CollectionFormats.CSVParams):
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, stringArray: typing.List[str]): ...
        @typing.overload
        def __init__(self, list: java.util.List[str]): ...
        def toString(self) -> str: ...
    class SSVParams(org.ergoplatform.explorer.client.CollectionFormats.CSVParams):
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, stringArray: typing.List[str]): ...
        @typing.overload
        def __init__(self, list: java.util.List[str]): ...
        def toString(self) -> str: ...
    class TSVParams(org.ergoplatform.explorer.client.CollectionFormats.CSVParams):
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, stringArray: typing.List[str]): ...
        @typing.overload
        def __init__(self, list: java.util.List[str]): ...
        def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.ergoplatform.explorer.client")``.

    CollectionFormats: typing.Type[CollectionFormats]
    DefaultApi: typing.Type[DefaultApi]
    ExplorerApiClient: typing.Type[ExplorerApiClient]
    JSON: typing.Type[JSON]
    StringUtil: typing.Type[StringUtil]
    auth: org.ergoplatform.explorer.client.auth.__module_protocol__
    model: org.ergoplatform.explorer.client.model.__module_protocol__
