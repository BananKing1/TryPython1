"""
1.
Skapa ett fönster med tkinter som innehåller textfält för att mata in namn, adress och personnummer, samt en dropdown-box
för att välja en mobiltelefon.

"""
from tkinter import *

root = Tk()

Tillägg = Label(root, text="+")
Tag_bort = Label(root, text="-")
Tillägg.grid(row=0, column=0)
Tag_bort.grid(row=0, column=1)

enKnapp = Button(root, text="Tryck på mig!", bg="blue")
enKnapp.pack()




root.mainloop()