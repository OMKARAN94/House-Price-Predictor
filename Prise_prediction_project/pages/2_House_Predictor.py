import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
st.set_page_config(layout="wide")


# --- Load Model & Data ---
model = pk.load(open(r'C:\Users\Lenovo\Prise_prediction_project\pages\House_prediction_model.pkl', 'rb'))
data = pd.read_csv(r'C:\Users\Lenovo\Prise_prediction_project\cleaned_data.csv')

# --- Add synthetic coordinates if not available ---
if 'latitude' not in data.columns or 'longitude' not in data.columns:
    np.random.seed(42)
    data['latitude'] = np.random.uniform(12.85, 13.10, len(data))
    data['longitude'] = np.random.uniform(77.45, 77.75, len(data))

# --- Page Config ---
st.set_page_config(page_title="House Price Predictor", page_icon="📊", layout="centered")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: #fff;
    }
    .main {
        background-color: #1e1e1e;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.1);
    }
    h1 {
        text-align: center;
        color: #00c6ff;
        font-size: 40px;
        background: -webkit-linear-gradient(45deg, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1>🏠 Bangalore House Price Predictor</h1>", unsafe_allow_html=True)
st.write("### Enter the details below to predict house price in Bangalore 💰")

# --- Sidebar Inputs ---
st.sidebar.header("🔧 Input Features")

loc = st.sidebar.selectbox("📍 Choose Location", data['location'].unique())
sqft = st.sidebar.number_input("📐 Enter Total Area (sqft)", min_value=200, step=50)
beds = st.sidebar.number_input("🛏️ Number of Bedrooms", min_value=1, step=1)
bath = st.sidebar.number_input("🛁 Number of Bathrooms", min_value=1, step=1)
balc = st.sidebar.number_input("🌿 Number of Balconies", min_value=0, step=1)

# --- Predict Button ---
if st.button("🔮 Predict Price"):
    with st.spinner("Calculating... Please wait ⏳"):
        input_data = pd.DataFrame([[loc, sqft, bath, balc, beds]],
                                  columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms'])
        prediction = model.predict(input_data)
        price_in_lakhs = prediction[0] * 100000

    # --- Display Result ---
    st.success("✅ Prediction Completed!")
    st.metric(label="🏡 Estimated House Price", value=f"₹ {price_in_lakhs:,.2f}")
    st.balloons()

    # --- Visualization Section ---
    st.write("### 📊 Price Trend Visualization")

    loc_data = data[data['location'] == loc]

    # Scatter plot: Price vs Sqft
    fig1, ax1 = plt.subplots()
    ax1.scatter(loc_data['total_sqft'], loc_data['price'], alpha=0.6)
    ax1.set_title(f"Price vs Sqft in {loc}", color="#00c6ff")
    ax1.set_xlabel("Total Sqft")
    ax1.set_ylabel("Price (Lakh ₹)")
    st.pyplot(fig1)

    # Bar Chart: Average Price by Bedrooms
    avg_price = loc_data.groupby('bedrooms')['price'].mean().reset_index()
    fig2, ax2 = plt.subplots()
    ax2.bar(avg_price['bedrooms'], avg_price['price'])
    ax2.set_title(f"Average Price by Bedrooms in {loc}", color="#00c6ff")
    ax2.set_xlabel("Bedrooms")
    ax2.set_ylabel("Average Price (Lakh ₹)")
    st.pyplot(fig2)

    # --- Interactive Map with Price Range Slider ---
    st.write("### 🗺️ Explore House Prices Across Bangalore")

    min_price = int(data['price'].min())
    max_price = int(data['price'].max())

    price_range = st.slider(
        "💸 Select Price Range (in Lakhs ₹)",
        min_value=min_price,
        max_value=max_price,
        value=(min_price, max_price),
        step=10
    )

    # Filter data based on selected price range
    filtered_data = data[(data['price'] >= price_range[0]) & (data['price'] <= price_range[1])]

    st.write(f"📍 Showing houses priced between **₹{price_range[0]} Lakh** and **₹{price_range[1]} Lakh**")

    # Create the map
    fig3 = px.scatter_mapbox(
        filtered_data,
        lat='latitude',
        lon='longitude',
        color='price',
        size='price',
        hover_name='location',
        hover_data={'price': True, 'latitude': False, 'longitude': False},
        color_continuous_scale='Turbo',
        title="House Price Heatmap of Bangalore",
        zoom=11,
        height=500
    )

    fig3.update_layout(mapbox_style="carto-darkmatter", margin={"r":0,"t":30,"l":0,"b":0})
    st.plotly_chart(fig3, use_container_width=True)

# --- Footer ---
st.write("---")
st.caption("✨ Created by **Omkaran & Team** | Powered by Streamlit, Plotly, and Machine Learning 🧠")
st.caption("copyright @2025 Alpha Analytics")


