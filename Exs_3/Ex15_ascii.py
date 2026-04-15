i = 0

#ate 255
while i<=255:
    #mostra 20 codigos de cada vez
    for j in range(21):
        if i > 255:
            break

        #mostra o codigo e o caracter correspondente
        print(i, "-", chr(i))

        #passa para o prox codigo ASCII
        i += 1

    continuar = input("continuar? (s/n): ").lower

    if continuar != "s":
        break