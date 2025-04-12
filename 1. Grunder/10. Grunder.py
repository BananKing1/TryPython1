#10. Formeln y = 265000 * 0,85x visar hur värdet y kr av en bil avtar med tiden x år.
#a) Beräkna efter hur många år värdet är 100 000 kr
y = 100000 #Värdet på bilen efter x antal år
x = y/(265000 * 0.85)
print (x, "eller ca.", round(x, 2), "år gammal.")


#b) Låt användaren får ange startvärdet på bilen själv.
y = int(input("Ange ett start värde på bilen: ")) # konvert till int för datorn tror den är str
x2 = y/(265000 * 0.85)
print ("Din bil är ca.", round(x2, 2), "år gammal.")

#c) Låt användaren få ange i vilken procentuell takt som bilens värde avtar varje år.
procent = float(input("Ange den procentuella takten bilens värde avtar:" )) #Deklaration antal minsknin procent
procentminskning = (procent/100) #procent i decimal
# ekvationen är: y = 265000 * procentuell * x
print("Din bils ekvation blir 265000 *", procentminskning, str("* x")) #Ekvationen
