import os

class gestionadorArchivos:
    def _init_(self, directorio: str):
        self.directorio = directorio

    def listar_archivos(self):
        return os.listdir(self.directorio)

    def crear_archivo(self, archivo: str):
        open(f"{self.directorio}/{archivo}", "w").close()

    def eliminar_archivo(self, archivo: str):
        os.remove(f"{self.directorio}/{archivo}")

    def renombrar_archivo(self, nombre_antiguo: str, nuevo_nombre: str):
        os.rename(f"{self.directorio}/{nombre_antiguo}", f"{self.directorio}/{nuevo_nombre}")

    @staticmethod
    def extension_archivo(nombre_archivo: str):
        return os.path.splitext(nombre_archivo)[1]

class gestionadorArchivosAudio(gestionadorArchivos):
    def _init_(self, directorio: str):
        super()._init_(directorio)

    def listar_archivos_audio(self):
        extensiones_audio = [".mp3", ".wav", ".flac"]
        archivos_en_directorio = self.listar_archivos()
        
        # Filtra archivos que tienen una extensión de audio usando el método estático heredado
        return [f for f in archivos_en_directorio if gestionadorArchivos.extension_archivo(f) in extensiones_audio]

## Ejemplos de pruebas / casos de uso
# NOTA: Las rutas de archivo en el ejemplo están codificadas (hardcoded) para un usuario específico.
# Para que este código funcione, debes reemplazar las rutas de ejemplo
# ('C://Users/laurentine.Masson/Carpeta_texto/', etc.) por rutas válidas en tu sistema
# donde existan o puedan crearse los archivos y directorios.

# # Ejemplo para gestionadorArchivos (Texto)
# gestion_archivo_texto = gestionadorArchivos("C://Users/laurentine.Masson/Carpeta_texto/")
# print(f"Los archivos existentes en el directorio {gestion_archivo_texto.directorio} son: {gestion_archivo_texto.listar_archivos()}")

# gestion_archivo_texto.crear_archivo("archivo_2.txt")
# print(f"Después de crear un nuevo archivo de son: {gestion_archivo_texto.listar_archivos()}")

# gestion_archivo_texto.eliminar_archivo("archivo_2.txt")
# print(f"Después de eliminar un archivo del directorio: {gestion_archivo_texto.listar_archivos()}")

# gestion_archivo_texto.renombrar_archivo('archivo_1.txt', 'mi_archivo.txt')
# print(f"Después de cambiar el nombre del archivo: {gestion_archivo_texto.listar_archivos()}")

# # Ejemplo para gestionadorArchivosAudio (Audio)
# gestion_archivo_audio = gestionadorArchivosAudio("C://Users/laurentine.Masson/Carpeta_audio/")
# print(f"Los archivos de audio de {gestion_archivo_audio.directorio} son: {gestion_archivo_audio.listar_archivos_audio()}")