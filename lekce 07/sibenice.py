import random
from vyhodnoceni_sibenice import vyhodnoceni

slova_seznam = ['slunce','zidle','rajce']

def tah():
    slovo = random.choice(slova_seznam)
    pocet_pokusu = 0
    pocatecni_stav = '-'* len(slovo)
    while '-' in pocatecni_stav:
        pismeno = input('Zadej písmeno:') 
        if pismeno in slovo:
            pocatecni_stav = pocatecni_stav[:slovo.index(pismeno)] + pismeno + pocatecni_stav[slovo.index(pismeno) + 1:]
            print(pocatecni_stav)
        else:
            pocet_pokusu = pocet_pokusu + 1
            if pocet_pokusu == 10:
                print(vyhodnoceni(pocet_pokusu))
                print('Konec. Prohrála jsi!')
                break
            print(vyhodnoceni(pocet_pokusu))
            print(pocatecni_stav)
            print('Špatně. Zadej dalsi pismeno:')
    if slovo == pocatecni_stav:
        print('Vyhrála jsi! Gratuluji!')
tah()