#funcs verificar num primo
def func_primo(num):
    if num < 2: # nums < 2 n sao primos
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


#func contar num de divisores de um num
def func_contar_divisores(num):
    contador=0
    for i in range(1, num+1):  #percorrer todos os nums de 1 ate x +1contacomele
        if num%i == 0:
            contador+=1  
    return contador


#func verificar se um num perfeito
def func_perfeito(num):
    soma=0
    #soma todos os divisores exclui o proprio num
    for i in range(1, num):
        if num % i == 0:
            soma += i
    return soma==num 



#op 1 
#validacao do valor de entrada
def func_analisar_nums():
    while True:
        try:
            num=int(input("insira um valor (1 a 30000): "))
            if 1<= num <=30000:
                break
            else:
                print("valor fora do intervalo!")
        except:
            print("entrada invalida")

    contador=0  #10 em 10

    #ciclo de 1 ate num
    for i in range(1, num + 1):
        #resultados
        print(f"\nNumero: {i}")
        print(f"Primo: {'sim' if func_primo(i) else 'nao'}")
        print(f"Nº divisores: {func_contar_divisores(i)}")
        print(f"Perfeito: {'sim' if func_perfeito(i) else 'nao'}")

        contador+=1

        #10 em 10
        if contador % 10 == 0:
            op=input("\nquer continuar? (s/n): ").lower()
            if op != 's':
                break


#op 2 - calculadora

def func_calculadora():
    while True:
        print("\nCALCULADORA")
        print("1 - Soma (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("5 - Tabuada")
        print("0 - Voltar")

        op=input("Escolha: ")

        if op == "0":
            break
        elif op in ["1", "2", "3", "4"]:
            try:
                a=float(input("insira primeiro número: "))
                b=float(input("insira segundo número: "))

                if op=="1":
                    print("Resultado:", a+b)
                elif op=="2":
                    print("Resultado:", a-b)
                elif op=="3":
                    print("Resultado:", a*b)
                elif op=="4":
                    if b!=0:
                        print("Resultado:", a/b)
                    else:
                        print("erro, nao da para dividir por zero")
            except:
                print("entrada invalida")

        #op 5 tabuada
        elif op=="5":
            while True:
                try:
                    num=int(input("insira um numero para fazer a tabuada (1 a 1000): "))
                    if 1<= num <=1000:
                        break
                    else:
                        print("fora do intervalo!")
                except:
                    print("entrada invalida")

            contador=0  #20 em 20

            #tabuada ate ao valor introduzido
            for i in range(1, num + 1):
                print(f"{num} x {i} = {num * i}")
                contador+=1
                #pausa 20 em 20 linhas
                if contador%20 == 0:
                    opc=input("\ncontinuar tabuada? (s/n): ").lower()
                    if opc != 's':
                        break
        else:
            print("opcão invalida")


#menu
def func_menu_main():
    while True:
        print("\nMENU PRINCIPAL")
        print("1 - Analisar números")
        print("2 - Calculadora")
        print("0 - Sair")

        op = input("Escolha: ")

        if op=="1":
            func_analisar_nums()
        elif op=="2":
            func_calculadora()
        elif op=="0":
            print("programa terminado.")
            break
        else:
            print("opcão invalida")




func_menu_main()