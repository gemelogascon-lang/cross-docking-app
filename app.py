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
    ["🏠 Inicio", "🥭 Productos", "🚛 Logística", "💰 Finanzas", "🧾 Conclusión", "📊 Descargar"]
)

# =================================
# SECCIÓN: INICIO
# =================================
if menu == "🏠 Inicio":
    # --- Banner tipo portada (sin texto y sin recortes) ---
    st.markdown(
        """
        <style>
        .hero {
            position: relative;
            width: 100%;
            height: auto;
            display: flex;
            justify-content: center;
            margin-bottom: 40px;
        }
        .hero img {
            width: 100%;
            height: auto;
            border-radius: 10px;
        }
        .centered {
            text-align: center;
            font-size: 18px;
            line-height: 1.7;
        }
        </style>

        <div class="hero">
            <img src="https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/logo.png" alt="Fresh Aurora Foods banner">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # --- Textos centrados ---
    st.markdown("<h2 style='text-align:center;'>History</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p class='centered'>
        "We've been in the fresh food market since 2010. While we've faced challenges, such
        as the rapid evolution of technology in the sector, we have consistently reinvented
        ourselves to offer our customers the highest quality."
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h2 style='text-align:center;'>Mission</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p class='centered'>
        "To deliver high-quality fresh food to customers across Mexico, the United States, and
        Canada, ensuring optimal speed and the most competitive pricing in the market."
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h2 style='text-align:center;'>Vision</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p class='centered'>
        "To become the fastest-growing and most trusted Mexican fresh fruit exporter in
        North America."
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h2 style='text-align:center;'>Values</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p class='centered'>
        <b>Trust, Support, Commitment, Modernization</b>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h2 style='text-align:center;'>Value Proposition</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p class='centered'>
        <b>Buy our products directly from farmers and manage the entire transformation process
        to make sure quality is not affected.</b>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("<h2 style='text-align:center;'>Business Context</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='centered'>
        <p><b>Industry:</b> Cold Chain / Agribusiness</p>
        <p><b>Country of Origin:</b> Mexico</p>
        <p><b>Export Markets:</b> United States and Canada</p>
        <p><b>Distribution Corridor:</b> North American refrigerated trucking network</p>
        <p><b>Cross-Docking Hub:</b> Laredo, Texas (inspection, redistribution, and customs clearance)</p>
        <p><b>Main Logistics Challenge:</b> Maintaining 2–4°C cold chain integrity and preventing spoilage during border inspections or customs delays.</p>
        <p><b>Transport Mode:</b> Refrigerated trucking (reefer units)</p>
        <p><b>Incoterms:</b> DAP (Delivered at Place) / FCA (Free Carrier)</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =================================
# SECCIÓN: PRODUCTOS
# =================================
elif menu == "🥭 Productos":
    st.title("Our Products")

    # ✅ PRODUCTO 1 ACTUALIZADO
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

    # PRODUCTO 2
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

    # PRODUCTO 3
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

# =================================
# SECCIÓN: DESCARGAR
# =================================
elif menu == "📊 Descargar":
    st.title("Descargar")

    # ---- SECCIÓN EXCEL ----
    st.markdown("<h3 style='color:green;'>Aquí podrás consultar nuestro Excel con la información requerida</h3>", unsafe_allow_html=True)
    st.write("")
    st.markdown(
        """
        <a href="https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/files/informacion.xlsx" download>
            <button style="background-color:green;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;font-size:16px;">📗 Descargar Excel</button>
        </a>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # ---- SECCIÓN PYTHON APP ----
    st.markdown("<h3 style='color:blue;'>Aquí puedes consultar nuestro código de Python (app.py)</h3>", unsafe_allow_html=True)
    st.write("")
    st.markdown(
        """
        <a href="https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/files/app.py" download>
            <button style="background-color:yellow;color:blue;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;font-size:16px;">🐍 Descargar Código Python</button>
        </a>
        """,
        unsafe_allow_html=True
    )
