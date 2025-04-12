""" 5. 
När vi har en sträng kan vi splitta strängen med funktionen .split() och spara den i en lista:
strMening = "Här är en sträng"
lista = strMening.split(' ')
print(lista)

Parametern till .split() anger vid vilket tecken vi skall splita strängen, i vårat fall ett mellanslag."""
""" a) Skriv ett program som räknar antalet ord i en sträng """
strMening = "Här är en sträng" #deklaration
lista = strMening.split(' ') #uppdelning str --> list
print(lista) #utskrivning (list)
print("Antal ord i meningen:", len(lista)) #utskrivning (antal ord)


"""b) Utveckla programmet så den räknar antalet ord med 5 eller fler bokstäver"""
mening = input("Ange en sträng: ") #deklaration
lista2 = mening.split(' ') #dela meningen
lista3 = [] #lista för True/False
for sentence in lista2: #loop för varje ord i lista
   if len(sentence) > 5: #deklaration (jämföring)
      lista3.append("True") #tilläg True i lista
   elif len(sentence) == 5: #deklaration (jämföring)
      lista3.append("True") #tilläg True i lista
print("Antal ord större än 5 bokstäver:", lista3.count("True")) #utskrivning