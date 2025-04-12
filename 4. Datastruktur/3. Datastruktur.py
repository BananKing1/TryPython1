"""3. 
Låt användaren skriva in fem meningar. Programmet skall sedan räkna ut medellängden på meningarna. 
Programmet skall sedan skriva ut i konsolen hur lång den längsta meningen är"""

list = [] #deklaration
for namn in range(5):  #For-loop 5 gånger
    namn = input("Skriv en mening: ") #inskrivning deklaration
    list.append(namn) #lägg till mening
print(list) #utskrivning


summa = 0 #deklaration
for sentence in list: #för mening i list
    summa += len(sentence) #summera
print ("Medelängden: ", summa / len(list)) #utskrivning


longest = 0 #deklaration
for sentence in list: #för mening i list
    if len(sentence) > longest: #jämföring i lista
        longest = len(sentence) #deklaration
print("Längsta mening: ", longest) #utskrivning