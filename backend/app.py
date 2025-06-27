from flask import Flask, request, jsonify
import pandas as pd
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained model
model = joblib.load("student_knn_model.pkl")

@app.route('/', methods=['GET'])
def home():
    return "Api is up and running..."
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'OPTIONS':
        return jsonify({'message': 'CORS preflight passed'}), 200

    try:
        data = request.get_json()

        input_data = {
            'Hours_Studied_Per_Day': float(data['Hours_Studied_Per_Day']),
            'Total_Study_Days': int(data['Total_Study_Days']),
            'Past_Percentage': float(data['Past_Percentage']),
            'Attendance_Percentage': float(data['Attendance_Percentage']),
            'Parental_Support': data['Parental_Support'],
            'Internet_Access': data['Internet_Access'],
            'School_Type': data['School_Type'],
            'Sleep_Hours': float(data['Sleep_Hours']),
            'Social_Media_Hours': float(data['Social_Media_Hours']),
            'Coaching': data['Coaching'],
            'Gender': data['Gender']
        }

        df = pd.DataFrame([input_data])
        prediction = model.predict(df)
        result = round(float(prediction[0]), 2)

        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
