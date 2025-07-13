#PROGRAMA SIMULADOR DE CAJERO AUTOMATICO
class CajeroAutomatico:
    def __init__(self, nombre_usuario, numero_cuenta):   #Constructor, inicializa el nombre y numero de cuenta
        self.nombre_usuario = nombre_usuario
        self.numero_cuenta = numero_cuenta
        print(f"Bienvenido usuario {self.nombre_usuario} de la cuenta {self.numero_cuenta}")
    
    def retirar_dinero(self, monto):           #Metodo para retirar dinero
        self.monto = monto
        print(f"Usuario {self.nombre_usuario} ha retirado el monto de ${self.monto}")

    def __del__(self):             #Destructor, indica que la seción se ha cerrado
        print(f"Sesión de cajero finalizada, seguridad activada.")

usuario = CajeroAutomatico("Bryan Escobar", 892893002)
usuario.retirar_dinero(150)
del usuario    #Para destruir el objeto justo después de que se termina de usar y no al final

print("-"*50)

#PROGRAMA USO DE UNA LAMPARA
class Lampara:
    def __init__(self):    #Constructor
        print("Lámpara encendida")  
    
    def __del__(self):     #Destructor
        print("Lámpara apagada, cuarto a oscuras")


l = Lampara()
print("Usando la lámpara, cuarto iluminado")

#Destructor se llama automaticamente

