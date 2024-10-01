import sys
import random

if len(sys.argv) != 2:
    print("Please choice one number to check")
    sys.exit()
    
def MCD(a,b):
    while b != 0:
        r=a%b #resto
        a=b
        b=r
        print(f"a,b: {a,b}")
    return a

def gen_zw(N):
    numero = N - 1
    # Inizializza w e z
    w = 0
    z = numero
    # Dividi per 2 finché è divisibile per 2 (estraendo tutte le potenze di 2)
    while z % 2 == 0:
        z //= 2
        w += 1
    # A questo punto z sarà dispari
    return z, w
    

def verifica(N,y,z,w):
    i=random.randint(0, w)
    print(f"i: {i}")
    if(MCD(N,y) != 1 and (((y^z)%N)==1 or ((y^(z*2^i))%N)==-1)): 
        return True
    else:
        return False

def test_MR(N,k):
    z,w= gen_zw(N)
    print(f"z,w: {z,w}")
    for i in range(0,k):
        y=random.randint(2, N-2)
        print(f"y:{y}")
        if verifica(N,y,z,w) == True:
            return False
    return True


if __name__== "__main__":
    n=int(sys.argv[1])
    result=test_MR(n, 10) #probabilità di errore pari a 1/4^10 = 1/2^20 = 1/10^6
    if result == True:
        print(f"Il numero {n} è primo")
    else:
        print(f"Il numero {n} è composto")
    
    