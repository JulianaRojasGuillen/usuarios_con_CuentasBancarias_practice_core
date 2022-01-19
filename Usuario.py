from CuentaBancaria import CuentaBancaria

class Usuario:

    relacion_usuarios=[]

    #constructor
    def __init__(self, nombre, correo):
        self.nombre=nombre
        self.correo=correo
        self.cuentas={
            "cuenta_ingreso": CuentaBancaria(),
        }
        Usuario.relacion_usuarios.append(self)
        
    #métodos
    def hacer_deposito(self,monto,cuenta):
        self.cuentas[cuenta].deposito(monto)
        return self

    def hacer_retiro(self,monto,cuenta):
        self.cuentas[cuenta].retiro(monto)
        return self
    
    def mostrar_balance_usuario(self):
        print("Mostrando balance de cuentas:")
        for clave, valor in self.cuentas.items():
            print(clave)
            valor.mostrar_info_cuenta()

    def transfer_dinero(self, other_user, monto, cuenta_emisora, cuenta_receptora):
        self.cuentas[cuenta_emisora].balance-=monto
        other_user.cuentas[cuenta_receptora].deposito(monto)
        print(f"{self.nombre} transfirió {monto} {self.cuentas[cuenta_emisora].moneda} a {other_user.nombre}. Saldo {cuenta_emisora}: {self.cuentas[cuenta_emisora].balance}")
        return self

    def crear_nueva_cuenta(self,nombre_cuenta,moneda="soles"):
        self.cuentas[nombre_cuenta]=CuentaBancaria()
        self.cuentas[nombre_cuenta].moneda=moneda
        print(f"se creó la cuenta de nombre: {nombre_cuenta} con la sgte información inicial")
        self.cuentas[nombre_cuenta].mostrar_info_cuenta()

    def mostrar_nombre_cuentas(self):
        print(f"Las cuentas de {self.nombre} son:")
        for clave in self.cuentas.keys():
            print(clave)

    @classmethod
    def mostrar_cuentasExistentes_por_usuario(cls):
        print("------------------------------------------------------------")
        print(" A CONTINUACIÓN SE MUESTRA LAS CUENTAS POR USUARIO EXISTENTES")
        for i in range (0,len(Usuario.relacion_usuarios)):
            print("-----")
            print(f" Usuario: {Usuario.relacion_usuarios[i].nombre}")
            Usuario.relacion_usuarios[i].mostrar_balance_usuario()
            


    ##Otra forma de crear balance_usuario usando transformación a lista
    # def mostrar_balance_usuario(self):
    #     nombres_claves=list(self.cuentas.keys())
    #     print("--------")
    #     print("Mostrando balance de cuentas: ")
    #     for i in range(0,len(nombres_claves)):
    #         print (f"{nombres_claves[i]} : ")
    #         self.cuentas[nombres_claves[i]].mostrar_info_cuenta()
    #     return self
