import math

def ciag(* liczby):
    if len(liczby) == 0:
        return 0
    else:
        iloczyn = 1
        for i in liczby:
            iloczyn = iloczyn*i
    return iloczyn
print(ciag())
print(ciag(2,6,10,14))