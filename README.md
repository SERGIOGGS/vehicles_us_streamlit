# vehicles_us_streamlit
Author: Sergio Gaitan
Sprint 7
# Vehicles US - Streamlit Dashboard

Esta aplicación web muestra un pequeño dashboard interactivo usando un conjunto de datos de anuncios de venta de vehículos (`vehicles_us.csv`).

## Funcionalidad
- Permite construir un **histograma** de la columna `odometer` (kilometraje).
- Permite construir un **gráfico de dispersión** entre `odometer` y `price`.
- Los gráficos se generan de forma interactiva usando Plotly y se controlan con casillas de verificación (checkboxes) en Streamlit.

## Cómo ejecutar la aplicación
1. Instala dependencias:
   ```bash
   pip install -r requirements.txt