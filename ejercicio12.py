class Video:
    def _init_(self, titulo, categoria, duracion):
        self.titulo = titulo  # Título del video
        self.duracion = duracion  # duración en minutos
        self.categoria = categoria  # categoría del video
        
    def mirar_video(self):
        print("Iniciando el video...")
        print(f"El video que estás viendo se titula '{self.titulo}' " +
              f"de la categoría '{self.categoria}' con una duración de {self.duracion} minutos.")
              
    def detener_video(self):
        print("Deteniendo el video.")

class Audio:
    def _init_(self, nombre_artista, titulo):
        self.titulo = titulo  # Titulo del audio
        self.nombre_artista = nombre_artista  # Nombre del artista
        
    def escuchar_audio(self):
        print("Iniciando el audio...")
        print(f"El audio que estás escuchando es '{self.titulo}' producido " +
              f"por el artista '{self.nombre_artista}'")
              
    def detener_audio(self):
        print("Deteniendo la reproducción del audio.")

class Media(Video, Audio):
    def _init_(self, titulo, categoria, duracion, nombre_artista):
        Video._init_(self, titulo, categoria, duracion)
        Audio._init_(self, nombre_artista, titulo)

medio_1 = Media("Titulo 1", "infantil", 180, "Artista 1")

medio_1.escuchar_audio()
medio_1.mirar_video()
medio_1.detener_audio()
medio_1.detener_video()