from ecdsa import SigningKey, VerifyingKey, NIST256p, BadSignatureError, MalformedPointError

CURVE = NIST256p


class User:
    def __init__(self, sk, vk):
        """
        :param sk: signing (private) key
        :type sk: ecdsa.SigningKey
        :param vk: verifying (public) key
        :type vk: ecdsa.VerifyingKey
        """
        self.__sk = sk
        self.__vk = vk

    @classmethod
    def generate(cls):
        """
        Creates new user with random sk and vk
        :return: User
        """
        sk = SigningKey.generate(curve=CURVE)
        return cls(sk, sk.verifying_key)

    @classmethod
    def from_sk_bytes(cls, sk):
        """
        Creates new user from a given signing (private) key
        :param sk: signing key
        :type sk: bytes
        :return: User
        """
        sk = SigningKey.from_string(sk, curve=CURVE)
        return cls(sk, sk.verifying_key)

    @classmethod
    def verify(cls, data_bytes, vk, signature):
        """
        Verifies a signature
        :param data_bytes: bytes of the signed data
        :param vk: verifying key (bytes)
        :param signature: signature (bytes)
        :return:
        """
        try:
            vk = VerifyingKey.from_string (vk, curve=CURVE)
            return vk.verify(signature, data_bytes)
        except BadSignatureError:
            return False
            # bad signature
        except MalformedPointError:
            return False
            # Length of string does not match lengths of any of the supported encodings of NIST256p curve

    def get_sk_bytes(self):
        """
        :return: signing key (bytes)
        """
        return self.__sk.to_string()

    def get_vk_bytes(self):
        """
        :return: verifying key (bytes)
        """
        return self.__vk.to_string()

    def __repr__(self):
        return "USER\nsk={0}\nvk={1}".format(self.__sk.to_string(),
                                             self.__vk.to_string())

    def sign(self, data_bytes):
        """
        sign data with the signing key
        :param data_bytes: data to sign on (bytes)
        :return: signature (bytes)
        """
        return self.__sk.sign(data_bytes)


if __name__ == "__main__":
    a = User.generate()
    b = User.from_sk_bytes(a.get_sk_bytes())
    print(repr(a))
    print(repr(b))
    print(repr(a) == repr(b))

    data = b"Alon Ben Dov"

    signature = a.sign(data)

    print(signature)

    print( User.verify(data, b.get_vk_bytes(), signature))
    print( User.verify (b'cxbnce', b'asdfghgd', signature))
