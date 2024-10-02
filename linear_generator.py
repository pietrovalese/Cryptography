import random
MODULUS=2**32
# Linear Congruential Generator (LCG)
def linear_generator(n):
    # Generate random parameters if not provided
    a = random.randint(1, MODULUS - 1)
    b = random.randint(0, MODULUS - 1)
    seed = random.randint(0, MODULUS - 1)
    seq = []
    seq.append(seed)
    for i in range(1, n):
        # LCG recurrence relation: X_{n+1} = (a * X_n + b) % MODULUS
        next_value = (a * seq[i - 1] + b) % MODULUS
        seq.append(next_value)
    return seq

if __name__ == "__main__":
    # Generate a sequence of 15 numbers
    result = linear_generator(15)
    print(result)
