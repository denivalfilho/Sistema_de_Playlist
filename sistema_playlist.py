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

class Biblioteca:
    def __init__(self):
        self.inicio = None

    def adicionar_musica(self, musica):
        novo_nodo = NodoLista(musica)
        
        if self.inicio is None:
            self.inicio = novo_nodo
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo
        print(f"Música '{musica.titulo}' adicionada com sucesso!")

    def listar_musicas(self):
            if self.inicio is None:
                print("A biblioteca está vazia.")
                return

            print("Biblioteca Completa")
            atual = self.inicio
            while atual is not None:
                print(atual.musica)
                atual = atual.proximo

biblioteca = Biblioteca()
biblioteca.adicionar_musica(Musica(1, "Imagine", "John Lennon", "Rock", 75))
biblioteca.adicionar_musica(Musica(2, "Stayin' Alive", "Bee Gees", "Disco", 103))
biblioteca.adicionar_musica(Musica(3, "Thunderstruck", "AC/DC", "Rock", 133))

biblioteca.listar_musicas()