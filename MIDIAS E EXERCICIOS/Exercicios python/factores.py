n=int(input("insira o númerodo qual quer saber o factoriar"))

resultado=n

while n>1:
    
    resultado=resultado*(n-1)
    n=n-1
    
print("o resultado é", resultado)
