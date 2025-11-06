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
    """
    Bienvenido a la plataforma de **Cross-Docking**.  
    Aquí se optimiza la logística y se reducen costos mediante la distribución directa de productos.
    """
)

st.subheader("Descripción de la Operación")
st.markdown(
    """
    El Cross-Docking consiste en recibir mercancía y enviarla directamente al punto de venta o cliente sin almacenamiento prolongado.  
    Esto permite minimizar inventarios y mejorar tiempos de entrega.
    """
)
st.markdown("---")

# -----------------------
# Proceso Cross-Docking
# -----------------------

st.header("Proceso de Cross-Docking")
st.markdown(
    """
    1. Recepción de mercancía en el muelle de entrada.  
    2. Inspección y clasificación de productos.  
    3. Preparación de pedidos según rutas y clientes.  
    4. Despacho inmediato hacia transporte o cliente final.
    """
)

st.subheader("Diagrama del Proceso")
st.image(
    "https://via.placeholder.com/700x300.png?text=Diagrama+Cross-Docking",
    caption="Flujo del Cross-Docking"
)
st.markdown("---")

# -----------------------
# KPIs y Métricas
# -----------------------

st.header("KPIs de Operación")
st.markdown("Algunos indicadores clave de desempeño del Cross-Docking:")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Tiempo promedio de despacho", "2.5 h")
with col2:
    st.metric("Porcentaje de entregas a tiempo", "97.8%")
with col3:
    st.metric("Reducción de inventario", "45%")

st.markdown("---")

# -----------------------
# Cierre
# -----------------------

st.subheader("Conclusión")
st.markdown(
    """
    El modelo de **Cross-Docking** permite una operación logística más eficiente,  
    reduciendo costos y mejorando la satisfacción del cliente final.
    """
)
