import math 
def proste(a1,a2):
    if(a1==a2):
        print("proste rownolegle")
    elif(a1*a2==-1):
        print("proste prostopadle")
    else:
        print("Nie sa rownolegle ani prostopadle")

a1=input("Podaj a1 z rownania y=a1x+b1")
a1=int(a1)

a2=input("Podaj a2 z rownania y=a2x+b2")
a2=int(a2)

print(proste(a1,a2))