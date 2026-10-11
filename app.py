from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)


# Load trained ML model
with open("../ml/spoilage_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return "Smart Groceries API is running!"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    food = pd.DataFrame([{
        "food_name": data["food_name"],
        "category": data["category"],
        "storage_method": data["storage_method"],
        "temperature_c": data["temperature_c"],
        "humidity_percent": data["humidity_percent"],
        "quantity_kg": data["quantity_kg"],
        "days_since_purchase": data["days_since_purchase"],
        "purchase_year": data["purchase_year"],
        "purchase_month": data["purchase_month"],
        "purchase_day": data["purchase_day"]
    }])

    prediction = model.predict(food)

    return jsonify({
        "food_name": data["food_name"],
        "predicted_shelf_life": round(float(prediction[0]), 2)
    })


if __name__ == "__main__":
    app.run(debug=True)