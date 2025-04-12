"""
a) Skapa en metod moms som lägger till momsen till en viss summa. Antag att momsen är 25%. 
(Tex talet 100 ger svaret 125). 
"""

def multiplikation(summa = int(input("Ange en summa som du vill räkna med: "))): #define + indata + konvert
    totsum = (1.25*summa) #räkna
    print("Summa efter moms är", totsum, "kr. " ) #utskrift


multiplikation() #def start