import random
from largeprimegen import largeprimegen
import sys

sys.setrecursionlimit(1500)


def gcdEx(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdEx(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def lcm(a, b):
    multiplier = abs(a * b) // gcdEx(a, b)[0]
    return multiplier


def RSAkeygen():
    while True:
        p = largeprimegen(1024)
        q = largeprimegen(1024)
        if p == q:
            continue
        else:
            break
    n = p * q
    ctf = lcm(p - 1, q - 1)
    while True:
        e = random.randrange(1, ctf)
        if gcdEx(e, ctf)[0] == 1:
            break
        else:
            continue
    d = gcdEx(e, ctf)[1]
    return e, n, d


def RSAencrypt(m, e_, n_):
    c = pow(m, e_, n_)
    return c


def RSAdecrypt(c, d_, n_):
    m = pow(c, d_, n_)
    return m


key = RSAkeygen()
encrypted = RSAencrypt(1550, key[0], key[1])
decrypted = RSAdecrypt(encrypted, key[2], key[1])

print(decrypted)
