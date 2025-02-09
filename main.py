from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import joblib

model = joblib.load('heartawaremodel.joblib')

def predict_custom_data(custom_data):
    custom_df = pd.DataFrame([custom_data])
    prediction = model.predict(custom_df)
    return prediction[0]

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/test/question1', methods=['POST', 'GET'])
def redir():
    custom_data = {}
    keys = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope']
    ranges = {
        'RestingBP' : [0, 200],
        'Cholesterol' : [0, 603],
        'MaxHR' : [60, 202],
        'Oldpeak' : [-2.6, 6.2]
    }
    if request.method == 'GET':
        return render_template('questions.html')
    else:
        for i in keys:
            val = request.form[i]

            if val.isnumeric():
                val = float(val)
            
            custom_data[i] = val
        data = [custom_data['RestingBP'], custom_data['Cholesterol'], custom_data['MaxHR'], custom_data['Oldpeak']]
        result = predict_custom_data(custom_data=custom_data)

        #Checking whether the values are within the range
        for i in ranges.keys():
            if ranges[i][0] <= float(custom_data[i]) <= ranges[i][1]:
                continue
            else:
                result = 1
                break

        if result == 0:
            return render_template('result.html', result='You don\'t have a risk of getting Heart Disease 🥳', user_data=data)
        else:
            return render_template('result.html', result='You have a risk of getting Heart Disease', user_data=data)


if __name__ == '__main__':
    app.run(debug=True)