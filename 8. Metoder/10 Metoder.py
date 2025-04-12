"""
a) Skapa ett program där vi skall räkna ut räntasatsen på ett banklån. Användaren skall ange räntan samt lånebeloppet. 
Programmat skall sedan räkna ut räntekostnaden för beloppet.
b) Bygg ut programmet mer fler funktioner. Tex att vi skall amortera på lånet över flera år. Vad blir räntekostnaden för varje år? 
Om vi betalar kvartalsvis/måndasvis? 
"""

def kostnadränta (ränta, belopp): #metod ränta på månad
    räntekostnad = int(ränta)/100 * int(belopp) #räkna
    return räntekostnad #return

def ammortering (ränta, belopp, år): #metod ränta på år
    Räntekostnad = (float(ränta)/100) * int(år)*2 * float(belopp) #räkna
    return Räntekostnad #return

ränta = input("Ange din ränta: ") #deklaration
belopp = input("Ange ditt belopp: ") #deklaration
år = input("Ange hur många år: ") #deklaration

while True: #evighets loop
    print("[M] Ränteräkning en månad") #utskriv
    print("[Å] Ränteräkning i antal år") #utskriv
    print("Vad vill du göra?") #utskriv

    svar = input("Svar: ") #deklaration

    if svar == "M" or svar == "m":  #if m
        print("Räntekosnaden är", (kostnadränta(ränta, belopp)), "kr.") #kostnad månad

    elif svar == "Å" or svar == "å": #if å
        print ("Räntekosnaden är", (ammortering(ränta, belopp, år)), "kr.") #kostnad år

    else: #annars
        print("Ogiltig inmatning, försök igen.") #försök igen

