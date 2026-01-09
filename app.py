import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Dashboard de anuncios de vehículos (vehicles_us.csv)")
st.write("Selecciona las casillas para construir los gráficos.")

car_data = pd.read_csv("vehicles_us.csv")

# Checkboxes
build_histogram = st.checkbox("Construir un histograma (odometer)")
build_scatter = st.checkbox(
    "Construir un gráfico de dispersión (odometer vs price)")

if build_histogram:
    st.write("Histograma para la columna **odometer**")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    st.write("Gráfico de dispersión **odometer** vs **price**")
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
