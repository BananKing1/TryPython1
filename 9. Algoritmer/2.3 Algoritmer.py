def binary_search_chr(inmat, list_chr): #metod för binär sökning
    list.sort(list_chr) #sortera listan # Om du inte tilldelar resultatet av list.sort(list_chr) till en variabel eller 
    #använder resultatet på något sätt, kommer ingen sortering att sparas. använd list_chr = list.sort(list_chr) eller list_chr.sort()
    vänster = 0 #för att tillägga# för att ha något att jämföra med
    höger = len(list_chr) - 1 #antal i list
    while vänster <= höger: #medan vänster är mindre eller lika med höger
        mitten = (vänster + höger) // 2 #räkna mitten 
        if list_chr[mitten] == inmat: #om mitten är lika med tal
            return True #hittad
        elif list_chr[mitten] < inmat: #om tal är större än mitten
            vänster = mitten + 1 #ta bort vänster sida av mitten
        else: #annaars
            höger = mitten - 1 #ta bort höger sida av mitten
    return False #inte hittad

def binary_search_num(inmat, list_num): #metod för binär sökning
    list.sort(list_num) #använd list_num.sort() för att sortera listan även här. Förklaringen är dendamma som ovan
    vänster = 0 #för att tillägga
    höger = len(list_num) - 1 #antal i list
    while vänster <= höger: #medan vänster är mindre eller lika med höger
        mitten = (vänster + höger) // 2 #räkna mitten
        if list_num[mitten] == inmat: #om mitten är lika med tal
            return True #hittad
        elif list_num[mitten] < inmat: #om tal är större än mitten
            vänster = mitten + 1 #ta bort vänster sida av mitten
        else: #annaars
            höger = mitten - 1 #ta bort höger sida av mitten
    return False #inte hittad

list_chr = [] #list för chr
list_num = [] # list för num
while True: #evighets loop
    print("Ange en tal eller bokstav") #fråga
    svar = (input("Svar: ")) #tillägg list
    print("[Stop] för att stoppa") #för stop
    if svar.lower() == 'stop': #om stop
        break #stop loop
    elif svar.isalpha(): #om svar chr
        list_chr.append(svar) #tillägg svar i chr list
    elif svar.isdigit(): #om svar num
        list_num.append(int(svar)) #tillägg svar i num list

print("Vad letar du efter? ") #utskrift
inmat = input("Svar: ") #sökande

if inmat.isdigit(): #om sök tal
    if binary_search_num(int(inmat), list_num): #kör metod num
        print("Talet finns i listan.") #hittad
    else: #annars
        print("Talet finns inte i listan.") #inte hittad
elif inmat.isalpha(): #om sök alphabet
    if binary_search_chr(inmat, list_chr): #kör metod chr
        print("Bokstaven finns i listan.") #hittad
    else: #annars
        print("Bokstaven finns inte i listan.") #inte hittad
