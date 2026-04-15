soma = 0

contador = 0

while contador<30:

    num=int(input("insira um numero entre 1 e 50: "))

    if num < 1 or num > 50:
        print("numero invalido. tente novamente.")
    
    #ver se e par
    elif num % 2 == 0:
        soma+=num      
        contador+=1   
    else:
        print("Nao e par. tente novamente.")

media=soma/30

print("Media dos 30 números pares:", media)