def par(n):
    if n%2 == 0:
        print ("o número é par")
        return 1
    else:
        print ("o número é impar")
        return 0

def semaforo(cor):
    if cor == "vermelho":
        print (" passagem prohibida")
        return 1
    if cor == "amarelo":
        print ("transição para vermelho")
        return 1
    if cor == "verde":
        print ("passagem autorizada")
        return 1
    else:
        print ("cor invalida")
        return 0

def fact_w (n):
    resultado=1
    while n>1:
        resultado=resultado* (n)
        n=n-1
    return resultado

def fact_f (n):
    resultado=1
    for i in range (n,1,-1):
        resultado=resultado* (i)
    return resultado 

def fact_r(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact_r(n-1)

def c_lista(lista):
    
    soma = 0
    quantidade=0
    
    for i in lista:
        soma = soma +numeros
        quantidade = quantide + 1

    media = soma / quantide
    return quantidade, soma, media
        

def val_nif(nif):
    if len(nif) != 9 or not nif.isdigit():
        return 0
    
    soma = sum(int(nif[i]) * (9 - i) for i in range(8))
    check_digit = 11 - (soma % 11)
    
    if check_digit >= 10:
        check_digit = 0
    
    return 1 if check_digit == int(nif[-1]) else 0
