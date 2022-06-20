from tkinter import *

window = Tk()
elemento = StringVar()
listbox = Listbox(window)

for marcas in ["Audi", "BMW", "Mercedes", "Honda", "Seat", "Fiat", "Ferrari", "Lamborgini"]:
    listbox.insert(END, marcas)
listbox.pack()
label = Label(text="Listado de Marcas de coches")
label.pack()
window.mainloop()