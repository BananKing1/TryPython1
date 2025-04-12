"""1. Låt användaren mata in fem tal, och spara dessa i en lista. Räkna på medelvärdet 
och medianen på dessa fem tal. """

import statistics

tal1 = int(input("Mata in ett tal: ")) #deklaration
tal2 = int(input("Mata in ett annat tal: ")) #deklaration
tal3 = int(input("Mata in ett annat tal: ")) #deklaration
tal4 = int(input("Mata in ett annat tal: ")) #deklaration
tal5 = int(input("Mata in det sista talet: ")) #deklaration

list = [tal1, tal2, tal3, tal4, tal5] #samlat i lista
medelvärde = tal1 + tal2 + tal3 + tal4 + tal5 #deklaration
median = statistics.median(list) #deklaration

print("Medelvärdet är: ", medelvärde) #utskrivning
print("Medianen är: ", median) #utskrivning