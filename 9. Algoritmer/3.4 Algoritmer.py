"""
4. Skriv ett program som räknar största gemensamma delare av två tal
"""
def hitta_gemensam_delare(täljare, nämnare): #metod hitta delare
    while nämnare != 0:# så länge nämnare inte noll
        täljare, nämnare = nämnare, täljare % nämnare #byt plats täljare och nämnare (lämnar resten)
    return täljare #spara tälare (delaren)

while True: #evighets loop
    try: #testa
        täljare = int(input("Ange täljare: ")) #deklaration tälare + konvert int
        print("              --") #division streck
        nämnare = int(input("Ange nämnare: ")) #deklaration nämnare + konvert int

        break #stop loop
    except ValueError: #om error
        print("Ogiltig inmatning, försök igen. ") #försök igen
            
#tag från 3.3
        
delare = hitta_gemensam_delare(täljare, nämnare) #utgör metod + deklarera delare
print("Största gemensamma delare: ", delare) #utskriv delare
