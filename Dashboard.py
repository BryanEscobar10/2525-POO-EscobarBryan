import os
import subprocess


def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def ejecutar_script(ruta_script):
    print(f"\n--- Ejecutando {ruta_script} ---\n")
    try:
        subprocess.run(['python', ruta_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script: {e}")
    except FileNotFoundError:
        print("No se encontró el ejecutable de Python. ¿Está correctamente instalado?")


def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Parcial_01/Semana_02/Tarea_Semana_02.py',
        '2': 'Parcial_01/Semana_02/Semana_3/POO.py',
        '3': 'Parcial_01/Semana_02/Semana_3/programacion_tradicional.py',
        '4': 'Parcial_01/Semana_02/Semana_4/ejemplo_mundo_real.py',
        '5': 'Parcial_01/Semana_02/Semana_5/tipos_de_datos-indicadores.py',
        '6': 'Parcial_01/Semana_02/Semana_6/aplicacion_conceptos_POO.py',
        '7': 'Parcial_01/Semana_02/Semana_7/Constructores_y_Destructores.py'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver y ejecutar, o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
            ejecutar_script(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    mostrar_menu()
