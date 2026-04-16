palavra = input("insira uma palavra: ")

#dic para contagens
contador={}

#cada letra da palavra
for letra in palavra:
    #se letra existe 
    if letra in contador:
        #+1
        contador[letra]+=1
    else:
        #se n cria a chave com valor 1
        contador[letra] = 1
print(contador)