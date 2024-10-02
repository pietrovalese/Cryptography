import sys
import random

# Function to calculate GCD (Euclid's algorithm)
def MCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute z and w for N-1 = z * 2^w
def gen_zw(N):
    numero = N - 1
    w = 0
    z = numero
    while z % 2 == 0:
        z //= 2
        w += 1
    return z, w

# Miller-Rabin primality test verification step
def verifica(N, y, z, w):
    # Compute y^z % N
    x = pow(y, z, N)
    
    if x == 1 or x == N - 1:
        return True
    
    # Square x w times, looking for a non-trivial square root of 1
    for i in range(w - 1):
        x = pow(x, 2, N)
        if x == N - 1:
            return True
        if x == 1:
            return False
    
    return False

# Main Miller-Rabin primality test function
def test_MR(N, k):
    if N < 2:
        return False
    if N == 2 or N == 3:
        return True
    if N % 2 == 0:
        return False
    
    z, w = gen_zw(N)
    for _ in range(k):
        y = random.randint(2, N - 2)
        if MCD(N, y) != 1 or not verifica(N, y, z, w):
            return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please choose one number to check")
        sys.exit()

    n = int(sys.argv[1])
    
    if n % 2 == 0:
        print(f"Il numero {n} è composto")
        sys.exit(1)

    result = test_MR(n, 20)  # Probability of error is 1/4^20 = 1/2^40 ≈ 1/10^12
    if result:
        print(f"Il numero {n} è primo")
    else:
        print(f"Il numero {n} è composto")
