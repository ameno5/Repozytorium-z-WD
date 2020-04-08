def monotonicznosc(a):
    if(a > 0):
        print("rosnie")
        return 0
    elif(a < 0):
        print("maleje")
        return 0
    else:
        print("stala")
        return 0

a=input("Podaj wartosc a z y=ax+b")
a=int(a)
print(monotonicznosc(a))