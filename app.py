import streamlit as st

# ---------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------------
st.set_page_config(page_title="Fresh Aurora Foods", page_icon="🥑", layout="wide")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5ebd8;
    }
    section[data-testid="stSidebar"] {
        background-color: #f5ebd8;
    }
    div[data-testid="stMarkdownContainer"] {
        background-color: transparent;
    }
    table {
        background-color: #fffaf0;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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

    # PRODUCTO 1
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.subheader("Frozen Avocado Pulp 🥑")
        st.markdown(
            """
            100% natural avocado pulp made from ripe Hass avocados grown in Michoacán, Mexico.
            Smooth texture and rich flavor ideal for guacamole, toast, dips, and foodservice use.
            Pasteurized, frozen, and packed under HACCP-certified conditions.

            **Specifications:**
            - Ingredients: 100% Hass avocado pulp  
            - Processing: Pasteurized and quick-frozen at -18°C  
            - Net Weight: 500 g  
            - Packaging: Vacuum-sealed LDPE pouch / 20 units per carton  
            - Dimensions: 20×15×3 cm  
            - Gross Weight: 0.55 kg  
            - Shelf Life: 18 months (frozen, unopened)  
            - USDA & FDA compliant, SENASICA certified  
            - Transport Mode: Refrigerated trucking (-18°C continuous cold chain)  
            - Estimated Selling Price: Wholesale $9.00 / 500g, Retail $11 / 500g  
            """
        )
    with col2:
        st.image("https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/avocado_pulp1.jpg", width=500)

    st.markdown("---")

    # PRODUCTO 2
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.subheader("Mango Cubes IQF 🥭")
        st.markdown(
            """
            Naturally sweet, hand-cut mango cubes from Mexican Kent. Individually quick-frozen (IQF)
            to preserve flavor, color, and texture.

            **Specifications:**
            - Ingredients: 100% mango  
            - Processing: Washed, diced, and IQF frozen at -18°C  
            - Net Weight: 1 kg  
            - Packaging: Transparent resealable LDPE pouch / 10 pouches per case  
            - Dimensions: 25×20×6 cm  
            - Gross Weight: 1.05 kg  
            - Shelf Life: 24 months (frozen)  
            - FDA & CFIA compliant, SENASICA certified  
            - Transport Mode: Reefer trucking (-18°C)  
            - Estimated Selling Price: Wholesale $12 / 1kg, Retail $15 / 1kg  
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
            and optional dressings. Designed for healthy convenience, with a crisp, garden-fresh taste.

            **Specifications:**
            - Ingredients: Lettuce, spinach, tomato, carrot, dressing (separate)  
            - Processing: Triple-washed, packed under modified atmosphere (MAP)  
            - Net Weight: 250 g  
            - Packaging: Clear PET bowl / Recyclable cardboard sleeve  
            - Dimensions: 18×18×5 cm  
            - Gross Weight: 0.27 kg  
            - Shelf Life: 5 days (refrigerated)  
            - HACCP & ISO 22000 certified  
            - Transport Mode: Refrigerated trucking (2–4°C)  
            - Estimated Selling Price: Wholesale $2.50 / 250g, Retail $3.80 / 250g  
            """
        )
    with col2:
        st.image("https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/salads.jpg", width=500)

    # --- TABLA AL FINAL ---
    st.markdown("---")
    st.markdown("### Product Logistics Summary Table")
    st.markdown(
        """
        <style>
        table {
            width: 100%;
            border-collapse: collapse;
            background-color: #f5ebd8;
        }
        th, td {
            border: 1px solid #00000033;
            padding: 10px;
            text-align: center;
        }
        th {
            background-color: #e9dbc0;
            font-weight: bold;
        }
        tr:nth-child(even) {
            background-color: #f8efe0;
        }
        </style>

        <table>
            <tr>
                <th>SKU</th>
                <th>Product</th>
                <th>Dimensions (cm)</th>
                <th>Weight (kg)</th>
                <th>Logistic Unit</th>
                <th>Pallet Configuration</th>
                <th>Temperature</th>
                <th>Incoterm</th>
            </tr>
            <tr>
                <td>AV500</td>
                <td>Frozen Avocado Pulp</td>
                <td>20×15×3</td>
                <td>0.55</td>
                <td>20 units/carton</td>
                <td>10×6 = 60 cartons</td>
                <td>-18°C</td>
                <td>DAP / FCA</td>
            </tr>
            <tr>
                <td>MG1000</td>
                <td>Mango Cubes IQF</td>
                <td>25×20×6</td>
                <td>1.05</td>
                <td>10 units/carton</td>
                <td>10×8 = 80 cartons</td>
                <td>-18°C</td>
                <td>DAP / FCA</td>
            </tr>
            <tr>
                <td>RS250</td>
                <td>Ready-to-Eat Salad</td>
                <td>18×18×5</td>
                <td>0.27</td>
                <td>24 units/crate</td>
                <td>8×5 = 40 crates</td>
                <td>2–4°C</td>
                <td>DAP / FCA</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True
    )
# =================================
# SECCIÓN: LOGÍSTICA (COMPLETA DEL PDF)
# =================================
elif menu == "🚛 Logística":
    st.title("Supply Chain & Logistics")

    st.markdown("### SCM & ILS Components Description")
    st.table({
        "Component": [
            "Procurement", "Processing & Packaging", "Cold Chain Transport", "Warehousing",
            "Cross-Docking", "Customs & 3PL", "Distribution"
        ],
        "Description": [
            "Sourcing of fresh produce from farms in Michoacán and Jalisco, including avocados, mangoes, and greens, ensuring consistent supply.",
            "HACCP-certified facility in Querétaro handles processing (pulping, IQF freezing) and packaging, maintaining quality standards.",
            "Products are transported in refrigerated trucks, maintaining -18°C (frozen) or 2–4°C (salads) during shipment.",
            "Cold storage in Querétaro for products, and temporary storage at Laredo, TX, for customs inspection and redistribution.",
            "Used at Laredo, TX, to consolidate shipments, reduce inventory holding, and speed up flow from warehouse to clients.",
            "Third-party logistics providers ensure customs clearance and border compliance for U.S. and Canadian shipments.",
            "Products are distributed to regional warehouses or directly to retail and foodservice clients in the U.S. and Canada."
        ]
    })

    st.markdown("---")
    st.markdown("### Cross-Docking Importance")
    st.markdown(
        """
        Cross-Docking is a critical part of the supply chain process, and it is used at the Laredo, TX hub.

        **Why Cross-Docking is Used:**
        - **Consolidation:** Allows for the grouping of multiple small shipments into larger, more efficient loads.  
        - **Flow Acceleration:** Reduces the need for extended storage, ensuring faster delivery times to U.S. and Canadian markets.  
        - **Inventory Reduction:** Minimizes holding time and reduces storage costs, leading to cost savings and faster movement of goods.
        """
    )

    st.markdown("---")
    st.markdown("### Transport Modes")
    st.markdown(
        """
        **Land (Refrigerated Trucking)**  
        - **Why Chosen:** Most cost-effective for the North American corridor (Mexico–U.S.–Canada).  
        - **Time:** 1.5 days from Querétaro to Laredo, then 3–5 days to regional U.S. and Canadian hubs.  
        - **Cost:** More economical compared to air transport, and faster than sea.  
        - **Service:** Reliable, with temperature control for sensitive products.
        """
    )

    st.markdown("---")
    st.markdown("### Explanatory Paragraph")
    st.markdown(
        """
        At **Aurora Fresh Foods**, our logistics network is meticulously designed to maintain the highest levels of freshness, quality, and efficiency throughout the supply chain.  
        The journey begins with sourcing premium, fresh produce from the best farms in Michoacán and Jalisco, known for their rich agricultural heritage.  
        Once the produce arrives, it is carefully processed and packaged in our state-of-the-art facility in Querétaro, where we maintain rigorous standards of hygiene and quality.  
        After packaging, the products are transported using refrigerated trucks to ensure temperature control and prevent spoilage.

        The next critical stage of the process occurs at our **cross-docking hub in Laredo, TX**.  
        Here, shipments are efficiently consolidated, inspected, and redistributed to U.S. and Canadian clients with minimal delays.  
        This cross-docking model is key to reducing inventory holding, accelerating the flow of goods, and minimizing storage costs.  
        By combining refrigerated trucking with strategic cross-docking, we ensure that products are delivered to our customers in the best possible condition and at an optimal speed, reducing lead time while keeping logistics costs low.
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

