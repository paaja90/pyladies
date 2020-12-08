from random import randrange

tah_cloveka = input('kámen, nůžky, papír nebo konec? ')
cislo = randrange(3)

if cislo == 0:
    tah_pocitace = 'kámen'
elif cislo == 1:
    tah_pocitace = 'nůžky'
else:
    tah_pocitace = 'papír'

while True: 
    if tah_cloveka == 'kámen'and tah_pocitace == 'nůžky' or tah_cloveka == 'nůžky' and tah_pocitace == 'papír' or tah_cloveka == 'papír' and tah_pocitace == 'kámen':
        print('Vyhrál jsi. Volba počítače byla:', tah_pocitace)
        tah_cloveka = input('kámen, nůžky, papír nebo konec? ')
    elif tah_cloveka == 'nůžky' and tah_pocitace == 'kámen' or tah_cloveka == 'kámen' and tah_pocitace == 'papír' or tah_cloveka == 'papír' and tah_pocitace == 'nůžky':
        print('Počítač vyhrál. Volba počítače byla:', tah_pocitace)
        tah_cloveka = input('kámen, nůžky, papír nebo konec? ')
    elif tah_cloveka == tah_pocitace:
        print('Plichta! Volba počítače byla:', tah_pocitace)
        tah_cloveka = input('kámen, nůžky, papír nebo konec? ')
    elif tah_cloveka == 'konec':
        print('Konec! Nashledanou příště :)')
        break   
    else:
        print('Nerozumím.')
        tah_cloveka = input('kámen, nůžky, papír nebo konec? ')
