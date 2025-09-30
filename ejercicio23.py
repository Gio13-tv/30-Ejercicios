## Ejercicio 23: Método de clase

class Usuario:
    ## variable de la clase que almacenará
    ## el número de usuarios activos
    usuarios_activos = 0

    def _init_(self, nombre: str, apellido: str, edad: int):
        """
        Constructor que permite inicializar los atributos de la clase
        y sumar 1 (incrementar) en la variable de clase
        con cada creación de instancia.
        """
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        Usuario.usuarios_activos += 1

    @classmethod
    def extraer_info(cls, cadena: str):
        """
        Este método de clase permite extraer el nombre, apellido y
        edad de la cadena pasada como parámetros y crear una instancia
        """
        nombre, apellido, edad = cadena.split(",")
        return cls(nombre, apellido, int(edad))

    @classmethod
    def mostrar_usuarios_activos(cls):
        """
        Este método de clase permite mostrar el
        número de usuarios activos
        """
        return f"Actualmente, hay {cls.usuarios_activos} usuarios(s) activos"

    def desconectar(self):
        """
        Este método permite al usuario desconectarse.
        Además, nos muestra el nombre y apellido del usuario que
        se ha desconectado.
        """
        Usuario.usuarios_activos -= 1
        return f"El/la usuario(a) {self.nombre} {self.apellido} se ha desconectado"

## Ejemplos de pruebas / casos de uso

## Creación de instancias
usuario_1 = Usuario("Martin", "Leboeuf", 35)

## Creación de una instancia usando un método de clase
usuario_2 = Usuario.extraer_info("Emilie, Dupont, 28")

## Llamadas a métodos
print(Usuario.mostrar_usuarios_activos())
print(usuario_2.desconectar())
print(usuario_1.mostrar_usuarios_activos())