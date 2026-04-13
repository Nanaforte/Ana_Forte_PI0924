num1=int(input("Introduza o valor do num1: "))
num2=int(input("Introduza o valor do num2: "))
num3=int(input("Introduza o valor do num3: "))

#   50     40       50     20       40     20       
if num1 > num2 and num1 > num3 and num2 > num3:
    print(f"\nCrescente: {num3}, {num2}, {num1}")
    print(f"Decrescente: {num1}, {num2}, {num3}")

#     50     40       50     20       40      20
elif num2 > num1 and num2 > num3 and num1 > num3:
    print(f"\nCrescente: {num3}, {num1}, {num2}")
    print(f"Decrescente: {num2}, {num1}, {num3}")

#     50     40       50     20       40      20
elif num3 > num1 and num3 > num2 and num1 > num2:
    print(f"\nCrescente: {num2}, {num1}, {num3}")
    print(f"Decrescente: {num3}, {num1}, {num2}")