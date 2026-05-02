from sistema_playlist import Biblioteca, Musica, Fila

def menu():
    minha_biblioteca = Biblioteca()
    proximo_id = 1

    fila_relaxar = Fila()
    fila_focar = Fila()
    fila_animar = Fila()
    fila_treinar = Fila()
    historico = Fila()

    while True:
        print("MENU PLAYLIST")
        print("1. Adicionar música")
        print("2. Remover música")
        print("3. Buscar música")
        print("4. Listar biblioteca")
        print("5. Montar filas de humor")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            t = input("Título: ")
            a = input("Artista: ")
            g = input("Gênero: ")
            b = int(input("BPM: "))
            
            nova_m = Musica(proximo_id, t, a, g, b)
            minha_biblioteca.adicionar_musica(nova_m)
            proximo_id += 1

        elif opcao == "2":
            id_para_remover = int(input("Digite o ID da música que deseja remover: "))
            minha_biblioteca.remover_musica(id_para_remover)
        
        elif opcao == "3":
                    termo = input("Digite o ID ou o Título da música: ")
                    encontrada = minha_biblioteca.buscar_musica(termo)
                    if encontrada:
                        print(f"Sucesso! Música encontrada:{encontrada}")
                    else:
                        print("Erro: Música não encontrada.")

        elif opcao == "4":
            minha_biblioteca.listar_musicas()

        elif opcao == "5":
            fila_relaxar = Fila()
            fila_focar = Fila()
            fila_animar = Fila()
            fila_treinar = Fila()

            atual = minha_biblioteca.inicio
            if atual is None:
                print("Biblioteca vazia.")
            else:
                while atual is not None:
                    m = atual.musica
                    if m.bpm <= 80:
                        fila_relaxar.enqueue(m)
                    elif 81 <= m.bpm <= 120:
                        fila_focar.enqueue(m)
                    elif 121 <= m.bpm <= 160:
                        fila_animar.enqueue(m)
                    else:
                        fila_treinar.enqueue(m)
                    
                    atual = atual.proximo
                
                print("Filas montadas com sucesso!")
                print("--- Relaxar ---")
                fila_relaxar.exibir_fila()
                print("--- Focar ---")
                fila_focar.exibir_fila()
                print("--- Animar ---")
                fila_animar.exibir_fila()
                print("--- Treinar ---")
                fila_treinar.exibir_fila()

        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()