import string
import random


class Jelszoobjektum():
    jelszo = ''
    jelszohossz = None
    van_szamjegy = None
    van_irasjel = None

    def __init__(self):
        self.jelszohossz = 8
        self.van_szamjegy = True
        self.van_irasjel = False

    def jelszo_alap(self):
        self.jelszo = '123456'

    def jelszogenerator(self):
        karakterlista = string.ascii_letters
        self.jelszo = ''
        if self.van_szamjegy:
            karakterlista = karakterlista + string.digits
        if self.van_irasjel:
            karakterlista = karakterlista + string.punctuation
        for _ in range(self.jelszohossz):
            self.jelszo = self.jelszo + karakterlista[random.randint(0, len(karakterlista) - 1)]

#class Felhasznalo(Jelszoobjektum):


if __name__ == '__main__':
    pwd = Jelszoobjektum()
    pwd.van_irasjel = True
    pwd.jelszogenerator()

    print(pwd.jelszo)
    print(pwd.jelszohossz)
    print(pwd.van_szamjegy)
    print(pwd.van_irasjel)
