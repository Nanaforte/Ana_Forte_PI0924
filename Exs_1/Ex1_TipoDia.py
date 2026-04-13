#Tipo de dia

dia=input("Escreva o nome de um dia da semana: ").lower()

match dia:
    case "sábado" | "sabado" | "domingo":
        print("Fim de semana")
    case "segunda" | "terça" | "terca" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case _:
        print("Dia invalido! Escreva um dia da semana")