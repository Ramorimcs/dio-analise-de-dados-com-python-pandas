#importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

#criando o df
df = pd.read_excel("C:/Users/ramor/Desktop/Adventureworks.xlsx")

#análises iniciais - 5 primeiras linhas
df.head()
#análises iniciais - qtde linhas e colunas
df.shape

