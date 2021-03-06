from app import sumar, restar, multiplicar, dividir, matematicas
import requests


def test_sumar():
    x = 5
    y = 6
    result = sumar(x, y)
    expected = 11
    assert result == expected, 'se esperaba un valor impar'


def test_restar():
    x = 4
    y = 1
    result = restar(x, y)
    expected = 3
    assert result == expected


def test_multiplicar():
    x = 5
    y = 6
    result = multiplicar(x, y)
    expected = 30
    assert result == expected


def test_dividir():
    x = 12
    y = 3
    result = dividir(x, y)
    expected = 4
    assert result == expected


# def test_web():
#     r = requests.get('http://0.0.0.0:5000')
#     result = r.status_code
#     expected = 200
#     assert result == expected


# def test_matematicas():
#     op1 = 25
#     op2 = 5
#     operador = 'dividir'
#     datos = {'operador': operador, 'op1': op1, 'op2': op2}
#     result = matematicas(**datos)
#     expected = 5
#     assert result == expected
