## Ejercicio 20: Polimorfismo

## clase Padre
class TrabajadorEmpresa:
    def _init_(self, nombre_trabajador: str, salario: float, edad: int):
        """
        Constructor: Inicialización de los atributos de la
        clase TrabajadorEmpresa
        """
        self.nombre_trabajador = nombre_trabajador
        self.salario = salario
        self.edad = edad

    def mostrar_funcion(self):
        """
        Este método permite mostrar la función del objeto
        proveniente de esta clase
        """
        print("Soy un trabajador en una empresa")

    def mostrar_info(self):
        """
        Este método permite mostrar la información relacionada
        con el trabajador
        """
        print(f"Nombre: {self.nombre_trabajador}")
        print(f"Salario: {self.salario}")
        print(f"Edad: {self.edad}")

## clase Hijo
class Director(TrabajadorEmpresa):
    def _init_(self, nombre_director: str, salario: float, edad: int, prima: float):
        """
        Este método permite inicializar los atributos de la
        clase Director
        """
        super()._init_(nombre_director, salario, edad)
        self.prima = prima

    def mostrar_funcion(self):
        """
        Este método muestra la función del objeto
        proveniente de la clase Director
        """
        print("Soy un director de empresa")

    def mostrar_info(self):
        """
        Este método permite mostrar la información
        concerniente al objeto de esta clase
        """
        super().mostrar_info()
        print(f"La prima anual percibida es de {self.prima} euros.")

## clase Hijo
class Ingeniero(TrabajadorEmpresa):
    def _init_(self, nombre_ingeniero: str, salario: float, edad: int, especialidad: str):
        """
        Constructor: Inicializar los atributos de la clase
        """
        super()._init_(nombre_ingeniero, salario, edad)
        self.especialidad = especialidad

    def mostrar_funcion(self):
        """
        Este método permite mostrar la función del objeto
        proveniente de esta clase
        """
        print("Soy ingeniero")

    def mostrar_info(self):
        """
        Este método permite mostrar la información relacionada
        con el objeto de la clase
        """
        super().mostrar_info()
        print(f"Soy un Ingeniero especializado en {self.especialidad}")


## Ejemplos de pruebas / casos de uso

## Instanciación de dos objetos provenientes de las dos
## clases Director e Ingeniero
director = Director("Julien Lecoq", 75000, 43, 5000)
ingeniero = Ingeniero("Baptiste Leblanc", 40000, 32, "Inteligencia Artificial")

trabajadores = [director, ingeniero]

## Llamada de métodos
for trabajador in trabajadores:
    trabajador.mostrar_funcion()
    trabajador.mostrar_info()
    print() # Salto de línea para separar la información de cada trabajador