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


m1 = Musica(1, "Música A", "Artista A", "Pop", 100)
m2 = Musica(2, "Música B", "Artista B", "Rock", 140)

no1 = NodoLista(m1)
no2 = NodoLista(m2)

no1.proximo = no2

print(f"O primeiro nó tem a música: {no1.musica.titulo}")
print(f"O próximo nó depois do primeiro tem a música: {no1.proximo.musica.titulo}")