num1=int(input("Introduz o 1 num: "))
num2=int(input("Introduz o 2 num: "))
num3=int(input("Introduz o 3 num: "))

maior=num1
menor=num1

if num2>maior:
    maior=num2
if num2<menor:
    menor=num2

if num3 > maior:
    maior = num3
if num3 < menor:
    menor = num3

print("maior:",maior)
print("menor:",menor)