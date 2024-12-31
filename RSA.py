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
        i=random.randint(10**90,10**100)
    p=i
    while not Test_Miller_Rabin.test_MR(j, 20):
        j=random.randint(10**90,10**100)
    q=j
    return p,q

def gen_e_parameter(phi):
    e=0
    while Test_Miller_Rabin.MCD(e, phi)!=1:
        e=random.randint(1,phi-1)
    return e

def int_to_string(n):
    # Converte l'intero in una stringa binaria
    bin_str = bin(n)[2:]  # Rimuove il prefisso '0b'
    
    # Aggiunge zeri all'inizio per far sì che la lunghezza sia un multiplo di 8
    # in modo da rappresentare correttamente i caratteri ASCII
    bin_str = bin_str.zfill((len(bin_str) + 7) // 8 * 8)
    
    # Divide la stringa binaria in blocchi di 8 bit e li converte in caratteri
    chars = [chr(int(bin_str[i:i+8], 2)) for i in range(0, len(bin_str), 8)]
    
    # Ritorna la stringa ricostruita
    return ''.join(chars)

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Please choose one number to check")
        sys.exit()
    try:
        m = int(sys.argv[1])  # Tenta di convertire direttamente in intero
    except ValueError:
    # Se non è un numero, convertilo in ASCII e poi in intero
        m = int(''.join(f'{ord(c):08b}' for c in sys.argv[1]), 2)
    keys=gen_key()
    public_key=keys[0]
    private_key=keys[1]
    print(f"Chiave pubblica: {public_key}\nChiave privata: {private_key}")
    crittogramma=pow(m,public_key[1],public_key[0])
    print(f"Crittogramma finale: {crittogramma}")
    messaggio=pow(crittogramma,private_key[0],public_key[0])
    print(f"Messaggio finale: {messaggio}")
    if isinstance(sys.argv[1], str):
        print(f"Mesaggio riconvertito: {int_to_string(messaggio)}")
    
    