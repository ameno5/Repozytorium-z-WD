def zakupy(** produkt):
    suma=0
    for cos in produkt:
        suma = suma + produkt[cos]
        print(suma)
zakupy(ser=1, piwo=2, chipsy=3)