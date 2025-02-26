import streamlit as st
import time

# Custom CSS for Animations and Styling
st.markdown("""
    <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .title {
            font-size: 32px;
            text-align: center;
            color: #4CAF50;
            font-weight: bold;
            animation: fadeIn 1s ease-in-out;
        }
        .stButton button {
            background-color: #4CAF50 !important;
            color: white !important;
            padding: 10px;
            font-size: 16px;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
        }
        .stButton button:hover {
            transform: scale(1.1);
            background-color: #45A049 !important;
        }
        .result-box {
            background-color: #E8F5E9;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #2E7D32;
            animation: fadeIn 0.8s ease-in-out;
        }
    </style>
""", unsafe_allow_html=True)

# Title with Icon
st.markdown("<p class='title'>🔄️ Animated Unit Converter</p>", unsafe_allow_html=True)

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

# Layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    category = st.selectbox("📂 Select Category", list(unit_types.keys()))
    
    col_a, col_b = st.columns(2)
    with col_a:
        from_unit = st.selectbox("🔄 From Unit", unit_types[category])
    with col_b:
        to_unit = st.selectbox("➡️ To Unit", unit_types[category])
    
    value = st.number_input("✏️ Enter Value", min_value=0.0, format="%.2f")
    
    if st.button("🚀 Convert with Animation"):
        with st.spinner("Converting..."):
            time.sleep(1.5)
        
        result = convert_units(value, from_unit, to_unit)
        if result is not None:
            st.markdown(f"<div class='result-box'>✅ {value} {from_unit} = {result:.2f} {to_unit}</div>", unsafe_allow_html=True)
        else:
            st.error("❌ Invalid conversion")


