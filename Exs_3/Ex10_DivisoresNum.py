num=int(input("Insira um numero: "))

contador=0

for i in range(1, num + 1):   #+1 para contar com o ultimo numero, o num inserido neste caso
    if num % i == 0:
        contador+=1

print("quantidade de divisores:",contador)