## Ejercicio 24: Método de clase

class CuentaBancaria:
    ## variables de clase
    tipo_de_cuenta = "Ahorros"
    tasa_interes = 0.07

    def _init_(self, nombre: str, apellido: str, num_cuenta: str, saldo_cuenta: float):
        """
        Constructor para inicializar los atributos de la clase
        """
        self.nombre = nombre
        self.apellido = apellido
        self.num_cuenta = num_cuenta
        self.saldo_cuenta = saldo_cuenta

    @classmethod
    def establecer_tasa_interes(cls, nueva_tasa: float):
        """
        Método de clase para modificar la tasa de interés
        """
        cls.tasa_interes = nueva_tasa

    @classmethod
    def cambiar_tipo_cuenta(cls, tipo_cuenta: str):
        """
        Método de clase
        """
        cls.tipo_de_cuenta = tipo_cuenta

    def deposito(self, cantidad: float):
        """
        Método para depositar dinero en la cuenta bancaria.
        Permite agregar la cantidad depositada al saldo de la cuenta.
        """
        self.saldo_cuenta = self.saldo_cuenta + cantidad

    def retiro(self, cantidad: float):
        """
        Este método permite retirar una cantidad de la cuenta bancaria.
        """
        if cantidad > self.saldo_cuenta:
            print("Su saldo es insuficiente")
        else:
            self.saldo_cuenta = self.saldo_cuenta - cantidad

    def aplicar_tasa_interes(self):
        """
        Este método permite aplicar una tasa de interés a la suma
        existente en la cuenta bancaria.
        """
        self.saldo_cuenta = self.saldo_cuenta + self.saldo_cuenta * CuentaBancaria.tasa_interes

    def _str_(self):
        """
        Este método especial permite personalizar la representación en cadena de caracteres
        del objeto de esta clase.
        """
        return (f"Número de cuenta: {self.num_cuenta} \n"
                f"Tipo de cuenta: {CuentaBancaria.tipo_de_cuenta} \n"
                f"Titular de la cuenta: {self.nombre} {self.apellido} \n"
                f"Saldo de cuenta: {self.saldo_cuenta} euros.")

## Ejemplos de pruebas / casos de uso

## Llamada a métodos de clase
CuentaBancaria.cambiar_tipo_cuenta("Corriente")
CuentaBancaria.establecer_tasa_interes(0.05)

## Creación de instancia y llamada a métodos
cuenta_1 = CuentaBancaria("Laurent", "Dubois", "983758XZ", 3000)

print(cuenta_1)
print("-" * 20)
print("Retiro de una cantidad de 4000 euros.")
cuenta_1.retiro(4000)

print("-" * 20)
print(cuenta_1)

print("-" * 20)
print("Retiro de una cantidad de 1500 euros.")
cuenta_1.retiro(1500)

print("-" * 20)
print(cuenta_1)

print("-" * 20)
print("Depósito de una cantidad de 500 euros.")
cuenta_1.deposito(500)

print("-" * 20)
print(cuenta_1)

print("-" * 20)
print(f"Aplicación de la tasa de interés de: {CuentaBancaria.tasa_interes}")
cuenta_1.aplicar_tasa_interes()
print(cuenta_1)