from flask import Flask, request, jsonify, render_template
import Calculator

app = Flask(__name__)

monthlysalary = Calculator.self

headings = ("Categories","Amount")
data = (
    ("KWSP", "X"),
    ("SOCSO", "Y"),
    ("Donations", "Z"),
    ("Deductibles", "A"),
    ("Chargeable Income", "B")
)


# For testing
@app.route('/hello', methods = ['GET'])
def hello():
    return "Hi"

@app.route('/')
def index():
    return render_template('app.html', headings=headings, data=data)

@app.route('/income_tax', methods=['GET', 'POST'])
def income_tax():
    monthlysalary = float(request.form['monthlysalary'])
    bonus = float(request.form['bonus'])
    donations = float(request.form['donations'])
    deductibles = float(request.form['deductibles'])
    epf_perc = int(request.form['epf_perc'])

    response = jsonify({
        'estimated_tax': Calculator.calc_tax(monthlysalary, bonus, donations, deductibles, epf_perc)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Tax Calculator")
    Calculator.load_saved_artifacts()
    app.run(debug=True)


