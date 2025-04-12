#8. Omvandla till grader:  Obs! Frivilligt att arbeta med
import math
"""Formel: 2*pi*radian = x *C
ridain = x / pi / 2"""

#a) PI radianer
radian1 = math.pi #deklaration
print(int(2*math.pi*radian1), "*C") #formel och utskrivning

#b) 2 * PI radianer
radian2 = (math.pi * 2) #deklaration
print (int(2*math.pi*radian2), "*C") #formel och utskrivning

#c) PI / 2 radianer
radian3 = (math.pi / 2) #deklaration
print (int(2*math.pi*radian3), "*C") #formel och utskrivning

#d) Låt användaren får ange radianantalet och omvandla till grader
radian4 = float(input("Ange ett radian antal: ")) #deklaration
print ("Antalet grader är", float(2*math.pi*radian4), "*C") #utskrivning

#e) Låt användaren även få ange hur många decimaler programmet skall avrunda till.
avrunda = int(input("Hur många decimaler vill du avrunda det till? ")) #deklaration
print ("Antalet grader är ca", round(2*math.pi*radian4, avrunda), "*C") #utskrivning