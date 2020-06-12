cislo = input('Zadej rodné číslo:')
while True: 
    if cislo.isalpha(): #ověří, zda uživatel nezadal písmena
        print('Rodné číslo neobsahuje pismena')
        cislo = input('Zadej rodné číslo znovu:')
    elif len(cislo) == 11: #mělo by obsahovat 11 znaků a splňovat 3 podmínky viz ř.8 
        rozdelene_cislo = cislo.split('/')
        if len(rozdelene_cislo[0]) == 6 and len(rozdelene_cislo[1]) == 4 and cislo[6] == '/': #pokud podmínky platí, ověříme zda je RD dělitelné 11ti 
            bez_lomitka = rozdelene_cislo[0] + rozdelene_cislo[1]
            licha_mista = bez_lomitka[::2]
            suda_mista = bez_lomitka[1::2]
            soucet_licha = 0
            for i in licha_mista:
                soucet_licha = soucet_licha + int(i)
            soucet_suda = 0
            for i in suda_mista:
                soucet_suda = soucet_suda + int(i)
            if soucet_licha - soucet_suda %11: #rozdil cisel na liche a sude pozici je dělitelny 11, takže RD je dělitelné 11ti. 
                print('Správně zadané rodné číslo!')
            break
    else:
        print('Špatně zadané rodné číslo') # pokud uživatel zadá čísla ale v nespravnem formatu, vytiskne se toto. 
        cislo = input('Zadej rodné číslo znovu:')