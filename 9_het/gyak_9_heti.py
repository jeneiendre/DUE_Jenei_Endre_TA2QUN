# jelszógenerátor
'''
import fuggveny
print(fuggveny.jelszogenerator(18, True, True))

from objektum import *

p = Jelszoobjektum()
p.jelszohossz = 15
print(p.jelszogenerator())
'''
from tkinter import *
import fuggveny

def jelszokiiras():
    jelszo_cimke.pack()

ablak = Tk()
ablak.title('Jelszógenerálás')
ablak.minsize(400, 300)
cimke = Label(ablak, text='A jelszó: ', fg='red')
jelszo_cimke = Label(ablak, text=fuggveny.jelszogenerator(10, True, True))
ok_gomb = Button(ablak, text='OK', command=ablak.destroy)
jelszo_gomb = Button(ablak, text='Generál', command=jelszokiiras())

cimke.pack()
jelszo_gomb.pack()
ok_gomb.pack()
mainloop()