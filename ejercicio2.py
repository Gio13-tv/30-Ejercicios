class Libro:
    def _init_(self, titulo, autor, precio):
        self.titulo=titulo
        self.autor=autor
        self.precio=precio
    
    def libreria(self):
        print("Este libro es", self.titulo, "y su autor es", self.autor, "tiene un precio de", self.precio )
        print("Espero que te guste :)")
        
libro_1=Libro("Noches Blancas", "Fiodor Dostoievski", "$210")
libro_1.libreria()