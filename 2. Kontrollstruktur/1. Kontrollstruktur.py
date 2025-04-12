""" Övning 1:
På ett gym kan man antingen köpa ett årskort eller köpa en biljett vid varje besök. Skriv ett program som
läser in priset för ett årskort, priset för en biljett samt antalet gånger man planerar att besöka gymmet 
under ett år. Därefter ska programmet ange om det lönar sig att köpa årskort eller inte. """
#Formeln a*1 kostnaden för årsbiljett
#Formeln b*x där x är antal dagar

a = float(input("Hur mycket kostar ett årsbiljett? ")) #deklaration av årsbiljett

b = float(input("Hur mycket kostar en engångs biljett? ")) #deklaration av en gångsbiljett
c = float(input("Hur många gånger vill du besöka gymmet om året? ")) #Deklaration av antal besök


if (b*c) < a: #Antal kostnad för årsbiljett (a) är mer än kostad för varje engångsbiljett (b*c)
    print("Det är inte värt det att köpa ett årsbiljett")
