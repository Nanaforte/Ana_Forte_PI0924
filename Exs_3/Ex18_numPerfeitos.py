limite = int(input("Insira um número limite: "))

contador_perfeitos=0

for num in range(1, limite + 1):

    soma_divisores=0

    for i in range(1, num):
        if num % i == 0:
            soma_divisores+=i

    if soma_divisores == num:
        contador_perfeitos+=1

print("Quantidade de números perfeitos:", contador_perfeitos)