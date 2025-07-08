#%%
import pandas as pd

idades = [32, 38, 30, 30, 31, 
          35, 25, 29, 31, 37, 
          27, 23, 36, 33, 39,
]

series_idades = pd.Series(idades)
series_idades


#%%

idades[0]
series_idades[0]

#%%

series_idades = series_idades.sort_values()
series_idades

#%%

series_idades.iloc[0]

#%%

series_idades.iloc[-1]


#%%

idades = [32, 38, 30, 30, 31, 
          35, 25, 29, 31, 37, 
          27, 23, 36, 33, 39,
]

index = ["Teo", "Rafael", "Maisa", "Melissa", "Dana",
         "Nah", "Dani", "Gio", "Mah", "Dio",
         "Lu", "Aline", "Pedro", "Thi", "Matheus",
]

series_idades = pd.Series(idades, index=index)
series_idades

#%%

series_idades["Pedro"]

#%%

series_idades.loc["Teo"]