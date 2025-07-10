#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

#%%

df.shape

#%%

df.info(memory_usage="deep")

#%%

df.dtypes

#%%

renamed_columns={"QtdePontos":"QtPontos"}

df.rename(columns=renamed_columns, inplace=True)


#%%

colunas = ["IdCliente", "qtPontos"]
df[["IdCliente"]]

#%%

# SELECT *FROM df

df

#%%

#SELECT IdCliente FROM df

df[["IdCliente"]]

#%%

#SELECT IdCliente, Qtpontos FROM df LIMIT 5

df[["IdCliente", "QtPontos"]].tail(5)

#%%

#SELECT IdCliente, idTransação, Qtpontos
#FROM df LIMIT 5

df[["IdCliente", "QtPontos", "IdTransacao"]].head(5)

#%%

colunas = df.columns.to_list()
colunas.sort()
colunas

df=df[colunas]
df
# %%
