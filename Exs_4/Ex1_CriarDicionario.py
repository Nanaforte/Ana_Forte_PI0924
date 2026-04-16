#dicionario guardar todos alunos
alunos = {}


while True:
    nome = input("insira o nome do aluno (ou ENTER para terminar): ")
    if nome == "":
        break

    idade=int(input("Idade: "))
    curso=input("Curso: ")

    #chave principal = nome do aluno
    #dentro outro dic com idade e curso
    alunos[nome] = {
        "idade": idade,
        "curso": curso
    }
print("\ndados guardados\n")

#percorrer o dici
for nome, dados in alunos.items():

    print(f"nome: {nome}")
    print(f"idade: {dados['idade']}")
    print(f"curso: {dados['curso']}")
    print()