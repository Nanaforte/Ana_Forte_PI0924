num1=int(input("Introduz o 1 num: "))
num2=int(input("Introduz o 2 num: "))

if num1 > num2:  
    print(f"\nCrescente: {num2}, {num1}")
    print(f"Decrescente: {num1}, {num2}")
else:
    print(f"Crescente: {num1}, {num2}")
    print(f"Decrescente: {num2}, {num1}")