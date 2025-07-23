#%%

import pandas as pd

#%%

df = pd.read_csv("../data/clientes.csv", sep=";")
df

#%%

df["QtdePontos"].astype(str)

#%%

df["DtCriacao"].replace({"0000-00-00 00:00:00": "2024-02-01 09:00:00"
                         })

#%%

pd.to_datetime(df["DtCriacao"])

#%%

df["DtCriacao"].dt.year()


