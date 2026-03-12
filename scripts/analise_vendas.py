import pandas as pd

dados = pd.read_csv('dados/vendas.csv')
dados["faturamento"] = dados["preco"] * dados["quantidade"]

print(dados)

faturamento_total = dados["faturamento"].sum()

print("faturamento total:", faturamento_total)
