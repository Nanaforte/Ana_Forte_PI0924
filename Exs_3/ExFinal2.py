clientes = []  #lista clientes

#func para calcular o valor final com desconto
def calcular_valor_final(compra): 
    if 100<= compra <=200:  #100 a 200
        desconto=compra *0.05  #5%
    elif 200< compra <500:  #200 a 500
        desconto=compra *0.10  #10%
    elif compra >=500:  #>= 500
        desconto=compra *0.15  #15%
    else:  #n desconto
        desconto=0 

    return compra-desconto  

#func inserir cliente
def func_inserir_cliente():  
    numcliente = len(clientes) + 1  #num automatico cliente    len-quantos tem na lista
    nome = input("Nome: ")
    morada = input("Morada: ")
    tel = input("Telefone: ")
    nif = input("NIF: ")
    compra = float(input("Compra: "))

    valor_final=calcular_valor_final(compra)

    cliente=[numcliente, nome, morada, tel, nif, compra, valor_final]  #lista do cliente

    clientes.append(cliente)  #append add a lista
    print("cliente guardado")

#func para listar clientes
def func_listar(): 
    for i in clientes: 
        print("\nCliente nº", i[0])
        print("Nome:", i[1])
        print("Morada:", i[2])
        print("Telefone:", i[3])
        print("NIF:", i[4])
        print("Compra:", i[5])
        print("Divisão final:", i[6])
        input("ENTER para próximo...")

#func para procurar cliente
def func_procurar():  
    num=int(input("numero do cliente: "))

    for i in clientes:  
        if i[0]==num:
            print("ENCONTRADO")
            print("Nome:", i[1])
            print("Morada:", i[2])
            print("Telefone:", i[3])
            print("NIF:", i[4])
            print("Compra:", i[5])
            print("Valor final compra:", i[6])
            return
    print("cliente nao encontrado")
    
#menu
while True:
    print("\n1 - Inserir")
    print("2 - Listar")
    print("3 - Procurar")
    print("0 - Sair")

    op=int(input("Opção: "))

    if op==1:
        func_inserir_cliente()
    elif op==2:
        func_listar()
    elif op==3:
        func_procurar()
    elif op==0:
        break
    else:
        print("invalido")