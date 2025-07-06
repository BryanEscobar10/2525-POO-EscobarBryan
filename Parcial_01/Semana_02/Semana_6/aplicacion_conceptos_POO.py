
class Persona:                    #Clase padre
    def __init__(self,nombre,cedula):
        self.nombre = nombre
        self._cedula = cedula     #Encapsulación

    def describir (self):         #Metodo a sobreescribir
        return f"El numero de cedula {self._cedula} pertenece a {self.nombre}"
    
    def get_cedula (self):                  # Getter (acceso controlado al atributo protegido)
        return f"Cedula de Messi: {self._cedula}"
    
    def set_cedula (self, nueva_cedula):    # Setter (modificación controlada del atributo)
        self._cedula = nueva_cedula
        return f"La cedula {self._cedula} pertenece a otra persona"



class Docente (Persona):          # Clase hija que hereda de Persona (Herencia)
    def __init__(self, nombre, cedula, area, nivel_preparacion):
        super().__init__(nombre, cedula)
        self.area = area
        self.nivel_preparacion = nivel_preparacion

    def describir (self):         #Metodo sobreescrito (Polimorfismo de sobreescritura)
        return f"El {self.nivel_preparacion} {self.nombre} de cedula {self._cedula} es docente del area de {self.area}"



class Estudiante (Persona):       # Clase hija que hereda de Persona (Herencia)
    def __init__(self, nombre, cedula, nivel, carrera):
        super().__init__(nombre, cedula)
        self.nivel = nivel
        self.carrera = carrera

    def describir(self):         #Metodo sobreescrito (Polimorfismo de sobreescritura)
        return f"El estudiante {self.nombre} de cedula {self._cedula} esta cursando el {self.nivel} nivel en la carrera de {self.carrera}"



#PROGRAMA PRINCIPAL    
Persona1 = Persona("Messi", 102456893)
Persona2 = Docente("GUSTAVO FERNÁNDEZ", 159993625, "POO", "Magister")
Persona3 = Estudiante("Bryan Escobar", 8826543587, "segundo", "TICS")

print(Persona1.describir())
print(Persona2.describir())
print(Persona3.describir())

print(Persona1.get_cedula())
print(Persona1.set_cedula(52528336958))
