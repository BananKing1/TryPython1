"""
2.
Skriv ett program som skriver ut multiplikationstabellen enligt följande mönster nedan. Användaren 
skall gå ange båda talen för antalet rader och kolumner.
"""
#collumns(^) rows(<->)
def multi_table(columns, rows): #metod tabrll
    spacer = '       | ' #deklaration uppdela 
    print(spacer, end="")  #dela
    for i in range(1, columns+1): #loop 1 och uppåt
        print(f"{i: >5}", end="") # huvudtabell (1 och uppåt mrf med 5 mellan slag)
    print("")#ny rad

    total_length = len(spacer) + columns * 6  # räkna hela förra rad i utskrift
    print("-" * total_length) #dela huvudtabell

    for j in range(0, rows): #loop antal rader
        print(j+1, "     | ", end='') #rader 1 och uppåt med utdelning, nästa börjar på samma rad
        for k in range (1, columns+1): #loop multiplicera alla kollumner
            print(f"{(j+1)*(k): >5}", end="") #utskiv och uträkning med 5 mellan slag, nästa börjar på samma rad

        print (" ") #ny rad



while True:
    try:
        columns = int(input("Hur många kollumner vill du ha? ")) #deklration + test konvert
        rows = int(input("Hur många rader vill du ha? ")) #deklration + test konvert
        print(multi_table(columns, rows)) #utgöra metod
    
    except ValueError: #om inte gick konvert
        print("Ogiltig inmatning försök igen: ") #försök igen
        print(" ") #ny rad

