import random


def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)
    return prime_list


prime_list = primesInRange(1, 350)
randomPrime = random.choice(prime_list)

# print("Generated random prime number: ", randomPrime)
# print("Generated random prime list: ", prime_list)
