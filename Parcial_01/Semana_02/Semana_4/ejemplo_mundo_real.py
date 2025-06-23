#PROGRAMA SIMULADOR DE SISTEMA BANCARIO
class cuenta_bancaria:
    
    #atributos
    def __init__(self,nombre_usuario,numero_cuenta,saldo):
        self.nombre_usuario = nombre_usuario
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        
    def datos_del_usuario(self):
        print("Usuario:",self.nombre_usuario)
        print("Numero de cuenta:",self.numero_cuenta)
        print("Saldo disponible:",self.saldo)
    
    #funcion deposito
    def depositar(self, monto):
        self.monto = monto
        self.saldo = self.saldo + monto
        print("Monto a depositar:", self.monto)
        print("Usuario:", self.nombre_usuario ,"\nSaldo disponible despues del deposito:", self.saldo)

    #funcion retirar
    def retirar(self,monto):
        if monto > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.monto = monto
            self.saldo = self.saldo - monto
            print("Monto a retirar:", self.monto)
            print("Usuario:", self.nombre_usuario,  "\nSaldo disponible despues del retiro:", self.saldo)
class Banco:   
    #atributos
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []
    
    #metodo agregar usuario
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        usuarios = usuario.nombre_usuario
        print(f"Usuario {usuarios} agregado al banco {self.nombre}.")

    
    def mostrar_usuarios(self):
        print(f"\nUsuarios registrados en {self.nombre}:")
        for u in self.usuarios:
            u.datos_del_usuario()
            print("***"*10)

    def buscar_por_cuenta(self, numero_cuenta):
        for u in self.usuarios:
            if u.numero_cuenta == numero_cuenta:
                return u
        return None
    
    #metodo transferir
    def transferir(self, cuenta_origen, cuenta_destino, monto):
        origen = self.buscar_por_cuenta(cuenta_origen)
        destino = self.buscar_por_cuenta(cuenta_destino)

        if origen is None or destino is None:
            print("Una de las cuentas no existe.")
            return

        if monto > origen.saldo:
            print(f"{origen.nombre_usuario} no tiene saldo suficiente para transferir.")
            return
        
        #para calculo dela transferencia (improvisado)
        origen.saldo = origen.saldo - monto
        destino.saldo = destino.saldo + monto

        print(f"Transferencia de ${monto} de {origen.nombre_usuario} a {destino.nombre_usuario} completada.")

            # ==== PROGRAMA PRINCIPAL ====
#datos de los usuarios
usuario1= cuenta_bancaria("Bryan Escobar",1020304050,1000)
usuario2= cuenta_bancaria("David Salinas",995013900,2250)
usuario1.datos_del_usuario()
print("***"*10)
usuario2.datos_del_usuario()
print("***"*10)

#Realizar deposito
usuario1.depositar(59)
print("***"*10)

#Realizar retiro
usuario2.retirar(200)
print("***"*10)

#Nombre del banco
banco = Banco("Banco Pichincha")

# Agregarlos al banco
banco.agregar_usuario(usuario1)
banco.agregar_usuario(usuario2)

# Mostrar usuarios antes de la transferencia
print("***"*10)
print("Usuarios antes de la transferencia:")
banco.mostrar_usuarios()

# Realizar transferencia de Bryan a David
print("***"*10)
print("Realizando transferencia de $450 de Bryan a David...")
banco.transferir(1020304050, 995013900, 450)

# Mostrar usuarios después de la transferencia
print("***"*10)
print("Usuarios después de la transferencia:")
banco.mostrar_usuarios()

