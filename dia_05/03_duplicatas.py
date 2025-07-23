#%%

import pandas as pd

#%%

df = pd.DataFrame({
    "nome": ['Jaderson', 'Teo', 'bia', 'nah', 'bia'],
    "sobrenome": ['Costa', 'Calvo', 'Silva', 'Costa', 'Silva'],
    "salario": ['3200', '4500', '1950', '5780', '2954'],

})

df

#%%

df.drop_duplicates(keep='last')

#%%

df = df.sort_values("salario", ascending=False)
df

#%%


df.drop_duplicates(subset=["nome", "sobrenome"])


