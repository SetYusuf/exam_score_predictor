# Exam Score Predictor

A simple Flask web app that uses a pre-trained machine learning model to predict exam scores based on study hours, sleep hours, and revision days.

**Live Demo:** Deploy to Render (free) — see instructions below

## Features
- Clean, professional UI with responsive design
- ML-powered predictions using scikit-learn
- Form validation and error handling
- One-click deployment to Render or Heroku

## Prerequisites
- Python 3.8+
- `exam_score_model.pkl` (included)

## Local Setup (Windows PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
python app.py
```
Then open http://127.0.0.1:5000/ in your browser.

## Files
- `app.py` — Flask application
- `templates/index.html` — Input form UI
- `templates/result.html` — Prediction result page
- `static/style.css` — Professional styling
- `exam_score_model.pkl` — Pre-trained ML model
- `Procfile` — Deployment configuration

## Deploy to Render (FREE & Easy)

1. Go to [render.com](https://render.com) and sign up (free tier available)
2. Click **New +** → **Web Service**
3. Connect your GitHub account and select this repo
4. Configure the service:
   - **Name:** exam-score-predictor
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Create Web Service** and wait ~2 minutes for deployment
6. Once live, you'll get a URL like: `https://exam-score-predictor-XXXX.onrender.com`
7. Share the link with anyone — they can predict exam scores!

**Alternative (Heroku):** Same steps but at [heroku.com](https://heroku.com)

## After Deployment
- Edit files locally → push to GitHub → auto-deploys to Render/Heroku
- Your ML model predictions are now live for everyone!
