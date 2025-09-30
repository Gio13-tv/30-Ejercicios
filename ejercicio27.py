## Ejercicio 27: Creación de un generador de contraseñas

## Importación de módulo
import string
import random
import os

class GeneradorContrasena:
    def _init_(self, longitud: int, caracteres_especiales: bool = True, numeros: bool = True, mayusculas: bool = True, minusculas: bool = True):
        """
        Constructor para inicializar los atributos de la clase
        """
        self.longitud = longitud
        self.caracteres_especiales = caracteres_especiales
        self.numeros = numeros
        self.mayusculas = mayusculas
        self.minusculas = minusculas

    # --- Métodos para modificar parámetros ---
    
    def incluir_mayusculas(self, mayusculas: bool):
        """
        Este método permite modificar el estado del parámetro "mayúsculas".
        """
        self.mayusculas = mayusculas
        
    def incluir_minusculas(self, minusculas: bool):
        """
        Este método permite modificar el estado del parámetro "minúsculas".
        """
        self.minusculas = minusculas

    def incluir_numeros(self, numeros: bool):
        """
        Este método permite modificar el estado del parámetro "numeros".
        """
        self.numeros = numeros

    def incluir_caracteres_especiales(self, caracteres_especiales: bool):
        """
        Este método permite modificar el estado del parámetro "caracteres_especiales".
        """
        self.caracteres_especiales = caracteres_especiales
    
    def modificar_longitud(self, longitud: int):
        """
        Este método permite modificar la longitud de la contraseña generada
        """
        self.longitud = longitud

    # --- Método de Generación y Evaluación ---

    def generar_contrasena(self):
        """
        Este método permite generar una contraseña tomando en cuenta
        los valores de los atributos de la clase.
        """
        ## inicialización de una variable vacía
        ## que contendrá nuestra contraseña.
        contrasena = ""
        caracteres_concat = ""
        
        ## si nuestra contraseña puede incluir caracteres especiales
        if self.caracteres_especiales:
            ## almacenar los caracteres especiales en una variable
            carac_esp_str = "!@#$%^&*()"
        ## en caso contrario
        else:
            ## dejar la variable vacía
            carac_esp_str = ""

        ## si nuestra contraseña puede incluir números
        if self.numeros:
            ## almacenar todos los números en una variable
            numeros_str = string.digits
        ## en caso contrario
        else:
            ## dejar la variable vacía
            numeros_str = ""
            
        # si nuestra contraseña puede incluir mayúsculas
        # pero no minúsculas
        if self.mayusculas and not self.minusculas:
            # entonces almacenamos las letras mayúsculas en una variable
            letras_str = string.ascii_uppercase
        # si nuestra contraseña debe incluir minúsculas pero no
        # mayúsculas
        elif self.minusculas and not self.mayusculas:
            # entonces almacenamos las letras minúsculas en una variable
            letras_str = string.ascii_lowercase
        # si nuestra contraseña debe incluir tanto mayúsculas como minúsculas
        elif self.minusculas and self.mayusculas:
            # almacenar tanto letras mayúsculas como minúsculas
            letras_str = string.ascii_letters
        else:
            # dejar la variable vacía
            letras_str = ""

        ## concatenación de todos los caracteres que se usarán para
        ## generar nuestra contraseña
        caracteres_concat = carac_esp_str + numeros_str + letras_str
        
        # verificar que haya caracteres para generar la contraseña
        if not caracteres_concat:
            return "Error: No se seleccionó ningún tipo de carácter."

        ## iterar tantas veces como la longitud de la contraseña
        for i in range(self.longitud):
            ## elegir un carácter de la cadena y añadirlo a
            ## la variable que contendrá nuestra contraseña
            contrasena += random.choice(caracteres_concat)

        return contrasena

    def evaluar_contrasena(self, contrasena: str):
        """
        Este método permite evaluar la robustez de una contraseña.
        """
        # Inicializar la variable que contendrá el grado
        # de robustez de la contraseña.
        robustez = 0
        
        # si la longitud de la contraseña es mayor o igual a 10
        if len(contrasena) >= 10:
            # añadir 1 punto a la robustez
            robustez += 1
        
        # si la contraseña contiene al menos una letra minúscula
        if any(char.islower() for char in contrasena):
            # añadir 1 punto a la robustez
            robustez += 1
            
        # si la contraseña contiene al menos una letra mayúscula
        if any(char.isupper() for char in contrasena):
            # añadir 1 punto a la robustez
            robustez += 1

        # si la contraseña contiene al menos un número
        if any(char.isdigit() for char in contrasena):
            # añadir 1 punto a la robustez
            robustez += 1

        # si la contraseña contiene al menos un carácter especial
        caracteres_especiales = "!@#$%^&*()"
        if any(char in caracteres_especiales for char in contrasena):
            # añadir 1 punto a la robustez
            robustez += 1

        # evaluación de la robustez
        if robustez == 5:
            return "Contraseña muy fuerte"
        elif robustez == 4:
            return "Contraseña fuerte"
        elif robustez == 3:
            return "Contraseña media"
        else:
            return "Contraseña débil"

    # --- Métodos de Gestión de Archivos ---

    def guardar_contrasena(self, contrasena: str, ruta_archivo: str):
        """
        Este método permite guardar una contraseña en un archivo.
        """
        # abrir el archivo en modo de escritura
        try:
            with open(ruta_archivo, "w") as f:
                # escribir la contraseña en el archivo
                f.write(contrasena)
            return "Guardado de la contraseña -- Ok"
        except IOError as e:
            return f"Error al guardar: {e}"

    def leer_contrasena(self, ruta_archivo: str):
        """
        Este método permite leer la contraseña guardada en el archivo.
        """
        # abrir un archivo en modo lectura.
        try:
            with open(ruta_archivo, "r") as f:
                # almacenar el contenido del archivo en una variable
                contrasena = f.read()
            return contrasena
        except FileNotFoundError:
            return "Error: Archivo no encontrado."
        except IOError as e:
            return f"Error al leer: {e}"

