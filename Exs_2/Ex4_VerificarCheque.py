"""
saldo inicial
valor do cheque

ver se cheque pode ser descontado ou n
saida
dizer se cheque foi descontado ou n e o saldo da conta
"""

saldo_inicial=int(input("Introduza o valor do saldo da sua conta: "))
valor_cheque=int(input("Introduza o valor do cheque: "))

if valor_cheque > saldo_inicial:
    print(f"Cheque não descontado, saldo: {saldo_inicial}")
else:
    novo_saldo=saldo_inicial-valor_cheque
    print(f"Cheque descontado, saldo: {novo_saldo}")