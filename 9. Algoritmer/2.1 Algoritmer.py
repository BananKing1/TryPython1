"""
Binär sökning:
1. Skapa ett program där vi kan binärsöka efter ett tal i en talmängd. Programmet behöver bara 
berätta ifall talet finns i talmängden.
"""

list = [3, 2, 5, 1, 4, 6, 7, 10, 8, 9] #klar lista


def binary_search(tal, list): #metod för binär sökning
    list.sort() #sortera lista
    vänster = 0 #för att tillägga
    höger = len(list) - 1 #antal i list
    while vänster <= höger: #medan vänster är mindre eller lika med höger
        mitten = (vänster + höger) // 2 #räkna mitten
        if list[mitten] == tal: #om mitten är lika med tal
            return True #hittad
        elif list[mitten] < tal: #om tal är större än mitten
            vänster = mitten + 1 #ta bort vänster sida av mitten
        else: #annars
            höger = mitten - 1 #ta bort höger sida av mitten
    return False #inte hittad


while True: #evighets loop
    try: #testa
        print("Vad vilket tal letar du efter?") #fråga
        tal = int(input("Svar: ")) #konvert svar till int
        break #stopp loop
    except ValueError: #inte kan konvert
        print("Ogiltig inmatning, försök igen. ") #mata igen
        

if binary_search(tal,list) == True: #om hittad
    print("Talet finns i talmängden. ") #fins i talmängd
else: #annars
    print("Talet finns inte med i talmängden. ") #inte hittad