num=int(input("Insira um número: "))

contador=0

for i in range(1, num+1):

    soma = num + i
    subtracao = num - i
    multiplicacao = num * i
    if i != 0:
        divisao = num / i

    print(num, "+", i, "=", soma)
    print(num, "-", i, "=", subtracao)
    print(num, "*", i, "=", multiplicacao)
    print(num, "/", i, "=", divisao)
    print("")

    contador+=4

print("Total de operações:", contador)