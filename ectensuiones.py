#Programa que valide correo electrónico
try:
    correo = input("Ingrese su correo: ")
    if "@" not in correo or "." not in correo:
        raise ValueError("Correo inválido")
    print("Correo válido")
except ValueError as e:
    print(f"Error: {e}")

#inventario de zapatos
try:
    inventario = {
        "tenis": {"talla": [38, 39, 40], "color": ["negro", "blanco"]},
        "botas": {"talla": [40, 41, 42], "color": ["café", "negro"]}
    }
    tipo = input("Tipo de zapato: ").lower()
    talla = int(input("Talla: "))
    color = input("Color: ").lower()
    if tipo not in inventario:
        raise KeyError("Tipo de zapato no disponible")
    if talla not in inventario[tipo]["talla"]:
        raise ValueError("Talla no disponible")
    if color not in inventario[tipo]["color"]:
        raise ValueError("Color no disponible")
    print("Producto disponible")
except KeyError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")

#Programa que reciba una fecha de nacimiento y arroje la edad de la persona
from datetime import datetime
try:
    nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
    fecha_nacimiento = datetime.strptime(nacimiento, "%Y-%m-%d")
    hoy = datetime.now()
    edad = hoy.year - fecha_nacimiento.year
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    print(f"Edad: {edad} años")
except ValueError:
    print("Formato de fecha inválido")

#calculo de una nomina
try:
    sueldo = float(input("Ingrese su sueldo mensual: "))
    if sueldo < 0:
        raise ValueError("El sueldo no puede ser negativo")
    pago_15_dias = sueldo / 2
    auxilio_transporte = 162000  # valor aproximado en Colombia
    auxilio_15_dias = auxilio_transporte / 2
    total = pago_15_dias + auxilio_15_dias
    print(f"Pago 15 días: {pago_15_dias}")
    print(f"Auxilio transporte: {auxilio_15_dias}")
    print(f"Total a pagar: {total}")
except ValueError as e:
    print(f"Error: {e}")

#Programa que guarde en un archivo.txt
try:
    palabras = []
    for i in range(10):
        palabra = input(f"Ingrese palabra {i+1}: ")
        palabras.append(palabra)
    with open("palabras.txt", "w") as archivo:
        for palabra in palabras:
            archivo.write(palabra + "\n")
    print("Palabras guardadas correctamente")
except Exception as e:
    print(f"Ocurrió un error: {e}")

#David cuellar y Sebastian NIeto
