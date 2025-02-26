import streamlit as st

# Custom CSS for Styling
st.markdown("""
    <style>
        .main {
            background-color: #f7f7f7;
        }
        .title {
            font-size: 32px;
            text-align: center;
            color: #4CAF50;
            font-weight: bold;
        }
        .stButton button {
            background-color: #4CAF50 !important;
            color: white !important;
            padding: 10px;
            font-size: 16px;
            border-radius: 8px;
        }
        .stTextInput input {
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Title with Icon
st.markdown("<p class='title'>🔄 Unit Converter</p>", unsafe_allow_html=True)

# Conversion Function
def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "km": 1000, "m": 1, "cm": 0.01, "mm": 0.001,
        "kg": 1000, "g": 1, "mg": 0.001,
        "l": 1, "ml": 0.001
    }
    if from_unit in conversion_factors and to_unit in conversion_factors:
        return value * (conversion_factors[to_unit] / conversion_factors[from_unit])
    return None

# Unit Categories
unit_types = {
    "📏 Length": ["km", "m", "cm", "mm"],
    "⚖️ Weight": ["kg", "g", "mg"],
    "🧪 Volume": ["l", "ml"]
}

# Columns for Layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Select Category
    category = st.selectbox("📂 Select Category", list(unit_types.keys()))

    # Columns for Unit Selection
    col_a, col_b = st.columns(2)
    with col_a:
        from_unit = st.selectbox("🔄 From Unit", unit_types[category])
    with col_b:
        to_unit = st.selectbox("➡️ To Unit", unit_types[category])

    # Value Input
    value = st.number_input("✏️ Enter Value", min_value=0.0, format="%.2f")

    # Convert Button
    if st.button("🚀 Convert"):
        result = convert_units(value, from_unit, to_unit)
        if result is not None:
            st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")
        else:
            st.error("❌ Invalid conversion")

