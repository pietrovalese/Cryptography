import sys

# Dizionario delle lettere con la loro frequenza in italiano
frequenze = {
    'e': 11.79,
    'a': 11.74,
    'i': 11.28,
    'o': 9.83,
    'n': 6.88,
    'l': 6.51,
    'r': 6.38,
    't': 5.63,
    's': 4.98,
    'c': 4.50,
    'd': 3.73,
    'p': 3.05,
    'u': 3.02,
    'm': 2.52,
    'v': 2.10,
    'g': 1.65,
    'h': 1.54,
    'f': 0.95,
    'b': 0.92,
    'q': 0.51,
    'z': 0.49
}

def convert_to_percentage(freq_mess):
    # Somma di tutti i valori nel dizionario
    total = sum(freq_mess.values())
    
    # Creazione di un nuovo dizionario con i valori convertiti in percentuale
    if total > 0:
        freq_percentage = {letter: round((value / total) * 100, 2) for letter, value in freq_mess.items()}
    else:
        freq_percentage = {letter: 0 for letter in freq_mess.keys()}  # Se la somma è zero, tutte le percentuali sono zero

    return freq_percentage

def message_frequency(m):
    # Dizionario per memorizzare la frequenza delle lettere nel messaggio
    freq_mess = {letter: 0 for letter in frequenze.keys()}  # Inizializzo tutte le lettere a 0
    
    # Calcolo della frequenza delle lettere nel messaggio
    for char in m:
        if char in freq_mess:
            freq_mess[char] += 1
    
    percented_freq = convert_to_percentage(freq_mess)
    # Ordinamento del dizionario in base ai valori (frequenze)
    sorted_freq_mess = sorted(percented_freq.items(), key=lambda item: item[1], reverse=True)

    return sorted_freq_mess
    
def frequency_attack(freq_sorted, m):
    res=[]
    # Ottieni le lettere ordinate dalle più frequenti alle meno frequenti nel dizionario di riferimento
    reference_sorted = sorted(frequenze.items(), key=lambda item: item[1], reverse=True)
    
    for r in range(0, 26):
    # Mappa di sostituzione tra la lettera del messaggio e la lettera più frequente secondo il dizionario
        substitution_map = {freq_sorted[i][0]: reference_sorted[i][0] for i in range(0,len(freq_sorted))}
        # Decodifica il messaggio usando la mappa di sostituzione
        decoded_message = ""
        for char in m:
            if char in substitution_map:
                decoded_message += substitution_map[char]
            else:
                decoded_message += char  # Lascia i caratteri non riconosciuti come sono
        
        res.append(decoded_message)
    return res

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a single message to analyze.")
        sys.exit()

    m = sys.argv[1]  # Messaggio da analizzare
    dict_sorted = message_frequency(m)
    
    print("Frequenze delle lettere nel messaggio ordinato:")
    for letter, freq in dict_sorted:
        print(f"{letter}: {freq}%")

    # Attacco alle frequenze
    res = frequency_attack(dict_sorted, m)
    print("Messaggio decodificato con attacco alle frequenze:")
    print(res)
