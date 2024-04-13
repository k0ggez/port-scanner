from random import randint


def is_prime(candidate):
    if candidate % 2 == 0 or candidate % 3 == 0 or candidate % 5 == 0:  # easy check
        return False

    for i in range(7, int(candidate**.5)+1, 2):  # brute force, skipping odd numbers up to root of number
        if i % 5 == 0:  # skips the fives
            i += 2
        if candidate % i == 0:
            return False

    return True


def is_coprime(a, b):
    if a % 2 == 0 and b % 2 == 0:  # get evens out of the way
        return False
    for i in range(3, int(max(a, b)**.5), 2):  # up to the largest root, check if they have a common divisor
        if a % i == 0 and b % i == 0:
            return False
    return True


def gen_prime():
    while True:
        prime = randint(1, 999_999)  # pick a number under 1,000,000 until you get a prime
        if is_prime(prime):
            break
    return prime


def gen_public(phin_n):
    while True:
        e = randint(2, phin_n - 1)  # generate some e where 1 < e < phi_n
        if is_coprime(e, phin_n):  # check that e and phi_n have no common factors
            break
    return e


def gen_private(phi_n, e):
    # This gave me a lot of grief. I initially computed it using (e**-1)%phi_n as per numerous online sources and
    # piazza posts, but this would give me very small numbers that wouldn't work. Only when I resorted to trying
    # literally everything did I use the built-in pow(base, exp, mod) using the same exact numbers would this give me
    # a key greater than -1. I'm guessing it has something to do with the compiler rounding or losing precision
    # inbetween operations or something. Idk I would've had this turned in on time if I was lazier and used built-in
    # functions rather than math it by hand.
    # d = (e**-1)%phi_n
    d = pow(e, -1, phi_n)
    return d


def crypt(M, key, n):  # function is the same for encrypt and decrypt, reduce reuse recycle
    return pow(M, key, n)


def main():
    p, q = gen_prime(), gen_prime()
    if p == q:
        print("wow that was unlikely, you should buy a lottery ticket")
        exit()
    print("p =", p, "\nq =", q)

    phi_n = (p - 1) * (q - 1)
    e = gen_public(phi_n)
    print("e =", e)

    d = gen_private(phi_n, e)
    print("d =", d)

    M = input("input message > ")
    C = crypt(int(M), e, (p * q))
    print("encrypted message: ", C)
    print("decrypted message: ", crypt(C, d, (p * q)))


main()


