""" 1.
Gissa talet
Programmet ska först välja en siffra mellan 1 och 100. En användare ska kunna välja en siffra mellan 1 
och 100 och försöka att gissa talet som har valts av programmet. om användare väljer större siffra än 
den hemliga siffra ska han eller hon få ett svar För högt. Om man väljer lägre ska man få ett svar För 
lågt. När man gissat rätt ska man få svar Bra jobbat eller liknande. Bestäm max antal gisningar, vi kan 
säga sju ,när användaren försöker gissa åttonde gången ska man få svar “Tyvärr , du har gissat fel 7 
gånger . Det rätta talet var ……. """

rätta = 50 #deklration (går även med random.randint)

for i in range (5):
    gissning = int(input("Gissa ett tal mellan 1 - 100: ")) #deklaration från användaren
    #if,elif och else för leda användaren.
    if gissning == rätta:
        print("Du har rätt!!")     
        break
    elif 1 <= gissning < rätta:
        print("Du har gissat för lågt.")
    elif rätta < gissning < 100:
        print("Du har gissat för högt.")
    else:
        print("Din gissning är mer än max värdet eller mindre än minst värde.")


if gissning == rätta: # rätt gissning
    print("Bra jobbat!")
else:
    print(f"Du har gissat 5 gånger, det rätta svaret är {rätta}") #för många gissningar
