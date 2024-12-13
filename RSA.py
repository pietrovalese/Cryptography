import random 
import Test_Miller_Rabin
import sys

def gen_key():
    p,q=gen_pq_RSA()
    n=p*q
    phi=(p-1)*(q-1)
    e=gen_e_parameter(phi)
    d=pow(e,-1,phi)
    return [[n,e],[d]]
    
def gen_pq_RSA():
    i=0
    j=0
    while not Test_Miller_Rabin.test_MR(i, 20):
        i=random.randint(10**50,10**60)
    p=i
    while not Test_Miller_Rabin.test_MR(j, 20):
        j=random.randint(10**50,10**60)
    q=j
    return p,q

def gen_e_parameter(phi):
    e=0
    while Test_Miller_Rabin.MCD(e, phi)!=1:
        e=random.randint(1,phi-1)
    return e

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Please choose one number to check")
        sys.exit()
    m = int(sys.argv[1]) #Value to check
    keys=gen_key()
    public_key=keys[0]
    private_key=keys[1]
    print(f"Chiave pubblica: {public_key}\nChiave privata: {private_key}")
    crittogramma=pow(m,public_key[1],public_key[0])
    print(f"Crittogramma finale: {crittogramma}")
    messaggio=pow(crittogramma,private_key[0],public_key[0])
    print(f"Messaggio finale: {messaggio}")
    