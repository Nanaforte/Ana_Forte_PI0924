d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
novo_dicionario = {}

for chave, valor in d1.items():
    novo_dicionario[chave] = valor

for chave, valor in d2.items():
    novo_dicionario[chave] = valor

print(novo_dicionario)