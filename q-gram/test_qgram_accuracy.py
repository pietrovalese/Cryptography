import os
import q_gram
import time

def generate_phrase(line):
    return line.split()

def routine(phrase):
    parola_ricostruita = phrase.strip()  # Default: la parola originale
    best = 0

    if len(phrase) > 2:
        q_gram.create_dictionary(phrase)
    else:
        with open("frasi_corrette.txt", "a") as file2:
            file2.write(parola_ricostruita + " " + "\n")
            return

    if not all(os.path.exists(f"q_gram_{k}dictionary.txt") for k in range(2, len(phrase))):
        for k in range(2, len(phrase)):
            q_gram.q_gram_dictionary("dizionario.txt", f"q_gram_{k}dictionary.txt", k)

    tutti_risultati = []
    for k in range(2, len(phrase)):
        risultati = q_gram.generate_and_check(phrase, "dizionario.txt", f"q_gram_{k}dictionary.txt", k)
        if risultati:
            tutti_risultati.extend(q_gram.calculate_confidence(risultati, phrase, k))

    best_match = q_gram.trova_migliore_confidenza(tutti_risultati)
    if best_match:
        parola_ricostruita = q_gram.ricostruisci_da_qgram(best_match[0].split())
        best = best_match[1] * 100
        print(f"La parola più probabile è '{parola_ricostruita}' con una confidenza di {round(best, 2)}%.")

    with open("frasi_corrette.txt", "a") as file:
        file.write(parola_ricostruita + " " + "\n")

    for k in range(2, len(phrase)):
        os.remove(f"q_gram_{k}dictionary.txt")
    if os.path.exists("dizionario.txt"):
        os.remove("dizionario.txt")

    print("File temporanei eliminati.")

if __name__ == "__main__":
    print("ciao")
    with open("frasi.txt", "r") as file:
        lines = [line.strip() for line in file]
        print(lines)
        for line in lines:
            words = generate_phrase(line)
            print(f"words: {words}")
            time.sleep(2)
            for word in words:
                routine(word)
