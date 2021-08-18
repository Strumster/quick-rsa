import random
from largeprimegen import largeprimegen
import sys

sys.setrecursionlimit(1500)


def gcdEx(a, b):
    if a == 0:
        return b, 0, 1
    prev_r = a
    r = b
    x0, x1, y0, y1 = 1, 0, 0, 1
    while r > 0:
        new_r = prev_r % r
        x = x0 - (prev_r // r) * x1
        y = y0 - (prev_r // r) * y1
        x0 = x1
        x1 = x
        y0 = y1
        y1 = y
        prev_r = r
        r = new_r
    return prev_r, x0, y0


def lcm(a, b):
    multiplier = abs(a * b) // gcdEx(a, b)[0]
    return multiplier


def RSAkeygen(bits):
    while True:
        p = largeprimegen(bits)
        q = largeprimegen(bits)
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


def RSAencrypt(m, e, n):
    c = pow(m, e, n)
    return c


def RSAdecrypt(c, d, n):
    m = pow(c, d, n)
    return m


key = RSAkeygen(1024)
encrypted = RSAencrypt(1550, key[0], key[1])
decrypted = RSAdecrypt(encrypted, key[2], key[1])

print(decrypted)
