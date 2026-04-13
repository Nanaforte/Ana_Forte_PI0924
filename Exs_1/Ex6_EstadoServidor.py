servidor = {"status": "ok", "tempo_resp": 350}

match servidor:
    case {"status": "erro", **resto}:
        resultado = "servidor indisponível"

    case {"status": "ok", "tempo_resp": tempo}:
        if tempo > 200:
            resultado = "servidor lento"
        else:
            resultado = "servidor ativo"

    case _:
        resultado = "estado desconhecido"

print(resultado)