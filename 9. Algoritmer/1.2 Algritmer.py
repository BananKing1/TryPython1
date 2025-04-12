"""
Testa hur bubbelsorteringen fungerar med strängar. Blanda även stora och små bokstäver.
"""

list = ["B", "c", "a", "C", "A", "b"] #klar lista med stora och små bokstäver

def bubble_sort(list):  #metod
    n = len(list) #antal karaktärer i listan
    for i in range(n - 1): #for-loop
        for j in range(0, n - i - 1): #for-loop 
            if list[j] > list[j + 1]: # om j är mindre än nästa i listan
                list[j], list[j + 1] = list[j + 1], list[j] #byt platts på dem


bubble_sort(list) #sortera listan
for chr in list: #printa alla karaktärer i listan
    print(chr)