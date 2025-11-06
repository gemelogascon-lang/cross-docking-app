import streamlit as st
import pandas as pd
import requests
from io import BytesIO

# -----------------------

# Configuración de la página

# -----------------------

st.set_page_config(
page_title="Cross-Docking Platform",
page_icon="📦",
layout="wide"
)

# -----------------------

# Introducción

# -----------------------

st.header("Cross-Docking Logistics")
st.markdown(
"Bienvenido a la plataforma de Cross-Docking.\n"
"Aquí se optimiza la logística y se reducen costos mediante la distribución directa de productos."
)
st.subheader("Descripción de la Operación")
st.markdown(
"El Cross-Docking consiste en recibir mercancía y enviarla directamente al punto de venta o cliente sin almacenamiento prolongado.\n"
"Esto permite minimizar inventarios y mejorar tiempos de entrega."
)
st.markdown("---")

# -----------------------

# Proceso Cross-Docking

# -----------------------

st.header("Proceso de Cross-Docking")
st.markdown(
"1. Recepción de mercancía en el muelle de entrada.\n"
"2. Inspección y clasificación de productos.\n"
"3. Preparación de pedidos según rutas y clientes.\n"
"4. Despacho inmediato hacia transporte o cliente final."
)
st.subheader("Diagrama del Proceso")
st.image(
"[https://via.placeholder.com/700x300.png?text=Diagrama+Cross-Docking](https://via.placeholder.com/700x300.png?text=Diagrama+Cross-Docking)",
caption="Flujo del Cross-Docking"
)
st.markdown("---")

# -----------------------

# KPIs y Métricas

# -----------------------

st.header("KPIs de Operación")
st.markdown("Algunos indicadores clave de desempeño del Cross-Docking:")

col1, col2, col3 = st.co
