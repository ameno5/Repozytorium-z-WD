class Parzyste:

def __init__(self, imie):
        self.imie= imie
        self.index = 0
def zwroc_imie(self):
        return self.imie
def __next__(self):
        index = self.index
        self.index +=2
        if(self.index > len(self.imie)+1):
            raise StopIteration
        else:
            return self.imie[index]

wyraz = Parzyste("michał")
print(next(wyraz))