vendas={"Janeiro":1000, "Fevereiro":1500, "Março":1200}

total=0

for valor in vendas.values():
    total+=valor
print("total de vendas:", total)