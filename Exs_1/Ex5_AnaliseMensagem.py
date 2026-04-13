mensagem = "Tudo bem?"
msg=mensagem.lower()

match msg.lower():
    case "olá" | "ola" | "bom dia" | "Hello" | "Hi" | "oi" | "boa tarde":
        print("Saudação")
    case _ if msg.endswith("?"):
        print("Pergunta")
    case _ if msg in ("tchau", "xau", "adeus", "até logo", "ate logo","bye", "goodbye"):
        print("Despedida")
    case _:
        print("Mensagem genérica")