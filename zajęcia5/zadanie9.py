# zadanie7 jako generator

def Parzyste(dane):
    for index in range(0, len(dane)):
        if index % 2 == 0:
            yield dane[index]
tekst = Parzyste("Mirosława")
print(next(tekst))
print(next(tekst))