#cislo = '905226/4496'
#a format
def spravny_format(cislo):
    rozdelene_cislo = cislo.split('/')
    if len(rozdelene_cislo[0]) == 6 and len(rozdelene_cislo[1]) == 4 and cislo[6] == '/':
        return True
    else:
        return False

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

datum_narozeni('905226/4496')
spravny_format('905226/4496')
delitelnost('905226/4496')
pohlavi('905226/4496')

