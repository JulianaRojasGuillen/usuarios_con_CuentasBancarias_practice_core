from Usuario import Usuario

#Creando usuarios
gaby=Usuario("Gaby","gabymaria100@gmail.com")
cilo=Usuario("Cilo","cilorojas24@mail.com")

#Haciendo depósitos y mostrando balance
cuenta_ingreso="cuenta_ingreso"
gaby.hacer_deposito(100,cuenta_ingreso).hacer_deposito(200,cuenta_ingreso).hacer_retiro(50,cuenta_ingreso).mostrar_balance_usuario()
cilo.hacer_deposito(1000,cuenta_ingreso).hacer_retiro(20,cuenta_ingreso).mostrar_balance_usuario()

#Haciendo transferencia a otra cuenta
gaby.transfer_dinero(cilo,20,cuenta_ingreso,cuenta_ingreso)

#Creando una nueva cuenta a un usuario existente
gaby.crear_nueva_cuenta("cuenta_ahorros")
cilo.crear_nueva_cuenta("cuenta_abc")

#Creando un tercer usuario
martha=Usuario("Martha", "martha@gmail.com") #por defecto se creó una cuenta en soles

#Cambiando el tipo de moneda a la cuenta creada de Martha
martha.cuentas["cuenta_ingreso"].cambiarMoneda("dólares")

# Mostrando el cambio de moneda en la cuenta de Martha
martha.cuentas["cuenta_ingreso"].mostrar_info_cuenta()

# Mostrando balance de Martha
martha.mostrar_balance_usuario()

# Mostrando qué cuentas tiene Gaby
gaby.mostrar_nombre_cuentas()
