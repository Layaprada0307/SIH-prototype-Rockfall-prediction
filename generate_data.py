import pandas as pd
import numpy as np

# Number of data points
n = 500

# Random synthetic data
data = {
    "displacement": np.random.uniform(0, 5, n),   # mm
    "strain": np.random.uniform(0, 0.05, n),      # strain ratio
    "pore_pressure": np.random.uniform(0, 2, n),  # MPa
    "rainfall": np.random.uniform(0, 100, n),     # mm/day
    "temperature": np.random.uniform(10, 40, n),  # °C
    "vibration": np.random.uniform(0, 5, n),      # arbitrary unit
    "rockfall_event": np.random.randint(0, 2, n)  # 0=no, 1=yes
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("synthetic_rockfall_data.csv", index=False)

print("Synthetic sensor data created: synthetic_rockfall_data.csv")
