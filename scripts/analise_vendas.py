import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('dados/vendas.csv')
dados["faturamento"] = dados["preco"] * dados["quantidade"]

print(dados)

faturamento_total = dados["faturamento"].sum()

print("faturamento total:", faturamento_total)

vendas_por_produto = dados.groupby("produto")["quantidade"].sum()

print(vendas_por_produto)

vendas_por_produto.plot(kind="bar")

plt.title("Vendas por Produto")
plt.xlabel("Produto")
plt.ylabel("Quantidade Vendida")

plt.savefig("grafico_vendas.png")

plt.show()

produto_mais_vendido = vendas_por_produto.idxmax()

print("Produto mais vendido:", produto_mais_vendido)
