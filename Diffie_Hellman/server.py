import socket
import threading
import hashlib
import base64
import sys
import os
import random
from cryptography.fernet import Fernet

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import El_gamal


# Configurazione del server
HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server in ascolto su {HOST}:{PORT}")
conn, addr = server_socket.accept()
print(f"Connessione accettata da {addr}")

# PROTOCOLLO Diffie-Hellman
p = El_gamal.gen_prime_EG()
g = El_gamal.create_generator(p)
x = random.randint(2, p - 2)
A = pow(g, x, p)

# Invio di p, g, A
conn.sendall(f"{p},{g},{A}".encode())

# Ricezione di B
data = conn.recv(1024)
B = int(data.decode())
print(f"Chiave pubblica ricevuta dal client: {B}")

# Calcolo della chiave condivisa
shared_key = pow(B, x, p)
print(f"Chiave condivisa calcolata: {shared_key}")

# Creazione della chiave Fernet
hashed_key = hashlib.sha256(str(shared_key).encode()).digest()  # Calcola l'hash (32 byte)
fernet_key = base64.urlsafe_b64encode(hashed_key)  # Codifica in base64 (compatibile con Fernet)
cipher = Fernet(fernet_key)

# Funzione per ricevere messaggi cifrati
def ricevi_messaggi():
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print("Connessione chiusa dal client.")
                break
            messaggio = cipher.decrypt(data).decode()
            print(f"Client: {messaggio}")
        except Exception as e:
            print(f"Errore nella ricezione: {e}")
            break

# Funzione per inviare messaggi cifrati
def invia_messaggi():
    while True:
        messaggio = input("Tu: ")
        try:
            conn.sendall(cipher.encrypt(messaggio.encode()))
        except Exception as e:
            print(f"Errore nell'invio: {e}")
            break

# Thread per invio e ricezione
threading.Thread(target=ricevi_messaggi, daemon=True).start()
threading.Thread(target=invia_messaggi, daemon=True).start()

# Mantiene il programma attivo
while True:
    pass
