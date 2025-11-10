def fact (n):
    if n == 1:
        return 1
    return n * fact(n-1)

def soma(num1, num2):
    if num2 == num1:
        return num1
    return num2 + soma(num1, num2-1)

def mult(mult1, mult2):
    if mult2 == 0 or mult1 == 0:
        return 0
    return mult1 + mult(mult1, mult2-1)

def Pot(base, exp):
    if exp==1:
        return base
    return base * Pot(base, exp-1) 

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def transporte (c, origem, destino, auxiliar):
    if c == 1:
        print(f'caixa {c} ► {origem} → {destino}')
    else:
        transporte(c-1, origem, auxiliar, destino)
        print(c)
