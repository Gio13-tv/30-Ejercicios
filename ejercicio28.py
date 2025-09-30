## Ejercicio 28: Creación de un diccionario personalizado

class MiDiccionario:
    def _init_(self):
        """
        Constructor: permite crear un objeto que contiene
        un diccionario vacío
        """
        self.objetos = {}

    def agregar_elemento(self, clave: str, valor: str):
        """
        Método que permite agregar un elemento
        """
        self.objetos[clave] = valor

    def eliminar_elemento(self, clave: str):
        """
        Método que permite eliminar un elemento
        del objeto de la clase
        """
        del self.objetos[clave]
        
    # --- Métodos Mágicos (Sobrecarga de Operadores) ---

    def _iter_(self):
        """
        Método especial que permite obtener un iterador
        sobre los elementos del objeto de la clase
        """
        return iter(self.objetos)

    def _getitem_(self, clave: str):
        """
        Método especial que permite obtener el valor asociado
        a una clave en un objeto de la clase
        """
        return self.objetos[clave]

    def _setitem_(self, clave: str, valor: str):
        """
        Método especial que permite modificar el valor de una
        clave en un objeto de la clase
        """
        self.objetos[clave] = valor

    def _len_(self):
        """
        Método especial que permite conocer el número de
        elementos contenidos en un objeto de la clase
        """
        return len(self.objetos)

    def _str_(self):
        """
        Método especial que permite personalizar la
        representación del objeto de la clase
        """
        return f"El contenido del diccionario es: {self.objetos}"

    # --- Métodos de Listado ---
    
    def listar_claves(self):
        """
        Método que permite devolver en forma de lista
        las claves del diccionario de la clase
        """
        return list(self.objetos.keys())

    def listar_valores(self):
        """
        Método que permite devolver en forma de lista
        los valores del objeto de la clase
        """
        return list(self.objetos.values())
    
    def listar_elementos(self):
        """
        Método que permite devolver en forma de lista
        los elementos del objeto de la clase
        """
        return list(self.objetos.items())

    # --- Métodos Funcionales ---

    def limpiar_diccionario(self):
        """
        Método que permite eliminar todos los elementos
        contenidos en el objeto de la clase
        """
        self.objetos.clear()
        return "Diccionario limpiado."

    def contiene_clave(self, clave: str):
        """
        Método que permite verificar si una
        clave existe en un objeto de la clase
        """
        if clave in self.objetos:
            return True
        return False

## Ejemplos de pruebas / casos de uso

## Creación de una instancia
dicc_1 = MiDiccionario()

## Llamada de métodos
dicc_1.agregar_elemento("fruta", "manzana")
dicc_1.agregar_elemento("vegetal", "zanahoria")
dicc_1.agregar_elemento("carne", "res")

# Usando _str_
print(dicc_1) 
print("-" * 30)

## Creación de un iterador sobre dicc_1 (usando _iter_)
dicc_iter_1 = iter(dicc_1)

print("primera iteración:")
print(next(dicc_iter_1))
print("segunda iteración:")
print(next(dicc_iter_1))
print("tercera iteración:")
print(next(dicc_iter_1))
print("-" * 30)

# Usando _len_
print(f"El número de elementos en el diccionario es: {len(dicc_1)}")
print(f"Las claves del diccionario 'dicc_1' son: {dicc_1.listar_claves()}")
print(f"Los valores del diccionario 'dicc_1' son: {dicc_1.listar_valores()}")

# Usando contiene_clave
print(f"¿'fruta' está en dicc_1? ({dicc_1.contiene_clave('fruta')})")

# Usando listar_elementos
print(f"La lista de elementos del diccionario 'dicc_1' es: {dicc_1.listar_elementos()}")
print("-" * 30)

# Usando limpiar_diccionario
print(dicc_1.limpiar_diccionario())
print("Después de limpiar el diccionario:")
print(dicc_1)