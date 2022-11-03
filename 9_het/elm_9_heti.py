import string
import random
from tkinter import *

print(string.digits)
print(random.randint(1, 6))

ablak = Tk()
ablak.title('Próba')
ablak.minsize(400, 300)

szoveg = Label(ablak, text='Szia!')
gomb = Button(ablak, text='OK', command=ablak.destroy)

szoveg.pack()
gomb.pack()
mainloop()