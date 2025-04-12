"""* I denna uppgift behöver vi använda principen att lägga in dictionaries i en lista. Detta kommer vi 
gå igenom i genomgången tillämpningar av dictionaries. Fundera gärna innan om ni kan komma på hur vi kan 
lösa detta.

a) Skapa ett program där du skall skriva in deltagare till en golftävling. 
Menyn kan se ut som följande:
1. Mata in deltagare
2. Visa alla deltagare
3. Sök efter deltagare
4. Avsluta

Varje deltagare skall ha ett namn samt handicap (Dessa är siffror mellan 0-52). 
Dessa matas in under “Mata in deltagare” och sparas i en lista som du sedan använder dig av för 
att visa alla eller söka efter deltagare.

TIPS!
Du kan lägga in dictionaries i en lista!"""



lista = []
while True: #evighets loop
    print("\n\n\n")
    print("Du kan välja en av dessa:")
    print("[M] Mata in deltagare")
    print("[V] Visa alla deltagare")
    print("[S] Sök efter deltagare")
    print("[A] Avsluta")
    #utskrivning val

    svar = input("Vad vill du göra? ") #Svar deklaration
    if svar == 'M' or svar == 'm':
        namn = input("Skriv in namnet: ") #tilläg namn
        handicap = int(input("Skriv in handicapen (0-52): ")) #tilläg handicap
        if handicap > 53 or handicap <= -1: #ej mer än 52
            print("Du får inte göra så.") #utskrivning
        else:
            lista.append({"Namn": namn,  "Handicap": handicap}) #tilläg namn & handicap i lista
    
    #utskrivning lista per person
    elif svar == 'V' or svar == 'v':
       for p in lista:
        print(p["Namn"], p["Handicap"]) 

    elif svar == 'S' or svar == 's':
        sök = input("Vem letar du efter? ") #deklaration (sök)
        for p in lista: #for-loop
            if sök == p["Namn"]: #if sats
                print(p["Namn"], p["Handicap"]) #utskrivning
    
    elif svar == 'A' or svar == 'a':
        break #stoppa loopen
    
    else: #annars
        print("Så får du inte göra. ") #utskrivning

#utskrivning lista per person
print("\nProgrammet är avslutad. ") 
print("Här är hela listan: ")
for p in lista:
    print(p["Namn"], p["Handicap"]) 



"""b) I golf spelar spelarna på lika vilkor, så alla kan möta alla. När man spelat färdigt en runda, så 
drar man av handikappet på resultatet, för att få slutresultatet.

Utveckla programmet så att användaren får mata in hur många slag som varje spelare gick runt på. 
När inmatningen är färdig, räknar programmet ut slutresultatet (där handikappet dragits av), skriver ut
listan, sorterad efter slutresultatet."""



print("\nNu ska du skriva in antal slag för personerna: ")
for p in lista: #for-loop
    print(p["Namn"], p["Handicap"]) #vem blir tillagd
    p["Slag"] = int(input("Ange antal slag: ")) #tilläg slag i dic (deklaration)
print("\n\n\n\n\n") #5 blanka rad

# slag - handicap
#Ju mindre slag ju bättre
#Ju högre handicap ju lättare att vinna

print("Så här ser listan ut så länge: ") #Visa ny lista
for p in lista: #for-loop
    p["Resultat"] = (p["Slag"] - int(p["Handicap"])) #tilläg resultat i dic (deklaration)
    print(p["Namn"], p["Resultat"], "poäng. ") #Utskrivning lista

#Minst poäng vinner
lista = sorted(lista, key = lambda k: k["Resultat"]) #sortera lista
print("\n\nSorterade listan: ") #utskrivning
for p in lista: #for-loop
    print(p["Namn"], p["Resultat"], "poäng. ") #Utskrivning lista

vinnare = [] #för tilläggning
for p in lista: #for-loop
    vinnare.append(p["Resultat"]) #list för poäng

for i in vinnare: 
    if vinnare.count(i) > 1: #Om poäng uppfinner mer än 2 gånger
        print("\nDet finns 2 eller flera som delar vinnar plattsen. ") #utskrivning
        break #Stop loop

    else: #annnars
        print("\nVinnaren är", lista[0]["Namn"], lista[0]["Resultat"]) #utskrivning vinnaren
        break #Stop loop
