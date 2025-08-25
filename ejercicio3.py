class Nota:
    def __init__(self, nota, nombreEstudiante):
        self.nota = nota
        self.nombreEstudiante = nombreEstudiante
        
    def ha_pasado(self):
        if self.nota > 75:
            print(f"El/la estudiante {self.nombreEstudiante} ha aprobado")
        else:
            print(f"El/la estudiante {self.nombreEstudiante} ha reprobado")
            

nota_1 = Nota(80, "Julien")
nota_1.ha_pasado()

nota_2 = Nota(45, "Amelie")
print(f"La nota obtenida por {nota_2.nombreEstudiante} en la primera correccción es: {nota_2.nota}")
nota_2.nota = 70
print(f"Segunda corrección, la nota de {nota_2.nombreEstudiante} es {nota_2.nota}")
nota_2.ha_pasado()
