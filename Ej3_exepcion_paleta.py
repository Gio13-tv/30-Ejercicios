# Custom exceptions
class InvalidPriceError(Exception):
    """Exception raised for invalid price values"""
    pass

class InvalidFlavorError(Exception):
    """Exception raised for invalid or empty flavor values"""
    pass

class Paleta:
    def __init__(self, sabor, precio):
        # Validate flavor is not empty
        if not sabor or not isinstance(sabor, str) or sabor.strip() == "":
            raise InvalidFlavorError("Flavor cannot be empty or non-string")
        
        # Validate price is positive
        if precio <= 0:
            raise InvalidPriceError(f"Price must be greater than 0. Received: {precio}")
        
        self.sabor = sabor.strip()
        self.precio = precio

    def mostrarInformacion(self):
        print(f"Ice pop flavor {self.sabor}, price: ${self.precio}")


class PaletaAgua(Paleta):
    def __init__(self, sabor, precio, baseAgua):
        super().__init__(sabor, precio)
        self.baseAgua = baseAgua

    def mostrarBaseAgua(self):
        print(f"Is it water-based?: {'Yes' if self.baseAgua else 'No'}")


class PaletaCrema(Paleta):
    def __init__(self, sabor, precio, cremosa):
        super().__init__(sabor, precio)
        self.cremosa = cremosa

    def mostrarTexturaCremosa(self):
        print(f"Is it creamy?: {'Yes' if self.cremosa else 'No'}")


# Test the implementation with exceptions
try:
    print("Testing valid ice pops:")
    paletas = [
        PaletaAgua("Mango", 15, True),
        PaletaCrema("Strawberries with cream", 20, True)
    ]

    for p in paletas:
        p.mostrarInformacion()
        if isinstance(p, PaletaAgua):
            p.mostrarBaseAgua()
        elif isinstance(p, PaletaCrema):
            p.mostrarTexturaCremosa()
        print()

    # Test invalid price
    print("Testing invalid price:")
    invalid_price_paleta = Paleta("Chocolate", 0)  # This will raise an exception

except InvalidPriceError as e:
    print(f"Error creating ice pop: {e}")

try:
    # Test invalid flavor
    print("\nTesting invalid flavor:")
    invalid_flavor_paleta = Paleta("", 10)  # This will raise an exception

except InvalidFlavorError as e:
    print(f"Error creating ice pop: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")