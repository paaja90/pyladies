def smycka():
    for animal in animals:
        print(animal +' je '+ animals[animal]+'.')
#1
animals = {'Šedivec':'vlk','Amalka':'ještěrka','Drákula':'netopýr'}
smycka()
#2
animals['Amalka'] = 'koza'
smycka()
#3
animals['Bystrouška'] = 'liška'
smycka()