op = "divide"
num1 = 20
num2 = 4

match op:
    case "soma":
        result = num1 + num2
    case "subtrai":
        result = num1 - num2
    case "multiplica":
        result = num1 * num2
    case "divide":
        if num2 == 0:
            result = "Erro. divisao por zero"
        else:
            result = num1 / num2
    case _:
        result = "Operacao invalida"

print(result)