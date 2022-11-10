# jelszógenerátor
from tkinter import *
import objektumok


def jelszokiiras():
    try:
        p.jelszohossz = int(hossz.get())
    except:
        hibaablak = Toplevel(ablak)
        hibaablak.geometry('200x120')
        hibauzenet = Label(hibaablak, text='A jelszó hossza csak szám lehet!', fg='red', height=5)
        hibauzenet.grid(row=0, rowspan=2, sticky=N)
        okgomb = Button(hibaablak, text='OK', command=hibaablak.destroy)
        okgomb.grid(row=3, sticky=E)
        hibaablak.mainloop()
    else:
        p.van_szamjegy = szamjegy.get()
        p.van_irasjel = irasjel.get()
        p.jelszogenerator()
        jelszo_ertek['state'] = NORMAL
        jelszo_ertek.delete(1.0, END)
        jelszo_ertek.insert(END, p.jelszo)
        jelszo_ertek.grid(row=0, column=1)
        jelszo_ertek['state'] = DISABLED

p = objektumok.Jelszoobjektum()


ablak = Tk()
ablak.title('Jelszógenerálás')
ablak.minsize(width=200, height=100)

jelszo_cimke = Label(ablak, text='A jelszó: ', fg='red')
jelszo_cimke.grid(row=0, column=0)

jelszo_hossza = Label(ablak, text='A jelszó hossza:')
jelszo_hossza.grid(row=1, column=0)

hossz = Entry(ablak, width=5)
hossz.insert(0, 8)
hossz.grid(row=1, column=1)

szamjegy = BooleanVar()
szamjegy_pipa = Checkbutton(ablak, text='Kell szamjegy?', variable=szamjegy)
szamjegy_pipa.grid(row=2, column=0)

irasjel = BooleanVar()
irasjel_pipa = Checkbutton(ablak, text='Kell írásjel?', variable=irasjel)
irasjel_pipa.grid(row=2, column=1)

jelszo_ertek = Text(ablak, height=1, width=15, state=DISABLED)
jelszo_ertek.grid(row=0, column=1)

lezaro_gomb = Button(ablak, text='Bezárás', command=ablak.destroy)
lezaro_gomb.grid(row=3, column=1)

jelszo_gomb = Button(ablak, text='Generálás', command=jelszokiiras)
jelszo_gomb.grid(row=3, column=0)


mainloop()
