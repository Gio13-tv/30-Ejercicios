## Ejercicio 19: Herencia

## clase Padre
class Texto:
    def _init_(self, frase: str):
        """
        Constructor que permite inicializar el atributo
        'frase'.
        """
        self.frase = frase

    def mostrar_texto(self):
        """
        Este método permite mostrar la 'frase'
        en la consola.
        """
        print(self.frase)

## clase Hijo
class TextoItalico(Texto):
    def _init_(self, frase: str):
        """
        Constructor
        """
        super()._init_(frase)

    def mostrar_texto(self):
        """
        Este método permite mostrar el texto en la consola en Itálica.
        Para indicar que una frase está en itálica, añadimos un guion
        bajo al principio y al final de la frase.
        """
        print("" + self.frase + "")

## clase Hijo
class TextoNegrita(Texto):
    def _init_(self, frase: str):
        """
        Constructor
        """
        super()._init_(frase)

    def mostrar_texto(self):
        """
        Este método permite mostrar el texto en la consola en Negrita.
        Para indicar que una frase está en negrita, añadimos un doble asterisco
        al principio y al final de la frase.
        """
        print("" + self.frase + "")

## Ejemplos de pruebas / casos de uso
## Instanciación de tres objetos
texto_1 = Texto("Aprender POO en Python a través de la práctica")
texto_2 = TextoItalico("Aprender POO en Python a través de la práctica")
texto_3 = TextoNegrita("Aprender POO en Python a través de la práctica")

## Creación de una lista para el código
textos = [texto_1, texto_2, texto_3]

## Llamando al método mostrar_texto()
## según el objeto de la clase correspondiente.
for texto in textos:
    texto.mostrar_texto()