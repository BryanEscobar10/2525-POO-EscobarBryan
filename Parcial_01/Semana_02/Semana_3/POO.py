class DiaClima:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.temperatura = temperatura

class SemanaClima:
    def __init__(self):
        self.dias = []

    def ingresar_datos(self):
        print("Ingrese la temperatura de cada día de la semana:")
        for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
            temp = float(input(f"Temperatura del dia {dia}: "))
            self.dias.append(DiaClima(dia, temp))

    def calcular_promedio(self):
        total = sum(dia.temperatura for dia in self.dias)
        return total / len(self.dias)

def main():
    semana = SemanaClima()
    semana.ingresar_datos()
    promedio = semana.calcular_promedio()
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
