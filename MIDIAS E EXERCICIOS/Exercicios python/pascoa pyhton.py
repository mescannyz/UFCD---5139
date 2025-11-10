ano=int(input("insira o ano que quer saber:"))

x=24
y=5
a=ano%19
b=ano%4
c=ano%7

d=((19*a)+x)%30
e=((2*b)+(4*c)+(6*d)+y)%7
if (d+e)<10:
    print("o dia é:",d+e22,"de março")
else:
    print("o dia é", d+e-9, "de abril")
    
    
