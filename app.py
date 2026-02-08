from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load model
model = joblib.load('exam_score_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    hours_study = float(request.form['hours_study'])
    hours_sleep = float(request.form['hours_sleep'])
    revision_days = float(request.form['revision_days'])
    
    prediction = model.predict([[hours_study, hours_sleep, revision_days]])[0]
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
