# Clase base: Persona
class Persona:
    def _init_(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        return ("Mi nombre es " + self.nombre + ", tengo " + str(self.edad) +
                " años y soy un " + self.genero + ".")

    def esAdulto(self):
        return self.edad >= 18

# Clase derivada: Estudiante
class Estudiante(Persona):
    def _init_(self, nombre, edad, genero, nivel):
        """
        Inicializar los atributos de la clase Estudiante
        nombre ::: str : el nombre del estudiante a inscribir
        edad ::: int : la edad del estudiante a inscribir
        genero ::: str : el género del estudiante a inscribir
        nivel ::: str : el nivel académico del estudiante
        """
        super()._init_(nombre, edad, genero)
        self.nivel = nivel

    def inscripcion(self, estudiantes_inscritos):
        """
        Método que permite agregar un estudiante a la lista
        de estudiantes inscritos en los cursos
        """
        estudiantes_inscritos.append((self.nombre, self.edad, self.genero, self.nivel))

# Lista para almacenar estudiantes inscritos
estudiantes_inscritos = []

# Creación de instancias
estudiante1 = Estudiante("Fabrice", 17, "hombre", "segundo año")
estudiante1.inscripcion(estudiantes_inscritos)

estudiante2 = Estudiante("Julie", 14, "mujer", "primaria")
estudiante2.inscripcion(estudiantes_inscritos)

# Visualización de los estudiantes inscritos
print("Los estudiantes inscritos en los cursos son:\n", estudiantes_inscritos)