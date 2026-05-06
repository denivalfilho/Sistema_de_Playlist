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
        print("\nMENU PLAYLIST")
        print("1. Adicionar música")
        print("2. Remover música")
        print("3. Buscar música")
        print("4. Listar biblioteca")
        print("5. Montar filas de humor")
        print("6. Reproduzir música (Ouvir)")
        print("7. Ver Histórico")
        print("7. Exibir fila de humor")
        print("8. Ver Histórico")
        print("9. Estatísticas")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            t = input("Título: ")
            a = input("Artista: ")

            if minha_biblioteca.existe_duplicada(t, a):
                print("Essa música já existe na biblioteca.")
                continue
            
            g = input("Gênero: ")
            
            bpm_input = input("BPM: ")
            if not bpm_input.isdigit() or int(bpm_input) <= 0:
                print("Erro: O BPM deve ser um número inteiro maior que zero.")
                continue
            b = int(bpm_input)
            
            nova_m = Musica(proximo_id, t, a, g, b)
            minha_biblioteca.adicionar_musica(nova_m)
            proximo_id += 1

        elif opcao == "2":
            id_input = input("Digite o ID da música que deseja remover: ")
            if id_input.isdigit():
                id_para_remover = int(id_input)
                minha_biblioteca.remover_musica(id_para_remover)
            else:
                print("Erro: Digite um ID numérico válido.")
        
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

        elif opcao == "6":
            print("Reproduzir")
            print("Escolha o humor: 1.Relax | 2.Foco | 3.Animar | 4.Treinar")
            humor = input("Escolha: ")
            
            fila_escolhida = None
            if humor == "1":
                fila_escolhida = fila_relaxar
            elif humor == "2":
                fila_escolhida = fila_focar
            elif humor == "3":
                fila_escolhida = fila_animar
            elif humor == "4":
                fila_escolhida = fila_treinar

            if fila_escolhida is None:
                print("Opção de humor inválida.")
            elif fila_escolhida.esta_vazia():
                print("Erro: Esta fila está vazia. Lembre-se de montar as filas (Opção 5) primeiro!")
            else:
                musica_tocando = fila_escolhida.dequeue()
                print(f"Reproduzindo agora: {musica_tocando.titulo} - {musica_tocando.artista}")
                historico.enqueue(musica_tocando)

        elif opcao == "7":
            print("Escolha a fila: 1.Relax | 2.Foco | 3.Animar | 4.Treinar")
            humor = input("Escolha: ")
            if humor == "1":
                print("--- Relaxar ---")
                fila_relaxar.exibir_fila()
            elif humor == "2":
                print("--- Focar ---")
                fila_focar.exibir_fila()
            elif humor == "3":
                print("--- Animar ---")
                fila_animar.exibir_fila()
            elif humor == "4":
                print("--- Treinar ---")
                fila_treinar.exibir_fila()
            else:
                print("Opção inválida.")

        elif opcao == "8":
            print("HISTÓRICO DE REPRODUÇÃO")
            if historico.esta_vazia():
                print("Nenhuma música foi tocada ainda.")
            else:
                historico.exibir_fila()

        elif opcao == "9":
            print("ESTATÍSTICAS")
            print(f"Total de músicas na biblioteca: {minha_biblioteca.contar()}")
            print(f"Tamanho da fila Relaxar: {fila_relaxar.tamanho()}")
            print(f"Tamanho da fila Focar: {fila_focar.tamanho()}")
            print(f"Tamanho da fila Animar: {fila_animar.tamanho()}")
            print(f"Tamanho da fila Treinar: {fila_treinar.tamanho()}")
            print(f"Total de músicas reproduzidas: {historico.tamanho()}")
        
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()