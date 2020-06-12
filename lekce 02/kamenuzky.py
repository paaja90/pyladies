from random import randrange
cislo = randrange(3)
if cislo == 0:
    tah_pocitace = 'kámen'
elif cislo == 1:
    tah_pocitace = 'nůžky'
else:
    tah_pocitace = 'papír'

tah_cloveka = input('kámen, nůžky, nebo papír? ')

if tah_cloveka == 'kámen'and tah_pocitace == 'nůžky' or tah_cloveka == 'nůžky' and tah_pocitace == 'papír' or tah_cloveka == 'papír' and tah_pocitace == 'kámen':
    print('Vyhrál jsi')
elif tah_cloveka == 'nůžky' and tah_pocitace == 'kámen' or tah_cloveka == 'kámen' and tah_pocitace == 'papír' or tah_cloveka == 'papír' and tah_pocitace == 'nůžky':
    print('Počítač vyhrál.')
elif tah_cloveka == tah_pocitace:
    print('Plichta!')
   
else:
    print('Nerozumím.')
print('Volba počítače byla:', tah_pocitace)