#%%
import pandas as pd

# Permitir exibir todas as colunas
pd.set_option('display.max_columns', None)

# Ler o arquivo
df_clientes = pd.read_csv("../data/clientes.csv", sep=";")

# Mostrar o DataFrame
df_clientes

#%%

##Amostras

df_clientes.head(n=10)

#%%

df_clientes.tail(n=10)

#%%

df_clientes.sample(n=10)

#%%

df_clientes.shape

#%%

df_clientes.columns

#%%

df_clientes.index

#%%

df_clientes.info(memory_usage ="deep")

#%%

df_clientes.dtypes