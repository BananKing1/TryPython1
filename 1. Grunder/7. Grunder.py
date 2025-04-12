#7.Omvandla till radianer: 
import math
"""Formel: 2*pi*radian = x *C
ridain = x / pi / 2"""

#a) 160 *C
x1 = 160 #ett värde på x för att sätta in i formeln.
print (round(x1 / math.pi / 2, 2))  #lägger in antal x i formeln.

#b) 360 *C
x2 = 360 #ett värde på x för att sätta in i formeln.
print (round(x2 / math.pi / 2, 2)) #lägger in antal x i formeln.

#c) 90 *C
x3 = 90 #ett värde på x för att sätta in i formeln.
print (round(x3 / math.pi / 2, 2)) #lägger in antal x i formeln.

#d) Låt användaren får ange gradantalet och omvandla till radianer
x4 = float(input("Ange ett gradtal för att omvandla till radian: ")) #deklaration
print ("Radianens värde är", (x4 / math.pi / 2, 2)) #Resultat

#e) Låt användaren även få ange hur många decimaler programmet skall avrunda till.
avrundartal = int(input("Hur många decimaler vill du avrunda det till? ")) #deklaration
print ("Radianens värde är", round(x4 / math.pi / 2, avrundartal)) #Resultat