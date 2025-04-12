"""
Skapa ett program som innehåller denna meny:
1. Omvandla C till F
2. Omvandla F till C
0. Avsluta.
"""

def ConvF (C):#Metod konvert till F
    F = C*1.8+32 #räkna
    return F

def ConvC (F): #Metod konvert till C
    C = (F-32)/1.8 #räkna
    return C


while True: #Evighets loop
    print("Du har dessa val: ") #val + fråga
    print("1. Omvandla C till F")
    print("2. Omvandla F till C")
    print("0. Avsluta")
    print("Vad vill du göra? (Obs! svara med nummreringen) ") 

    svar = int(input("Svar: ")) #deklaration svar

    if svar == 1: #om 1
        C = int(input("Ange ett värde på C: ")) #Deklaration C
        F = ConvF(C) #konverta till F
        print("Temperatur i fahrenheit:", F) #utskrift
        print(" ")

    elif svar == 2:
        F = int(input("Ange ett värde på F: ")) #Deklaration F
        C = ConvC(F) #konverta till C
        print("Temperatur i celcius:", C) #utskrift  
        print(" ")

    elif svar == 0: #om 0
        print("Programmet är avslutad. ") #utskrift
        break #stopp loop

    else: #annars
        print("Ogiltig inmatning. Försök igen") #försök igen
        print(" ")