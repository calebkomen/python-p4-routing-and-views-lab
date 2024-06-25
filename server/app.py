from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')  # Print to console
    return f'{parameter}'  # Return plain text

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(i) for i in range(parameter))
    return f'{numbers}\n'

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation'

    return f'{result}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
