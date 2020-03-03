def paty_pad(jmeno):
    return jmeno[:-1] + 'o'

def pozdrav(jmeno):
    print('Hello,', paty_pad(jmeno))
    print('How are you?')
pozdrav(input('Zadej sve jmeno:'))

jmena = ['Anna','Katka','Veronika']
for jmeno in jmena:
    pozdrav(jmeno)


for cislo in range(8):
    print("Už nikdy nebudu házet igelit do táboráku!")
