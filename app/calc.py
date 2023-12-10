"""
Calculadora simple para realizar operaciones matemáticas.
"""

from flask import Flask, render_template, request

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True # Sensitive

@app.route('/')
def welcome():
    """
    Ruta de inicio que muestra el formulario para ingresar números y seleccionar una operación.
    """
    return render_template('form.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Ruta principal que realiza la operación matemática seleccionada y muestra el resultado.
    """
    # Se inicia en 1 (add)
    operation = 1
    
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    operation = int(request.form["operation"])

    if operation == 1:
        result = add(num1, num2)
    elif operation == 2:
        result = subtract(num1, num2)
    elif operation == 3:
        result = multiply(num1, num2)
    elif operation == 4:
        result = divide(num1, num2)
    return render_template('form.html', result=result)

def add(num1, num2):
    """
    Realiza la operación de suma.

    Args:
        num1 (float): Primer número.
        num2 (float): Segundo número.

    Returns:
        float: Resultado de la suma.
    """
    return num1 + num2

def subtract(num1, num2):
    """
    Realiza la operación de resta.

    Args:
        num1 (float): Número del que se resta.
        num2 (float): Número que se resta.

    Returns:
        float: Resultado de la resta.
    """
    return num1 - num2

def multiply(num1, num2):
    """
    Realiza la operación de multiplicación.

    Args:
        num1 (float): Primer número.
        num2 (float): Segundo número.

    Returns:
        float: Resultado de la multiplicación.
    """
    return num1 * num2

def divide(num1, num2):
    """
    Realiza la operación de división.

    Args:
        num1 (float): Número dividendo.
        num2 (float): Número divisor.

    Returns:
        float or str: Resultado de la división o mensaje de error si el divisor es 0.
    """
    if num2 == 0:
        return 'NONE'
    return num1 / num2