## Ejemplos de pruebas / casos de uso

# Creación de una instancia de contraseña.
# La longitud de la contraseña de la instancia es de 12,
# y todos los demás parámetros son por defecto = True.
generador_contrasena = GeneradorContrasena(12)

# --- Primer Contraseña (con todo activado) ---
print("--- Test 1: Contraseña por defecto (12 caracteres, todo incluido) ---")
contrasena_1 = generador_contrasena.generar_contrasena()
print(contrasena_1)
print("Robustez de la contraseña 1:", generador_contrasena.evaluar_contrasena(contrasena_1))
print("-" * 20)

# --- Segunda Contraseña (sin caracteres especiales) ---
print("--- Test 2: Contraseña sin caracteres especiales ---")
generador_contrasena.incluir_caracteres_especiales(False)
contrasena_2 = generador_contrasena.generar_contrasena()
print(contrasena_2)
print("Robustez de la contraseña 2:", generador_contrasena.evaluar_contrasena(contrasena_2))
print("-" * 20)

# --- Tercer Contraseña (solo números) ---
print("--- Test 3: Contraseña solo con números (débil) ---")
generador_contrasena.incluir_caracteres_especiales(True)
generador_contrasena.incluir_mayusculas(False)
generador_contrasena.incluir_minusculas(False)
generador_contrasena.incluir_numeros(True) # Se queda solo con números y caracteres especiales
contrasena_3 = generador_contrasena.generar_contrasena()
print(contrasena_3)
print("Robustez de la contraseña 3:", generador_contrasena.evaluar_contrasena(contrasena_3))
print("-" * 30)

# --- Gestión de Archivos ---
# NOTA: La ruta debe ser válida en tu sistema. Usamos una ruta simple por defecto
# en lugar de la ruta de usuario codificada de la imagen.
ruta_ejemplo = os.path.join(os.getcwd(), 'contrasena_guardada.txt')

print("Guardando la contraseña en curso...")
resultado_guardar = generador_contrasena.guardar_contrasena(contrasena_1, ruta_ejemplo)
print(resultado_guardar)

print("Leyendo la contraseña guardada:")
contrasena_leida = generador_contrasena.leer_contrasena(ruta_ejemplo)
print(contrasena_leida)