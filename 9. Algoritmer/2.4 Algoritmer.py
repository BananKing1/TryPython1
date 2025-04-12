"""
4.
a) Skapa en metod för linjärsökning. 
b) Lägg till så att programmet presenterar hur många sökningar som behövs innan den hittar ett tänkt
element i båda metoderna.
"""

def linear_search_chr(sök, list_chr, count): #metod linjär sökning (str)
    for chr in list_chr: #för alla element i listan 
        count += 1 #tillägg antal sök
        if chr == sök:  #om hittad
            return True, count #stopp loop spara resultat
    return False, count #stopp loop spara resultat
    
def linear_search_num(sök, list_num, count): #metod linjär sökning (int)
    for num in list_num: #för alla element i listan 
        count += 1 #tillägg antal sök
        if num == sök:  #om hittad
            return True, count #stopp loop spara resultat
    return False, count #stopp loop spara resultat

list_chr = ['a', 'b', 'c'] #list str
list_num = [1, 2, 3] #list int
count = 0 #antal sökning


sök = input("Vad letar du efter? ") #inmat sök
if sök.isalpha(): #om söker str
    found, count = linear_search_chr(sök, list_chr, count) #dela upp tup till found och count
    if found: #om hittad
        print("Hittad. ") #utskriv hittad
        print("Antal sökningar:", count) #utskriv antal sök
    else: #annars
        print("Inte hittad. ") #utskriv inte hittad
        print("Antal sökningar:", count) #utskriv antal sök

elif sök.isdigit(): #om söker int
    found, count = linear_search_num(sök, list_num, count) #dela upp tup till found och count
    if found: #om hittad
        print("Hittad. ") #utskriv hittad
        print("Antal sökningar:", count) #utskriv antal sök
    else: #annars
        print("Inte hittad. ") #utskriv inte hittad
        print("Antal sökningar:", count) #utskriv antal sök
