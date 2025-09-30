## Ejercicio 22: Métodos estáticos, herencia, polimorfismo

class Computadora:
    def _init_(self, marca: str, modelo: str, precio: float):
        """
        Constructor para inicializar las variables
        de instancia
        """
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    @staticmethod
    def listar_marcas():
        """
        Este método estático permite devolver las
        marcas disponibles
        """
        return "Dell, HP, Lenovo, Apple"

## clase Hijo
class ComputadorEscritorio(Computadora):
    def _init_(self, marca: str, modelo: str, precio: float, tamano_unidad_central: str):
        """
        Constructor que permite inicializar los atributos
        de la clase OrdenadorDeMesa
        """
        super()._init_(marca, modelo, precio)
        self.tamano_unidad_central = tamano_unidad_central

    def mostrar_informacion(self):
        """
        Este método permite mostrar la información relacionada
        con el objeto de esta clase
        """
        return (f"La computadora de escritorio de la marca {self.marca} ({self.modelo}) - "
                f"con una unidad central de tamaño {self.tamano_unidad_central} - "
                f"cuesta {self.precio} euros.")

## clase Hijo
class ComputadoraPortatil(Computadora):
    def _init_(self, marca: str, modelo: str, precio: float, tamano_pulgadas: float):
        """
        Constructor
        """
        super()._init_(marca, modelo, precio)
        self.tamano_pulgadas = tamano_pulgadas

    def mostrar_informacion(self):
        """
        Este método permite mostrar la información relacionada
        con el objeto de esta clase
        """
        return (f"La computadora portátil de la marca {self.marca} ({self.modelo}) "
                f"con una pantalla de {self.tamano_pulgadas} pulgadas cuesta {self.precio} euros.")


## Ejemplos de pruebas / casos de uso

## Llamada del método estático
print("Las marcas de computadoras disponibles son:", Computadora.listar_marcas())

## Creación de las instancias
ordenador_escritorio = ComputadorEscritorio("Dell", "78L", 800, "5L")
computador_portatil = ComputadoraPortatil("HP", "X1A", 950, 15.6)

## Llamadas de los métodos de instancia
print(ordenador_escritorio.mostrar_informacion())
print(computador_portatil.mostrar_informacion())