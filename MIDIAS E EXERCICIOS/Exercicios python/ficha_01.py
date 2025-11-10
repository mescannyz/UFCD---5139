a=5
print (a)

b=7
print (b)

c=a+b
print (c)


idade= int(input("insira a sua idade"))

if idade >= 18:
    print("é maior de idade")
else:
    print ("é menor de idade")

km = int(input("quantos km foram efetuados na viagem"))

gastomedio=float(input("qual é o gasto medio do carro em litros por 100km?"))
precolitro=float(input("qual é o valor do litro de combustivel em €?"))

litrosconsumidos = (km/100)* gastomedio
valorgasto = litrosconsumidos * precolitro

print (litrosconsumidos)
print (valorgasto)

peso = float(input("insira o seu peso"))
altura =float(input("insira a sua altura"))

imc = peso/(altura**2)
print (imc)

if imc<18.5:
    print("abaixo do peso")
if imc>=18.25 and imc<25:
    print("peso adequado")
if imc>=25 and imc<30:
    print("sobrepeso")
if imc>=30:
    print("obesidade")

def factoriala (a):
    resultado=1
    for i in range (a,1-1):
        resultado=resultado*(i)
    return resultado
def factorial (b):
    resultado=b
    while b>1:
        resultado=resultado*(b-1)
        b=b-1
    return resultado

def soma_W(inf, sup):
    resultado = 0
    i = inf
    while i <= sup:
        resultado += i
        i=i+1
    return resultado

def soma_nf(inf, sup):
    resultado = 0
    for i in range(inf,sup+1):
        resultado+=i
    return resultado

def multi (m,n):
    resultado=0
    while n>0:
        resultado=resultado+m
        n=n-1
    return resultado
def mult (m,n):
    resultado=0
    for i in range (n):
        resultado = resultado + m
    return resultado

def potencial_w(b,e):
    resultado = 1
    while e>0:
        resultado=resultado*b
        e=e- 1
    return resultado

def potencial_f(b,e):
    resultado = 1
    for i in range(e):
        resultado=resultado * b
    return resultado


