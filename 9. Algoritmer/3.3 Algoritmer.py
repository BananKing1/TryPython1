"""
3. 
Skriv ett program där användaren får skriva in ett bråk (tex på formen 22/54) och programmet förkortar bråket så långt som möjligt.
"""
def hitta_gemensam_delare(täljare, nämnare): #metod hitta delare
    while nämnare != 0:# så länge nämnare inte noll
        täljare, nämnare = nämnare, täljare % nämnare #byt plats täljare och nämnare (lämnar resten)
    return täljare #spara tälare (delaren)

def förkorta_bråk(täljare, nämnare): #metod förkorta    
    delare = hitta_gemensam_delare(täljare, nämnare) #deklarera delare

    förkortad_täljare = täljare // delare #förkorta med delaren
    förkortad_nämnare = nämnare // delare #förkorta med delaren
    
    return förkortad_täljare, förkortad_nämnare #spara ny tälare och nämnare

while True: #evighets loop
    try: #testa
        täljare = int(input("Ange täljare: ")) #deklaration tälare + konvert int
        print("              --") #division streck
        nämnare = int(input("Ange nämnare: ")) #deklaration nämnare + konvert int

        break #stop loop
    except ValueError: #om error
        print("Ogiltig inmatning, försök igen. ") #försök igen



förkortat_täljare, förkortat_nämnare = förkorta_bråk(täljare, nämnare) #utgöra metod + deklarera ny täljare och nämnare


print("Det förkortade bråket är: ") #utskriv
print(förkortat_täljare) #förkortat tälare
print("-") #division streck
print(förkortat_nämnare) #förkortat 

