ano=int(input("insira o ano"))

if (ano%400==0):
    print("o ano é bissexto")

elif (ano%100==0):
    print("o ano não é bissexto")
elif(ano%4==0):
    print(" o ano é bissexto")
else:
    print("o ano não é bissexto")
