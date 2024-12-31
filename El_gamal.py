import random
import Test_Miller_Rabin
import sys

RANGE_START=10**5
RANGE_END=10**10

def gen_keys_EG(p, g, x):
    y = pow(g, x, p)
    keys = [[g, y, p], [x]]
    return keys

def gen_prime_EG():
    n = random.randint(RANGE_START, RANGE_END)
    check = Test_Miller_Rabin.test_MR(n, 20)
    while not check: 
        n = random.randint(RANGE_START, RANGE_END)
        check = Test_Miller_Rabin.test_MR(n, 20)
    return n

def create_generator(prime):
    phi = prime - 1
    factors = factorize(phi)  # Fattorizza φ = p-1
    for g in range(2, prime):
        if is_generator(g, prime, phi, factors):
            return g
    return None

def is_generator(g, prime, phi, factors):
    for factor in factors:
        if pow(g, phi // factor, prime) == 1:
            return False
    return True

def factorize(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please choose one number to check")
        sys.exit()
    m = int(sys.argv[1]) #Value to check
    p = gen_prime_EG()
    x = random.randint(2, p - 2)
    print(f"Prime: {p}")
    g = create_generator(p)
    if g is None:
        print("No generator found.")
    else:
        print(f"Generator: {g}")
        keys = gen_keys_EG(p, g, x)
        print(f"Chiave pubblica: {keys[0]}\nChiave privata: {keys[1]}\n")
    r=random.randint(2,p-2)
    y=pow(g,x,p)
    c1=pow(g,r,p)
    c2=(m*pow(y,r,p))%p
    critto=[c1,c2]
    m=(critto[1]*pow(critto[0],-x,p))%p
    print(f"Crittogrammi: {critto}\nMessaggio finale:{m}")
