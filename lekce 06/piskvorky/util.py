def tah(herni_pole, cislo_policka, symbol):   #Vrátí herní pole s daným symbolem umístěným na danou pozici
    herni_pole = herni_pole[:cislo_policka] + symbol + herni_pole[cislo_policka + 1:]
    return herni_pole