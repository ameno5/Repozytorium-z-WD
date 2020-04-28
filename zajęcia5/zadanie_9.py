# zadanie7 jako

def Parzyste(dane):
    for index in range(0, len(dane)):
        if index % 2 == 0:
            yield dane[index]
tekst = Parzyste("Konstantynopolitańczykowianeczka")
print(next(tekst))
print(next(tekst))