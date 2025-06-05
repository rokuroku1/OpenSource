# Ejercicios de la clase 3
# Funciones auxiliares para obtener entradas numéricas de forma segura
def obtener_numero_float(mensaje_prompt: str) -> float:
    """Solicita un número flotante al usuario y maneja errores de entrada."""
    while True:
        try:
            return float(input(mensaje_prompt))
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def obtener_numero_int(mensaje_prompt: str) -> int:
    """Solicita un número entero al usuario y maneja errores de entrada."""
    while True:
        try:
            return int(input(mensaje_prompt))
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

# --- Definiciones de los Ejercicios Modificados ---

def ejercicio_1():
    """Suma de dos números."""
    print("\n--- Suma de dos números ---")
    num1 = obtener_numero_float("Ingresa el primer número: ")
    num2 = obtener_numero_float("Ingresa el segundo número: ")
    suma = num1 + num2
    print(f"La suma de {num1} y {num2} es: {suma}")

def ejercicio_2():
    """Conversor de Celsius a Fahrenheit."""
    print("\n--- Conversor de Celsius a Fahrenheit ---")
    celsius = obtener_numero_float("Ingresa la temperatura en grados Celsius: ")
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

def ejercicio_3():
    """Área de un triángulo."""
    print("\n--- Área de un triángulo ---")
    base = -1.0
    while base <= 0:
        base = obtener_numero_float("Ingresa la base del triángulo (debe ser positiva): ")
        if base <= 0:
            print("La base debe ser un número positivo. Inténtalo de nuevo.")
    
    altura = -1.0
    while altura <= 0:
        altura = obtener_numero_float("Ingresa la altura del triángulo (debe ser positiva): ")
        if altura <= 0:
            print("La altura debe ser un número positivo. Inténtalo de nuevo.")
            
    area = (base * altura) / 2
    print(f"El área del triángulo con base {base} y altura {altura} es: {area}")

def ejercicio_4():
    """Verificador de número Par o Impar."""
    print("\n--- Verificador de número Par o Impar ---")
    numero = obtener_numero_int("Ingresa un número entero: ")
    if numero % 2 == 0:
        print(f"El número {numero} es PAR.")
    else:
        print(f"El número {numero} es IMPAR.")

def ejercicio_5():
    """Intercambio de valores de dos variables."""
    print("\n--- Intercambio de valores de dos variables ---")
    a = obtener_numero_int("Ingresa el primer número entero (valor de 'a'): ")
    b = obtener_numero_int("Ingresa el segundo número entero (valor de 'b'): ")
    print(f"Valores originales: a = {a}, b = {b}")
    a, b = b, a  # Intercambio elegante en Python
    print(f"Después del intercambio: a = {a}, b = {b}")

def ejercicio_6():
    """Calculadora Básica (Suma, Resta, Multiplicación, División)."""
    print("\n--- Calculadora Básica ---")
    num1 = obtener_numero_float("Ingresa el primer número: ")
    num2 = obtener_numero_float("Ingresa el segundo número: ")

    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    
    print(f"\nResultados para los números {num1} y {num2}:")
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")

    if num2 != 0:
        division = num1 / num2
        print(f"División ({num1}/{num2}): {division:.4f}")
    else:
        print(f"División ({num1}/{num2}): No se puede dividir entre cero.")

def ejercicio_7():
    """Calculadora de Edad Aproximada en meses y días."""
    print("\n--- Calculadora de Edad Aproximada ---")
    edad = -1
    while edad < 0:
        edad = obtener_numero_int("Ingresa tu edad en años (número entero positivo): ")
        if edad < 0:
            print("La edad no puede ser negativa. Inténtalo de nuevo.")
    
    meses = edad * 12
    dias_aprox = edad * 365 
    print(f"Con {edad} años, tienes aproximadamente:")
    print(f"- {meses} meses")
    print(f"- {dias_aprox} días")
    print("(Nota: El cálculo de días es una aproximación y no considera años bisiestos).")

