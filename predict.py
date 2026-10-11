import pandas as pd
import pickle


# Load trained model
with open("spoilage_model.pkl", "rb") as file:
    model = pickle.load(file)


# New grocery item
new_data = pd.DataFrame([
    {
        "food_name": "Tomato",
        "category": "Vegetable",
        "storage_method": "Refrigerator",
        "temperature_c": 5,
        "humidity_percent": 70,
        "quantity_kg": 2,
        "days_since_purchase": 2,
        "purchase_year": 2026,
        "purchase_month": 10,
        "purchase_day": 6
    }
])


# Make prediction
prediction = model.predict(new_data)


print("Food:", new_data["food_name"].iloc[0])
print("Predicted remaining shelf life:",
      round(prediction[0], 2), "days")