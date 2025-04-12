"""
Skapa en metod ToPercentage() som tar in ett decimaltal och returnerar ett heltal 
(Tex flyttalet 0.73 ger heltalet 73)
"""

def ToPercentage(tal): #metod
    talNy = float(tal*100) #räkna
    return (str(talNy) + "%") #return
            
tal = (0.75) #deklaration
print(ToPercentage(tal)) #utskrift