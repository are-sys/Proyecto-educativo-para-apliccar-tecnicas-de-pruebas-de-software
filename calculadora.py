
def sumar(a, b):
    return a + b


def dividir(a, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("El primer valor debe ser numérico")

    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("El segundo valor debe ser numérico")

    if b == 0:
        raise ValueError("No se puede dividir entre cero")

    return a / b
