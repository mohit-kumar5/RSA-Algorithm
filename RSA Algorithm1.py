# program for generating keys (p,q,N,ϕ(n),e and d)


import random

# generating Random PrimeNumber's

def GenerateRandomPrimeNumbers():
    while 1:
        d=0
        PrimeNumber = random.randint(32769, 65535)  # values should be of 16 bit
        for i in range(1, PrimeNumber):
            if PrimeNumber % i == 0:
                d=d + 1
        if d==1:
            return PrimeNumber


p = GenerateRandomPrimeNumbers()
print("\n 16-bit Prime Number (p): ", p)
q = GenerateRandomPrimeNumbers()
print("\n 16-bit Prime Number (q): ", q)

# calculating the value N by multiplying the two prime numbers(p & q) generated above
N = p * q
print("\n N = p*q =", N)

# calculating ϕ(n)
PHI_N = (p - 1) * (q - 1)
print("\n ϕ(n) = (p-1)*(q-1) =", PHI_N)


# picking a random value for "e" based on ϕ(n) by making sure that GCD(e,ϕ(n))==1
def GeneratingRandomValueofe(PHI_N):
    while (1):
        UPHI_N = round(PHI_N / 2)
        e = random.randint(3, UPHI_N)  # random function in python
        e = (e * 2) + 1
        if (e % 2 == 1 and e < PHI_N):
            x = PHI_N
            y = e
            while (y):
                x, y = y, x % y
                if (y == 1):
                    return e


e = GeneratingRandomValueofe(PHI_N)
print("\n value of ϕ(n) is:", PHI_N)
print(" value of e is:", e)


# calculating the secret key "d", such that (e*d) mod Phi(N)=1
def GeneratingModInverse(e, PHI_N):
    s = 0
    o_s = 1
    t = 1
    o_t = 0
    r = e
    o_r = PHI_N
    while r != 0:
        q = o_r // r
        o_r, r = r, o_r - (q * r)
        o_s, s = s, o_s - (q * s)
        o_t, t = t, o_t - (q * t)
    if o_t < 0:
        o_t += PHI_N
    print('\n gcd of e and ϕ(n)', o_r)
    print(' d=', o_t)
    return o_t


d = GeneratingModInverse(e, PHI_N)
print("\n d = e(inverse) mod ϕ(n): =", d)