def ejercicio_8():
    """Encontrar el mayor de tres números."""
    print("\n--- Encontrar el mayor de tres números ---")
    print("Ingresa tres números para identificar cuál es el mayor.")
    num1 = obtener_numero_float("Primer número: ")
    num2 = obtener_numero_float("Segundo número: ")
    num3 = obtener_numero_float("Tercer número: ")
    
    mayor = max(num1, num2, num3) # Usando la función incorporada max()
    
    print(f"De los números {num1}, {num2} y {num3}, el mayor es: {mayor}")

def ejercicio_9():
    """Verificador de múltiplos."""
    print("\n--- Verificador de múltiplos ---")
    num1 = obtener_numero_int("Ingresa el primer número entero (dividendo): ")
    num2 = 0
    while num2 == 0:
        num2 = obtener_numero_int("Ingresa el segundo número entero (divisor, distinto de cero): ")
        if num2 == 0:
            print("El divisor no puede ser cero. Inténtalo de nuevo.")
            
    if num1 % num2 == 0:
        print(f"{num1} es múltiplo de {num2}.")
    else:
        print(f"{num1} no es múltiplo de {num2}.")

def ejercicio_10():
    """Calculadora de Salario con Bono."""
    print("\n--- Calculadora de Salario con Bono ---")
    salario_base = -1.0
    while salario_base < 0:
        salario_base = obtener_numero_float("Ingresa el salario base del empleado (ej: 30000): ")
        if salario_base < 0:
            print("El salario base no puede ser negativo.")

    porcentaje_bono = -1.0
    while not (0 <= porcentaje_bono <= 100): 
        porcentaje_bono = obtener_numero_float("Ingresa el porcentaje de bono a aplicar (ej: 10 para 10%): ")
        if not (0 <= porcentaje_bono <= 100):
            print("El porcentaje de bono debe estar entre 0 y 100.")

    bono = salario_base * (porcentaje_bono / 100)
    salario_total = salario_base + bono
    
    print("\n--- Detalle Salarial ---")
    print(f"Salario Base: ${salario_base:,.2f}")
    print(f"Bono ({porcentaje_bono}%): ${bono:,.2f}")
    print(f"Salario Total (con bono): ${salario_total:,.2f}")

# --- Función Principal para Ejecutar los Ejercicios ---
def ejecutar_ejercicio():
    """Función principal para seleccionar y ejecutar los ejercicios."""
    
    ejercicio_funciones = {
        '1': ejercicio_1, '2': ejercicio_2, '3': ejercicio_3, '4': ejercicio_4, '5': ejercicio_5,
        '6': ejercicio_6, '7': ejercicio_7, '8': ejercicio_8, '9': ejercicio_9, '10': ejercicio_10
    }
    
    ejercicio_descripciones = {
        num: (func.__doc__.split('\n')[0] if func.__doc__ else f"Ejercicio {num}")
        for num, func in ejercicio_funciones.items()
    }

    print("Bienvenido al selector de mini-programas Python!")
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("Elige un ejercicio:")
        for i in range(1, 11):
            num_str = str(i)
            print(f"  {num_str}. {ejercicio_descripciones.get(num_str, 'Descripción no disponible')}")
        print("  salir. Terminar el programa")
        
        eleccion = input("Ingresa el número del ejercicio o 'salir' para terminar: ").strip().lower()

        ejercicio_ejecutado_correctamente = False
        
        if eleccion in ejercicio_funciones:
            ejercicio_funciones[eleccion]() 
            ejercicio_ejecutado_correctamente = True
        elif eleccion == 'salir':
            print("Hasta luego! Gracias por usar el programa.")
            break 
        else:
            print("Opción inválida. Por favor, ingresa un número entre 1 y 10 o 'salir'.")

        if ejercicio_ejecutado_correctamente:
            while True:
                otra = input("\n¿Quieres ejecutar otro ejercicio? (sí/no): ").strip().lower()
                if otra in ['sí', 'si', 's', 'yes', 'y', '1']:
                    break 
                elif otra in ['no', 'n', '2']:
                    print("Hasta la próxima! Gracias por usar el programa.")
                    return 
                else:
                    print("Respuesta no válida. Por favor, escribe 'sí' o 'no'.")

# Iniciar el programa
if __name__ == "__main__":
    ejecutar_ejercicio()