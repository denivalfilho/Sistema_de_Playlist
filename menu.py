from sistema_playlist import Biblioteca, Musica

def menu():
    minha_biblioteca = Biblioteca()
    proximo_id = 1

    while True:
        print("MENU PLAYLIST")
        print("1. Adicionar música")
        print("3. Buscar música")
        print("4. Listar biblioteca")
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

        elif opcao == "3":
                    termo = input("Digite o ID ou o Título da música: ")
                    encontrada = minha_biblioteca.buscar_musica(termo)
                    if encontrada:
                        print(f"Sucesso! Música encontrada:{encontrada}")
                    else:
                        print("Erro: Música não encontrada.")

        elif opcao == "4":
            minha_biblioteca.listar_musicas()

        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()