# Importar librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos y agruparlos
df = pd.read_excel("Indian Rainfall Measurements.xlsx")

# Link a los datos: https://www.kaggle.com/datasets/ankitgaikar1995/imd-rainfall-dataset-2022 

monthly_precipitation = df.groupby('month')['precipitation'].mean()
# Dividir los valores de precipitación por 1000 para escalar
monthly_precipitation /= 1000

# Preparar los datos para el gráfico de rosa
angulos = np.linspace(0, 2 * np.pi, 12, endpoint=False).tolist()
precipitation_values = monthly_precipitation.tolist()

# Para que el gráfico sea circular, duplicar el primer valor al final de la lista
precipitation_values += precipitation_values[:1]
angulos += angulos[:1]

# Crear el gráfico
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angulos, precipitation_values, alpha=0.7)
ax.plot(angulos, precipitation_values, color="blue", linewidth=2)

# Configurar etiquetas de los meses
month_names = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
               "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
ax.set_xticks(angulos[:-1])  # Excluye el último ángulo duplicado
ax.set_xticklabels(month_names)

# Agregar título
plt.title("Chart Rose: Promedio de precipitación mensual en la India (2022)", fontsize=16)
plt.show()
