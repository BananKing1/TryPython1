"""
4. När din metod sorteras, låt programmet även räkna hur många gånger två element byter plats. 
Presentera sedan resultatet i konsolen för användaren.
"""

list = ["B", "c", "a", "C", "A", "b"] #Klar lista


def bubble_sort(list):  #metod
    n = len(list) #antal karaktärer i listan
    tal = 0 #för räkna gånger bytt
    for i in range(n): #for-loop
        for j in range(0, n - i - 1): #for-loop 
            if list[j] > list[j + 1]: # om j är mindre än nästa i listan
                list[j], list[j + 1] = list[j + 1], list[j] #byt platts på dem
                tal += 1 #tilläg 1 varje gång bytt
    return tal #värdet för metod

print (list)#printa osorterad lista
#Printa sorterat lista
num = bubble_sort(list) #sätter variabel värde till antal byten
print (list) #printar sorterad lista
print (num) #printar antal byten

