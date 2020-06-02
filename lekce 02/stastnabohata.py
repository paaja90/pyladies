print('Odpovídej "ano" nebo "ne".')
stastna = input('Jsi šťastná?')
bohata = input('Jsi bohatá?')
if stastna == 'ano':
    if bohata == 'ano':
        print('Gratuluji!')
    elif bohata == 'ne':
        print('Zkus míň utrácet.')
elif stastna == 'ne': 
    if bohata == 'ne':
        print('To je mi líto:(')
    elif bohata == 'ano':
        print('Zkus se víc usmívat.')
else:
    print('Nerozumím')

