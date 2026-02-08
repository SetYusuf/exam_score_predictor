# Exam Predictor Project

Minimal Flask app that loads a pre-trained model (`exam_score_model.pkl`) and predicts exam scores from a simple form.

Prerequisites
- Python 3.8+
- `exam_score_model.pkl` placed in the project root (already present in the workspace).

Setup (PowerShell)
```powershell
python -m venv venv
venv\Scripts\Activate
pip install -r requirements.txt
```

Run
```powershell
python app.py
# Then open http://127.0.0.1:5000/ in your browser.
```

Files
- `app.py`: Flask application
- `templates/index.html`: form UI
- `exam_score_model.pkl`: pre-trained model (provided)
