while True:  #evighets loop
    try: #test
        antaltemp = int(input("Hur många temperaturer vill du mata in. ")) #antal inmatning av temp
        list = [] #för att sparas
        break #stop
    except ValueError: #förutom
        print("Ogiltig inmatning, ange igen.") #utskriv

if antaltemp < 1: #mindre 1
    while True: #Evighets loop
        try: #test
            antaltemp = int(input("Ange ett positivt tal med värde övger noll. ")) # ny inskriv
            if antaltemp < 1: #mindre 1
                print("Ogiltig inmatning") #utskriv
            else: #annars
                break #stopp
        except (ZeroDivisionError, ValueError): #förutom
            print("Ogiltig inmatning") #utskriv



while True: #evighets loop
    try: #test
        temp = int(input("Ange ett temperatur: ")) #deklaration
        list.append(temp) #deklration sparas i lista     
        if len(list) == antaltemp: #om lika många 
            break #stopp

    except ValueError: #förutom
        print("Ogiltig inmatning, försök igen. ") #utskriv

print("Temperaturs listan ser ut så här: ", list) #utskrivning
try: #test
    medeltemperatur = sum(list)/antaltemp #deklaration
    print("Medeltemperaturen är: ", medeltemperatur) #utskrivning 

except (ZeroDivisionError): #förutom
    print("Medeltemperaturen är 0, temperaturs listan är tom. ") #utskri    
        
