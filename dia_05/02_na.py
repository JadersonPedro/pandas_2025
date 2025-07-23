#%%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

#%%

clientes.dropna(how="any")

#%%

df = pd.DataFrame(
    {
        "nome": ["Jads", None, "Teo", "Dana"],
        "idade": [None, None, "32", "28"],
        "salario": ["3200", "4500", None, "6000"]
    }
)

df.dropna(how="all", subset=["idade", "nome"])



#%%
          
df['idade'] = pd.to_numeric(df['idade'], errors='coerce')
df['salario'] = pd.to_numeric(df['salario'], errors='coerce')

#%%

medias = df[['idade', 'salario']].mean()
df = df.fillna(medias)
print(df[['idade', 'salario']])

