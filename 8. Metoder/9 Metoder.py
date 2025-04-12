"""
a) Skapa ett program som fungerar som en miniräknare. Programmet skall fråga vilket räknesätt som 
du skall använda (+, -, /, *) och sedan ange två tal. Svaret skall sedan beräknas och skrivas ut på 
ett lämplig sätt. Detta upprepas tills användaren anger “Q” som avslutar programmet. Programmet skall
innehålla fyra metoder som heter addition, subtraktion, multiplikation och division, som alla tar två
tal som parametrar
b) Utöka programmet med funktioner för att räkna ut potenser och kvadratroten
"""

import math
def Add(term1, term2): #metod addition
    summa = int(term1) + int(term2)
    return summa

def Subtract(term1, term2): #metod subtraktion
    differens = int(term1) - int(term2)
    return differens

def Multi (faktor1, faktor2): #metod multiplikation
    produkt = int(faktor1) * int(faktor2)
    return produkt

def Divi (täljare, nämnare): #metod division
    kvot = int(täljare) / int(nämnare)
    return kvot  

def Potens (bas, potens):
    potenstal = int(bas) ** int(potens)
    return potenstal

def ruten (bas):
    tal = math.sqrt(int(bas))
    return tal


while True: #evighets loop
    print("Du har dessa val: ") #utskriv (val)
    print("[A] Addition")
    print("[S] Subtraktion")
    print("[M] Multiplikation")
    print("[D] Division")
    print("[P] Potens")
    print("[R] Kvdratrutenur")
    print("Vilken räknesätt vill du räkna med? ")

    svar = input("Svar: ") #delaration

    if svar == "A" or svar == "a": #if a
        term1 = input("Ange första termen: ") #delaration
        term2 = input("Ange andra termen: ") #delaration
        print("Summa:", Add(term1, term2)) #utskriv

    elif svar == "S" or svar == "s": #if s
        term1 = input("Ange första termen: ") #delaration
        term2 = input("Ange andra termen: ") #delaration
        print("Differens:", Subtract(term1, term2)) #utskriv

    elif svar == "M" or svar == "m": #if m
        faktor1 = input("Ange första faktorn: ") #delaration
        faktor2 = input("Ange andra faktorn: ") #delaration
        print("Produkt:", Multi(faktor1, faktor2)) #utskriv

    elif svar == "D" or svar == "d": #if d
        täljare = input("Ange täljare: ") #delaration
        nämnare = input("Ange nämnare: ") #delaration
        print("Kvot:", Divi(täljare, nämnare)) #utskriv

    elif svar == "P" or svar == "p":
        bas = input("Ange en bas: ")
        potens = input ("Ange en potens: ")
        print("Potenstal: ", Potens(bas, potens))

    elif svar == "R" or svar == "r":
        bas = input("Ange ett tal: ")
        print("Kvadratruten:", ruten(bas))

    elif svar == "Q" or svar == "q": #if q
        print("Programmet är avslutad.") #utskriv
        break #stop loop

    else: #annars
        print("Ogiltig inmatning.") #utskriv