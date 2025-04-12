""" 6.

Använd metoden .rjust() för att i ett Pythonprogram skriva ut en snygg tabell över alla tal från 
1 till 10 med deras kvadrater och kuber. (Gör om varje tal för utskrift till en sträng med 
str() först). """


tal = "tal" #deklaration
kvadrat = "kvadrat" #deklaration
kub = "kub" #deklaration
print((tal.rjust(20)) + (kvadrat.rjust(20)) + (kub.rjust(20))) #Huvudtabell

for i in range(10): #loop
   ta = str(i**1) #deklaration
   kva = str(i**2) #deklaration
   ku = str(i**3) #deklaration
   print(ta.rjust(20) + kva.rjust(20) + ku.rjust(20)) #utkrivning 