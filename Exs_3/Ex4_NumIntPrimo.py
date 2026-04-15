"""
num<2  nao é primo
"""

num = int(input("Insira um número: "))

if num<2:
    print("Não é primo")
else:
    #percorre os valores até ao num inserido para ver se os mesmo sao divisiveis pelo proprio num
    for i in range(2, num):
        if num % i == 0:
            #se for divisivel por outro num alem de 1 e ele proprio n e primo
            print("Não é primo")
            break

    else:
        print("É primo")