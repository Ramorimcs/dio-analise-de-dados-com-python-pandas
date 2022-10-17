#importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")
#criando o df
df = pd.read_excel("C:/Users/ramor/Desktop/Adventureworks.xlsx")
#análises iniciais - 5 primeiras linhas
df.head()
#Pergunta 1 - Receita Total?
round(df["Valor Venda"].sum(),2)
#Pergunta 2 - Custo Total?
df["Custo Total"] = df["Custo Unitário"]*df["Quantidade"]
round(df["Custo Total"].sum(),2)
#Pergunta 3 - Lucro Total?
df["Lucro Total"] = df["Valor Venda"]-df["Custo Total"]
round(df["Lucro Total"].sum(),2)
#Pergunta 4 - Total de dias para envio de cada produto?
df["Prazo Entrega"] = df["Data Envio"]-df["Data Venda"]
#Pergunta 5 - Média do tempo de envio para cada marca de produto?
df["Prazo Entrega"].dtype
df["Prazo Entrega"] = df["Prazo Entrega"].dt.days
df["Prazo Entrega"].dtype
df["Prazo Entrega"].groupby(df["Marca"]).mean()
#Pergunta 6 - Lucro por ano E por marca?
df["Ano"] = df["Data Venda"].dt.year
df["Lucro Total"].groupby([df["Ano"], df["Marca"]]).sum()