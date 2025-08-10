from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingRegressor
import joblib
import pandas as pd

# Example training data (replace with actual data)
d = pd.read_csv('football_datawc2019v2.csv')

# Define your features and target
X = d.drop(columns=['shot_statsbomb_xg'])  # Replace with the actual features
y = d['shot_statsbomb_xg']  # The target column

# Step 1: Preprocessing pipeline
numerical_cols = ['location_x', 'location_y', 'end_loc_x', 'end_loc_y', 'end_loc_z']
categorical_cols = ['play_pattern', 'position', 'shot_body_part', 'shot_outcome', 'shot_technique', 'shot_type']

numerical_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', MinMaxScaler())
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_pipeline, numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ]
)

# Fit the preprocessor
X_processed = preprocessor.fit_transform(X)

# Step 2: Model training
model = GradientBoostingRegressor()
model.fit(X_processed, y)

# Step 3: Save the preprocessor and model
joblib.dump(preprocessor, 'preprocessor.pkl')
joblib.dump(model, 'gradient_boosting_model.pkl')

print("Model and preprocessor saved.")
