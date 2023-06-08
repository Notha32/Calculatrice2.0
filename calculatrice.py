import tkinter as tk
from tkinter import *

print("Connection...")

def un():
    entrer.insert(END, 1)

def deux():
    entrer.insert(END, 2)

def trois():
    entrer.insert(END, 3)

def quatre():
    entrer.insert(END, 4)

def cinq():
    entrer.insert(END, 5)

def six():
    entrer.insert(END, 6)

def sept():
    entrer.insert(END, 7)

def huit():
    entrer.insert(END, 8)

def neuf():
    entrer.insert(END, 9)

def zero():
    entrer.insert(END, 0)

def delete():
    entrer.delete(0, END)

def multi():
    b = "*"
    entrer.insert(END, b)

def divi():
    e = "/"
    entrer.insert(END, e)

def moins():
    c = "-"
    entrer.insert(END, c)

def plus():
    d = "+"
    entrer.insert(END, d)

def calcul():
    a = entrer.get()
    if "/0" in a:
        entrer.delete(0, END)
        entrer.insert(0, "Erreur !")    
    else:
        entrer.delete(0, END)
        entrer.insert(0, eval(a))
    

window = tk.Tk()

window.geometry("425x475")
window.resizable(height=False, width=False)
window.title("Calculatrice")

# on créer un input avec tkinter pour afficher le futur résultat

entrer = Entry(window, font=('Helvetica', 20))
entrer.place(x=20, y=20, width=385, height=50 )

# boutton première ranger

boutton1 = Button(window, text='1', font=('Helvetica', 15), command=un)
boutton1.place(x=20, y=90, width=70, height=70)

boutton2 = Button(window, text='2', font=('Helvetica', 15), command=deux)
boutton2.place(x=125, y=90, width=70, height=70)

boutton3 = Button(window, text='3', font=('Helvetica', 15), command=trois)
boutton3.place(x=230, y=90, width=70, height=70)

bouttonpoint = Button(window, text='↩', font=('Helvetica', 15), command=delete)
bouttonpoint.place(x=335, y=90, width=70, height=70)

# boutton deuxième ranger

boutton4 = Button(window, text='4', font=('Helvetica', 15), command=quatre)
boutton4.place(x=20, y=180, width=70, height=70)

boutton5 = Button(window, text='5', font=('Helvetica', 15), command=cinq)
boutton5.place(x=125, y=180, width=70, height=70)

boutton6 = Button(window, text='6', font=('Helvetica', 15), command=six)
boutton6.place(x=230, y=180, width=70, height=70)

bouttonmulti = Button(window, text='x', font=('Helvetica', 15), command=multi)
bouttonmulti.place(x=335, y=180, width=70, height=70)

# boutton troisième ranger

boutton7 = Button(window, text='7', font=('Helvetica', 15), command=sept)
boutton7.place(x=20, y=270, width=70, height=70)

boutton8 = Button(window, text='8', font=('Helvetica', 15), command=huit)
boutton8.place(x=125, y=270, width=70, height=70)

boutton9 = Button(window, text='9', font=('Helvetica', 15), command=neuf)
boutton9.place(x=230, y=270, width=70, height=70)

bouttondivi = Button(window, text='÷', font=('Helvetica', 15), command=divi)
bouttondivi.place(x=335, y=270, width=70, height=70)

# boutton quatrième ranger

boutton0 = Button(window, text='0', font=('Helvetica', 15), command=zero)
boutton0.place(x=20, y=360, width=70, height=70)

bouttonplus = Button(window, text='+', font=('Helvetica', 15), command=plus)
bouttonplus.place(x=125, y=360, width=70, height=70)

bouttonmoins = Button(window, text='-', font=('Helvetica', 15), command=moins)
bouttonmoins.place(x=230, y=360, width=70, height=70)

bouttonegal = Button(window, text='=', font=('Helvetica', 15), command=calcul)
bouttonegal.place(x=335, y=360, width=70, height=70)

# vérification si l'appareil est connecté

print("Connecté")

window.mainloop()