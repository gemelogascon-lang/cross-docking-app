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
    ["🏠 Home", "🥭 Products", "🚛 Logistics", "💰 Finance", "🧾 Conclusion", "📊 Downloads"]
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
            - Preferred: DAP (Laredo TX, Dallas, Chicago) / FCA (Guadalajara or Querétaro plant)  
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
            - Preferred: DAP (Laredo or San Antonio distribution hub) / FCA (Querétaro plant)  
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
#TABLA PROFIT AND LOSSES
st.markdown("### Profit and Losses Table (Nov 25 Estimate)")
    
    # --- Estilo CSS para la tabla de P&L ---
    st.markdown(
        """
        <style>
        .pnl-table table {
            width: 100%;
            border-collapse: collapse;
            background-color: #fffaf0; /* Fondo más claro para la tabla */
            border-radius: 10px;
            overflow: hidden;
            margin-top: 20px;
        }
        .pnl-table th, .pnl-table td {
            border: 1px solid #00000033;
            padding: 8px 10px;
            text-align: left; /* Alineación por defecto a la izquierda para texto */
            font-size: 14px;
        }
        .pnl-table th {
            background-color: #e9dbc0;
            color: #1f1f1f;
            font-weight: bold;
            text-align: center; /* Encabezados centrados */
        }
        .pnl-table .header-row th {
            background-color: #d6c7a1; /* Encabezado de sección */
            font-size: 16px;
        }
        .pnl-table .subtotal-row td {
            font-weight: bold;
            background-color: #f2e6d0; /* Fondo para totales */
            border-top: 2px solid #2b3a2e;
        }
        .pnl-table .net-profit-row td {
            font-weight: bold;
            background-color: #a7c957; /* Fondo verde para utilidad neta */
            color: white;
            border-top: 3px solid #2b3a2e;
        }
        .pnl-table .category-col {
            text-align: right;
            font-weight: bold;
        }
        .pnl-table .percentage-col {
            text-align: center;
            font-weight: bold;
        }
        .pnl-table .unit-price-col {
            text-align: right;
        }
        .pnl-table .total-col {
            text-align: right;
        }
        .pnl-table .total-unit-cost {
            font-weight: bold;
            background-color: #f8efe0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # --- DATA & RENDERING ---
    # Nota: Los valores de la tabla se codifican directamente en HTML
    st.markdown(
        """
        <div class="pnl-table">
        <table>
            <!-- Título y Unidades -->
            <thead>
                <tr class="header-row">
                    <th colspan="3" style="text-align:left;">PROFIT AND LOSSES</th>
                    <th colspan="2" style="text-align:right;">November 25</th>
                </tr>
                <tr>
                    <td colspan="3" style="font-weight:bold;">TOTAL UNITS</td>
                    <td colspan="2" style="text-align:right;">200,000</td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="padding-left: 20px;">AVOCADO</td>
                    <td colspan="2">100,000</td>
                    <td colspan="2"></td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">MANGO</td>
                    <td colspan="2">40,000</td>
                    <td colspan="2"></td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">SALADS</td>
                    <td colspan="2">60,000</td>
                    <td colspan="2"></td>
                </tr>
                
                <!-- SECCIÓN DE VENTAS -->
                <tr class="header-row">
                    <th style="text-align:left;">SALES</th>
                    <th>Unit Price</th>
                    <th class="total-col">TOTAL</th>
                    <th colspan="2"></th>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Avocado</td>
                    <td class="unit-price-col">$ 9.00</td>
                    <td class="total-col">$ 900,000.00</td>
                    <td colspan="2"></td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Mango</td>
                    <td class="unit-price-col">$ 12.00</td>
                    <td class="total-col">$ 480,000.00</td>
                    <td colspan="2"></td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Salads</td>
                    <td class="unit-price-col">$ 2.50</td>
                    <td class="total-col">$ 150,000.00</td>
                    <td colspan="2"></td>
                </tr>
                
                <!-- TOTAL SALES -->
                <tr class="subtotal-row">
                    <td style="text-align:left;">TOTAL SALES</td>
                    <td></td>
                    <td class="total-col">$ 1,530,000.00</td>
                    <td colspan="2">Category (COGS / OPEX)</td>
                </tr>

                <!-- SECCIÓN COGS -->
                <tr class="header-row">
                    <th style="text-align:left;">COGS</th>
                    <th></th>
                    <th class="total-col">TOTAL</th>
                    <th colspan="2"></th>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Avocado</td>
                    <td class="unit-price-col">$ 3.69</td>
                    <td class="total-col">$ 369,000.00</td>
                    <td colspan="2" style="text-align:center;">COGS</td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Mango</td>
                    <td class="unit-price-col">$ 4.77</td>
                    <td class="total-col">$ 190,800.00</td>
                    <td colspan="2" style="text-align:center;">COGS</td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Salads</td>
                    <td class="unit-price-col">$ 2.01</td>
                    <td class="total-col">$ 120,448.00</td>
                    <td colspan="2" style="text-align:center;">COGS</td>
                </tr>

                <!-- GROSS PROFIT -->
                <tr class="subtotal-row">
                    <td style="text-align:left;">GROSS PROFIT</td>
                    <td></td>
                    <td class="total-col">$ 849,752.00</td>
                    <td colspan="2" class="percentage-col">56%</td>
                </tr>
                
                <!-- SECCIÓN OPEX -->
                <tr class="header-row">
                    <th style="text-align:left;"></th>
                    <th>PER UNIT</th>
                    <th class="total-col">TOTAL</th>
                    <th colspan="2"></th>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Depreciation</td>
                    <td class="unit-price-col">$ 1.50</td>
                    <td class="total-col">$ 300,000.00</td>
                    <td colspan="2" style="text-align:center;">OPEX</td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Indirect Labor ( per unit )</td>
                    <td class="unit-price-col">$ 0.33</td>
                    <td class="total-col">$ 65,000.00</td>
                    <td colspan="2" style="text-align:center;">OPEX</td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Custom Broker Fee</td>
                    <td class="unit-price-col">$ 0.01</td>
                    <td class="total-col">$ 1,050.00</td>
                    <td colspan="2" style="text-align:center;">COGS</td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Taxation and Rights</td>
                    <td class="unit-price-col">$ -</td>
                    <td class="total-col">$ -</td>
                    <td colspan="2"></td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Import Freight</td>
                    <td class="unit-price-col">$ -</td>
                    <td class="total-col">$ -</td>
                    <td colspan="2"></td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Export Freight</td>
                    <td class="unit-price-col">$ -</td>
                    <td class="total-col">$ -</td>
                    <td colspan="2"></td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Handling</td>
                    <td class="unit-price-col">$ 0.02</td>
                    <td class="total-col">$ 4,300.00</td>
                    <td colspan="2" style="text-align:center;">COGS</td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Customs Warehouse</td>
                    <td class="unit-price-col">$ 0.00</td>
                    <td class="total-col">$ 900.00</td>
                    <td colspan="2" style="text-align:center;">COGS</td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Rent ( total units) per month</td>
                    <td class="unit-price-col">$ 0.02</td>
                    <td class="total-col">$ 3,000.00</td>
                    <td colspan="2" style="text-align:center;">OPEX</td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Energy (total units) per month</td>
                    <td class="unit-price-col">$ 0.01</td>
                    <td class="total-col">$ 1,500.00</td>
                    <td colspan="2" style="text-align:center;">OPEX</td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Water (total unit) per month</td>
                    <td class="unit-price-col">$ 0.00</td>
                    <td class="total-col">$ 400.00</td>
                    <td colspan="2" style="text-align:center;">OPEX</td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">ERP License (total unit) per month</td>
                    <td class="unit-price-col">$ 0.00</td>
                    <td class="total-col">$ 300.00</td>
                    <td colspan="2" style="text-align:center;">OPEX</td>
                </tr>
                <tr>
                    <td style="padding-left: 20px;">Insurance</td>
                    <td class="unit-price-col">$ 0.01</td>
                    <td class="total-col">$ 1,800.00</td>
                    <td colspan="2"></td>
                </tr>

                <!-- TOTAL COGS AND OPEX -->
                <tr class="subtotal-row">
                    <td style="text-align:left;">TOTAL COGS AND OPEX</td>
                    <td></td>
                    <td class="total-col">$ 378,250.00</td>
                    <td colspan="2"></td>
                </tr>

                <!-- EBIT -->
                <tr class="subtotal-row">
                    <td style="text-align:left;">EBIT</td>
                    <td></td>
                    <td class="total-col">$ 471,502.00</td>
                    <td colspan="2" class="percentage-col">31%</td>
                </tr>

                <!-- TAX -->
                <tr class="subtotal-row">
                    <td style="text-align:left;">TAX</td>
                    <td></td>
                    <td class="total-col">$ 141,450.60</td>
                    <td colspan="2"></td>
                </tr>
                
                <!-- NET PROFIT -->
                <tr class="net-profit-row">
                    <td style="text-align:left;">NET PROFIT</td>
                    <td></td>
                    <td class="total-col">$ 330,051.40</td>
                    <td colspan="2" class="percentage-col">22%</td>
                </tr>
            </tbody>
        </table>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- TABLA INFERIOR DE COSTOS UNITARIOS ---
    st.markdown("---")
    st.markdown("### Total Unit Cost Analysis")
    st.markdown(
        """
        <div class="pnl-table">
        <table>
            <tbody>
                <tr class="total-unit-cost">
                    <td style="font-weight:bold;">TOTAL UNIT COST</td>
                    <td class="unit-price-col"></td>
                    <td colspan="3"></td>
                </tr>
                <tr class="total-unit-cost">
                    <td style="padding-left: 20px;">TOTAL FIXED COST PER UNIT</td>
                    <td class="unit-price-col">$ 1.89</td>
                    <td colspan="3"></td>
                </tr>
                <tr class="total-unit-cost">
                    <td style="padding-left: 20px;">TOTAL COST PER UNIT AVOCADO</td>
                    <td class="unit-price-col">$ 5.58</td>
                    <td colspan="3"></td>
                </tr>
                <tr class="total-unit-cost">
                    <td style="padding-left: 20px;">TOTAL COST PER UNIT MANGO</td>
                    <td class="unit-price-col">$ 6.86</td>
                    <td colspan="3"></td>
                </tr>
                <tr class="total-unit-cost">
                    <td style="padding-left: 20px;">TOTAL COST PER UNIT SALAD</td>
                    <td class="unit-price-col">$ 3.90</td>
                    <td colspan="3">Salad is not a great product, after adding the fixed cost, our cost is higher than our selling price</td>
                </tr>
            </tbody>
        </table>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    st.markdown(
        """
        **Fuel and Refrigeration Costs:** - Fuel: 20–25% of logistics expenses.  
        - Reefer maintenance adds 10–12% per pallet.  
        - *Mitigation:* Include fuel surcharge clauses.  

        **Customs Delay Management:** - Use temperature loggers for compliance.  
        - Utilize Laredo cross-docking hub.  
        - Keep buffer inventory near border (McAllen or Laredo).  
        """
    )

    # ---- SECCIÓN EXCEL (Se mantiene el código original para la descarga) ----
    st.markdown("<h3 style='color:green;'>Here you can access our Excel file with the required information.</h3>", unsafe_allow_html=True)
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
# =================================
# SECCIÓN: LOGÍSTICA (COMPLETA DEL PDF)
# =================================
elif menu == "🚛 Logistics":
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

# =================================
# SECCIÓN: FINANZAS
# =================================
elif menu == "💰 Finance":
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

    # ---- SECCIÓN EXCEL ----
    st.markdown("<h3 style='color:green;'>Here you can access our Excel file with the required information.</h3>", unsafe_allow_html=True)
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

# =================================
# SECCIÓN: CONCLUSIÓN
# =================================
elif menu == "🧾 Conclusion":
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
elif menu == "📊 Downloads":
    st.title("Downloads")

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

