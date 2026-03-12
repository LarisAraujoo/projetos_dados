import pandas as pd

dados = {
    "produto": ["caneta", "caderno", "lapis" ], "preco": [2.5, 15, 1.5]
}

df = pd.DataFrame(dados)

print(df)