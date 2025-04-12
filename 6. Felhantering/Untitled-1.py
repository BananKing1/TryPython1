"""
2. 

Skapa ett program där användaren får välja i en meny om användaren vill räkna Addition, Subtraktion, 
Multiplikation eller Division. Användaren skall sedan få skriva in två tal och programmet skall sedan göra en 
uträkning med det valda räknesättet. 

Programmet skall även ta hand om de undantagsfall som kan ske. Om användaren tex skriver in bokstäver istället för 
siffror, skall ett felmeddelande ges och användaren skall få försöka igen.
"""

while True:
    print("[A] Addition")
    print("[S] Subtraktion")
    print("[M] Multiplikation")
    print("[D] Division")
    print("[ST] Stopp")
    svar = input("Välj ett räkne för uträkning: ")

    if svar == 'A' or 'a':
        while True:
            try:
                tal1 = int(input("Ange ett tal: "))
                tal2 = int(input("Ange ett annat tal: "))
                print(str(tal1), "+", str(tal2), "=", (tal1+tal2))
                break

            except ValueError:
                print("Ogiltig inmatning, försök igen: ")

    elif svar == 'S' or 's':
        while True:
            try:
                tal1 = int(input("Ange ett tal: "))
                tal2 = int(input("Ange ett annat tal: "))
                print(str(tal1), "-", str(tal2), "=", (tal1-tal2))
                break

            except ValueError:
                print("Ogiltig inmatning försök igen: ")

    elif svar == 'M' or 'm':
        while True:
            try:
                tal1 = int(input("Ange ett tal: "))
                tal2 = int(input("Ange ett annat tal: "))
                print(str(tal1), "*", str(tal2), "=", (tal1*tal2))
                break

            except ValueError:
                print("Ogiltig inmatning försök igen: ")

    elif svar == 'D' or 'd':
        while True:
            try:
                tal1 = int(input("Ange ett tal: "))
                tal2 = int(input("Ange ett annat tal: "))
                print(str(tal1), "/", str(tal2), "=", (tal1/tal2))
                break

            except ValueError:
                print("Ogiltig inmatning försök igen: ")

    elif svar == 'St' or 'ST' or 'sT':
        print("Programmet är avslutad. ")
        break
    
    else:
        print("Ogiltig inmatning, försök igen: ")