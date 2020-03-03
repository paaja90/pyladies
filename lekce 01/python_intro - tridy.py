class Kotatko:
    def zamnoukej(self):
        print(self.jmeno + ': Mnaaau!')

mourek = Kotatko()

mourek.jmeno = 'Mourek'
print(mourek.jmeno)
mourek.zamnoukej()

micka = Kotatko()
micka.jmeno = 'Micka'
print(micka.jmeno)
micka.zamnoukej()
