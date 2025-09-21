import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the synthetic data
df = pd.read_csv("synthetic_rockfall_data.csv")

# Features and target
X = df[["displacement", "strain", "pore_pressure", "rainfall", "temperature", "vibration"]]
y = df["rockfall_event"]

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model trained! Accuracy on test set: {acc*100:.2f}%")

# Save the model
joblib.dump(model, "rockfall_model.pkl")
print("Model saved as rockfall_model.pkl")
