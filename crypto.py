from ecdsa import SigningKey, NIST384p
sk = SigningKey.generate(curve=NIST384p)
sk_string = sk.to_string()
sk2 = SigningKey.from_string(sk_string, curve=NIST384p)
print(sk_string.hex())
print(sk2.to_string().hex())

from ecdsa import SigningKey, VerifyingKey, NIST384p
sk = SigningKey.generate(curve=NIST384p)
vk = sk.verifying_key
vk_string = vk.to_string()
vk2 = VerifyingKey.from_string(vk_string, curve=NIST384p)
# vk and vk2 are the same key

from ecdsa import SigningKey, VerifyingKey, NIST384p
sk = SigningKey.generate(curve=NIST384p)
vk = sk.verifying_key
vk_pem = vk.to_pem()
vk2 = VerifyingKey.from_pem(vk_pem)