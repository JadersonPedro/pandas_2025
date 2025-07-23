#%%

## Selecione a primeira transação diaria de cada cliente.

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes

transacoes.head()



#%%

transacoes = transacoes.sort_values("DtCriacao")
transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"], utc=True, format="mixed").dt.date
first = transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])

first

#%%

last = transacoes.drop_duplicates(keep="last", subset=["IdCliente", "data"])
last

#%%

pd.concat([first, last])
