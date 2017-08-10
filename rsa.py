import random
import math

# generate prime numbers up to a given number so that encryption is random
# within given list of primes


def prime(value):
    p = []
    c = []
    for i in range(2, value+1):
        if i not in c:
            p.append(i)
            for j in range(i*i, value+1, i):
                c.append(j)
    return p  # contains list of prime numbers within given "value"


""" 
in case any of the variable:
data ^ integer % public_key
encrypted ^ private_key % public_key
result in OVERFLOW which is handled by large_mod
a * b % c = ((a % c) * (b % c)) % c
"""


def large_mod(ev, mval, pval):
    res = 1
    for i in range(mval):
        res = res * ev % pval  # associativity of '%', '/', '*' is left to right
    res %= pval
    return res


# generating private and public keys
# self-explanatory variables


def key_gen(value, data):
    prime_list = prime(value)
    # randomly select two prime numbers from list of prime_list
    # key generation
    p1 = random.randint(0, int((len(prime_list)-1)/2))
    p2 = random.randint(int((len(prime_list)+1)/2), len(prime_list)-1)
    print(prime_list, prime_list[p1], prime_list[p2], sep='\n')
    public_key = prime_list[p1]*prime_list[p2]
    q = (prime_list[p1]-1)*(prime_list[p2]-1)
    print("q =", q)
    integer = 1

    # co-prime number of {x, q}
    for i in range(2, q):
        if math.gcd(i, q) != 1:
            continue
        integer = i
        break
    print("PUBLIC KEY:", public_key, "INTEGER:", integer, end='\n')
    k = random.randint(0, len(prime_list)-1)
    while k == p1 or k == p2:
        k = random.randint(0, len(prime_list) - 1)
    k = prime_list[k]
    print("Random Number =", k)
    private_key = ((k*q)+1)//integer  # floor division
    print("PRIVATE KEY:", private_key, "INTEGER:", integer, end='\n')

    # data encryption and decryption
    encrypted = large_mod(data, integer, public_key)
    print("ENCRYPTED DATA: ", encrypted, end='\n')
    decrypted = large_mod(encrypted, private_key, public_key)
    print("DECRYPTED DATA: ", decrypted, end='\n')


# main function definition and calling


def main():
    val, d = [int(i) for i in input("Enter a number and data \n").split()]
    key_gen(val, d)


if __name__ == '__main__':
    main()
