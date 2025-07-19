#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

#%%

pontos = [10, 1, 50, 25, 1, 1, 130, 3, 25, 100, 135, 60]

valores_50_mais= []
for i in pontos:
    if i>=50:
        valores_50_mais.append(i)

valores_50_mais

#%%


pontos = [10, 1, 50, 25, 1, 1, 130, 3, 25, 100, 135, 60]
filtro = []

valores_50_mais= []
for i in pontos:
    filtro.append(i>=50)

resultado = []
for i in range (len(pontos)):
    if filtro [i]:
        resultado.append(pontos[i])

resultado

#%%

import pandas as pd

brinquedo = pd.DataFrame(
    {
    "nome": ["teo", "nah", "mah"], 
    "idade": [32, 35, 14], 
    "uf": ["sp", "pr", "rj"],
    }
)

filtro = brinquedo["idade"] >= 18
     
brinquedo[filtro]

#%%

df= pd.read_csv("../data/transacoes.csv", sep=";")
df.head()


#%%

#valores maiores que 50

filtro = df["QtdePontos"] >=50
df[filtro]

#%%


#valores entre 50 e 100 

filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
filtro

df[filtro]

#%%


#valores igual a 50 ou 100

filtro = (df["QtdePontos"] ==1) | (df["QtdePontos"] ==100) 
df[filtro]


#%%

(df["QtdePontos"] >0) & (df["QtdePontos"] <=50) & (df["DtCriacao"] >='2025-01-01') 
df[filtro]