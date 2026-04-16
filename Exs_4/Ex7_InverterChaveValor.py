d={'a':1, 'b':2, 'c':3}

invertido={}

for chave,valor in d.items():
    """
    invertido[1] = 'a'
    invertido[2] = 'b'
    invertido[3] = 'c'
    """
    invertido[valor]=chave
print(invertido)