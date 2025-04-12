"""
Skapa en metod som tar två tal som indata och sedan multiplicerar dessa. Metoden skall returnera '
produkten av talet.
"""

def multiplikation(a, b): #define
    produkt =(a*b) #räkna
    return produkt #svar


a = int(input("Skriv en siffra: ")) #indata + int konvert
b = int(input("Skriv den andra siffran: " )) #indata + int konvert
Resultat = multiplikation(a,b) #räkna
print(Resultat) #utskrift
    