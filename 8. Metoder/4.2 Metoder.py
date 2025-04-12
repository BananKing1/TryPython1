"""
b) Gör funktionen i 3a så att man i metodanropet även får ange vad momsen ligger på.
"""


def multiplikation(summa, moms): #define + indata + konvert
    momsproc= (moms/100)+1
    totsum = (momsproc*summa) #räkna
    print("Summa efter moms är", totsum, "kr. " ) #utskrift

moms = int(input("Ange procentuell moms som du vill räkna med: "))
summa = int(input("Ange en summa som du vill räkna med: "))
multiplikation(summa, moms) #def start