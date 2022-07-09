import java.lang
import java.math
import java.util
import org.bouncycastle.math.ec.custom.sec
import org.ergoplatform
import sigmastate.basics
import typing



class ErgoSignature:
    def __init__(self): ...
    def sign(self, byteArray: typing.List[int], bigInteger: java.math.BigInteger) -> typing.List[int]: ...
    def verify(self, byteArray: typing.List[int], byteArray2: typing.List[int], secP256K1Point: org.bouncycastle.math.ec.custom.sec.SecP256K1Point) -> bool: ...

class ErgoUnsafeProver:
    def __init__(self): ...
    @typing.overload
    def prove(self, unsignedErgoLikeTransaction: org.ergoplatform.UnsignedErgoLikeTransaction, map: typing.Union[java.util.Map[typing.Union[java.lang.String, str], sigmastate.basics.DLogProtocol.DLogProverInput], typing.Mapping[typing.Union[java.lang.String, str], sigmastate.basics.DLogProtocol.DLogProverInput]]) -> org.ergoplatform.ErgoLikeTransaction: ...
    @typing.overload
    def prove(self, unsignedErgoLikeTransaction: org.ergoplatform.UnsignedErgoLikeTransaction, dLogProverInput: sigmastate.basics.DLogProtocol.DLogProverInput) -> org.ergoplatform.ErgoLikeTransaction: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.ergoplatform.wallet.interface4j.crypto")``.

    ErgoSignature: typing.Type[ErgoSignature]
    ErgoUnsafeProver: typing.Type[ErgoUnsafeProver]
