def suma(a, b):
    """
    Devuelve la suma de dos números.
    """
    return a + b

def resta(a, b):
    """
    Devuelve la resta de dos números.
    """
    return a - b

def multiplicacion(a, b):
    """
    Devuelve la multiplicación de dos números.
    """
    return a * b

def division(a, b):
    """
    Devuelve la división de dos números. Maneja de división entre cero
    """
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero"
    else:
        return resultado
    finally:
        pass

    
def radicacion(base, indice):
    """
    Devuelve la raiz cuadrada del número dado en el indice
    """
    try:
        return base ** (1/indice)
    except ZeroDivisionError:
        return "Error: El índice de la raiz no puede ser cero."

def potenciacion(base, exponente):
    """
    Devuelve la potencia de un número dado un exponente.
    """
    return base ** exponente