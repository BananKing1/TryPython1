"""
2.
Skriv ett program som frågar användaren efter ett tal och skriver ut
    om talet är jämnt eller udda.
    Exempel:
    Skriv in ett tal: 5
    Talet är udda.
    Skriv in ett tal: 6
    Talet är jämnt.
    Tips: Använd modulooperatorn % för att kontrollera om talet är jämnt eller udda.
 

    Tips: Använd input() för att fråga användaren efter ett tal.
    Tips: Använd print() för att skriva ut resultatet. """


tal = int(input("skriv ett tal: "))
if tal % 2 == 0: #modulooperatorn (är det delbart?)
    print("Talet är jämn")
else: #andra tal måste vara udda
    print("Talet är udda")
