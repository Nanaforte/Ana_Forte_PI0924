valor = [10, 20, 30]

match valor:
    case int():
        print("Num inteiro")
    case float():
        print("Num decimal")
    case str() if valor.isdigit():
        print("String numérica")
    case str():
        print("String textual")
    case list():
        print("Lista")
    case _:
        print("Tipo desconhecido")