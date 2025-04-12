import math
#6.
"""Räkna hypotenusan i en rätvinklig triangel där kateterna är:"""
"""Avrunda svaren till 2 decimaler"""
#a) 3 cm och 4 cm
print(round(math.sqrt(3**2 + 4**2)),2) #Hypotenusan i cm som inte har avrundat, den tror att det är float.
#b) 2 cm och 5 cm
print(round(math.sqrt(2**2 + 5**2)),2) #Hypotenusan i cm som inte har avrundat
#c) 14 cm och 11 cm
print(round(math.sqrt(14**2 + 11**2),2)) #Hypotenusan i cm som inte har avrundat
#d) Låt användaren ange kateterna själv och skriv ut hypotenusans läng
a = int(input("Ange en katet: "))
b = int(input("Ange den andra kateten: "))
print ("Hypotenusan av katetet är", round(((math.sqrt(a**2 + b**2))),2), "cm.") #Hypotenusan som är avrundat
