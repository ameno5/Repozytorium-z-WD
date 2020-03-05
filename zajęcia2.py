import math as m
# git push -u origin master

print(list(range(5)))
[0, 1, 2, 3, 4]
print(list(range(10, 0, -2)))
print(list(range(0, -10, -2)))


imie = "Małgorzata"
print(imie[0::2])

# Zadanie 1
# zdanie - input("Podaj Zdanie: ")
# print(zdanie)
# print(zdanie.count(' '))

# zadanie 2
import sys
a = input("Podaj wartość a: ")
b = input("Podaj wartość b: ")
wynik = int(a) * int(b)
s = sys.stdin.readline()
print("wynik to: " +s)
sys.stdout.write(s)
