## Ejercicio 17: Une classe string personnalisé contenant des méthodes spéciales

class MiCadenaPersonal:
    def _init_(self, variable_str: str):
        """
        Una clase String personalizado que contiene métodos especiales
        """
        self.variable_str = variable_str

    def _add_(self, cadena):
        """
        Este método especial permite concatenar dos cadenas utilizando el operador +.
        Nuestra concatenación personalizada contendrá el separador |
        """
        return self.variable_str + " | " + cadena.variable_str

    def _mul_(self, escalar: int):
        """
        Este método especial permite repetir una cadena un número de veces igual al
        escalar pasado como parámetro
        """
        return self.variable_str * escalar

    def _len_(self):
        """
        Este método permite contar el número de caracteres en una cadena sin tener
        en cuenta las comas/puntos, los signos de exclamación, los
        signos de interrogación, los espacios y el carácter | .
        """
        caracter_eliminar = [",", ".", "?", "!", " ", "|"]
        variable_str_1 = self.variable_str
        
        # Eliminamos los caracteres especificados
        for c in caracter_eliminar:
            variable_str_1 = variable_str_1.replace(c, "")
            
        return len(variable_str_1)

    def _str_(self):
        """
        Este método especial permite personalizar la representación del
        objeto de la clase en forma de cadena de caracteres.
        """
        return self.variable_str

    def _contains_(self, subcadena: str):
        """
        Este método especial permite verificar si una cadena está contenida
        en el objeto de la clase.
        """
        if subcadena in self.variable_str:
            return True
        return False


## Ejemplos de pruebas / casos de uso

## Instanciación de dos objetos de la clase MiCadenaPersonal
cadena_1 = MiCadenaPersonal("¡Hola, cómo estás!")
cadena_2 = MiCadenaPersonal("Bienvenido a este curso.")

## Llamada a métodos
print(cadena_1 + cadena_2)
print("Cadena_1 + cadena_2 es:", cadena_1 + cadena_2)

# Multiplicación y longitud
print(cadena_2 * 2)
print(f"La longitud de cadena_1 es: {len(cadena_1)}")
print(f"La longitud de cadena_2 es: {len(cadena_2)}")

# Uso de _contains_ (operador 'in')
print(f"¿La cadena 'cómo' contiene en cadena_1?: {'cómo' in cadena_1}")