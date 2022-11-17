import string
import random


class Jelszoobjektum():
    jelszo = ''
    jelszohossz = None
    van_szamjegy = None
    van_irasjel = None

    def __init__(self):
        self.jelszohossz = 5
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

class Szemely(Jelszoobjektum):
    def __init__(self):
        super().__init__()
        self.nev = ''
        self.kor = 0
        self.email = ''

    def email_ellenorzese(self, email):
        if '@' not in email:
            print('Nem jó az e-mail')


class Dolgozok(Szemely):
    def __init__(self):
        super().__init__()
        self.reszleg = ''
        self.beosztas = ''
        self.fizetes = ''


if __name__ == '__main__':
    dolgozo1 = Dolgozok()
    print(dolgozo1.nev, dolgozo1.kor, dolgozo1.email, dolgozo1.reszleg, dolgozo1.beosztas, dolgozo1.fizetes)
    dolgozo1.jelszohossz = 15
    dolgozo1.jelszogenerator()
    print(dolgozo1.jelszo)

    dolgozo1.email_ellenorzese(dolgozo1.email)



    # pwd = Jelszoobjektum()
    # pwd.van_irasjel = True
    # pwd.jelszogenerator()
    #
    # print(pwd.jelszo)
    # print(pwd.jelszohossz)
    # print(pwd.van_szamjegy)
    # print(pwd.van_irasjel)
