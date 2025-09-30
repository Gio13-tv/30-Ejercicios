## Ejercicio 16: Gestión de archivos

class ManipuladoresArchivos:
    def _init_(self, nombreArchivo: str):
        """
        constructor
        """
        self.nombreArchivo = nombreArchivo
        # Abrimos el archivo en modo lectura y escritura ('r+')
        self.archivo = open(nombreArchivo, "r+") 
        print(f"El archivo '{nombreArchivo}' sido abierto en modo lectura y escritura!")

    def escribir_archivo(self, frase: str):
        """
        Este método permite escribir una frase en un archivo
        """
        self.archivo.write(frase)
        print(f"La frase '{frase}' ha sido escrita en el archivo {self.nombreArchivo}")

    def _del_(self):
        """
        Destructor: permite cerrar el archivo y eliminar las referencias de objetos
        vinculadas al objeto creado.
        """
        self.archivo.close()
        print(f"El archivo {self.nombreArchivo} ha sido cerrado.")


## Ejemplos de pruebas / casos de uso

## Creación de una instancia
# Nota: La ruta de archivo debe ser válida en tu sistema.
# Usaré un nombre de archivo simple para evitar errores de ruta.
archivo_1 = ManipuladoresArchivos('archivo_prueba.txt')

## Escritura en el archivo
archivo_1.escribir_archivo("Hola, ¿cómo estás?")

## Cierre y eliminación del objeto archivo_1
# Esto llama al destructor _del_
del archivo_1