from random import randrange
import util
def tah_pocitace(herni_pole):
    while True:
        cislo_policka = (randrange(0,19))
        if herni_pole[cislo_policka] == '-':
            return util.tah(herni_pole, cislo_policka, symbol='o')
            break
        else:
            cislo_policka = (randrange(0,19))
