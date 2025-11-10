import streamlit as st

# ---------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------------
st.set_page_config(page_title="Fresh Aurora Foods", page_icon="🥑", layout="wide")

# ---------------------------------
# MENÚ LATERAL
# ---------------------------------
st.sidebar.title("Menú de Navegación")
menu = st.sidebar.radio(
    "Ir a:",
    ["🏠 Inicio", "🥭 Productos", "🚛 Logística", "💰 Finanzas", "📦 Supply Chain", "🧾 Conclusión"]
)

# =================================
# SECCIÓN: INICIO
# =================================
if menu == "🏠 Inicio":
    st.title("Fresh Aurora Foods")
    st.image("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/logo.png", width=400)
    st.markdown("---")

    st.header("Historia")
    st.markdown(
        """
        *"We've been in the fresh food market since 2010. While we've faced challenges,
        such as the rapid evolution of technology in the sector, we have consistently reinvented
        ourselves to offer our customers the highest quality."*
        """
    )

    st.header("Misión")
    st.markdown(
        """
        *"To deliver high-quality fresh food to customers across Mexico, the United States,
        and Canada, ensuring optimal speed and the most competitive pricing in the market."*
        """
    )

    st.header("Visión")
    st.markdown(
        """
        *"To become the fastest-growing and most trusted Mexican fresh fruit exporter in North America."*
        """
    )

    st.header("Valores")
    st.markdown("**Trust, Support, Commitment, Modernization**")

    st.header("Propuesta de Valor")
    st.markdown(
        """
        **Buy our products directly from farmers and manage the entire transformation process
        to make sure quality is not affected.**
        """
    )

# =================================
# SECCIÓN: PRODUCTOS
# =================================
elif menu == "🥭 Productos":
    st.title("Nuestros Productos")

    # PRODUCTO 1
    st.subheader("Frozen Avocado Pulp 🥑")
    st.image("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/avocado_pulp.jpg", width=500)
    st.markdown(
        """
        100% natural avocado pulp made from ripe Hass avocados grown in Michoacán, Mexico.
        Smooth texture and rich flavor ideal for guacamole, toast, dips, and foodservice use.
        Pasteurized, frozen, and packed under HACCP-certified conditions.
        """
    )
    st.markdown(
        """
        **Especificaciones:**
        - Ingredients: 100% Hass avocado pulp  
        - Processing: Pasteurized and quick-frozen at -18°C  
        - Shelf Life: 18 months (frozen, unopened)
        - Regulatory: USDA & FDA compliant, SENASICA certification  
        **Precio:**  
        - Wholesale: $9 USD / 500 g  
        - Retail: $11 USD / 500 g
        """
    )
    st.markdown("---")

    # PRODUCTO 2
    st.subheader("Mango Cubes IQF 🥭")
    st.image("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/mango_cubes.jpg", width=500)
    st.markdown(
        """
        Naturally sweet, hand-cut mango cubes from Mexican Kent mangoes.
        Individually quick-frozen (IQF) to preserve flavor, color, and texture.
        Ideal for smoothies, desserts, and bulk foodservice use.
        """
    )
    st.markdown(
        """
        **Especificaciones:**
        - Ingredients: 100% mango  
        - Processing: IQF frozen at -18°C  
        - Shelf Life: 24 months  
        - Regulatory: FDA & CFIA compliant  
        **Precio:**  
        - Wholesale: $12 USD / kg  
        - Retail: $15 USD / kg
        """
    )
    st.markdown("---")

    # PRODUCTO 3
    st.subheader("Ready-to-Eat Salads 🥬")
    st.image("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/salads.jpg", width=500)
    st.markdown(
        """
        Fresh, pre-washed salad mixes combining Mexican leafy greens, cherry tomatoes, shredded carrots,
        and optional dressings. Designed for healthy convenience.
        """
    )
    st.markdown(
        """
        **Especificaciones:**
        - Ingredients: Lettuce, spinach, tomato, carrot  
        - Processing: Packed under modified atmosphere (MAP)  
        - Shelf Life: 5 days refrigerated  
        - Regulatory: HACCP & ISO 22000 certified  
        **Precio:**  
        - Wholesale: $2.50 USD / 250 g  
        - Retail: $3.80 USD / 250 g
        """
    )

# =================================
# SECCIÓN: LOGÍSTICA
# =================================
elif menu == "🚛 Logística":
    st.title("Logística y Distribución")
    st.markdown(
        """
        **Cross-Docking Hub:** Laredo, Texas  
        **Transport Mode:** Refrigerated trucking (-18°C or 2–4°C)  
        **Incoterms:** DAP / FCA  
        """
    )

    st.subheader("Why Cross-Docking is Used")
    st.markdown(
        """
        - **Consolidation:** Combines multiple small shipments into efficient loads.  
        - **Flow Acceleration:** Reduces need for storage and speeds up delivery.  
        - **Inventory Reduction:** Minimizes storage time and costs.
        """
    )

    st.subheader("Transport Modes")
    st.markdown(
        """
        **Mode:** Land (Refrigerated Trucking)  
        - Cost-effective for Mexico–U.S.–Canada corridor  
        - Transit: 1.5 days to Laredo, 3–5 days to regional hubs  
        - Reliable, temperature-controlled deliveries
        """
    )

# =================================
# SECCIÓN: FINANZAS
# =================================
elif menu == "💰 Finanzas":
    st.title("Financial & Operational Considerations")
    st.markdown(
        """
        **Fuel and Refrigeration Costs:**  
        - Fuel = 20–25% of logistics costs  
        - Reefer maintenance adds 10–12%  
        - *Mitigation:* Include fuel surcharge clauses  
        
        **Customs Delay Management:**  
        - Use data loggers for temperature  
        - Laredo hub reduces border congestion  
        - Maintain buffer inventory near the border  
        """
    )
    st.image("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/supply_chain_diagram.png", caption="Supply Chain Flow Diagram")

# =================================
# SECCIÓN: SUPPLY CHAIN
# =================================
elif menu == "📦 Supply Chain":
    st.title("Supply Chain & Logistics")
    st.table({
        "Component": [
            "Procurement", "Processing & Packaging", "Cold Chain Transport",
            "Warehousing", "Cross-Docking", "Customs & 3PL", "Distribution"
        ],
        "Description": [
            "Sourcing from Michoacán and Jalisco farms (avocados, mangoes, greens).",
            "Processing in HACCP-certified Querétaro facility.",
            "Transported in refrigerated trucks (-18°C or 2–4°C).",
            "Cold storage in Querétaro and temporary in Laredo, TX.",
            "Cross-docking consolidates and accelerates flows.",
            "3PL manages customs and documentation.",
            "Distribution to U.S. and Canadian warehouses."
        ]
    })

# =================================
# SECCIÓN: CONCLUSIÓN
# =================================
elif menu == "🧾 Conclusión":
    st.title("Conclusión")
    st.markdown(
        """
        At **Aurora Fresh Foods**, our logistics network is designed to ensure freshness,
        quality, and efficiency from farm to customer.
        Through strategic sourcing, controlled processing, and refrigerated cross-docking,
        we deliver top-quality products across North America with speed and reliability.
        """
    )
