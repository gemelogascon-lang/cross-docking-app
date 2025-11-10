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
    st.title("Fresh Aurora Foods")
    st.image("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/logo.png", width=400)
    st.markdown("---")

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

    # BUSINESS CONTEXT
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
    st.title("Products")

    # PRODUCT 1
    st.subheader("Product 1 – Frozen Avocado Pulp 🥑")
    st.image("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/avocado_pulp.jpg", width=500)
    st.markdown(
        """
        **Description:**  
        100% natural avocado pulp made from ripe Hass avocados grown in Michoacán, Mexico.  
        Smooth texture and rich flavor ideal for guacamole, toast, dips, and foodservice use.  
        Pasteurized, frozen, and packed under HACCP-certified conditions.  

        **Key Specifications:**  
        - Ingredients: 100% Hass avocado pulp  
        - Processing: Pasteurized and quick-frozen at -18°C  
        - Net Weight: 500 g  
        - Packaging:
            - Primary: Vacuum-sealed LDPE pouch  
            - Secondary: Carton box (20 units per carton)  
        - Dimensions (Retail Unit): 20 × 15 × 3 cm  
        - Gross Weight: 0.55 kg  
        - Labeling Requirements:
            - Product name, net weight, nutritional facts  
            - Country of origin: Product of Mexico  
            - Allergen statement: Contains no allergens  
            - Storage instruction: Keep Frozen (-18°C)  
        - Shelf Life: 18 months (frozen, unopened)  
        - Regulatory / Export Constraints:
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
    st.markdown("---")

    # PRODUCT 2
    st.subheader("Product 2 – Mango Cubes IQF (Individually Quick Frozen) 🥭")
    st.image("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/mango_cubes.jpg", width=500)
    st.markdown(
        """
        **Description:**  
        Naturally sweet, hand-cut mango cubes from Mexican Kent. Individually quick-frozen (IQF)
        to preserve flavor, color, and texture. Ideal for smoothies, desserts, and bulk foodservice use.  

        **Key Specifications:**  
        - Ingredients: 100% mango  
        - Processing: Washed, diced, and IQF frozen at -18°C  
        - Net Weight: 1 kg  
        - Packaging:
            - Primary: Transparent resealable LDPE pouch  
            - Secondary: Corrugated box (10 pouches per case)  
        - Dimensions (Retail Unit): 25 × 20 × 6 cm  
        - Gross Weight: 1.05 kg  
        - Labeling Requirements:
            - Product name, net weight, nutritional information, batch code  
            - “Keep Frozen (-18°C)”  
            - Country of origin: Mexico  
        - Shelf Life: 24 months (frozen)  
        - Regulatory / Export Constraints:
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
    st.markdown("---")

    # PRODUCT 3
    st.subheader("Product 3 – Ready-to-Eat Salads 🥬")
    st.image("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/images/salads.jpg", width=500)
    st.markdown(
        """
        **Description:**  
        Fresh, pre-washed salad mixes combining Mexican leafy greens, cherry tomatoes, shredded
        carrots, and optional dressings. Designed for healthy convenience, with a crisp, garden-fresh taste.  

        **Key Specifications:**  
        - Ingredients: Lettuce, spinach, tomato, carrot, dressing (Separate)  
        - Processing: Triple-washed, packed under modified atmosphere (MAP)  
        - Net Weight: 250 g  
        - Packaging:
            - Primary: Clear PET bowl with tamper-proof lid  
            - Secondary: Recyclable cardboard sleeve  
        - Dimensions: 18 cm diameter × 5 cm height  
        - Gross Weight: 0.27 kg  
        - Labeling Requirements:
            - Product name, expiration date, ingredients, allergens  
            - “Keep Refrigerated (2–4°C)”  
            - Country of origin: Mexico  
        - Shelf Life: 5 days (refrigerated)  
        - Regulatory / Export Constraints:
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

# =================================
# SECCIÓN: LOGÍSTICA
# =================================
elif menu == "🚛 Logística":
    st.title("Supply Chain & Logistics")

    st.subheader("Supply Chain Components")
    st.markdown(
        """
        - **Procurement:** Sourcing of fresh produce from farms in Michoacán and Jalisco, including avocados, mangoes, and greens.  
        - **Processing & Packaging:** HACCP-certified facility in Querétaro handles pulping, IQF freezing, and packaging.  
        - **Cold Chain Transport:** Products transported in refrigerated trucks maintaining -18°C (frozen) or 2–4°C (salads).  
        - **Warehousing:** Cold storage in Querétaro and temporary storage at Laredo, TX, for customs inspection.  
        - **Cross-Docking:** Used at Laredo, TX to consolidate shipments, reduce inventory holding, and accelerate flow.  
        - **Customs & 3PL:** Third-party logistics providers manage customs clearance and border compliance.  
        - **Distribution:** Products are sent to regional warehouses or directly to U.S. and Canadian clients.  
        """
    )

    st.subheader("Why Cross-Docking is Used")
    st.markdown(
        """
        - **Consolidation:** Group multiple small shipments into larger, more efficient loads.  
        - **Flow Acceleration:** Reduces need for extended storage, ensuring faster delivery times.  
        - **Inventory Reduction:** Minimizes holding time and storage costs.  
        """
    )

    st.subheader("Transport Modes")
    st.markdown(
        """
        **Land (Refrigerated Trucking):**  
        - Most cost-effective for the North American corridor (Mexico–U.S.–Canada).  
        - Time: 1.5 days from Querétaro to Laredo; 3–5 days to U.S. and Canadian hubs.  
        - Cost: Cheaper than air, faster than sea.  
        - Reliable, with temperature control for sensitive products.
        """
    )

    st.subheader("Operational Summary")
    st.markdown(
        """
        At Aurora Fresh Foods, our logistics network is meticulously designed to maintain the
        highest levels of freshness, quality, and efficiency throughout the supply chain.
        The journey begins with sourcing premium produce from the best farms in Michoacán and Jalisco.
        After processing in Querétaro, products are transported via refrigerated trucks to the
        cross-docking hub in Laredo, TX, where shipments are consolidated, inspected, and redistributed
        efficiently to clients across North America.
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
        - Fuel accounts for 20–25% of total logistics expenses.  
        - Reefer maintenance and energy consumption add 10–12% per pallet, especially during customs hold times.  
        - *Recommended mitigation:* Build fuel surcharge clauses into distributor contracts.  

        **Customs Delay Management:**  
        - Employ data loggers to monitor temperature compliance.  
        - Utilize Laredo cross-docking hub to minimize border congestion and reroute to regional distribution centers.  
        - Maintain buffer inventory in cold storage near the U.S. border (e.g., McAllen or Laredo warehouses).  
        """
    )

# =================================
# SECCIÓN: CONCLUSIÓN
# =================================
elif menu == "🧾 Conclusión":
    st.title("Conclusion")
    st.markdown(
        """
        The next critical stage of the process occurs at our cross-docking hub in Laredo, TX.
        Here, shipments are efficiently consolidated, inspected, and redistributed to U.S. and Canadian clients
        with minimal delays. This cross-docking model is key to reducing inventory holding, accelerating
        the flow of goods, and minimizing storage costs.
        By combining refrigerated trucking with strategic cross-docking, we ensure that products are delivered
        to our customers in the best possible condition and at an optimal speed, reducing lead time while
        keeping logistics costs low.
        """
    )
