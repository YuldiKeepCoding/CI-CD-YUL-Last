"""
Este es un módulo de prueba para el proyecto.
Incluye funciones de prueba para probar la funcionalidad del código.
"""
from . import calc

def test_add():
    """
    Pruebas unitarias para el método add de la clase Calculadora.
    """
    assert calc().add(1, 2) == 3

def test_subtract():
    """
    Pruebas unitarias para el método subtract de la clase Calculadora.
    """
    assert calc().subtract(2, 1) == 1

def test_multiply():
    """
    Pruebas unitarias para el método multiply de la clase Calculadora.
    """
    assert calc().multiply(1, 2) == 2

def test_divide():
    """
    Pruebas unitarias para el método divide de la clase Calculadora.
    """
    assert calc().divide(0, 2.0) == 0
