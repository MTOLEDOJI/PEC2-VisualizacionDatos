# Importar liberías necesarias
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Cargar los datos de población mundial
df = pd.read_csv('world_population.csv')

# Link a los datos: https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset/data. 

# Filtrar las columnas necesarias: País y Población (population)
df = df[['Country/Territory', '2022 Population']]
df.columns = ['Country', 'Population']  # Renombrar 

# Cargar geometría de los países con geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Realizar un merge entre los datos de población y el mapa mundial
world_population = world.merge(df, left_on='name', right_on='Country', how='left')

# Ajustar el tamaño de los símbolos proporcionalmente a la población
size_scale = 0.0000005 

# Crear el gráfico
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.plot(ax=ax, color = "lightblue")
for _, row in world_population.dropna(subset=['Population']).iterrows():
    ax.scatter(
        row.geometry.centroid.x, 
        row.geometry.centroid.y,
        s=row['Population'] * size_scale,
        color='red',
        alpha=0.6,
        edgecolor="k",
        linewidth=0.5
    )

plt.title("Proportional Symbol Map: Población por País en 2022")
plt.axis('off') 
plt.show()

