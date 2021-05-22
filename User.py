from ecdsa import SigningKey, VerifyingKey, NIST256p

CURVE = NIST256p


class User:
    def __init__(self, sk, vk):
        self.__sk = sk
        self.__vk = vk

    @classmethod
    def generate(cls):
        sk = SigningKey.generate(curve=CURVE)
        return cls(sk, sk.verifying_key)

    @classmethod
    def from_sk_bytes(cls, sk):
        sk = SigningKey.from_string(sk, curve=CURVE)
        return cls(sk, sk.verifying_key)

    @classmethod
    def verify(cls, data_bits, vk, signature):
        vk = VerifyingKey.from_string(vk, curve=CURVE)
        return vk.verify(signature, data_bits)

    def get_sk_vk_bytes(self):
        return self.__sk.to_string(), self.__vk.to_string()

    def __repr__(self):
        return "USER\nsk={0}\nvk={1}".format(self.__sk.to_string(),
                                             self.__vk.to_string())

    def sign(self, data_bits):
        return self.__sk.sign(data_bits)

if __name__ == "__main__":
    a = User.generate()
    b = User.from_sk_bytes(a.get_sk_vk_bytes()[0])
    print(repr(a))
    print(repr(b))
    print(repr(a) == repr(b))

    data = b"Alon Ben Dov"

    signature = a.sign(data)

    print(signature)

    assert User.verify(data,b.get_sk_vk_bytes()[1],signature)

