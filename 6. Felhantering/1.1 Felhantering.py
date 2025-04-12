while True: #evighets loop
    n = input("Skriv ett tal: ") #deklaration
    try:
        if  int(n) > 0: #testa om int + kolla om positiv
            break #stop loop
        else: #annars
            print("Du får inte ange ett nummer mindre eller lika med 0. ") #utskriv
    except ValueError: #om error
        print("Svaret för inte innehålla bokstäver ellen tecken, försök igen: ") #utskriv

primtal = [] #list för primtal

#undersök om primtal
for k in range (2, int(n)+1): #kolla alla tal (2 - n)
    är_primtal = True #antag alltid true
    
    for i in range(2, k): #dela med allan världen (2 - k(själv))
        if k % i == 0:#om k dividerbar med annat än själv = false
            är_primtal = False #tänk att det är falsk
    
    if är_primtal == True: #om primtal
        primtal.append(k) #tilläg i list

if len(primtal) == 0: #om
    print("Det finns inga primtal upp till angett nummer. ") #utskriv
else:#annars
    print("Här är listan för alla primtal upp till angett nummer: ", primtal) #utskrivning all primtal
