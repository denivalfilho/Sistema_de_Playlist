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

    def buscar_por_id(self, id_procurado):
        atual = self.inicio
        
        while atual is not None:
            if atual.musica.id == id_procurado:
                print(f"Música encontrada: {atual.musica}")
                return atual.musica
            atual = atual.proximo
        
        print(f"Música com ID {id_procurado} não encontrada.")
        return None
    
    def buscar_musica(self, termo):
        atual = self.inicio
        
        while atual is not None:
            if str(atual.musica.id) == str(termo) or atual.musica.titulo.lower() == str(termo).lower():
                return atual.musica
            atual = atual.proximo
            
        return None

    def remover_musica(self, id_alvo):
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.musica.id == id_alvo:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                
                print(f"Música '{atual.musica.titulo}' removida com sucesso!")
                return True
            
            anterior = atual
            atual = atual.proximo

        print("Erro: ID não encontrado.")
        return False