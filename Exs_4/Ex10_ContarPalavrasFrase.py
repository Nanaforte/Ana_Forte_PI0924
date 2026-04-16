frase = input("insira uma frase: ")

#divide a frase em palavras
palavras = frase.split()

contador={}

#percorrer cada palavra
for palavra in palavras:
    #palavra ja existe soma 1
    if palavra in contador:
        contador[palavra] += 1
    else:
        #se n cria com valor 1
        contador[palavra] = 1

print(contador)