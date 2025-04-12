"""Tuples
1. 
I en lista med heltal kan vi få fram tex maximum och minimum-värden i en lista eller tuple:
tup = (3, 5, 7)

print(min(tup))
print(max(tup))

Skriv ett program som hittar max- och minimumvärdet utan att använda de inbyggda funktionerna. 

Tips! Du kommer behöva iterera igenom listorna med hjälp av förslagsvis for-loopen."""

tup = (5, 3, 7) #tup
lista = [] #list
for nr in tup: #for-loop
    lista.append(nr) #tilläg nummer
lista.sort() #sort
print("Minst värde:", lista[0]) #utskrivning min
print("Max värde:", lista[2]) #utskrivning max