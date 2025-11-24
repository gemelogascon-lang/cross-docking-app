import streamlit as st

# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------
st.set_page_config(page_title="Fresh Aurora Foods", page_icon="🥑", layout="wide")

# --- PROFESSIONAL DESIGN & STYLE ---
st.markdown(
    """
    <style>
    /* GLOBAL BACKGROUND AND FONT */
    .stApp {
        background-color: #f5ebd8;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #2c2c2c;
    }

    /* SIDEBAR STYLING */
    section[data-testid="stSidebar"] {
        background-color: #f5ebd8;
        border-right: 2px solid #e0d5b5;
    }

    /* HEADINGS */
    h1, h2, h3 {
        color: #2b3a2e;
        text-align: center;
        font-weight: 700;
        letter-spacing: 0.5px;
    }

    h2 {
        border-bottom: 2px solid #a7c957;
        display: inline-block;
        padding-bottom: 4px;
    }

    /* DIVIDERS */
    hr, .stHorizontalBlock {
        border: none;
        border-top: 2px solid #d6c7a1;
        margin: 30px 0;
    }

    /* TEXT ALIGNMENT */
    .centered {
        text-align: center;
        font-size: 18px;
        line-height: 1.8;
        color: #333333;
    }

    /* HERO (BANNER) IMAGE */
    .hero {
        position: relative;
        width: 100%;
        height: auto;
        display: flex;
        justify-content: center;
        margin-bottom: 40px;
        transition: transform 0.4s ease;
    }

    .hero img {
        width: 100%;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
        transition: transform 0.5s ease;
    }

    .hero img:hover {
        transform: scale(1.02);
    }

    /* PRODUCT SECTIONS (CARDS) */
    .product-section {
        padding: 20px 30px;
        background-color: #fffaf0;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 30px;
        transition: box-shadow 0.3s ease, transform 0.3s ease;
    }

    .product-section:hover {
        transform: scale(1.01);
        box-shadow: 0px 6px 16px rgba(0,0,0,0.15);
    }

    /* PRODUCT IMAGES */
    .stImage img {
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    }

    /* PRODUCT TABLE */
    table {
        width: 100%;
        border-collapse: collapse;
        background-color: #f5ebd8;
        border-radius: 10px;
        overflow: hidden;
        margin-top: 20px;
    }

    th, td {
        border: 1px solid #00000033;
        padding: 10px;
        text-align: center;
    }

    th {
        background-color: #e9dbc0;
        color: #1f1f1f;
        font-weight: bold;
    }

    tr:nth-child(even) {
        background-color: #f8efe0;
    }

    tr:hover {
        background-color: #f2e6d0;
        transition: background-color 0.3s ease;
    }

    /* BUTTONS */
    button, .stDownloadButton>button {
        background-color: #a7c957 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 10px 25px !important;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

    button:hover {
        background-color: #8ab34f !important;
        transform: scale(1.05);
    }

    /* TEXT BODY */
    p, li {
        font-size: 16px;
        line-height: 1.8;
        color: #2f2f2f;
    }

    /* ANIMATIONS */
    .fade-in {
        animation: fadeIn 1s ease-in;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    /* DOWNLOAD SECTIONS */
    .download-section {
        text-align: center;
        padding: 15px;
    }

    .download-section h3 {
        margin-bottom: 10px;
        color: #204d66;
    }

    /* SIDEBAR TITLE */
    [data-testid="stSidebarNav"]::before {
        content: "Fresh Aurora Foods";
        margin-left: 10px;
        font-size: 20px;
        font-weight: 700;
        color: #2b3a2e;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------
# SIDEBAR MENU (IN ENGLISH)
# ---------------------------------
st.sidebar.image("https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/logo.png", width=150)
st.sidebar.title("Navigation Menu")
st.sidebar.markdown("Select a section to explore:")
menu = st.sidebar.radio(
    "",
    ["🏠 Home", "🥭 Products", "🚛 Logistics", "💰 Finance", "🗺️ Routes", "🧾 Contact", "Infographic"]
)


# =================================
# SECCIÓN: INICIO
# =================================
if menu == "🏠 Home":
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
elif menu == "🥭 Products":
    st.title("Our Products")

    # PRODUCTO 1 – FROZEN AVOCADO PULP
    st.subheader("Product 1 – Frozen Avocado Pulp 🥑")
    st.markdown(
        """
        ### Description  
        100% natural avocado pulp made from ripe Hass avocados grown in Michoacán, Mexico.  
        Smooth texture and rich flavor ideal for guacamole, toast, dips, and foodservice use.  
        Pasteurized, frozen, and packed under HACCP-certified conditions.
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(
            """
            ### Key Specifications  
            - **Ingredients:** 100% Hass avocado pulp  
            - **Processing:** Pasteurized and quick-frozen at -18°C  
            - **Net Weight:** 500 g  

            **Packaging:**  
            - Primary: Vacuum-sealed LDPE pouch  
            - Secondary: Carton box (20 units per carton)  
            - Dimensions (Retail Unit): 20 × 15 × 3 cm  
            - Gross Weight: 0.55 kg  

            **Labeling Requirements:**  
            - Product name, net weight, nutritional facts  
            - Country of origin: Product of Mexico  
            - Allergen statement: Contains no allergens  
            - Storage instruction: Keep Frozen (-18°C)  
            - Shelf Life: 18 months (frozen, unopened)  

            **Regulatory / Export Constraints:**  
            - USDA & FDA compliant  
            - SENASICA phytosanitary certification for avocado exports  

            **Target Markets & Channels:**  
            - B2B: Foodservice distributors, restaurants, guacamole manufacturers  
            - B2C: Retail frozen sections (supermarkets, specialty stores)  
            - E-commerce: Online grocery and meal prep platforms  

            **Incoterms & Transport:**  
            - Preferred: DAP (Laredo TX, Dallas, Chicago) / FCA (Guadalajara or Uruapan plant)  
            - Transport Mode: Refrigerated trucking (-18°C continuous cold chain)  

            **Estimated Selling Price:**  
            - Wholesale (FCA): USD $9.00 per 500 g  
            - Retail (DAP): USD $11 per 500 g  
            """
        )
    with col2:
        st.image(
            "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/avocado_pulp1.jpg",
            width=500,
            caption="Frozen Avocado Pulp"
        )

    st.markdown("---")

    # PRODUCTO 2 – MANGO CUBES IQF
    st.subheader("Product 2 – Mango Cubes IQF (Individually Quick Frozen) 🥭")
    st.markdown(
        """
        ### Description  
        Naturally sweet, hand-cut mango cubes from Mexican Kent.  
        Individually quick-frozen (IQF) to preserve flavor, color, and texture.  
        Ideal for smoothies, desserts, and bulk foodservice use.
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(
            """
            ### Key Specifications  
            - **Ingredients:** 100% mango  
            - **Processing:** Washed, diced, and IQF frozen at -18°C  
            - **Net Weight:** 1 kg  

            **Packaging:**  
            - Primary: Transparent resealable LDPE pouch  
            - Secondary: Corrugated box (10 pouches per case)  
            - Dimensions (Retail Unit): 25 × 20 × 6 cm  
            - Gross Weight: 1.05 kg  

            **Labeling Requirements:**  
            - Product name, net weight, nutritional information, batch code  
            - “Keep Frozen (-18°C)”  
            - Country of origin: Mexico  
            - Shelf Life: 24 months (frozen)  

            **Regulatory / Export Constraints:**  
            - Must meet U.S. FDA and CFIA labeling requirements  
            - Phytosanitary certificate (SENASICA)  

            **Target Markets & Channels:**  
            - B2B: Smoothie producers, hotels, airlines, institutional catering  
            - B2C: Supermarkets, health food stores, frozen fruit brands  
            - E-commerce: Subscription boxes and meal prep kits  

            **Incoterms & Transport:**  
            - Preferred: FCA (Guadalajara or Michoacán processing facility) / DAP (Houston, Toronto)  
            - Transport Mode: Reefer trucking (-18°C)  

            **Estimated Selling Price:**  
            - Wholesale (FCA): USD $12 per 1 kg  
            - Retail (DAP): USD $15 per 1 kg  
            """
        )
    with col2:
        st.image(
            "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/mango_cubes.jpg",
            width=500,
            caption="Mango Cubes IQF"
        )

    st.markdown("---")

    # PRODUCTO 3 – READY-TO-EAT SALADS
    st.subheader("Product 3 – Ready-to-Eat Salads 🥬")
    st.markdown(
        """
        ### Description  
        Fresh, pre-washed salad mixes combining Mexican leafy greens, cherry tomatoes, shredded carrots,  
        and optional dressings. Designed for healthy convenience, with a crisp, garden-fresh taste.  
        Packaged in recyclable bowls.
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(
            """
            ### Key Specifications  
            - **Ingredients:** Lettuce, spinach, tomato, carrot, dressing (Separate)  
            - **Processing:** Triple-washed, packed under modified atmosphere (MAP)  
            - **Net Weight:** 250 g  

            **Packaging:**  
            - Primary: Clear PET bowl with tamper-proof lid  
            - Secondary: Recyclable cardboard sleeve  
            - Dimensions: 18 cm diameter × 5 cm height  
            - Gross Weight: 0.27 kg  

            **Labeling Requirements:**  
            - Product name, expiration date, ingredients, allergens  
            - “Keep Refrigerated (2–4°C)”  
            - Country of origin: Mexico  
            - Shelf Life: 5 days (refrigerated)  

            **Regulatory / Export Constraints:**  
            - HACCP and ISO 22000 certification required  
            - U.S. FDA registration for ready-to-eat produce  

            **Target Markets & Channels:**  
            - B2B: Corporate cafeterias, airlines, hotels, convenience chains  
            - B2C: Urban consumers via supermarkets and grab-and-go fridges  
            - E-commerce: Local meal delivery and healthy-living platforms  

            **Incoterms & Transport:**  
            - Preferred: DAP (Laredo or San Antonio distribution hub) / FCA (Hermosillo plant)  
            - Transport Mode: Refrigerated trucking (2–4°C, insulated crates)  

            **Estimated Selling Price:**  
            - Wholesale (FCA): USD $2.50 per 250 g  
            - Retail (DAP): USD $3.80 per 250 g  
            """
        )
    with col2:
        st.image(
            "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/salads.jpg",
            width=500,
            caption="Ready-to-Eat Salads"
        )

    st.markdown("---")


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
#=====
# SECCIÓN: LOGÍSTICA (COMPLETA DEL PDF)
# =================================
elif menu == "🚛 Logistics":
    st.title("Supply Chain & Logistics")
    
    st.markdown("---")
    st.markdown("### Explanatory Paragraph")
    st.markdown(
        """
        At **Aurora Fresh Foods**, our logistics network is meticulously designed to maintain the highest levels of freshness, quality, and efficiency throughout the supply chain.  
        The journey begins with sourcing premium, fresh produce from the best farms in Michoacán and Jalisco, known for their rich agricultural heritage.  
        Once the produce arrives, it is carefully processed and packaged in our state-of-the-art facility in Monterrey, where we maintain rigorous standards of hygiene and quality.  
        After packaging, the products are transported using refrigerated trucks to ensure temperature control and prevent spoilage.

        The next critical stage of the process occurs at our **cross-docking hub in Laredo, TX**.  
        Here, shipments are efficiently consolidated, inspected, and redistributed to U.S. and Canadian clients with minimal delays.  
        This cross-docking model is key to reducing inventory holding, accelerating the flow of goods, and minimizing storage costs.  
        By combining refrigerated trucking with strategic cross-docking, we ensure that products are delivered to our customers in the best possible condition and at an optimal speed, reducing lead time while keeping logistics costs low.
        """
    )

    
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

      # --- Interactive Plotly Bar Chart: Warehouse Equipment Alternatives ---
    import pandas as pd
    import plotly.graph_objects as go

    # Datos
    data = {
        "Warehouse Equipment Alternatives": [
            "Automated Storage/Retrieval System (AS/RS)",
            "Conveyor + Picking System",
            "Drive-in Racks + Reach Trucks",
            "Selective Racks + Counterbalance Forklifts"
        ],
        "Weighted Score": [1.0, 0.9, 0.7, 0.65]
    }

    df = pd.DataFrame(data)
    colors = ["#A7D78D", "#F2C94C", "#56CCF2", "#F2994A"]

    # Crear figura
    fig = go.Figure(
        data=[
            go.Bar(
                x=df["Warehouse Equipment Alternatives"],
                y=df["Weighted Score"],
                marker_color=colors,
                text=df["Weighted Score"],
                textposition="auto",
                textfont=dict(size=22, color="#000000"),
                hovertemplate="<b>%{x}</b><br>Weighted Score: %{y}<extra></extra>"
            )
        ]
    )

    # Layout corregido (centrado real)
    fig.layout = go.Layout(
        title="<b>Warehouse Equipment Alternatives Comparison</b>",
        title_font=dict(size=32, family="Segoe UI, sans-serif", color="#2b3a2e"),
        title_x=0.5,  # centra el título en el ancho de la gráfica
        title_xanchor="center",  # asegura que el centro del título sea el punto de referencia
        xaxis=dict(
            title="<b>Warehouse Equipment Alternatives</b>",
            title_font=dict(size=22),
            tickangle=35,
            tickfont=dict(size=18),
            showline=True,
            linecolor="#999",
            automargin=True  # ✅ evita que las etiquetas largas empujen el título
        ),
        yaxis=dict(
            title="<b>Weighted Score</b>",
            title_font=dict(size=22),
            tickfont=dict(size=18),
            range=[0, 1.05],
            showgrid=True,
            gridcolor="rgba(0,0,0,0.1)",
            automargin=True
        ),
        plot_bgcolor="white",
        paper_bgcolor="#f5ebd8",
        margin=dict(l=100, r=100, t=160, b=200),  # márgenes balanceados
        height=700,
        width=1600
    )

    # Mostrar gráfica centrada y grande
    st.plotly_chart(
        fig,
        use_container_width=False,
        config={"displayModeBar": True},
    )

    # Datos exactos de la tabla AQUI EMPIEZA LA TABLA DE LA GRAFICA 
      # --- Equipment Alternatives Comparison Table (Styled using st.table) ---
    st.table({
        "Equipment Alternative": [
            "Selective Racks + Counterbalance Forklifts",
            "Drive-in Racks + Reach Trucks",
            "Conveyor + Picking System",
            "Automated Storage/Retrieval System (AS/RS)"
        ],
        "Initial Investment (USD)": [
            "100,000", "150,000", "120,000", "500,000"
        ],
        "Maintenance Cost (USD/year)": [
            "5,000", "6,000", "7,000", "10,000"
        ],
        "Space Utilization (%)": [
            "75%", "85%", "90%", "95%"
        ],
        "Efficiency Rating (1–10)": [
            6, 8, 9, 10
        ],
        "Throughput (units/day)": [
            500, 400, 700, 800
        ]
    })
#TABLA DE DIMENSIONES DEL CAMION
    # --- Dimension Calculations Tables ---
    st.markdown("<h3 style='text-align:center;'><b>Dimension Calculations per Product</b></h3>", unsafe_allow_html=True)

    # ---------- AVOCADO ----------
    st.markdown("### 🥑 Avocado")
    st.table({
        "Item": [
            "TRUCK CAPACITY",
            "BOX WEIGHT (20 BAGS)",
            "BOX PER TRUCK",
            "BOX DIMENSION 40×25×20 cm",
            "TOTAL BOX DIMENSION",
            "TRUCK CUBIC CAPACITY",
            "ROOM LEFT",
            "ACHIEVABLE!!",
            "Total unit per truck"
        ],
        "Value": [
            "25,000 KG",
            "10 KG",
            "2,500",
            "0.02 M³",
            "50.00 M³",
            "90.00 M³",
            "40.00 M³",
            "✔️ ACHIEVABLE!!",
            "50,000"
        ]
    })

    st.markdown("---")

    # ---------- MANGO CUBES ----------
    st.markdown("### 🥭 Mango Cubes")
    st.table({
        "Item": [
            "TRUCK CAPACITY",
            "BOX WEIGHT (10 BAGS)",
            "BOX PER TRUCK",
            "BOX DIMENSION 45×30×25 cm",
            "TOTAL BOX DIMENSION",
            "TRUCK CUBIC CAPACITY",
            "ROOM LEFT",
            "ACHIEVABLE!!",
            "Total unit per truck"
        ],
        "Value": [
            "25,000 KG",
            "10 KG",
            "2,000 M³ LIMITED",
            "0.034 M³",
            "67.50 M³",
            "90.00 M³",
            "22.50 M³",
            "✔️ ACHIEVABLE!!",
            "20,000"
        ]
    })

    st.markdown("---")

    # ---------- SALADS ----------
    st.markdown("### 🥬 Salads")
    st.table({
        "Item": [
            "TRUCK CAPACITY",
            "BOX WEIGHT (20 BAGS)",
            "BOX PER TRUCK",
            "BOX DIMENSION 40×40×30 cm",
            "TOTAL BOX DIMENSION",
            "TRUCK CUBIC CAPACITY",
            "ROOM LEFT",
            "ACHIEVABLE!!",
            "Total unit per truck"
        ],
        "Value": [
            "25,000 KG",
            "5 KG",
            "1,500 M³ LIMITED",
            "0.05 M³",
            "72.00 M³",
            "90.00 M³",
            "18.00 M³",
            "✔️ ACHIEVABLE!!",
            "30,000"
        ]
    })

    st.markdown("---")
     # --- KPI’S SECTION ---
    st.markdown("<h2 style='text-align:center; color:#2b3a2e;'><b>KPI’s: The Foundation of Continuous Improvement with Our Clients</b></h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:17px;'>We continuously monitor, analyze, and optimize our logistics processes to ensure better service performance and customer satisfaction.</p>", unsafe_allow_html=True)

    # Display the three KPI images (one below the other)
    st.image("https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Escenarios1.png", caption="Scenario 1 - Productivity KPIs", use_container_width=True)
    st.image("https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Escenarios2.png", caption="Scenario 2 - Efficiency KPIs", use_container_width=True)
    st.image("https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Escenarios3.png", caption="Scenario 3 - Global Performance KPIs", use_container_width=True)

    #LAYOUT PART
    # 🔹 Título centrado + espacio extra
    st.markdown(
    "<h2 style='text-align:center; color:#2b3a2e; margin-top:25px; margin-bottom:40px;'><b>Warehousing, Layout & Equipment Selection</b></h2>",
    unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='text-align:center;'>
        Conveyor System is the best choice for Aurora Fresh Foods due to its balance of high efficiency, low operating costs, and suitability for a U-shape warehouse layout. The conveyor system requires fewer trips, reducing labor costs, and optimizing space, making it the most cost-effective solution in the long run.
        </p>
        """,
        unsafe_allow_html=True
    )

    # 🔹 Alternatives + Layout side by side
    col1, col2 = st.columns(2)
    with col1:
        st.image(
            "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Alternatives.png",
            caption="Equipment Alternatives",
            use_container_width=True
        )
    with col2:
        st.image(
            "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Layout.png",
            caption="Warehouse Layout (U-shape)",
            use_container_width=True
        )

    st.markdown(
        """
        <p style='text-align:center;'>
            <span style='font-size:19px; font-weight:bold;'>
                Benefits of Using a Conveyor System in a U-shape Warehouse:
            </span><br><br>
            The U-shape layout maximizes warehouse space, facilitating smooth material flow, while the conveyor can easily fit within this layout, transporting items from one end of the warehouse to the other.<br><br>
            Conveyors reduce the need for manual labor compared to forklifts or pallet jacks, minimizing the risk of accidents and fatigue. This improves safety and helps save costs on personnel.<br><br>
            The conveyor system supports a continuous flow of goods without delays, which is essential for keeping up with the high-volume demands of the avocado business.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.image(
        "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Altcost.png",
        caption="Equipment Cost Comparison",
        use_container_width=True
    )

    #END OF LAYOUT PART

elif menu == "💰 Finance":
    # --- PROFIT AND LOSSES SECTION (SIDE BY SIDE) ---
    st.markdown("<h2 style='text-align:center; color:#2b3a2e;'><b>Profit Analysis</b></h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    # -------- LEFT SIDE: Profit and Losses --------
    with col1:
        st.markdown("<h3 style='text-align:center; color:#2b3a2e;'><b>Profit and Losses</b></h3>", unsafe_allow_html=True)
        st.image(
            "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Profit.png",
            caption="Profit and Losses Overview",
            use_container_width=True
        )

        # ✅ Conclusión movida aquí debajo de la imagen “Profit”
        st.markdown("<h4 style='text-align:center; color:#2b3a2e;'>Conclusions</h4>", unsafe_allow_html=True)
        st.markdown(
            """
            <p style='text-align:justify; font-size:16px; color:#333333;'>
            The <b>profit margin</b> would drop to <b>5%</b> if all of these 5 effects occurred simultaneously.  
            A key takeaway is the <b>significant impact freight costs</b> have on overall profitability — indicating that
            freight optimization and negotiation should be a priority to <b>maximize profits</b>.
            </p>
            """,
            unsafe_allow_html=True
        )

    # -------- RIGHT SIDE: Profit and Losses with Scenarios --------
    with col2:
        st.markdown("<h3 style='text-align:center; color:#2b3a2e;'><b>Profit and Losses with Scenarios</b></h3>", unsafe_allow_html=True)

        # Imagen principal de escenarios
        st.image(
            "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Profit2.png",
            caption="Profit and Losses with Scenarios",
            use_container_width=True
        )

        # Tabla de los 5 impactos (colores)
        st.markdown("<h4 style='color:#2b3a2e;'>5 IMPACTS</h4>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="background-color:#E8F5E9; padding:8px; font-size:15px;"><b>1 - INCREASE OF 20% IN THE FREIGHT FOR ALL THE PRODUCTS</b></div>
            <div style="background-color:#E3F2FD; padding:8px; font-size:15px;"><b>2 - DOUBLE AMOUNT INVESTED IN EQUIPMENT, RESULTING IN DOUBLE DEPRECIATION</b></div>
            <div style="background-color:#FFEB3B; padding:8px; font-size:15px;"><b>3 - INCREASE IN 30% IN INDIRECT LABOR</b></div>
            <div style="background-color:#CFD8DC; padding:8px; font-size:15px;"><b>4 - INCREASE IN 20% IN INSURANCE</b></div>
            <div style="background-color:#0288D1; padding:8px; font-size:15px; color:white;"><b>5 - PAYING HIGHER RENT BY 10%</b></div>
            """,
            unsafe_allow_html=True
        )

    # END OF PROFIT AND LOSSES SECTION
    st.markdown("---")


    # =================================
    # COST ANALYSIS SECTION
    # =================================
    st.markdown("<h2 style='text-align:center; color:#2b3a2e; font-size:34px;'><b>Cost Analysis by Product</b></h2>", unsafe_allow_html=True)

    # -------- FIRST ROW: Cost1 and Cost2 --------
    col1, col2 = st.columns(2, gap="large")

    # LEFT SIDE (Cost1)
    with col1:
        st.image(
            "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Cost1.png",
            caption="Avocado Cost Impact",
            use_container_width=True
        )
        st.markdown(
            """
            <p style='font-size:16px; color:#333333; margin-top:10px;'>
            <b>Impact:</b> Increase in freight price (20%) = <b>$0.14</b><br>
            <i>*Since there are 50,000 pieces per truck.</i>
            </p>
            """,
            unsafe_allow_html=True
        )

    # RIGHT SIDE (Cost2)
    with col2:
        st.image(
            "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Cost2.png",
            caption="Mango Cubes Cost Impact",
            use_container_width=True
        )
        st.markdown(
            """
            <p style='font-size:16px; color:#333333; margin-top:10px;'>
            <b>Impact:</b> Increase in freight price (20%) = <b>$0.35</b><br>
            <i>*Since there are 20,000 pieces per truck.</i>
            </p>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # -------- SECOND ROW: Cost3 (image on right, text on left) --------
    col_left, col_right = st.columns(2, gap="large")

    # LEFT SIDE (Text)
    with col_left:
        st.markdown(
            """
            <h4 style='color:#2b3a2e;'>Salads Cost Impact</h4>
            <p style='font-size:16px; color:#333333; margin-top:10px;'>
            <b>Impact:</b> Increase in freight price (20%) = <b>$0.21</b><br>
            <i>*Since there are 30 units per truck.</i><br><br>
            - Cheaper transport for lighter weight.<br>
            - Product with the lowest profit margin.
            </p>
            """,
            unsafe_allow_html=True
        )

    # RIGHT SIDE (Cost3 image)
    with col_right:
        st.image(
            "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Cost3.png",
            caption="Salads Cost Impact",
            use_container_width=True
        )
    
    # --- FINANCIAL & OPERATIONAL CONSIDERATIONS ---
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

     # ---- EXCEL SECTION ----
    st.markdown(
        """
        <div style="background-color:#e0f5e0;padding:20px;border-radius:10px;">
            <h3 style="color:#006400;margin-top:0;">
                Here you can access our Excel file with the required information.
            </h3>
            <div style="text-align:center; margin-top:10px;">
                <a href="https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/AURORA%20FOODS%20COSTS.xlsx" download>
                    <button style="background-color:#008000;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;font-size:16px;margin-top:10px;">
                        Download Excel
                    </button>
                </a>
            </div>  
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

elif menu == "🗺️ Routes":
    st.title("Routes")

    # ---------- TRANSPORTATION COST ANALYSIS ----------
    st.markdown(
        "<h2 style='text-align:center; color:#2b3a2e;'><b>Transportation Cost Analysis & Route Methodology</b></h2>",
        unsafe_allow_html=True
    )

    st.markdown("""
The transportation cost analysis was built using a straightforward, two-step methodology:

First, the point-to-point distances between each origin city and each destination market were sourced from the internet (Google Maps).

Second, the total truck cost for each product route was divided by these pre defined distances to calculate a unique cost per kilometer for every single origin and destination pair. 

This is why the cost per kilometer varies between routes, it is not a single flat rate but a direct reflection of the total cost allocated over the specific distance for that route.

Essentially, we calculated the per kilometer rate from the total cost and the distance for each route.
""")

    # 1) Line.png
    st.markdown(
        "<h3 style='text-align:center; color:#2b3a2e;'><b>Distribution Distances & Avocado Route Cost per km</b></h3>",
        unsafe_allow_html=True
    )
    st.image(
        "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Line.png",
        use_container_width=True
    )

    # 2) Trans1.png
    st.markdown(
        "<h3 style='text-align:center; color:#2b3a2e;'><b>Warehouse Supply Line – Scenarios 1 & 2</b></h3>",
        unsafe_allow_html=True
    )
    st.image(
        "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Trans1.png",
        use_container_width=True
    )

    # 3) Trans2.png
    st.markdown(
        "<h3 style='text-align:center; color:#2b3a2e;'><b>Warehouse Supply Line – Scenarios 3 & 4</b></h3>",
        unsafe_allow_html=True
    )
    st.image(
        "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Trans2.png",
        use_container_width=True
    )

    # 4) Supply.png
    st.markdown(
        "<h3 style='text-align:center; color:#2b3a2e;'><b>Supply Allocation from Consolidation Centers</b></h3>",
        unsafe_allow_html=True
    )
    st.image(
        "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Supply1.png",
        use_container_width=True
    )

    # 5) Demand1.png
    st.markdown(
        "<h3 style='text-align:center; color:#2b3a2e;'><b>Demand by Destination Centers</b></h3>",
        unsafe_allow_html=True
    )
    st.image(
        "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Demand11.png",
        use_container_width=True
    )

    # 6) Demand2.png
    st.image(
        "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Demand12.png",
        use_container_width=True
    )

    # 7) Totaltranscost.png
    st.markdown(
        "<h3 style='text-align:center; color:#2b3a2e;'><b>Total Transportation Cost – Northwest Corner Solution</b></h3>",
        unsafe_allow_html=True
    )
    st.image(
        "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Totaltranscost1.png",
        use_container_width=True
    )

    st.markdown("""
The analysis of the three scenarios reveals a clear hierarchy in logistics challenges. Avocados represent a high-volume, high-cost operation, with expenses driven by the massive demand in major hubs like New York and Chicago. Mangoes demonstrate a more cost-efficient model, with nearly half the transportation cost of avocados due to optimized routes and lower total volume. 

For instance, shipments from Hermosillo to Phoenix cost $60.34, while those from Guadalajara to Seattle cost $9.59. This reflects the reliance on Mexican producing regions to supply the U.S. market, with costs increasing for distant destinations such as the Northeast.

However, salads emerge as the most logistically demanding and expensive product, combining the highest volume with the inherent challenges of transporting a bulky, perishable item. This leads to the highest total transportation cost.

The key takeaway is that for fresh produce, product characteristics (perishability, bulk) are as critical as volume and distance in determining cost. Strategic origin selection and route optimization are paramount, especially for time-sensitive goods, to minimize expenses and maintain quality.
""")

    # ---------- DIRECT & INDIRECT ROUTES COMPARISON ----------
    st.markdown(
        "<h2 style='text-align:center; color:#2b3a2e;'><b>Direct and Indirect Distribution Routes Comparison</b></h2>",
        unsafe_allow_html=True
    )

    # 🔹 Direct routes
    st.markdown(
        "<h3 style='text-align:center; color:#2b3a2e;'><b>Direct Routes: West & East Long-Haul Corridors</b></h3>",
        unsafe_allow_html=True
    )
    st.image(
        "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Routes1.png",
        use_container_width=True
    )
    st.image(
        "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Routes2.png",
        use_container_width=True
    )

    # 🔹 Indirect routes
    st.markdown(
        "<h3 style='text-align:center; color:#2b3a2e;'><b>Indirect Routes: Multi-Node Distribution via Laredo, TX</b></h3>",
        unsafe_allow_html=True
    )
    st.image(
        "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Routes3.png",
        use_container_width=True
    )
    st.image(
        "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Routes4.png",
        use_container_width=True
    )

    st.markdown("""
This analysis compares four distinct freight distribution routes connecting Mexican production centers with North American markets, evaluating total distance and network efficiency for Aurora Foods transportation logistics.

**Direct routes analysis:**

Route 1 is 23% more efficient (1,630 km shorter) than Route 2.

It benefits from geographical proximity, more direct highway connections, and optimized border crossings, making it the undisputed best choice for a direct, long-haul shipment.
""")

    st.markdown("""
In conclusion, **Route 1 provides the perfect balance of lowest cost, highest speed, and operational reliability**, making it the most effective logistics chain for direct avocado distribution from Mexico to key North American markets and is the one we are going for in this project.
""")
        
    st.markdown(
        """
        <div style="background-color:#e0f5e0;padding:20px;border-radius:10px;">
            <h3 style="color:#006400;margin-top:0;">
                Here you can access our Excel file with the required information.
            </h3>
            <div style="text-align:center; margin-top:10px;">
                <a href="https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/ROUTE%20DESIGNNEW.xlsx" download>
                    <button style="background-color:#008000;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;font-size:16px;margin-top:10px;">
                        Routes Design
                    </button>
                </a>
            </div>
            <div style="text-align:center; margin-top:10px;">
                <a href="https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Cost%20Supply1.xlsx" download>
                    <button style="background-color:#008000;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;font-size:16px;margin-top:10px;">
                        Cost Supply
                    </button>
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
elif menu == "🧾 Contact":
    st.markdown("---")

    # CONTACT SECTION
    st.markdown(
        "<h2 style='text-align:center; color:#2b3a2e;'><b>Contact & Legal Information</b></h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:left; color:#2b3a2e; font-size:20px;'><b>Contact / Legal</b></h3>",
        unsafe_allow_html=True
    )

    st.markdown("""
    **Email Address** contact@aurorafreshfoods.com  
    **Phone Number** 3338543245  

    **Facebook:** https://www.facebook.com/AuroraFreshFoods  
    **Instagram:** https://www.instagram.com/AuroraFreshFoods  
    **Twitter:** https://www.twitter.com/AuroraFreshFoods  
    **LinkedIn:** https://www.linkedin.com/company/aurorafreshfoods  
    **YouTube:** https://www.youtube.com/c/AuroraFreshFoods
    """)

    # --- Privacy Policy ---
    st.markdown(
        "<h3 style='text-align:left; color:#2b3a2e; font-size:20px; margin-top:25px;'><b>Privacy Policy</b></h3>",
        unsafe_allow_html=True
    )

    st.markdown("""
    At Aurora Fresh Foods, we are committed to protecting your privacy. This privacy policy outlines how we collect, use, and protect your personal data when you visit our website or use our services.

    1. **Information We Collect**  
    We collect personal information such as your name, email address, phone number, and any other information you provide through our contact form or during the use of our services.

    2. **How We Use Your Information**  
    We use the information we collect to respond to your inquiries, provide our services, and improve your user experience.

    3. **Data Protection**  
    We take reasonable measures to protect your data from unauthorized access, alteration, or disclosure. However, no method of transmission over the internet is 100% secure.

    4. **Cookies**  
    We use cookies to enhance your experience on our website. By using our website, you consent to our use of cookies.

    5. **Your Rights**  
    You have the right to access, correct, or delete your personal data. If you would like to exercise these rights, please contact us at contact@aurorafreshfoods.com.

    6. **Changes to Privacy Policy**  
    We reserve the right to update this privacy policy at any time. Any changes will be posted on this page.
    """)

    # --- Disclaimer ---
    st.markdown(
        "<h3 style='text-align:left; color:#2b3a2e; font-size:20px; margin-top:25px;'><b>Disclaimer</b></h3>",
        unsafe_allow_html=True
    )

    st.markdown("""
    The information provided on this website is for general informational purposes only. While we strive to ensure the accuracy and completeness of the information, Aurora Fresh Foods makes no representations or warranties of any kind, express or implied, about the accuracy, reliability, or availability of the information on this website.  

    Aurora Fresh Foods is not responsible for any losses or damages that may occur from the use of information from this website, including but not limited to, direct, indirect, or consequential losses.  

    By using this website, you agree to the terms of this disclaimer and our privacy policy.
    """)
    
elif menu == "Infographic":

    # Fondo tipo infografía solo alrededor de las imágenes
    st.markdown(
        """
        <div style="background-color:#0b3f33;padding-top:20px;padding-bottom:30px;">
        """,
        unsafe_allow_html=True
    )

    # Primera mitad de la infografía
    st.image(
        "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Info1.png",
        use_container_width=True
    )

    # Segunda mitad, lo más pegada posible a la primera
    st.image(
        "https://raw.githubusercontent.com/gemelogascon-lang/cross-docking-app/main/images/Info2.png",
        use_container_width=True
    )

    # Cerrar el div del fondo
    st.markdown("</div>", unsafe_allow_html=True)
