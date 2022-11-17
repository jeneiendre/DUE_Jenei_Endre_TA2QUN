from tkinter import *
import objektumok_11

class Ember():
    nev = ''
    kor = 0
    diak = ''

    def __init__(self):
        self.diak = 'közép'

    def info(self):
        print(self.nev, self.kor, self.diak)


class Hallgato(Ember):
    neptunkod = ''

    def __init__(self):
        super().__init__()
        self.neptunkod = 'XXXXXX'


def info():
    hallgato_cimke = Label(ablak, text='Hallgató neve: ')
    hallgato_cimke.pack()


ablak = Tk()

menusor = Menu(ablak)

home = Menu(menusor)
home.add_command(label='Információ', command=info)
home.add_command(label='Kilépés', command=ablak.destroy)
menusor.add_cascade(label='Home', menu=home)

ablak.config(menu=menusor)
ablak.mainloop()

valaki = Hallgato()

valaki.nev = 'Jenő'
valaki.kor = 50
valaki.neptunkod = 'TA2QUN'

valaki.info()
print(valaki.neptunkod)
