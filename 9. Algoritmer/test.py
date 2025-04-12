def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def förkorta_bråk(bråk):
    # Dela upp bråket i täljare och nämnare
    täljare, nämnare = map(int, bråk.split('/'))
    
    # Hitta största gemensamma delaren
    största_gemensam_delare = gcd(täljare, nämnare)
    
    # Förkorta bråket genom att dela både täljare och nämnare med största gemensamma delaren
    förkortad_täljare = täljare // största_gemensam_delare
    förkortad_nämnare = nämnare // största_gemensam_delare
    
    return förkortad_täljare, förkortad_nämnare

# Låt användaren ange ett bråk
bråk = input("Ange ett bråk på formen täljare/nämnare: ")

# Förkorta bråket
förkortat_täljare, förkortat_nämnare = förkorta_bråk(bråk)

# Skriv ut det förkortade bråket
print("Det förkortade bråket är:", förkortat_täljare, "/", förkortat_nämnare)
