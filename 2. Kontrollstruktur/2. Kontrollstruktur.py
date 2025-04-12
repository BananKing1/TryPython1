"""Övningar 2:

På ett matteprov kunde man få högst 50 poäng. Gränsen för betyget E var 25 poäng och för betyg 
D , C, B och A 30, 35, 40 respektive 45 poäng. Skriv ett program som läser in poängen för en elev och 
som visar vilket betyg han eller hon fick på provet. """

poäng = int(input("Hur många poäng fick eleven? ")) #Deklaration

if poäng < 25:
    print("Du fick F") 
elif poäng < 30:
    print ("Du fick E")
elif poäng < 35:
    print ("Du fick D")
elif poäng < 40:
    print ("Du fick C")
elif poäng < 45:
    print ("Du fick B")
elif poäng <= 50:
    print ("Du fick A")
else:
    print("Det är omöjligt")
#Användning av if, elif och else kommando för att undvika senare problem. 