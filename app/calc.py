"""
Calculadora simple para realizar operaciones matemáticas.
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('form.html')

@app.route('/', methods=['GET','POST'])
def index():
    """
    Comentarios
    """
    # Se inicia en 1 (add)
    operation = 1

    # Se inicia en None
    result = None

    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    operation = int(request.form["operation"])

    if(operation == 1):
        result = add(num1, num2)
    elif(operation == 2):
        result = subtract(num1, num2)
    elif(operation == 3):
        result = multiply(num1, num2)
    elif(operation == 4):
        result = divide(num1, num2)
    else:
        result = 0
    entry = result
    return render_template('form.html', entry=entry)

def add(self, num1, num2):
    """
    Realiza la operación de suma.

    Args:
        num1 (int): Primer número.
        num2 (int): Segundo número.

    Returns:
        int: Resultado de la suma.
    """
    return num1 + num2

def subtract(self, num1, num2):
    """
    Realiza la operación de resta.

    Args:
        num1 (int): Número del que se resta.
        num2 (int): Número que se resta.

    Returns:
        int: Resultado de la resta.
    """
    return num1 - num2

def multiply(self, num1, num2):
    """
    Realiza la operación de multiplicación.

    Args:
        num1 (int): Primer número.
        num2 (int): Segundo número.

    Returns:
        int: Resultado de la multiplicación.
    """
    return num1 * num2

def divide(self, num1, num2):
    """
    Realiza la operación de división.

    Args:
        num1 (int): Número dividendo.
        num2 (int): Número divisor.

    Returns:
        float or str: Resultado de la división o mensaje de error si el divisor es 0.
    """
    if num2 == 0:
        return 'Cannot divide by 0'
    return num1 * 1.0 / num2

if __name__ == '__main__':
    app.run(debug=True)