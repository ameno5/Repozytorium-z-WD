with open("zadanie3.txt", "w") as plik:
    plik.writelines("Zadanie3 z Wizualizacji danych")
with open("zadanie3.txt", "r") as zadanie3_txt:
    for linia in zadanie3_txt:
        print(linia, end="")