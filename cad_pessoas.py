import os

opcao = 0

while opcao != 3:

    print("------ MENU -----")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")

    opcao = int(input("Escolha a opção: "))

    if opcao == 1:

        nome = input("Digite seu nome: ")
        telefone = input("Digite seu telefone: ")
        email = input("Digite seu E-mail: ")

        arquivo = open("cad_pessoas.txt", "a", encoding="utf-8")
        arquivo.write(f"{nome},{telefone},{email}\n")
        arquivo.close()

        print("\nUsuário cadastrado com sucesso!")

        input("\nPressione ENTER para continuar...")
        os.system("cls")

    elif opcao == 2:

        print("\n--- LISTA DE PESSOAS ---\n")

        try:
            arquivo = open("cad_pessoas.txt", "r", encoding="utf-8")

            for linha in arquivo:
                nome, telefone, email = linha.strip().split(",")

                print(f"Nome: {nome}")
                print(f"Telefone: {telefone}")
                print(f"E-mail: {email}")
                print("-" * 30)

            arquivo.close()

        except FileNotFoundError:
            print("Nenhum cadastro encontrado.")

        input("\nPressione ENTER para continuar...")
        os.system("cls")

    elif opcao == 3:

        print("Programa encerrado.")

    else:

        print("Opção inválida!")    
 