usuarios = {} 
proximo_id = 1

def criar_usuario():
    global proximo_id
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    usuarios[proximo_id] = {"Nome": nome, "Email": email}
    print(f"Usuário {nome} cadastrado com sucesso! ID: {proximo_id}")
    proximo_id += 1 

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("\nLista de Usuários:")
        for id, dados in usuarios.items():
            print(f"ID: {id}, Nome: {dados['Nome']}, Email: {dados['Email']}")

def atualizar_usuario():
    id = int(input("Digite o ID do usuário a ser atualizado: "))
    if id in usuarios:
        nome = input("Digite o novo nome: ")
        email = input("Digite o novo email: ")
        if nome:
            usuarios[id]["Nome"] = nome
        if email:
            usuarios[id]["Email"] = email
        print(f"Usuário {id} atualizado com sucesso!")
    else:
        print("Erro: Usuário não encontrado.")

def deletar_usuario():
    id = int(input("Digite o ID do usuário a ser removido: "))
    if id in usuarios:
        del usuarios[id]
        print(f"Usuário {id} removido com sucesso!")
    else:
        print("Erro: Usuário não encontrado.")

def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Criar Usuário")
        print("2 - Listar Usuários")
        print("3 - Atualizar Usuário")
        print("4 - Deletar Usuário")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            atualizar_usuario()
        elif opcao == "4":
            deletar_usuario()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()
