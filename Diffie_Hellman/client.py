import socket
import threading
import random
import hashlib
import base64
from cryptography.fernet import Fernet

# Configurazione del client
HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Ricezione di p, g, A
data = client_socket.recv(1024)
p, g, A = map(int, data.decode().split(','))
print(f"Ricevuti dal server -> p: {p}, g: {g}, A: {A}")

# PROTOCOLLO Diffie-Hellman
y = random.randint(2, p - 2)
B = pow(g, y, p)
client_socket.sendall(str(B).encode())
print(f"Inviata chiave pubblica: {B}")

# Calcolo della chiave condivisa
shared_key = pow(A, y, p)
print(f"Chiave condivisa calcolata: {shared_key}")

# Creazione della chiave Fernet
hashed_key = hashlib.sha256(str(shared_key).encode()).digest()  # Calcola l'hash (32 byte)
fernet_key = base64.urlsafe_b64encode(hashed_key)  # Codifica in base64 (compatibile con Fernet)
cipher = Fernet(fernet_key)

# Funzione per ricevere messaggi cifrati
def ricevi_messaggi():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("Connessione chiusa dal server.")
                break
            messaggio = cipher.decrypt(data).decode()
            print(f"Server: {messaggio}")
        except Exception as e:
            print(f"Errore nella ricezione: {e}")
            break

# Funzione per inviare messaggi cifrati
def invia_messaggi():
    while True:
        messaggio = input("Tu: ")
        try:
            client_socket.sendall(cipher.encrypt(messaggio.encode()))
        except Exception as e:
            print(f"Errore nell'invio: {e}")
            break

# Thread per invio e ricezione
threading.Thread(target=ricevi_messaggi, daemon=True).start()
threading.Thread(target=invia_messaggi, daemon=True).start()

# Mantiene il programma attivo
while True:
    pass
