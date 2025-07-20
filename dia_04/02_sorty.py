#%%

import pandas as pd 

clientes = pd.read_csv("../data/clientes.csv", sep=";")

max_ponto = clientes["QtdePontos"].max()
filtro = clientes["QtdePontos"] == max_ponto
clientes[filtro]

#%%

clientes.sort_values(by="QtdePontos", ascending=False).head(5)

#%%

top_5 = (clientes.sort_values(by="QtdePontos", ascending=False)
 .head(5)["IdCliente"] )

type(top_5)
#%%

brinquedo = pd.DataFrame(
    {
        "nome": ["Jads", "Teo", "Dana", "Balto"],
        "idade": ["35", "32", "28", "3"],
        "salario": ["4533", "4533", "7200", "0"], 
    }
)

brinquedo

#%%

brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])

