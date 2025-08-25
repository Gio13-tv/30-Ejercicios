class Persona:
    def _init_(self, nombre, edad, genero):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        
    def presentarse(self):
        return ("Mi nombre es " + self.nombre + ", tengo " + str(self.edad) +
            " años y soy un " + self.genero + ".")

    def esAdulto(self):
       if self.edad >= 18:
        return True
       else:
        return False

persona1 = Persona("Martin", 23, "hombre")

print(persona1.presentarse())
print(persona1.esAdulto())