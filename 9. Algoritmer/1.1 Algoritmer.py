"""
1. Skapa ett program som bubbelsorterar en talföljd. Låt användaren skriva in talen, för att sedan sorteras när användaren är
klar med inmatningen.
"""

def bubble_sort(inmat): #Funktion för bubbel sortering i lista
    n = len(inmat) #deklaration
    for i in range(n - 1): # Loop för att gå igenom alla element i listan
        for j in range(0, n - i - 1):# Loop för att jämföra och byta element
            # Jämför två intilliggande element och byt plats om de är i fel ordning
            if inmat[j] > inmat[j + 1]:
                inmat[j], inmat[j + 1] = inmat[j + 1], inmat[j]

list = [] #tom lista
while True: #evighetsloop
    num = input("Ange ett tal (Avsluta koden genom att skriva 'slut'):") #deklaration
    if num.lower() == 'slut': #if "Slut"
        break #stopp loop
    try: #kolla om nummer
        num = int(num) #kovert till int
        list.append(num) #tillägg i list
    except ValueError: #om valueerror
        print("Felaktig inmatning, försök igen") #utskriv

    bubble_sort(list) #sortera lista
print("Sorterade lista:", list) #utskriv resultat