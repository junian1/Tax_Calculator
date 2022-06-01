from flask import Flask, request, jsonify
import Calculator

app = Flask(__name__)

@app.route('/hello', methods = ['GET'])
def hello():
    return "Hi"

@app.route('/income_tax', methods=['GET', 'POST'])
def income_tax():
    monthlysalary = float(request.form['monthlysalary'])
    donations = float(request.form['donations'])
    deductibles = float(request.form['deductibles'])
    percentage = int(request.form['percentage'])

    response = jsonify({
        'estimated_tax': Calculator.calc_tax(monthlysalary, donations, deductibles, percentage)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Tax Calculator")
    Calculator.load_saved_artifacts()
    app.run()





