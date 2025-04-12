"""Övning 3
Detta program frågar hur många tärningar som användaren vill kasta.
Programmet kommer sedan att kasta det angivna antalet tärningar och
visa resultatet i konsolen. Programmet kommer även räkna ut den totala
summan och medelvärdet av tärningarna"""

import random
import math
kast = int(input("Hur många träningar vill du kasta? ")) #deklaration
summa = 0 #för att lägga till

for i in range (kast):
    tärning = random.randint(1, 6) # deklaration
    summa += tärning #Lägg till alla resultat på kastning
    print(f"Tärning {i+1}: {tärning}") #f sträng för att räkna tärningar

#formel för medelvärde : tot. summa/ kast
print("Summa:", (summa)) #utskrivning av summan
print("Medelvärde (ca):", round(summa/kast, 2)) #utskrivning av medelvärde