import random
import string

def jelszogenerator(jelszohossz, kell_szamjegy, kell_irasjel):
    jelszo = ''
    karakterlista = string.ascii_letters
    if kell_szamjegy:
        karakterlista = karakterlista + string.digits
    if kell_irasjel:
        karakterlista = karakterlista + string.punctuation

    for _ in range(jelszohossz):
        karakter = karakterlista[random.randint(0, len(karakterlista) - 1)]
        jelszo = jelszo + karakter
    return jelszo

if __name__ == '__main__':
    print(jelszo)
