"""
requisicao GET recebida == GET
requisicao POST com dados validos == POST and conteudo not null
requisicao POST sem dados == POST and conteudo not null
caso contrario == metodo nao suportado 
"""

requisicao = {"metodo": "POST", "conteudo": ""}

match requisicao["metodo"]:
    case "GET":
        result = "Requisição GET recebida"
    case "POST":
        if requisicao["conteudo"]:
            result="Requisição POST com dados válidos"
        else:
            result="Requisição POST sem dados"
    case _:
        result = "Método não suportado"
print(result)