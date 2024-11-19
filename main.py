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
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero"
    
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

# Punto de Entrada

if __name__ == "__main__":
    print("Bienvenido a la Calculadora básica")
    num1 = float(input("Por favor ingrese el primer número: "))
    num2 = float(input("Por favor ingrese el segundo número: "))

    print(f"Suma: {suma(num1, num2)}")
    print(f"Resta: {resta(num1, num2)}")
    print(f"Multiplicación: {multiplicacion(num1, num2)}")
    print(f"División: {division(num1, num2)}")
    print(f"Radicación: {radicacion(num1, num2)}")
    print(f"Potenciación: {potenciacion(num1, num2)}")
