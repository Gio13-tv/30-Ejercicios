## Ejercicio 18: Polimorfismo

class Animal:
    def _init_(self, nombre_Animal: str):
        """
        Constructor de la clase Animal
        """
        self.nombre_animal = nombre_Animal

    def hablar(self):
        """
        Este método está vacío.
        Solo sirve para ilustrar el polimorfismo.
        """
        pass

## Una clase hija que hereda de la Clase Animal
class Gato(Animal):
    def _init_(self, nombre_gato: str):
        """
        Constructor
        """
        super()._init_(nombre_gato)

    def hablar(self):
        """
        Este método devuelve una cadena de caracteres
        que hace referencia al perro
        """
        return self.nombre_animal + " dice ¡Miau miau!"

## Una clase hija que hereda de la Clase Animal
class Perro(Animal):
    def _init_(self, nombre_perro: str):
        """
        Constructor
        """
        super()._init_(nombre_perro)

    def hablar(self):
        """
        Este método devuelve una cadena de caracteres
        que hace referencia al perro
        """
        return self.nombre_animal + " dice ¡Guau guau!"

## Ejemplos de pruebas / casos de uso

## Instanciación de dos objetos
rocky = Perro("Rocky")
felix = Gato("Felix")

## Llamada a métodos
print(rocky.hablar())
print(felix.hablar())