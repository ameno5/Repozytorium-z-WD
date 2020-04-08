import math

def suma(a1=1, r=1, ile_elementow=10):
    ostatniwyraz = a1+(ile_elementow-1)*r
    return ((a1 + ostatniwyraz)/2)*ile_elementow
print(suma())