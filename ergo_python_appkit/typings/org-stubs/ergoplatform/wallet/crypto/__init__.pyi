import java.lang
import org.bouncycastle.math.ec.custom.sec
import org.ergoplatform.wallet.settings
import scala
import scala.math
import scala.util
import typing



class AES:
    @staticmethod
    def AuthTagBitsLen() -> int: ...
    @staticmethod
    def CipherAlgo() -> java.lang.String: ...
    @staticmethod
    def CipherAlgoInstance() -> java.lang.String: ...
    @staticmethod
    def NonceBitsLen() -> int: ...
    @staticmethod
    def decrypt(ciphertext: typing.List[int], pass_: typing.List[str], salt: typing.List[int], iv: typing.List[int], authTag: typing.List[int], settings: org.ergoplatform.wallet.settings.EncryptionSettings) -> scala.util.Try[typing.List[int]]: ...
    @staticmethod
    def encrypt(data: typing.List[int], pass_: typing.List[str], salt: typing.List[int], iv: typing.List[int], settings: org.ergoplatform.wallet.settings.EncryptionSettings) -> scala.Tuple2[typing.List[int], typing.List[int]]: ...

class ErgoSignature:
    @staticmethod
    def sign(msg: typing.List[int], sk: scala.math.BigInt) -> typing.List[int]: ...
    @staticmethod
    def verify(msg: typing.List[int], signature: typing.List[int], pk: org.bouncycastle.math.ec.custom.sec.SecP256K1Point) -> bool: ...

class HmacSHA512:
    @staticmethod
    def hash(key: typing.List[int], data: typing.List[int]) -> typing.List[int]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.ergoplatform.wallet.crypto")``.

    AES: typing.Type[AES]
    ErgoSignature: typing.Type[ErgoSignature]
    HmacSHA512: typing.Type[HmacSHA512]
