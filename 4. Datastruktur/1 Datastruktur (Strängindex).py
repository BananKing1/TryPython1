"""Strängindexerade variabler

a) Skriv ett program där användaren skall få mata in information om en hund. Det som användaren skall 
skrivas in är namn, ras och vikt. Programmet skall spara denna information i en strängindexerad variabel
(dictionary) och sedan skriva ut informationen till användaren i en utskrift på skärmen."""

hund = {"namn":"X", "ras":"Y", "vikt":"Z"} #tup
hund["namn"] = input("Vad heter hunden? ") #deklaration
hund["ras"] = input("Vilken ras? ") #deklaration
hund["vikt"] = (input("Hur mycket väger den? ") + ("kg")) #deklaration
print(hund) #utskrivning


"""
b) Låt användaren kunna få en valmöjlighet att kunna ändra information om hunden. Tex skall användaren 
kunna välja om den vill ändra namn, ras eller vikt och sedan få ange det nya värdet.
Ett tips är att göra programmet menybaserat."""


hund = {"namn":"X", "ras":"Y", "vikt":"Z"} #tup
while True: #oändligt loop
    print("Välj för att byta: ") #Visning av olika val.
    print("[N] Namn:", hund["namn"])
    print("[R] Ras:", hund["ras"])
    print("[V] Vikt:", hund["vikt"] + "kg")
    print("[K] Jag är klar.")
    val = input("Vilken vill du ändra på? ") #deklaration
    
    if val == 'N' or 'n': #val N
        hund["namn"] = input("Vad vill du byta hundens namn till? ") #deklaration
    elif val == 'R' or 'r': #val R
        hund["ras"] = input("Vad vill du byta hundens ras till? ") #deklaration
    elif val == 'V' or 'v': #val V
        hund["vikt"] = input("Vad vill du byta hundens vikt till? ") #deklaration
    elif val == 'K' or 'k': #val K
        print("[N] Namn:", hund["namn"]) #utskrivning
        print("[R] Ras:", hund["ras"]) #utskrivning
        print("[V] Vikt:", hund["vikt"] + "kg") #utskrivning
        print(hund) #utskrivning
        break #stop loop
    else:
        print("Så kan du inte göra. ") #utskrivning

