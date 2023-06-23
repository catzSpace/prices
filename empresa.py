from tkinter import *


w = Tk()
w.title("automata") #si, en referencia al juego de Nier Automata
w.geometry("500x500")


bienvenida = Label(w, text="ingrese su edad por favor")
bienvenida.place(x=10, y=10)
e = Entry() #soy malisimo nombrando variables
e.place(x=10, y=30)


T = Label(w, text="calculando...")
T.pack()
T.place(y=120)

def calculo():
    a = int(e.get())

    if a < 5:
        T["text"] = "entras gratis"

    elif a >= 5 and a <= 18:
        T["text"] = "debes pagar 5000"

    elif a > 18:
        T["text"] = "tu entrada cuesta 10000"



b = Button(text="enviar", command=lambda: calculo())
b.pack(padx=50, pady=60)




w.mainloop()