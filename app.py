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
layout="wide",
)

# -----------------------

# Sidebar para navegación

# -----------------------

st.sidebar.title("Navegación")
section = st.sidebar.radio("Ir a sección:", [
"Introducción",
"Proceso Cross-Docking",
"KPIs y Métricas",
"Beneficios",
"Descargas"
])

# -----------------------

# Sección: Introducción

# -----------------------

if section == "Introducción":
st.header("Cross-Docking Logistics")
st.markdown("""
Bienvenido a la plataforma de Cross-Docking.
Aquí se optimiza la logística y se reducen costos mediante la distribución directa de productos.
""")
st.subheader("Descripción de la Operación")
st.markdown("""
El Cross-Docking consiste en recibir mercancía y enviarla directamente al punto de venta o cliente sin almacenamiento prolongado.
Esto permite minimizar inventarios y mejorar tiempos de entrega.
""")

# -----------------------

# Sección: Proceso Cross-Docking

# -----------------------

elif section == "Proceso Cross-Docking":
st.header("Proceso de Cross-Docking")
st.markdown("""
1. Recepción de mercancía en el muelle de entrada.
2. Inspección y clasificación de productos.
3. Preparación de pedidos según rutas y clientes.
4. Despacho inmediato hacia transporte o cliente final.
""")
st.subheader("Diagrama del Proceso")
st.image("[https://via.placeholder.com/700x300.png?text=Diagrama+Cross-Docking](https://via.placeholder.com/700x300.png?text=Diagrama+Cross-Docking)", caption="Flujo del Cross-Docking")

# -----------------------

# Sección: KPIs y Métricas

# -----------------------

elif section == "KPIs y Métricas":
st.header("KPIs de Operación")
st.markdown("Algunos indicadores clave de desempeño del Cross-Docking:")

```
col1, col2, col3 = st.columns(3)
col1.metric("Tiempo Promedio (hrs)", 2.5, "↓0.3")
col2.metric("Productos Movidos", 1200, "↑100")
col3.metric("Errores en Despacho", 5, "↓1")

st.subheader("Tabla de Datos de Ejemplo")
df = pd.DataFrame({
    "Producto": ["A", "B", "C"],
    "Cantidad Recibida": [500, 300, 400],
    "Cantidad Despachada": [480, 295, 390]
})
st.dataframe(df)
```

# -----------------------

# Sección: Beneficios

# -----------------------

elif section == "Beneficios":
st.header("Beneficios del Cross-Docking")
st.markdown("""
- Reducción de inventarios y costos de almacenamiento.
- Mejoras en tiempos de entrega.
- Minimización de errores y devoluciones.
- Optimización de recursos logísticos.
""")

# -----------------------

# Sección: Descargas

# -----------------------

elif section == "Descargas":
st.header("Descargar Recursos")

```
st.subheader("Imágenes")
image_urls = {
    "Imagen 1": "TU_URL_DE_IMAGEN_1",
    "Imagen 2": "TU_URL_DE_IMAGEN_2"
}
selected_image = st.selectbox("Selecciona la imagen a descargar:", list(image_urls.keys()))
if st.button("Descargar Imagen"):
    url = image_urls[selected_image]
    response = requests.get(url)
    if response.status_code == 200:
        img_data = BytesIO(response.content)
        st.download_button(
            label="Descargar",
            data=img_data,
            file_name=f"{selected_image}.png",
            mime="image/png"
        )
    else:
        st.error("No se pudo descargar la imagen.")

st.subheader("Archivos Excel")
excel_urls = {
    "Reporte 1": "TU_URL_DE_EXCEL_1",
    "Reporte 2": "TU_URL_DE_EXCEL_2"
}
selected_excel = st.selectbox("Selecciona el Excel a descargar:", list(excel_urls.keys()), key="excel_select")
if st.button("Descargar Excel"):
    url = excel_urls[selected_excel]
    response = requests.get(url)
    if response.status_code == 200:
        excel_data = BytesIO(response.content)
        st.download_button(
            label="Descargar",
            data=excel_data,
            file_name=f"{selected_excel}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.error("No se pudo descargar el Excel.")
```

# -----------------------

# Footer

# -----------------------

st.markdown("---")
st.markdown("© 2025 Cross-Docking Platform")

