def spravny_format(cislo):
    while True: 
        if cislo.isalpha(): #tady se mě ty try/except bloky nezdály, když bych tím ověřovala zda zadal integer, tak to neuzná '/' a s tím .isalpha si to nerozumnělo
            print('Rodné číslo neobsahuje pismena')
            cislo = input('Zadej rodné číslo znovu:')
        elif len(cislo) == 11:
            rozdelene_cislo = cislo.split('/')
            while True:   # a tady jsem je teda zkusila použít, ale nefunguje to, protože když zadám nesprávný formát tak vrátí True :D takhle se ten try/except nepoužívá, což? 
                len(rozdelene_cislo[0]) == 6 and len(rozdelene_cislo[1]) == 4 and cislo[6] == '/'
                try:   
                    return True
                except:
                    print('Špatně zadané rodné číslo')
                    return False
        else:
            print('Špatně zadané rodné číslo')  
            cislo = input('Zadej rodné číslo znovu:')

def delitelnost(cislo):
    rozdelene_cislo = cislo.split('/')
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
        return True
    else:
        return False

def datum_narozeni(cislo):
    rok = ''
    if int(cislo[:2]) < 21 and int(cislo[:2]) >= 0:
        rok = 2000 + int(cislo[:2]) 
    else:
        int(cislo[:2]) > 21 and int(cislo[:2]) < 99
        rok = 1900 + int(cislo[:2])
    mesic = ''
    if int(cislo[2:3]) > 12:
        mesic = int(cislo[2:3]) - 50 
    else:
        mesic = int(cislo[2:3])
    den = cislo[4:6]
    print('Datum narození je:',den + '.'+ str(mesic) + '.' + str(rok))

def pohlavi(cislo):
    if int(cislo[2:3]) > 12:
        print('žena')
    else:
        print('muž')


print(spravny_format(input('Zadej rodne cislo:')))
