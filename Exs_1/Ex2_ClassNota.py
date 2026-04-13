def def_intervalo(classf):
    classf=classf.lower()

    match classf:
        case "excelente":
            return "90 ou mais"
        case "bom":
            return "70 - 89"
        case "suficiente":
            return "50 - 69"
        case "insuficiente":
            return "Abaixo de 50"
        
classificacao=input("Escreva a classificacao (excelente, bom, suficiente, insuficiente): ")

intervalo=def_intervalo(classificacao)
print(intervalo)