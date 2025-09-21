import streamlit as st
import pandas as pd
import joblib
import folium
from streamlit_folium import st_folium

# Load trained model
model = joblib.load("rockfall_model.pkl")

st.title("AI-Based Rockfall Prediction Dashboard")

st.write("Enter sensor and environmental values:")

# User input sliders
displacement = st.slider("Displacement (mm)", 0.0, 5.0, 1.0)
strain = st.slider("Strain", 0.0, 0.05, 0.01)
pore_pressure = st.slider("Pore Pressure (MPa)", 0.0, 2.0, 0.5)
rainfall = st.slider("Rainfall (mm/day)", 0.0, 100.0, 10.0)
temperature = st.slider("Temperature (°C)", 10.0, 40.0, 25.0)
vibration = st.slider("Vibration (unit)", 0.0, 5.0, 1.0)

# Create input DataFrame
input_data = pd.DataFrame([[displacement, strain, pore_pressure, rainfall, temperature, vibration]],
                          columns=["displacement", "strain", "pore_pressure", "rainfall", "temperature", "vibration"])

# Predict
prediction = model.predict(input_data)[0]
prediction_prob = model.predict_proba(input_data)[0][1]

st.write("---")
st.write(f"**Rockfall Prediction:** {'Yes ⚠️' if prediction==1 else 'No ✅'}")
st.write(f"**Probability of Rockfall:** {prediction_prob*100:.2f}%")

# ---------------- Simulated alert ----------------
if prediction == 1:
    st.warning(f"⚠️ ALERT: High rockfall risk detected! Probability: {prediction_prob*100:.2f}%")
# ------------------------------------------------

# Create a mine map with multiple locations and probability-based color
st.write("### Mine Risk Map")

# Example coordinates for multiple mines (latitude, longitude)
mine_locations = {
    "Mine A": [22.5726, 88.3639],
    "Mine B": [22.5750, 88.3700],
    "Mine C": [22.5700, 88.3600]
}

# Initialize map centered around first mine
m = folium.Map(location=[22.5726, 88.3639], zoom_start=14)

# Add markers for each mine with probability-based color
for name, coord in mine_locations.items():
    # For demo, use same prediction probability for all mines
    prob = prediction_prob  # value between 0 and 1
    
    # Determine color based on probability
    if prob < 0.45:
        color = 'green'
    elif prob < 0.6:
        color = 'yellow'
    else:
        color = 'red'
    
    folium.CircleMarker(
        location=coord,
        radius=15,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=f"{name} - Risk Probability: {prob*100:.2f}%"
    ).add_to(m)

# Show map in Streamlit
st_data = st_folium(m, width=700, height=450)
