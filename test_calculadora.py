
import pytest

from calculadora import sumar, dividir


def test_sumar_positivos():
    assert sumar(2, 3) == 5


def test_sumar_negativos():
    assert sumar(-2, -3) == -5


def test_dividir_exactamente():
    assert dividir(10, 2) == 5


def test_dividir_decimal():
    assert dividir(7, 2) == 3.5


def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_dividir_texto_primer_valor():
    with pytest.raises(TypeError):
        dividir("10", 2)


def test_dividir_texto_segundo_valor():
    with pytest.raises(TypeError):
        dividir(10, "2")


def test_dividir_booleanos():
    with pytest.raises(TypeError):
        dividir(True, 2)
