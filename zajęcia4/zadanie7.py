class Robaczek:

    def __init__(self, x, y, krok):
        self.x=x
        self.y=y
        self.krok=krok
    def idz_w_gore(self, ilosc):
        self.y+=ilosc*self.krok
    def idz_w_dol(self, ilosc):
        self.y-=ilosc*self.krok
    def idz_w_prawa(self, ilosc):
        self.x+=ilosc*self.krok
    def idz_w_lewa(self, ilosc):
        self.x-=ilosc*self.krok
    def pokaz_gdzie_jestes(self):
        return "x: "+str(self.x)+"; y: "+str(self.y)

    def __del__(self):
        print("usunieto")
    

robaczek=Robaczek(0, 0, 0)
print(robaczek.pokaz_gdzie_jestes())
robaczek.idz_w_gore(1)
robaczek.idz_w_dol(1)
robaczek.idz_w_prawa(2)
robaczek.idz_w_lewa(2)
print(robaczek.pokaz_gdzie_jestes())

    
