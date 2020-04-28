class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)

class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, pensja):
    osoba.__init__(self, imie, nazwisko)
        self.pensja = pensja
    def przedstaw_sie(self):
        return "{} {}, jestem pracownikiem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

class Menadzer(Pracownik):
    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

Jozek = Pracownik("Józek", "Bajka", 2000)
Adrian = Menadzer("Adrian", "Mikulski", 12000)
print(isinstance(Jozek, Pracownik))
print(isinstance(Adrian, Pracownik))
print(issubclass(Pracownik, Osoba))
print(issubclass(Osoba, Pracownik))
print(issubclass(Menadzer, Pracownik))
print(issubclass(Osoba, Menadzer))