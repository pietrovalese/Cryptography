import sys
import random

ALFABETH = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def complete_chiper(s, k):
    lis = []
    for i in range(0, len(s)):
        for j in range(0, len(ALFABETH)):
            if s[i] == ALFABETH[j]:
                lis.append(k[j])
    return "".join(lis)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please choose one phrase to secure")
        sys.exit()

    s = sys.argv[1]  # Valore da cifrare
    k = ALFABETH[:]  # Crea una copia di ALFABETH
    random.shuffle(k)  # Mescola la copia

    res = complete_chiper(s, k)
    print(f"The initial message was: {s}")
    print(f"The key generated is: {k}")
    print(f"The final result is: {res}")
    