"""2. Version 1 (Enklare):
Låt användaren får mata in temperaturmätningar på en väderstation. Dessa mätningar skall sparas i en lista och användaren skall få 
skriva så många som den vill.

När programmet är färdigt skall listan med alla mätningar skrivas ut och även medeltemperaturen."""

antaltemp = int(input("Hur många temperaturer vill du mata in. ")) #antal inmatning av temp
list = [] #för att sparas

for i in range (antaltemp):
    temp = int(input("Ange ett temperatur: ")) #deklaration
    print(f"Temperatur {i+1}: {temp}°C") #anger temps nummer
    list.append(temp) #deklration sparas i lista       

print("Temperaturslistan ser ut så här: ", list) #utskrivning

medeltemperatur = sum(list)/antaltemp #deklaration
print("Medeltemperaturen är: ", medeltemperatur) #utskrivning