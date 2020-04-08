skroty = {'jablka' : "sztuki", 'woda' : "litry", 'pistacje' : "kg"}

produkty = [i for i in skroty if skroty[i] == "sztuki"]
print(produkty)