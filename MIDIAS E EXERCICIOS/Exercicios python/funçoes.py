def paridade(n):
    if n%2==0:
        return "par"
    else:
        return"impar"

def sinal(n):
    if n==0:
        return"zero"
    
    if n>=0 :
        return"positivo"
    else:
        return "negativo"
    
def resultado(c,f):
    if c==f:
        return "totobola x"
    if c>f:
        return "totobola 1"
    else:
        return "totobola2"
def pascua (ano):
    x=24
    y=5
    a=ano%19
    b=ano%4
    c=ano%7

    d=((19*a)+x)%30
    e=((2*b)+(4*c)+(6*d)+y)%7
     
    if (d+e)<10:
        print("o dia é:",d+e+22,"de março")
    else:
        print("o dia é", d+e-9, "de abril")
        
def anobissexto (ano):

    if (ano%400==0):
        print("o ano é bissexto")

    elif (ano%100==0):
        print("o ano não é bissexto")
        
    elif(ano%4==0):
        print(" o ano é bissexto")
    else:
        print("o ano não é bissexto")

def factorial (n) :
    resultado=1
    for i in range (n,1,-1):
        resultado=resultado* (i)
    return resultado

