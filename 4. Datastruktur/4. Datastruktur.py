"""4. Skriv ett program som testar ifall det finns dubbletter i en lista. Skapa sedan egna listor och 
testa programmet. Programmet skall enbart meddela användaren ifall programmet innehåller dubletter 
eller ej."""

"""list = ["Katt", "Hund", "Fågel", "Fisk", "Häst"] #lista
if list.count("Katt") > 2: #jämföring om den uppfinner sig mer än 1 gång
    print("Det finns dublletter.") #utskrivning
else: #annars finns inga dubbletter
     print("Det finnas inga dubbletter.") #utskrivning"""



list2 = [] #för att lägga till
for word in range(5): #for-loop (sätta gräns för lista)
    list2.append(input("Lägg till ord i listan: ")) #tillägg i lista
print(list2) #utskrivning list (Behövs inte)

for word in list2: #for loop
    if list2.count(word) > 1: #jämföring, uppfinner sig mer än 1 gång
        print("Det finns dublletter.") #utskrivning
        break #avbryta for-loop
else: #annars
        print("Det finnas inga dubbletter.")#utskrivning

