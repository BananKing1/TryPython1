"""
2. 

Skapa ett program där användaren får välja i en meny om användaren vill räkna Addition, Subtraktion, 
Multiplikation eller Division. Användaren skall sedan få skriva in två tal och programmet skall sedan göra en 
uträkning med det valda räknesättet. 

Programmet skall även ta hand om de undantagsfall som kan ske. Om användaren tex skriver in bokstäver istället för 
siffror, skall ett felmeddelande ges och användaren skall få försöka igen.
"""

while True: #evighets loop + val
    print("[A] Addition")
    print("[S] Subtraktion")
    print("[M] Multiplikation")
    print("[D] Division")
    print("[ST] Stopp")
    svar = input("Välj ett räknesätt för uträkningen: ") #val av räknesätt

    if svar == 'A' or svar == 'a': #addition
        while True: #evighets loop
            try: #testa
                tal1 = int(input("Ange ett tal: ")) #konvert
                tal2 = int(input("Ange ett annat tal: ")) #konvert
                print(str(tal1), "+", str(tal2), "=", (tal1 + tal2)) #utskriv
                break #stopp

            except ValueError: #förutom
                print("Ogiltig inmatning, försök igen: ") #utskriv

    elif svar == 'S' or svar == 's': #subtraktion
        while True: #evighets loop
            try: #testa
                tal1 = int(input("Ange ett tal: ")) #konvert
                tal2 = int(input("Ange ett annat tal: ")) #konvert
                print(str(tal1), "-", str(tal2), "=", (tal1 - tal2)) #utskriv
                break #stopp

            except ValueError: #förutom
                print("Ogiltig inmatning försök igen: ") #utskriv 

    elif svar == 'M' or svar == 'm': #multiplikation
        while True: #evighets loop
            try: #testa
                tal1 = int(input("Ange ett tal: ")) #konvert
                tal2 = int(input("Ange ett annat tal: ")) #konvert
                print(str(tal1), "*", str(tal2), "=", (tal1 * tal2)) #utskriv
                break #stopp

            except ValueError: #förutom
                print("Ogiltig inmatning försök igen: ") #utskriv

    elif svar == 'D' or svar == 'd': #division
        while True: #evighets loop
            try: #testa
                tal1 = int(input("Ange ett tal: ")) #konvert
                tal2 = int(input("Ange ett annat tal: ")) #konvert
                print(str(tal1), "/", str(tal2), "=", (tal1 / tal2))
                break #stopp

            except (ValueError, ZeroDivisionError): #förutom
                print("Ogiltig inmatning försök igen: ") #utskriv

    elif svar == 'St' or svar == 'ST' or svar == 'sT' or svar == 'st': #stopp
        print("Programmet är avslutad. ") #utskriv
        break #stopp loop
    
    else: #annars
        print("Ogiltig inmatning, försök igen: ") #utskriv