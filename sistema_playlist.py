class Musica:
    def __init__(self, id, titulo, artista, genero, bpm):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def __str__(self):
        return f"[{self.id}] {self.titulo} - {self.artista} ({self.genero}) BPM: {self.bpm}"

class NodoLista:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


minha_musica = Musica(1, "Imagine", "John Lennon", "Rock", 75)
print(minha_musica)