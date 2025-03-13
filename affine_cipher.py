import sys
import random
from Test_Miller_Rabin import MCD

ALFABETH=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def gen_key():
    n1=random.randint(0,26)
    n2=random.randint(0,25)
    lis=[]
    while(MCD(n1,26)!=1):
        n1=random.randint(0,26)
    lis.append(n1)
    lis.append(n2)
    return lis

def affine_chiper(m,k):
    lis=[]
    for i in range(0, len(m)):
        index=((k[0]*i)+k[1])%26
        lis.append(ALFABETH[index])
    return lis

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Please choose one number to secure")
        sys.exit()
    s = sys.argv[1] #Value to check
    k=gen_key()
    res="".join(affine_chiper(s,k))
    print(f"The initial message was: {s}\nThe key generated is: {k}\nThe final result is: {res}")