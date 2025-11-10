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
    # Estilo centrado
    st.markdown(
        """
        <style>
        .centered {
            text-align: center;
            font-size: 18px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align:center;'>Fresh Aurora Foods</h1>", unsafe_allow_html=True)
    st.image("https://github.com/gemelogascon-lang/cross-docking-app/blob/main/images/logo.png", width=350)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center;'>History</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p class='centered'>“We've been in the fresh food market since 2010. While we've faced challenges, such "
        "as the rapid evolution of technology in the sector, we have consistently reinvented ourselves "
        "to offer our customers the highest quality.”</p>",
        unsafe_allow_html=True
    )

    st.markdown("<h2 style='text-align:center;'>Mission</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p class='centered'>“To deliver high-quality fresh food to customers across Mexico, the United States, "
        "and Canada, ensuring optimal speed and the most competitive pricing in the market.”</p>",
        unsafe_allow_html=True
    )

    st.markdown("<h2 style='text-align:center;'>Vision</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p class='centered'>“To become the fastest-growing and most trusted Mexican fresh fruit exporter in "
        "North America.”</p>",
        unsafe_allow_html=True
    )

    st.markdown("<h2 style='text-align:center;'>Values</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p class='centered'><b>Trust, Support, Commitment, Modernization</b></p>",
        unsafe_allow_html=True
    )

    st.markdown("<h2 style='text-align:center;'>Value Proposition</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p class='centered'><b>Buy our products directly from farmers and manage the entire transformation process "
        "to make sure quality is not affected.</b></p>",
        unsafe_allow_html=True
    )

    st.markdown("<hr>", unsafe_allow_html=True)
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

    # PRODUCT 1 – Avocado Pulp
    st.markdown("---")
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("Frozen Avocado Pulp 🥑")
        st.markdown(
            """
            **Description:**  
            100% natural avocado pulp made from ripe Hass avocados grown in Michoacán, Mexico.  
            Smooth texture and rich flavor ideal for guacamole, toast, dips, and foodservice use.  

            **Specifications:**  
            - 100% Hass avocado pulp  
            - Pasteurized & quick-frozen at -18°C  
            - Shelf Life: 18 months (frozen)  
            - USDA & FDA compliant, SENASICA certified  

            **Target Markets:**  
            - B2B: Restaurants, distributors  
            - B2C: Supermarkets  
            - E-commerce: Grocery platforms  

            **Estimated Price:**  
            - Wholesale: USD $9 / 500 g  
            - Retail: USD $11 / 500 g
            """
        )
    with col2:
        st.image("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/avocado_pulp.jpg", width=500)

    # PRODUCT 2 – Mango Cubes
    st.markdown("---")
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("Mango Cubes IQF 🥭")
        st.markdown(
            """
            **Description:**  
            Naturally sweet, hand-cut mango cubes from Mexican Kent.  
            Individually quick-frozen (IQF) to preserve flavor, color, and texture.  

            **Specifications:**  
            - 100% mango  
            - IQF frozen at -18°C  
            - Shelf Life: 24 months  
            - FDA & CFIA compliant, SENASICA certified  

            **Target Markets:**  
            - B2B: Smoothie producers, airlines  
            - B2C: Supermarkets, health food stores  
            - E-commerce: Subscription meal kits  

            **Estimated Price:**  
            - Wholesale: USD $12 / 1 kg  
            - Retail: USD $15 / 1 kg
            """
        )
    with col2:
        st.image("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/mango_cubes.jpg", width=500)

    # PRODUCT 3 – Ready-to-Eat Salads
    st.markdown("---")
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("Ready-to-Eat Salads 🥬")
        st.markdown(
            """
            **Description:**  
            Fresh, pre-washed salad mixes with Mexican leafy greens, cherry tomatoes, shredded carrots, and optional dressings.  

            **Specifications:**  
            - Ingredients: Lettuce, spinach, tomato, carrot  
            - Triple-washed, MAP packed  
            - Shelf Life: 5 days refrigerated  
            - HACCP & ISO 22000 certified  

            **Target Markets:**  
            - B2B: Airlines, hotels, cafeterias  
            - B2C: Supermarkets  
            - E-commerce: Healthy meal delivery  

            **Estimated Price:**  
            - Wholesale: USD $2.50 / 250 g  
            - Retail: USD $3.80 / 250 g
            """
        )
    with col2:
        st.image("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/salads.jpg", width=500)

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

    st.subheader("Why Cross-Docking is Used")
    st.markdown(
        """
        - **Consolidation:** Groups multiple small shipments into larger, efficient loads.  
        - **Flow Acceleration:** Minimizes storage, speeds up deliveries.  
        - **Inventory Reduction:** Reduces holding costs and lead time.  
        """
    )

    st.subheader("Transport Modes")
    st.markdown(
        """
        **Land (Refrigerated Trucking):**  
        - Cost-effective for North America (Mexico–U.S.–Canada).  
        - Transit: 1.5 days to Laredo, +3–5 days to final hubs.  
        - Reliable temperature control for perishable goods.
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
    st.image("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/supply_chain_diagram.png", caption="Supply Chain Diagram")

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
