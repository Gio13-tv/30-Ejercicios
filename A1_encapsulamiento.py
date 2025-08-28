class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular     # Público 
        self._saldo = saldo        # Protegido (convención, accesible pero no recomendado)
        self.__pin = "1234"        # Privado porque solo se accede dentro de la clase
        
    def depositar(self, monto):
        self._saldo += monto # Agrega monto al saldo siempre y cuando no sea negativo 
        
    def retirar(self, monto, pin):
        if pin == self.__pin: # procede si el pin es correcto
            if monto <= self._saldo: # Revisa que haya saldo suficiente
                self._saldo -= monto
                print('Retiro exitoso')
            else:
                print('Fondos insuficientes') # Mensaje de error
        return f'Saldo actual: {self._saldo}' # El monto no cambia
    
    def mostrar_saldo(self):
        return f"Saldo actual: {self._saldo}" # Muestra saldo actual


# prueba
cuenta = CuentaBancaria("Lucas", 1500)
print(cuenta.titular)    # Público
#print(cuenta.__pin)     # Privado → Error
print(cuenta.mostrar_saldo())

while True:
    print("\n--- Menú ---")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Mostrar saldo")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        monto = float(input("¿Cuánto quieres depositar?: "))
        cuenta.depositar(monto)
        print("Depósito exitoso")
        print(cuenta.mostrar_saldo())

    elif opcion == "2":
        monto = float(input("¿Cuánto quieres retirar?: "))
        pin = input("Ingresa tu PIN: ")
        print(cuenta.retirar(monto, pin))

    elif opcion == "3":
        print(cuenta.mostrar_saldo())

    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida")
