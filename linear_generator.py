import random

# Linear Congruential Generator (LCG)
def linear_generator(n, modulus=2**32, a=None, b=None, seed=None):
    # Generate random parameters if not provided
    if a is None:
        a = random.randint(1, modulus - 1)
    if b is None:
        b = random.randint(0, modulus - 1)
    if seed is None:
        seed = random.randint(0, modulus - 1)

    seq = []
    seq.append(seed)
    
    for i in range(1, n):
        # LCG recurrence relation: X_{n+1} = (a * X_n + b) % modulus
        next_value = (a * seq[i - 1] + b) % modulus
        seq.append(next_value)
    
    return seq

if __name__ == "__main__":
    # Generate a sequence of 15 numbers
    result = linear_generator(15)
    print(result)
