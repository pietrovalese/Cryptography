import sys
import os

def q_gram_dictionary(file_to_read, file_to_write, k):
    """Genera un file contenente i q-gram per le parole di un dizionario."""
    dictionary = []
    # Lettura e creazione del dizionario
    with open(file_to_read, "r") as file:
        for riga in file:
            riga = riga.strip()
            qgrams = generate_qgrams(riga, k)
            dictionary.append(qgrams)

    # Scrittura su file
    with open(file_to_write, "w") as file:
        for qgrams in dictionary:
            file.write(" ".join(qgrams) + "\n")

def generate_qgrams(riga, k):
    """Genera i q-gram di lunghezza k per una riga."""
    riga = [c for c in riga if c != ' ']  # Rimuovi spazi
    if len(riga) < k:  # Controlla se la riga è troppo corta
        return []  # Restituisci una lista vuota
    return ["".join(riga[i:i + k]) for i in range(len(riga) - k + 1)]

def generate_and_check(phrase, file_to_read, q_gram_file, k):
    """Confronta i q-gram di una frase con un dizionario di q-gram."""
    phrase_qgrams = generate_qgrams(phrase, k)  # Genera i q-gram della frase
    risultati = []
    max_somiglianza = 0  # Variabile per tracciare la massima somiglianza

    # Verifica se la frase è già nel dizionario
    with open(file_to_read, "r") as file:
        if phrase in (riga.strip() for riga in file):
            print(f"La parola '{phrase}' è già presente nel dizionario.")
            return [(phrase, 0)]  # Nessun calcolo necessario

    # Confronta i q-gram della frase con quelli del dizionario
    with open(q_gram_file, "r") as file:
        dizionario = [line.strip().split() for line in file]
        for riga in dizionario:
            somiglianza = len(set(phrase_qgrams) & set(riga))  # Intersezione
            if somiglianza > 0:
                risultati.append((" ".join(riga), somiglianza))
                # Aggiorna la massima somiglianza
                if somiglianza > max_somiglianza:
                    max_somiglianza = somiglianza

    # Stampa della massima somiglianza
    print(f"{k}-gram della frase '{phrase}': {phrase_qgrams} con la massima somiglianza: {max_somiglianza}")
    
    return risultati

def ricostruisci_da_qgram(qgrams):
    """Ricostruisce una parola dai q-gram eliminando duplicati consecutivi."""
    # Inizializza la parola ricostruita con il primo q-gram
    ricostruita = qgrams[0]
    
    # Inizia dal secondo q-gram, perché il primo è già incluso
    for qgram in qgrams[1:]:
        # Aggiungi alla parola ricostruita solo l'ultimo carattere del q-gram, per evitare duplicati
        ricostruita += qgram[-1]  # Aggiunge solo l'ultimo carattere del q-gram

    return ricostruita

def confidence_score(common_qgrams, total_qgrams):
    """Calcola il punteggio di confidenza basato sui q-gram in comune."""
    return common_qgrams / total_qgrams

def calculate_confidence(risultati, phrase, k):
    """Calcola il punteggio di confidenza per ogni risultato."""
    phrase_qgrams = generate_qgrams(phrase, k)
    total_qgrams = len(phrase_qgrams)
    return [(word, confidence_score(similarity, total_qgrams)) for word, similarity in risultati]

def create_dictionary(phrase):
    """Crea un dizionario ristretto basato sulla lunghezza della parola."""
    k = 1 if len(phrase) <= 5 else 2
    word_length = len(phrase)
    matching_words = []

    with open("dizionario_completo.txt", "r") as infile:
        for line in infile:
            word = line.strip()
            if word_length - k <= len(word) <= word_length + k:
                matching_words.append(word)

    with open("dizionario.txt", "w") as outfile:
        for word in matching_words:
            outfile.write(word + "\n")

def trova_migliore_confidenza(all_confidences):
    """Trova la parola con il punteggio di confidenza più alto."""
    return max(all_confidences, key=lambda x: x[1], default=None)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Per favore, inserisci una frase da verificare.")
        sys.exit()

    phrase = sys.argv[1].strip()  # Frase da controllare

    # Creazione del dizionario ristretto
    if len(phrase) > 2:
        create_dictionary(phrase)

    # Generazione dei file q-gram se non esistono
    if not all(os.path.exists(f"q_gram_{k}dictionary.txt") for k in range(2, len(phrase))):
        for k in range(2, len(phrase)):
            q_gram_dictionary("dizionario.txt", f"q_gram_{k}dictionary.txt", k)

    # Genera e verifica q-gram
    tutti_risultati = []
    for k in range(2, len(phrase)):
        risultati = generate_and_check(phrase, "dizionario.txt", f"q_gram_{k}dictionary.txt", k)
        tutti_risultati.extend(calculate_confidence(risultati, phrase, k))

    # Trova il miglior risultato
    best_match = trova_migliore_confidenza(tutti_risultati)
    if best_match:
        parola_ricostruita = ricostruisci_da_qgram(best_match[0].split())
        print(f"La parola più probabile è '{parola_ricostruita}' con una confidenza di {round(best_match[1] * 100, 2)}%.")
    else:
        print("Nessuna corrispondenza trovata.")

    # Pulizia dei file temporanei
    for k in range(2, len(phrase)):
        os.remove(f"q_gram_{k}dictionary.txt")
    if os.path.exists("dizionario.txt"):
        os.remove("dizionario.txt")

    print("File temporanei eliminati.")
