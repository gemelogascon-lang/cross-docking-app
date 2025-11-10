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
    ["🏠 Inicio", "🥭 Productos", "🚛 Logística", "💰 Finanzas", "🧾 Conclusión"]
)

# =================================
# SECCIÓN: INICIO
# =================================
if menu == "🏠 Inicio":
    # --- Banner tipo portada ---
    st.markdown(
        """
        <style>
        .hero {
            position: relative;
            width: 100%;
            height: 300px;
            background-image: url('https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/logo.png');
            background-size: cover;
            background-position: center;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 40px;
        }
        .hero-text {
            background-color: rgba(0, 0, 0, 0.4);
            padding: 20px 40px;
            border-radius: 8px;
            font-size: 28px;
            font-weight: bold;
            color: white;
            text-shadow: 1px 1px 4px rgba(0,0,0,0.7);
        }
        </style>

        <div class="hero">
            <div class="hero-text">
                Exportando sabor, frescura y confianza 🌿
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Título principal ---
    st.markdown("<h1 style='text-align:center;'>Fresh Aurora Foods</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # --- Información de la empresa ---
    st.header("History")
    st.markdown(
        """
        *"We've been in the fresh food market since 2010. While we've faced challenges, such
        as the rapid evolution of technology in the sector, we have consistently reinvented
        ourselves to offer our customers the highest quality."*
        """
    )

    st.header("Mission")
    st.markdown(
        """
        *"To deliver high-quality fresh food to customers across Mexico, the United States, and
        Canada, ensuring optimal speed and the most competitive pricing in the market."*
        """
    )

    st.header("Vision")
    st.markdown(
        """
        *"To become the fastest-growing and most trusted Mexican fresh fruit exporter in
        North America."*
        """
    )

    st.header("Values")
    st.markdown("**Trust, Support, Commitment, Modernization**")

    st.header("Value Proposition")
    st.markdown(
        """
        **Buy our products directly from farmers and manage the entire transformation process
        to make sure quality is not affected.**
        """
    )

    st.markdown("---")

    st.header("Business Context")
    st.markdown(
        """
        **Industry:** Cold Chain / Agribusiness  
        **Country of Origin:** Mexico  
        **Export Markets:** United States and Canada  
        **Distribution Corridor:** North American refrigerated trucking network  
        **Cross-Docking Hub:** Laredo, Texas (inspection, redistribution, and customs clearance)  
        **Main Logistics Challenge:** Maintaining 2–4°C cold chain integrity and preventing spoilage
        during border inspections or customs delays.  
        **Transport Mode:** Refrigerated trucking (reefer units)  
        **Incoterms:** DAP (Delivered at Place) / FCA (Free Carrier)
        """
    )

# =================================
# SECCIÓN: PRODUCTOS
# =================================
elif menu == "🥭 Productos":
    st.title("Our Products")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("Frozen Avocado Pulp 🥑")
        st.markdown(
            """
            100% natural avocado pulp made from ripe Hass avocados grown in Michoacán, Mexico.
            Smooth texture and rich flavor ideal for guacamole, toast, dips, and foodservice use.
            Pasteurized, frozen, and packed under HACCP-certified conditions.

            **Specifications:**
            - 100% Hass avocado pulp  
            - Pasteurized & quick-frozen at -18°C  
            - Shelf Life: 18 months  
            - USDA & FDA compliant, SENASICA certified  
            """
        )
    with col2:
        st.image("https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/avocado_pulp.jpg", width=500)

    st.markdown("---")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("Mango Cubes IQF 🥭")
        st.markdown(
            """
            Naturally sweet, hand-cut mango cubes from Mexican Kent.
            Individually quick-frozen (IQF) to preserve flavor, color, and texture.

            **Specifications:**
            - 100% mango  
            - IQF frozen at -18°C  
            - Shelf Life: 24 months  
            - FDA & CFIA compliant, SENASICA certified  
            """
        )
    with col2:
        st.image("https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/mango_cubes.jpg", width=500)

    st.markdown("---")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("Ready-to-Eat Salads 🥬")
        st.markdown(
            """
            Fresh, pre-washed salad mixes combining Mexican leafy greens, cherry tomatoes, shredded carrots,
            and optional dressings. Designed for healthy convenience.

            **Specifications:**
            - Ingredients: Lettuce, spinach, tomato, carrot  
            - Triple-washed, MAP packed  
            - Shelf Life: 5 days refrigerated  
            - HACCP & ISO 22000 certified  
            """
        )
    with col2:
        st.image("https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/salads.jpg", width=500)

# =================================
# SECCIÓN: LOGÍSTICA
# =================================
elif menu == "🚛 Logística":
    st.title("Supply Chain & Logistics")
    st.markdown(
        """
        **Procurement:** Sourcing fresh produce from farms in Michoacán and Jalisco.  
        **Processing & Packaging:** HACCP-certified facility in Querétaro for pulping, freezing, and packing.  
        **Cold Chain Transport:** -18°C (frozen) or 2–4°C (fresh salads).  
        **Warehousing:** Querétaro cold storage and Laredo, TX for customs inspection.  
        **Cross-Docking:** Used at Laredo hub to consolidate and accelerate shipments.  
        **Distribution:** To regional warehouses or directly to clients in U.S. and Canada.  
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
        - Fuel: 20–25% of logistics expenses.  
        - Reefer maintenance adds 10–12% per pallet.  
        - *Mitigation:* Include fuel surcharge clauses.  

        **Customs Delay Management:**  
        - Use temperature loggers for compliance.  
        - Utilize Laredo cross-docking hub.  
        - Keep buffer inventory near border (McAllen or Laredo).  
        """
    )

# =================================
# SECCIÓN: CONCLUSIÓN
# =================================
elif menu == "🧾 Conclusión":
    st.title("Conclusion")
    st.markdown(
        """
        The next critical stage occurs at our cross-docking hub in Laredo, TX.  
        Shipments are efficiently consolidated, inspected, and redistributed to U.S. and Canadian clients.  
        This model minimizes storage, reduces costs, and ensures faster deliveries.  

        By combining refrigerated trucking with strategic cross-docking, we deliver products  
        in the best possible condition — fresh, fast, and reliable.
        """
    )
