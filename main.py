from operaciones import suma, resta, multiplicacion, division, radicacion, potenciacion

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
