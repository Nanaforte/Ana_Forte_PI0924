"""
produto de luxo = eletronico  preço >  1000 
produto comum = eletrônico <= 1000 
produto alimentar = alimento 
categoria desconhecida caso contrário 
"""

produto={"categoria": "eletrônico", "preco": 1500}

match produto:
    case {"categoria": "eletrônico", "preco": p} if p > 1000:
        print("Produto de luxo")
    case {"categoria": "eletrônico", "preco": p} if p <= 1000:
        print("Produto comum")
    case {"categoria": "alimento"}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")