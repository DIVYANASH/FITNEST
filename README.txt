FITNEST - Smart Fitness Adviser

Files:
- app.py
- requirements.txt
- templates/index.html
- static/style.css
- static/script.js

Run locally:
1. Open this folder in VS Code.
2. In terminal run: pip install -r requirements.txt
3. Run: python app.py
4. Open: http://127.0.0.1:5000

Render deployment:
- Build command: pip install -r requirements.txt
- Start command: gunicorn app:app

Note:
This is an educational BMI and calorie-estimate app. It does not store user entries.
BMI and calorie calculations are estimates, not medical advice.
