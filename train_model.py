import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load crime data
data = pd.read_csv('crime_data.csv')

# Encode severity
data['severity_label'] = data['severity'].map({'Low':0, 'Medium':1, 'High':2})

# Features and target
X = data[['latitude','longitude','hour','day']]
y = data['severity_label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'risk_model.pkl')
print("Model trained and saved!")