class CalculadoraMCD:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcular_mcd(self):
        """
        Calcula el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides.
        :return: El máximo común divisor de self.num1 y self.num2.
        """
        a = self.num1
        b = self.num2
        while b != 0:
            a, b = b, a % b
        return a

# Solicitar al usuario que ingrese los números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Crear una instancia de la clase CalculadoraMCD
calculadora = CalculadoraMCD(num1, num2)

# Calcular el máximo común divisor
resultado = calculadora.calcular_mcd()

# Mostrar el resultado
print("El máximo común divisor de", num1, "y", num2, "es:", resultado)
