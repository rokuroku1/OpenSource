# Taller Parte 2
def es_par():
    """Verifica si un número es par."""
    num = int(input("Ingrese un número: "))
    print(f"¿Es par?: {num % 2 == 0}")

def tiene_longitud_minima():
    """Verifica si un texto tiene al menos una cierta longitud."""
    texto = input("Ingrese un texto: ")
    min_longitud = int(input("Ingrese la longitud mínima requerida: "))
    print(f"¿Tiene la longitud mínima?: {len(texto) >= min_longitud}")

def es_vocal():
    """Comprueba si un carácter ingresado es una vocal (mayúscula o minúscula)."""
    caracter = input("Ingrese un carácter: ").lower()
    print(f"¿Es una vocal?: {caracter in 'aeiou'}")

def rango_exclusivo():
    """Verifica si un número está estrictamente entre dos límites."""
    num = int(input("Ingrese un número: "))
    lim_inf = int(input("Ingrese el límite inferior: "))
    lim_sup = int(input("Ingrese el límite superior: "))
    print(f"¿Está entre {lim_inf} y {lim_sup} (exclusivo)?: {lim_inf < num < lim_sup}")

def tiene_subcadena():
    """Verifica si una cadena contiene una subcadena específica (sin distinción de mayúsculas)."""
    cadena_principal = input("Ingrese la cadena principal: ").lower()
    subcadena = input("Ingrese la subcadena a buscar: ").lower()
    print(f"¿Contiene la subcadena?: {subcadena in cadena_principal}")

def es_multiplo_de_x_o_y():
    """Determina si un número es múltiplo de X o de Y."""
    numero = int(input("Ingrese un número: "))
    x = int(input("Ingrese el primer divisor (X): "))
    y = int(input("Ingrese el segundo divisor (Y): "))
    print(f"¿Es múltiplo de {x} o de {y}?: {numero % x == 0 or numero % y == 0}")

def ambas_condiciones():
    """Verifica si dos valores son ambos positivos."""
    val1 = int(input("Ingrese el primer valor: "))
    val2 = int(input("Ingrese el segundo valor: "))
    print(f"¿Ambos son positivos?: {val1 > 0 and val2 > 0}")

def es_negativo_o_cero():
    """Comprueba si un número es negativo o cero."""
    num = int(input("Ingrese un número: "))
    print(f"¿Es negativo o cero?: {num <= 0}")

def no_es_igual():
    """Verifica si dos números no son iguales."""
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print(f"¿Son diferentes?: {num1 != num2}")

def comienza_con_letra():
    """Verifica si un texto comienza con una letra (a-z o A-Z)."""
    texto = input("Ingrese un texto: ")
    print(f"¿Comienza con una letra?: {texto[0].isalpha()}")

def tiene_permiso_especial():
    """Determina si un usuario tiene permiso especial basándose en rol y estado."""
    rol = input("Ingrese el rol (admin/editor/visitante): ").lower()
    activo = input("¿Está activo? (s/n): ").lower() == 's'
    print(f"¿Tiene permiso especial?: {rol == 'admin' or (rol == 'editor' and activo)}")

def es_mayoria_de_edad():
    """Verifica si una persona tiene la mayoría de edad en un país dado (ej. 18 o 21)."""
    edad = int(input("Ingrese la edad: "))
    pais = input("Ingrese el país (ej. 'USA' para 21, 'Spain' para 18): ").lower()
    
    if pais == 'usa':
        print(f"¿Es mayor de edad en USA?: {edad >= 21}")
    elif pais == 'spain':
        print(f"¿Es mayor de edad en España?: {edad >= 18}")
    else:
        print("País no reconocido para la verificación de edad.")

def acceso_combinado():
    """Verifica el acceso basándose en credenciales válidas y ubicación."""
    credenciales_validas = input("¿Credenciales válidas? (s/n): ").lower() == 's'
    ubicacion_autorizada = input("¿Ubicación autorizada? (s/n): ").lower() == 's'
    print(f"¿Acceso concedido?: {credenciales_validas and ubicacion_autorizada}")

