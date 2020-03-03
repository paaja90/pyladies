def podil_a_zbytek(a,b):
    podil = a // b
    zbytek = a % b

    return podil, zbytek

print(podil_a_zbytek(13,4))



ruka = [(2, 'piky'), (10, 'kříže'), (8, 'káry')]

for karta in ruka:
    hodnota, barva = karta
    print ('mam', hodnota, 'barvy', barva)

veci = ['tráva', 'slunce', 'mrkev', 'řeka']
barvy = ['zelená', 'žluté', 'oranžová', 'modrá']
mista = ['na zemi', 'nahoře', 'na talíři', 'za zídkou']

for vec, barva, misto in zip(veci, barvy, mista):
    print(barva, vec, 'je', misto)

slovnik = {'Jablko': 'Apple', 'Knoflik': 'Button', 'Mys' : 'Mouse'}
print(slovnik)
