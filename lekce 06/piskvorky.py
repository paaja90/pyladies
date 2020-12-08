from random import randrange

def vyhodnot(herni_pole): 
    if 'xxx' in herni_pole:
        return 'x'   #Vyhrál hráč s křížky 
    elif 'ooo' in herni_pole:
        return 'o'   #Vyhrál hráč s kolečky
    elif '-' not in herni_pole:
        return '!'   #nikdo nevyhrál
    else:
        return '-'  #hra ještě neskončila

def tah(herni_pole, cislo_policka, symbol):   #Vrátí herní pole s daným symbolem umístěným na danou pozici
    herni_pole = herni_pole[:cislo_policka] + symbol + herni_pole[cislo_policka + 1:]
    return herni_pole

def tah_hrace(herni_pole):
    while True: 
        try: 
            cislo_policka = int(input('Vyber číslo 0-19, pro tvůj další tah:'))
        except ValueError:
            print('Toto nevypadá jako číslo, zkus to znova!')
        else:
            if cislo_policka < 0 or cislo_policka >= len(herni_pole):
                print('Hrací pole je velké pouze od 0 do 19 pozic!')
            elif herni_pole[cislo_policka] != '-':
                print('Toto políčko je již obsazené!')
            else:
                return tah(herni_pole, cislo_policka, symbol='x')
                break

def tah_pocitace(herni_pole):
    while True:
        cislo_policka = (randrange(0,19))
        if herni_pole[cislo_policka] == '-':
            return tah(herni_pole, cislo_policka, symbol='o')
            break
        else:
            cislo_policka = (randrange(0,19))

def piskvorky():
    herni_pole = '-'*20
    vyhodnot(herni_pole)
    pocet_kol = 0
    while True:
        if vyhodnot(herni_pole) == '-':
            herni_pole = tah_hrace(herni_pole)
            pocet_kol = pocet_kol + 1 
            print(str(pocet_kol)+'.kolo', herni_pole)
            herni_pole = tah_pocitace(herni_pole)
            pocet_kol = pocet_kol + 1
            print(str(pocet_kol)+'.kolo', herni_pole)
        elif vyhodnot(herni_pole) == 'x':
            print('Vyhrál hráč s křížky')
            break
        elif vyhodnot(herni_pole) == 'o':
            print('Vyhrál hráč s kolečky')
            break
        elif vyhodnot(herni_pole) == '!':
            print('Remiza')
            break

piskvorky()
    
