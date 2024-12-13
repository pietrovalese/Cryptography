# Cryptography Repository

In this repository, I aim to recreate a variety of cryptographic algorithms to build an application that is cryptographically secure. This repository is organized into the following components:

## Contents

### Random Sequence Generators
- **`BBS_gen.py`**: Implements the Blum-Blum-Shub (BBS) generator for cryptographically secure random sequences.
- **`linear_generator.py`**: Implements a linear congruential generator (LCG) for random sequence generation.

### Prime Number Checking Functions
- **`Test_Miller_Rabin.py`**: Implements the Miller-Rabin primality test to verify whether a given number is prime.

### Ciphers
- **`Caesar_chiper.py`**: Implements the Caesar cipher for basic substitution encryption.
- **`affine_chiper.py`**: Implements the Affine cipher, a type of substitution cipher.
- **`complete_chiper.py`**: A comprehensive implementation combining various cipher techniques.

### Analysis Tools
- **Q-gram Analysis**: This folder contains scripts for performing q-gram analysis, a method used in text analysis and cryptanalysis.

### RSA
- **RSA Implementation**: This folder contains scripts for generating RSA keys and performing RSA encryption and decryption.

## Dependencies
Some scripts depend on others in this repository. Be sure to check the script dependencies before execution.

## Usage
1. Clone the repository.
2. Install necessary Python dependencies (if any).
3. Navigate to the desired script and execute it to test or use its functionality.

```bash
# Example of cloning the repository
git clone https://github.com/your_username/cryptography.git
cd cryptography

# Example of running a script
python3 BBS_gen.py
```

## Contributions
Feel free to contribute by adding new cryptographic algorithms, improving existing implementations, or enhancing the documentation. Open an issue or submit a pull request for any suggestions or additions.
