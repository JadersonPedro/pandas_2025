#%%
import pandas as pd

idades = [32, 38, 30, 30, 31, 
          35, 25, 29, 31, 37, 
          27, 23, 36, 33, 39,
]

nomes = ["Teo", "Rafael", "Maisa", "Melissa", "Dana",
         "Nah", "Dani", "Gio", "Mah", "Dio",
         "Lu", "Aline", "Pedro", "Thi", "Matheus",
]

series_idades = pd.Series(idades)
series_nomes =pd.Series(nomes)
series_idades

#%%

df= pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes
df

#%%

df.iloc[-1]["idades"]

#%%

df.iloc[0]["nomes"]

