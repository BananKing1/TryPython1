"""1.
I vårt exempel “Primtal” läser man in ett tal och undersöker om talet var ett primtal. 

Använd detta program som förebild och skriv ett nytt program som läser in ett positivt heltal n och som
skriver ut alla primtal som är mindre än eller lika med n. Skapa Pseudokod först till programmet. 

Tips: Prova alla tal i intervalet 1 till n och se om de är primtal
Obs: Grupparbete: jobba två och två
VAd ska lämnas in: Både pseudokod och programkod
"""

"""
#Primtal Exempel
while True: #Evighets loop
    s = int(input("Ange talet: ")) #deklaration 
    if s == '':
        break
     

    #undersök om talet är primtal
    är_primtal = True
    for k in range(2, s):
        if s % k == 0:
            är_primtal = False

    #Resultat
    if är_primtal:
        print("Primtal")
    else:
        print("Ej primtal")
"""

"""
Pseudokod:
Deklaration 'n' -->
kolla öppet sträng -->
Beräkna alla primtal mindre än 'n' med while-loop -->
Skriv ut lista av primtal
"""

while True: #evighets loop
    n = input("Skriv ett tal: ") #deklaration
    try:
        n = int(n) #testa om int
        break #stop loop
    except ValueError: #om error
        print("Så får du inte göra. ") #utskriv

primtal = [] #list för primtal

#undersök om primtal
for k in range (2, n+1): #kolla alla tal (2 - n)
    är_primtal = True #antag alltid true
    
    for i in range(2, k): #dela med allan världen (2 - k(själv))
        if k % i == 0:#om k dividerbar med annat än själv = false
            är_primtal = False 
    
    if är_primtal == True: #om primtal
        primtal.append(k) #tilläg i list

print("Här är listan för alla primtal upp till angett nummer: ", primtal) #utskrivning all primtal
