""" 3.
Skriv ett program som frågar användaren efter ett tal och skriver ut
    om talet är positivt, negativt eller noll.
    Exempel:
    Skriv in ett tal: 5
    Talet är positivt.
    Skriv in ett tal: -3
    Talet är negativt.
    Skriv in ett tal: 0
    Talet är noll.
    Tips: Använd input() för att fråga användaren efter ett tal.
    Tips: Använd print() för att skriva ut resultatet. """


tal = int(input("Skriv ett tal: ")) #deklaration
if tal == 0:
    print("Ditt tal noll. ")
elif tal < 0: 
    print("Ditt tal är negativ. ")
else:
    print("Ditt tal är positiv. ")
