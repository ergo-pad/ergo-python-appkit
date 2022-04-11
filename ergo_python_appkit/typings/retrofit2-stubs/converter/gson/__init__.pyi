import com.google.gson
import java.lang.annotation
import java.lang.reflect
import okhttp3
import retrofit2
import typing



class GsonConverterFactory(retrofit2.Converter.Factory):
    @typing.overload
    @staticmethod
    def create() -> 'GsonConverterFactory': ...
    @typing.overload
    @staticmethod
    def create(gson: com.google.gson.Gson) -> 'GsonConverterFactory': ...
    def requestBodyConverter(self, type: java.lang.reflect.Type, annotationArray: typing.List[java.lang.annotation.Annotation], annotationArray2: typing.List[java.lang.annotation.Annotation], retrofit: retrofit2.Retrofit) -> retrofit2.Converter[typing.Any, okhttp3.RequestBody]: ...
    def responseBodyConverter(self, type: java.lang.reflect.Type, annotationArray: typing.List[java.lang.annotation.Annotation], retrofit: retrofit2.Retrofit) -> retrofit2.Converter[okhttp3.ResponseBody, typing.Any]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("retrofit2.converter.gson")``.

    GsonConverterFactory: typing.Type[GsonConverterFactory]
