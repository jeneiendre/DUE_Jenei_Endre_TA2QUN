import string
import random


class Jelszoobjektum():
    jelszo = ''
    jelszohossz = None
    kell_szamjegy = None
    kell_irasjel = None

    def __init__(self):
        self.jelszohossz = 8
        self.kell_szamjegy = True
        self.kell_irasjel = False

    def jelszogeneralas_alap(self):
        self.jelszo = '123456'

    def jelszogenerator(self):
        karakterlista = string.ascii_letters
        if self.kell_szamjegy:
            karakterlista = karakterlista + string.digits
        if self.kell_irasjel:
            karakterlista = karakterlista + string.punctuation

        for _ in range(self.jelszohossz):
            karakter = karakterlista[random.randint(0, len(karakterlista) - 1)]
            self.jelszo = self.jelszo + karakter


if __name__ == '__main__':
    pwd = Jelszoobjektum()
    pwd.jelszohossz = 15
    pwd.kell_irasjel = True
    pwd.jelszogenerator()

    print(pwd.jelszo)
    print(pwd.jelszohossz)
    print(pwd.kell_szamjegy)
    print(pwd.kell_irasjel)
