zvirata = ['kocka', 'had', 'kralik', 'pes']
zvirata.append('andulka')
# šlo to udělat i jednodušeji, ale to asi nebylo cílem zadání, že?
#def second_char(zvire):
#    return zvire[1]
#zvirata.sort(key=second_char)
#print(zvirata)

slovnik = {} # slovnik, kde klíč je druhé písmeno slova a hodnota je slovo
for zvire in zvirata:
    druhe_pismeno = zvire[1]
    slovnik[druhe_pismeno] = zvire
print(slovnik)

l_slovnik = list(slovnik) # jelikož se nedá slovník seřadit (nebo dá? google nic neporadil :D) tak převádím na seznam
l_slovnik.sort()
print(l_slovnik)

slovnik_2 = {} # po sežazení seznamu, převádím zpět na slovník, aby se dostala k původním slovům
for i in l_slovnik:
    if i in slovnik:
        slovnik_2[i] = slovnik[i]
print(slovnik_2)

hodnoty = slovnik_2.values()
print(hodnoty)

