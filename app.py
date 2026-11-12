from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            name = request.form["name"].strip()
            age = int(request.form["age"])
            gender = request.form["gender"]
            weight = float(request.form["weight"])
            height = float(request.form["height"])  # metres
            activity = int(request.form["activity"])

            if not name:
                raise ValueError("Please enter your name.")
            if age <= 0 or age > 120:
                raise ValueError("Please enter a valid age.")
            if gender not in ("male", "female"):
                raise ValueError("Please select a valid gender.")
            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be greater than zero.")
            if activity not in (1, 2, 3, 4):
                raise ValueError("Please select a valid activity level.")

            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal Weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"

            height_cm = height * 100

            if gender == "male":
                bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5
            else:
                bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161

            multipliers = {
                1: 1.2,
                2: 1.375,
                3: 1.55,
                4: 1.725
            }
            maintenance = bmr * multipliers[activity]

            result = {
                "name": name,
                "bmi": round(bmi, 2),
                "category": category,
                "bmr": round(bmr),
                "maintenance": round(maintenance),
                "weight_gain": round(maintenance + 300),
                "weight_loss": round(maintenance - 300)
            }

        except (ValueError, KeyError):
            error = "Please check your details and enter valid values."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
