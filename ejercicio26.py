## Ejercicio 26:

class CarritoCompra:
    def _init_(self):
        """
        Constructor para inicializar los atributos de la clase.
        Parámetros:
        articulos_precio_total ::: dict: permite almacenar el artículo con su precio total
        articulos_cantidad ::: dict: permite almacenar el artículo con la cantidad elegida
        articulos_precio_u ::: dict: permite almacenar el artículo con su precio unitario
        """
        self.articulos_precio_total = {}
        self.articulos_cantidad = {}
        self.articulos_precio_u = {}

    def agregar_articulo(self, articulo: str, precio_u: float, cantidad: int):
        """
        Método que permite añadir un artículo al carrito.
        """
        
        # Si el artículo ya está en el carrito, actualiza la cantidad y el precio total
        if articulo in self.articulos_precio_total:
            self.articulos_precio_total[articulo] += round(precio_u * cantidad, 2)
            self.articulos_cantidad[articulo] += cantidad
        # Si el artículo es nuevo, lo agrega
        else:
            self.articulos_precio_total[articulo] = round(precio_u * cantidad, 2)
            self.articulos_cantidad[articulo] = cantidad
            self.articulos_precio_u[articulo] = precio_u

    def eliminar_articulo(self, articulo: str, cantidad: int):
        """
        Método que permite quitar una cantidad dada de un artículo del carrito
        """
        if articulo in self.articulos_precio_total:
            # 1. Reducir el precio total
            self.articulos_precio_total[articulo] -= round(self.articulos_precio_u[articulo] * cantidad, 2)
            # 2. Reducir la cantidad
            self.articulos_cantidad[articulo] -= cantidad
            
            # 3. Si el precio total o la cantidad se vuelven no positivos, eliminar el artículo del carrito
            if self.articulos_precio_total[articulo] <= 0 or self.articulos_cantidad[articulo] <= 0:
                del self.articulos_precio_total[articulo]
                del self.articulos_cantidad[articulo]
                del self.articulos_precio_u[articulo]

    def precio_total(self):
        """
        Método que permite conocer el precio total del carrito.
        """
        return sum(self.articulos_precio_total.values())

    def listar_articulos(self):
        """
        Método que permite listar los artículos del carrito.
        """
        return list(self.articulos_precio_total.keys())
    
    def costo_total_articulo(self, articulo: str):
        """
        Método que permite conocer el precio total de un artículo
        en el carrito
        """
        return self.articulos_precio_total[articulo]

    def obtener_cantidad(self, articulo: str):
        """
        Método para conocer la cantidad de un artículo en el carrito
        """
        return self.articulos_cantidad[articulo]

    def contar_articulos_distintos(self):
        """
        Método para conocer la cantidad de artículos distintos
        existentes en el carrito
        """
        return len(self.articulos_precio_total)

    def _str_(self):
        """
        Método especial que permite personalizar la representación
        de un objeto de la clase
        """
        articulos_lista = self.listar_articulos()
        costo_total = self.precio_total()
        
        return (f"Los artículos contenidos en el carrito son: {articulos_lista} \n"
                f"El costo actual del carrito es: {costo_total} euros.")

## Ejemplos de pruebas / casos de uso
## Creación de una Instancia
carrito_1 = CarritoCompra()

## Añadido de artículos
carrito_1.agregar_articulo("zumo de naranja", 2, 4)
carrito_1.agregar_articulo("pan", 1.2, 3)

## Llamada de métodos
print(f"La cantidad de zumo de naranja seleccionada es: {carrito_1.obtener_cantidad('zumo de naranja')}")
print(f"El costo total del 'pan' es: {round(carrito_1.costo_total_articulo('pan'), 2)}")

print("-" * 20)
print("El estado actual del carrito:")
print(carrito_1)

print("-" * 20)
carrito_1.eliminar_articulo("pan", 2)
print("El costo total del artículo 'pan' después de haber quitado 2 unidades del carrito es:")
print(round(carrito_1.costo_total_articulo('pan'), 2))

print("-" * 20)
print("El estado actual del carrito:")
print(carrito_1)

print("-" * 20)
print(f"El número de artículos distintos comprados es: {carrito_1.contar_articulos_distintos()}")

# Imprime los artículos restantes y el precio total
print(f"Artículos y el precio total correspondiente en el carrito: {carrito_1.articulos_precio_total}")