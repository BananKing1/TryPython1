lista2= ["katter", "är", "fina"] #ny lista för True/False
lista3 = []
for sentence in lista2: #loop för varje ord i lista
   if len(sentence) > 5: #deklaration (jämföring)
      lista3.append(True) #tilläg True i lista

print("Antal ord större än 5 bokstäver:", lista3.count("True")) #utskrivning