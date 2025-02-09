import pandas as pd
import joblib

model = joblib.load('heartawaremodel.joblib')

def predict_custom_data(custom_data):
    custom_df = pd.DataFrame([custom_data])
    prediction = model.predict(custom_df)
    return prediction[0]

custom_data = {
    'Age': 50,
    'Sex': 'M',
    'ChestPainType': 'ATA',
    'RestingBP': 130,
    'Cholesterol': 250,
    'FastingBS': 0,
    'RestingECG': 'Normal',
    'MaxHR': 150,
    'ExerciseAngina': 'N',
    'Oldpeak': 1.0,
    'ST_Slope': 'Up'
}


predicted_value = predict_custom_data(custom_data)
print(f"Predicted HeartDisease for custom data: {predicted_value}")
