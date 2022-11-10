from tkinter import *

win = Tk()
win.title('Példa ablak')
win.geometry('400x200')
win.minsize(200, 100)

valtozo = StringVar()
valtozo.set('Ez egy változó szöveg')
Label(win, text=valtozo, fg='blue').pack()
Label(win, text='Ez egy másik szöveg').pack()

Button(win, text='Bezárás', command=win.destroy).pack()

mainloop()