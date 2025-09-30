class Empleado:
    def _init_(self, nombre, funcion, salario):
        self.nombre = nombre
        self.funcion = funcion
        self.salario = salario
        self.horas_trabajo = 0
        
    def trabajar(self, numero_horas):
        self.horas_trabajo += numero_horas
        return f"El empleado {self.nombre} ha trabajado {self.horas_trabajo} horas."
        
    def info_sueldo(self):
        return f"El empleado {self.nombre} recibe un salario de {self.salario} euros."
        
    def dar_aumento(self, cantidad):
        self.salario += cantidad
        return f"El empleado {self.nombre} ha recibido un aumento de {cantidad} euros, lo que le da un salario de " \
               f"{self.salario} euros."
               
    def info_funcion(self):
        return f"El empleado {self.nombre} trabaja como {self.funcion}."

empleado_1 = Empleado("Julien", "Ingeniero", 4000)

print(empleado_1.trabajar(8)) # Se corrige el ejemplo de uso para incluir las 8 horas
print(empleado_1.info_sueldo())
print(empleado_1.dar_aumento(600))
print(empleado_1.info_funcion())