import random
from smallprimegen import primesInRange

low_primes = primesInRange(2, 350)


def nBitRN(n):
    while True:
        r = random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)
        if r % 2 == 0:
            continue
        else:
            break
    return r


def lowTested(n):
    while True:
        candidate = nBitRN(n)
        for g in low_primes:
            if candidate % g == 0 and g != candidate:
                break
            else:
                return candidate


def MillerRabinTested(mrc):
    maxdivby2 = 0
    evenc = mrc - 1
    while evenc % 2 == 0:
        evenc >>= 1
        maxdivby2 += 1
    assert 2 ** maxdivby2 * evenc == mrc - 1

    def isComposite(a):
        if pow(a, evenc, mrc) == 1:
            return False
        for i in range(maxdivby2):
            if pow(a, 2 ** i * evenc, mrc) == mrc - 1:
                return False
        return True

    numberoftrials = 30
    for i in range(numberoftrials):
        a = random.randrange(2, mrc)
        if isComposite(a):
            return False
    return True


def largeprimegen(n):
    while True:
        largeprime = lowTested(n)
        if not MillerRabinTested(largeprime):
            continue
        else:
            return largeprime


# x = input("Input bit size of candidate: ")
# try:
#     x = int(x)
# except:
#     print("Input was not an integer.")
# target = largeprimegen(x)
# print("Generated prime: ", target)
