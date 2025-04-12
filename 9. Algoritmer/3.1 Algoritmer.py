"""
1. 
Skapa ett program där användaren får ange ett tal och programmet skall sedan räkna ut alla primtal
upp till och med det angivna talet.
"""    

def prime_num(primtal, num): #metod hitta primtal
    for k in range (2, num+1): #kolla alla tal (2 till angett nummer)
        är_primtal = True #antag true
        
        for i in range(2, k): #dela med allan världen (2 - k(själv))
            if k % i == 0:#om k dividerbar med annat än själv = false
                är_primtal = False #inte primtal
        
        if är_primtal == True: #om primtal
            primtal.append(k) #tilläg i list
    return primtal #spara list


"""
primtal = [] #list för primtal
num = 12
print(prime_num(primtal, num))
"""