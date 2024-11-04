# Importar librerías necesarias
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Definir la carpeta donde están los archivos de texto
carpeta = "trump-speeches"

# Link a los datos: https://www.kaggle.com/datasets/alandu20/2016-us-presidential-campaign-texts-and-polls

# Concatenar todos en una sola cadena
texto = ""

# Recorrer todos los archivos en la carpeta
for archivo in os.listdir(carpeta):
    if archivo.endswith(".txt"):  # Solo procesar archivos .txt
        ruta_archivo = os.path.join(carpeta, archivo)
        with open(ruta_archivo, "r", encoding="utf-8") as file:
            texto += file.read() + " "  # Añadir el texto de cada archivo y un espacio

# Crear la nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color="white", 
                      max_words=200, contour_color='steelblue', contour_width=1).generate(texto)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
