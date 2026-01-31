import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
df = pd.read_csv("datasets/training_data.csv")

X = df.drop("placed", axis=1)
y = df["placed"]

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train
model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    max_iter=1000,
    random_state=42
)
model.fit(X_scaled, y)

# Save
joblib.dump(model, "models/placement_mlp.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("✅ MLP model trained and saved successfully")




