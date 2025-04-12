"""
2. Skapa ett program där vi kan söka efter en textsträng i en lista med strängar. Effektivisera 
programmet så det inte är känsligt för stora eller små bokstäver.
"""


def bubble_sort(list):  #metod
    n = len(list) #antal karaktärer i listan
    for i in range(n): #for-loop
        for j in range(0, n - i - 1): #for-loop 
            if list[j] > list[j + 1]: # om j är mindre än nästa i listan
                list[j], list[j + 1] = list[j + 1], list[j] #byt platts på dem

def binary_search(inmat, list): #metod för binär sökning
    bubble_sort(list) #sortera list
    vänster = 0 #för att tillägga
    höger = len(list) - 1 #antal i list
    while vänster <= höger: #medan vänster är mindre eller lika med höger
        mitten = (vänster + höger) // 2 #räkna mitten
        if list[mitten] == inmat: #om mitten är lika med tal
            return True #hittad
        elif list[mitten] < inmat: #om tal är större än mitten
            vänster = mitten + 1 #ta bort vänster sida av mitten
        else: #annars
            höger = mitten - 1 #ta bort höger sida av mitten
    return False #inte hittad


list = ['B', 'c', 'A', 'a', 'b', 'C'] # klar lista

while True: #evighets loop
    try: #testa
        print("Vad vilket tal letar du efter?") #fråga
        inmat = str(input("Svar: ")) #konvert svar till int
        break #stopp loop
    except ValueError: #inte kan konvert
        print("Ogiltig inmatning, försök igen. ") #försök igen
        
if binary_search(inmat, list) == True: #om hittad
    print("Bokstaven finns i listan. ") #fins i talmängd
else: #annars
    print("Bokstaven finns inte med i listan. ") #inte hittad