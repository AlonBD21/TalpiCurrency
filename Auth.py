from hashlib import sha256
import random
from math import sqrt

ROUNDS = 50


def miller_rabin(n):
    assert(n>2)
    m = n - 1
    s = 0
    while m % 2 == 0:
        s += 1
        m = m // 2
    for _ in range(ROUNDS):
        a = int(random.randrange(2, n))
        if (is_compostite(n, m, s, a)):
            return False
    return True


def is_compostite(n, m, s, a):
    p = pow(a, m, n)
    if p == n - 1 or p == 1:
        return False

    for _ in range(s):
        p = pow(p, 2, n)
        if p == 1:
            return True
        if p == n - 1:
            return False
    return True


def get_prime(len):
    assert(len > 2)
    while True:
        num = random.randint(10 ** len, 10 ** (len + 1) - 1)
        if num % 2 == 0:
            num -= 1
        if miller_rabin(num):
            return num


def generate_pair(sk):
    pass


def sign(sk, doc):
    hashed = sha256(doc).digest()
    rand = random.randint(500)
    print(rand)
    signature = ""

    return signature


def verify(pk, doc, sig):
    hashed = sha256(doc).digest()
    pass


