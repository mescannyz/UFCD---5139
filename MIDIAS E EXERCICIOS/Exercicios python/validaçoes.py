str="abcd.pt"

len (str)

for i in str:
    i>="0" and i<="9"
    i in range (10)
    i>="a" and i>="z"

def v_nome(nome):

    val=0
    
    if len (nome) <6:
        print ("o nome está vazio")
        return val
    
    if not (nome.isalpha() or ' ' in nome):
        print ("caracter não alfabeticos ou espaço")
        return (val)
    
    if not ' ' in nome:
        print ("não tem espaço")
        return val
    print ("tudo ok")
    val=1
    return val

def v_email_iefp(email):
    val=0
    if email [-17]!= "formacao.iefp.pt":
        print (" terminação incorreta")
        return val
    print (email.index("@"))
    print (email[:email.index("@")])
    if notemail[:email.index("@")].isdigit():
        print ("caracter incorretos no 'user'")
        return val
    print ("tudo ok")
    val =1
    return val

def val_tlf (telefone):
    val=0
    if not len (telefone)==9:
        print ("comprimento inválido")
        return val
    if not telefone.isdigit():
        print("tem caracteres inválidos")
        return val
    print (telefone[0])
    if not (telefone[0] =="2" or telefone[0]=="9"):
        print ( "primeiro digito inválido")
        return val
    print ("tudo ok")
    val=1
    return val

def val_cp (codpostal):
    val=0
    if not len (codpostal)==8:
        print("comprimento inválido")
        return val
    print (codpostal[:4])
    if not codpostal[:4].isdigit():
        print ("carcacter inválidos no código")
        return val
    print (codpostal[4])
    if codpostal [4]!="-":
        print ("caracter separador inválido")
        return val
    print(codpostal[5:])
    if not codpostal [5:].isdigit():
        print("caracter inválidos na extensão")
        return val
    print("tudo ok")
    val=1
    return val

def check_ISBN(ISBN):
    
    if len(ISBN) != 13 or not ISBN.isdigit():
        print("Nao tem 13 digitos")
        return 0

    soma=0
    for  i in range (len(ISBN)):
        if i%2==0:
            soma=soma+int(ISBN[i])*1
        else:
            soma=soma+int(ISBN[i])*3
        print (soma)
    
        print("O ISBN está correto")
        return 1
    else :
        print("ISBN não está correto")
        return 0
   



    







    
