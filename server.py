from flask import Flask,render_template,request
from calculator import calculate

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/calculated", methods=["POST"])

def calculation():
    number1 = int(request.form["number1"])
    number2 = int(request.form["number2"])
    operator = request.form["operator"]

    ans = calculate(number1, number2, operator)
    return render_template("calculated.html", answer = ans, num1 = number1, oper = operator, num2 = number2)


if(__name__ == "__main__"):
    app.run(host="0.0.0.0", port=5000)