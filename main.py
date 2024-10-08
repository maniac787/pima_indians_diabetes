import pandas as pd

# Cargar el dataset
df = pd.read_csv("pima-indians-diabetes.csv")

# 1. Revisar los primeros registros
print("Primeras filas del dataset:\n", df.head())

# 2. Dimensiones del conjunto de datos
print("\nDimensiones del dataset:", df.shape)

# 3. Tipos de datos
print("\nTipos de datos por columna:\n", df.dtypes)

# 4. Resumen estadístico
print("\nResumen estadístico:\n", df.describe())

# 5. Distribución entre clases
print("\nDistribución entre clases:\n", df.groupby('class').size())

# 6. Matriz de correlación
print("\nMatriz de correlación:\n", df.corr())

# 7. Asimetría
print("\nAsimetría:\n", df.skew())