def valor_distinto_de_cero():
    """Comprueba si un número es distinto de cero y no nulo."""
    try:
        valor = float(input("Ingrese un número: "))
        print(f"¿Es distinto de cero?: {valor != 0}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

def es_palindromo():
    """Verifica si una palabra es un palíndromo (se lee igual al revés)."""
    palabra = input("Ingrese una palabra: ").lower()
    print(f"¿Es un palíndromo?: {palabra == palabra[::-1]}")

def tiene_digito_o_longitud_par():
    """Verifica si un número contiene un dígito específico O si su longitud es par."""
    num_str = input("Ingrese un número como texto: ")
    digito_buscado = input("Ingrese el dígito a buscar: ")
    
    contiene_digito = digito_buscado in num_str
    longitud_par = len(num_str) % 2 == 0
    
    print(f"¿Contiene '{digito_buscado}' o tiene longitud par?: {contiene_digito or longitud_par}")

def validacion_compra():
    """Determina si una compra es válida (stock disponible y monto suficiente)."""
    stock_disponible = input("¿Hay stock disponible? (s/n): ").lower() == 's'
    monto_suficiente = input("¿El monto es suficiente? (s/n): ").lower() == 's'
    print(f"¿Compra válida?: {stock_disponible and monto_suficiente}")

def estado_semaforo():
    """Simula el estado de un semáforo (puede ser rojo, amarillo, o verde)."""
    color = input("Ingrese el color del semáforo (rojo/amarillo/verde): ").lower()
    print(f"¿El semáforo está en rojo o amarillo?: {color == 'rojo' or color == 'amarillo'}")

def cumple_criterios_seguridad():
    """Verifica si una contraseña cumple con varios criterios de seguridad."""
    password = input("Ingrese una contraseña: ")
    
    tiene_mayuscula = any(c.isupper() for c in password)
    tiene_minuscula = any(c.islower() for c in password)
    tiene_digito = any(c.isdigit() for c in password)
    longitud_minima = len(password) >= 8
    
    print(f"¿Contraseña segura (mayúscula, minúscula, dígito, >=8 chars)?: {tiene_mayuscula and tiene_minuscula and tiene_digito and longitud_minima}")

def es_numero_positivo_y_par():
    """Comprueba si un número es positivo y par."""
    try:
        num = int(input("Ingrese un número: "))
        print(f"¿Es positivo y par?: {num > 0 and num % 2 == 0}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

def menu():
    """Muestra un menú de opciones y ejecuta la función seleccionada."""
    while True:
        print("\n--- Operadores Relacionales y Lógicos ---\n")
        print("--- PARTE 2 ---\n")
        print("11. ¿Es par?")
        print("12. ¿Tiene longitud mínima?")
        print("13. ¿Es vocal?")
        print("14. Rango exclusivo")
        print("15. ¿Tiene subcadena?")
        print("16. ¿Es múltiplo de X o Y?")
        print("17. ¿Ambas condiciones?")
        print("18. ¿Es negativo o cero?")
        print("19. ¿No son iguales?")
        print("20. ¿Comienza con letra?")
        print("21. ¿Tiene permiso especial?")
        print("22. ¿Es mayoría de edad (por país)?")
        print("23. Acceso combinado")
        print("24. Valor distinto de cero")
        print("25. ¿Es un palíndromo?")
        print("26. ¿Tiene dígito o longitud par?")
        print("27. Validación de compra")
        print("28. Estado del semáforo")
        print("29. Cumple criterios de seguridad")
        print("30. ¿Es número positivo y par?")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ")

        match opcion:
            case "11": es_par()
            case "12": tiene_longitud_minima()
            case "13": es_vocal()
            case "14": rango_exclusivo()
            case "15": tiene_subcadena()
            case "16": es_multiplo_de_x_o_y()
            case "17": ambas_condiciones()
            case "18": es_negativo_o_cero()
            case "19": no_es_igual()
            case "20": comienza_con_letra()
            case "21": tiene_permiso_especial()
            case "22": es_mayoria_de_edad()
            case "23": acceso_combinado()
            case "24": valor_distinto_de_cero()
            case "25": es_palindromo()
            case "26": tiene_digito_o_longitud_par()
            case "27": validacion_compra()
            case "28": estado_semaforo()
            case "29": cumple_criterios_seguridad()
            case "30": es_numero_positivo_y_par()
            case "0":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción inválida. Intente de nuevo.")

# Ejecutar menú
menu()