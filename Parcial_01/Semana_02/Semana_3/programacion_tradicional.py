def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese la temperatura de cada día de la semana:")
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
        temp = float(input(f"Temperatura del dia {dia}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"\nEl promedio semanal de temperatura es de: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
