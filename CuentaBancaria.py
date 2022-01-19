class CuentaBancaria:

    relacion_cuentas=[]

    def __init__(self, moneda="soles" , tasa_interes=0.01, balance=0):
        self.tasa_interes=tasa_interes
        self.balance=balance
        self.moneda=moneda
        CuentaBancaria.relacion_cuentas.append(self)

    def deposito(self,monto):
        self.balance+=monto
        return self
    
    def retiro(self,monto):
        self.balance-=monto
        return self
    
    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}, Tasa de interés: {self.tasa_interes}, Moneda: {self.moneda}")
        return self
    
    def generar_interes(self):
        if self.balance>0:
            self.balance=self.balance*(1+self.tasa_interes)
            return self
        else:
            print("Saldo negativo, no es posible generar interés")
            return self
    
    def cambiarMoneda(self,nuevaMoneda):
        print(f"Se cambió la moneda de {self.moneda} a {nuevaMoneda}")
        self.moneda=nuevaMoneda
        return self
        

    @classmethod
    def info_cuentas_global(cls):
        print("Las cuentas registradas son: ")
        for i in range(0,len(CuentaBancaria.relacion_cuentas)):
            CuentaBancaria.mostrar_info_cuenta(CuentaBancaria.relacion_cuentas[i])

    

