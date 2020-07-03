
strana2 = input('Zadej delku strany:')
strana = int(strana2) #chceš li načíst desetinné číslo, použij funkci 'float'#
cislo_je_spravne = strana > 0 
#strana = float(strana2)#
obvod = 4*strana
obsah = strana*strana
str(obvod)
str(obsah) #komentar#

if cislo_je_spravne:
    print('Obvod ctverce se stranou', strana, 'cm je', str(obvod) + ' cm')
  print('Obsah ctverce se stranou' , strana, 'cm je', str(obsah) +' cm2')
else: 
    print('Strana musí být kladná, jinak z toho nebude čtverec!')
print('Děkujeme za použití kalkulačky')



