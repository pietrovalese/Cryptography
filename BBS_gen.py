from Test_Miller_Rabin import test_MR
from Test_Miller_Rabin import MCD
import random

# Function to generate two large primes p and q, where p ≡ 3 (mod 4) and q ≡ 3 (mod 4)
def gen_pq():
    p=random.randint(100000, 1000000000)
    q=random.randint(100000, 1000000000)
    n1=2*(p//4)+1
    n2=2*(q//4)+1
    while test_MR(n1,10) == False or test_MR(n2,10) == False:
        # Randomly generate large odd numbers
        p = random.randint(100000, 1000000000)
        if p % 2 == 0:
            p += 1
        # Ensure p ≡ 3 (mod 4) and that p is prime
        while not (p % 4 == 3 and test_MR(p, 10)):
            p += 2
        
        q = random.randint(100000, 1000000000)
        if q % 2 == 0:
            q += 1
        # Ensure q ≡ 3 (mod 4) and that q is prime
        while not (q % 4 == 3 and test_MR(q, 10)):
            q += 2
            
        n1=2*(p//4)+1
        n2=2*(q//4)+1
        # Return the product of the two primes
    print(p,q)
    return p * q

# Function to generate a Blum Blum Shub pseudorandom sequence of length n
def BBS(n):
    # Generate Blum integer (product of two primes p and q, where p ≡ 3 (mod 4) and q ≡ 3 (mod 4))
    num = gen_pq()
    # Choose a random seed y such that GCD(y, num) == 1
    y = random.randint(100000, 1000000000)
    while MCD(y, num) != 1:
        y += 1
    print(y)
    # Initialize the BBS sequence
    x = (y ** 2) % num
    sequence = [x]
    
    # Generate the sequence of n numbers
    for i in range(1, n):
        x = (sequence[i - 1] ** 2) % num
        sequence.append(x)
    
    return sequence

if __name__ == "__main__":
    # Generate a Blum Blum Shub sequence of length 15
    result = BBS(15)
    print(result)
