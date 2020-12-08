def ano_nebo_ne(otazka):
    "Vrátí True nebo False, podle odpovědi uživatele"
    while True:
        odpoved_1 = input(otazka)
        odpoved = odpoved_1.strip()
        if odpoved.lower() == 'ano' or odpoved.lower() == 'a' :
            return True
        elif odpoved.lower() == 'ne'or odpoved.lower() == 'n':
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne".')

if ano_nebo_ne('Chceš si zahrát hru? '):
    print('OK! Ale napřed si ji musíš naprogramovat.')
else:
    print('Škoda.')