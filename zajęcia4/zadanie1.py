import random

A = [random.randint(0, 100) for i in range(20) ]
B = [x for x in A if x % 4 == 0]

plik = open("zadanie1.txt", "w")
plik.writelines(str(B))
plik.close()