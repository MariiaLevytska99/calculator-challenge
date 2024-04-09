from flask import Flask, render_template, request, jsonify
from strategy.factory import OperationFactory
from strategy.expression_startegy import ExpressionStrategy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    try:
        operation = OperationFactory.get_operation(operation)
        result = operation.execute(num1, num2)

        color = 'green' if result % 2 == 0 else 'red'
    
        return jsonify({'result': result, 'color': color})
    
    except ZeroDivisionError:
        return jsonify({"result": "Division by zero is not allowed",
                       "error": "Division by zero is not allowed"}), 400


@app.route('/complex_calculate', methods=['POST'])
def complex_calculate():
    try:
        expression = request.form['expression']
        result = ExpressionStrategy(expression).execute()

        color = 'green' if result % 2 == 0 else 'red'
    
        return jsonify({'result': result, 'color': color})
    
    except ZeroDivisionError:
        return jsonify({"result": "Division by zero is not allowed",
                       "error": "Division by zero is not allowed"}), 400

if __name__ == '__main__':
    app.run(debug=True)
