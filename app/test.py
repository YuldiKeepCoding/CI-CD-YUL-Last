"""
Este es un módulo de prueba para el proyecto.
Incluye funciones de prueba para probar la funcionalidad del código.
"""
from calc import Calculadora

def test_add():
    """
    Pruebas unitarias para el método add de la clase Calculadora.
    """
    assert Calculadora().add(1, 2) == 3

def test_subtract():
    """
    Pruebas unitarias para el método subtract de la clase Calculadora.
    """
    assert Calculadora().subtract(2, 1) == 1

def test_multiply():
    """
    Pruebas unitarias para el método multiply de la clase Calculadora.
    """
    assert Calculadora().multiply(1, 2) == 2

def test_divide():
    """
    Pruebas unitarias para el método divide de la clase Calculadora.
    """
    assert Calculadora().divide(0, 2.0) == 0
