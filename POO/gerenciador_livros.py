print ("Bem-vindo ao Gerenciador de Livros!")


livros = []
historico_emprestimos = []

while True:
    print ("Escolha uma opção:")
    print ("1 - Adicionar um livro")
    print ("2 - Listar livros")
    print ("3 - Remover um livro")
    print ("4 - Atualizar quantidade de um livro")
    print ("5 - Registrar empréstimo de um livro")
    print ("6 - Exibir histórico de empréstimos")
    print ("0 - Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        try:
            quantidade = int(input("Digite a quantidade disponível: "))
        except ValueError:
            print("Por favor, insira um número válido para a quantidade.")
            continue
        if quantidade < 0:
            print("Quantidade não pode ser negativa. Livro não adicionado.")
            continue
        livro = {"titulo": titulo, "autor": autor, "quantidade": quantidade}
        if any(l['titulo'].lower() == titulo.lower() and l['autor'].lower() == autor.lower() for l in livros):
            print("Este livro já está cadastrado. Livro não adicionado.")
            continue
        livros.append(livro)
        print("Livro adicionado com sucesso!")

    elif opcao == "2":
        if not livros:
            print("Nenhum livro cadastrado.")
        else:
            for idx, livro in enumerate(livros):
                print(f"{idx + 1} - {livro['titulo']} por {livro['autor']} (Quantidade: {livro['quantidade']})")

    elif opcao == "3":
        try:
            indice = int(input("Digite o número do livro a ser removido: ")) - 1
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
        if 0 <= indice < len(livros):
            removed_book = livros.pop(indice)
            print(f"Livro '{removed_book['titulo']}' removido com sucesso!")
        else:
            print("Número inválido.")

    elif opcao == "4":
        try:
            indice = int(input("Digite o número do livro para atualizar a quantidade: ")) - 1
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
        if 0 <= indice < len(livros):
            try:
                nova_quantidade = int(input("Digite a nova quantidade disponível: "))
            except ValueError:
                print("Por favor, insira um número válido para a quantidade.")
                continue
            if nova_quantidade < 0:
                print("Quantidade não pode ser negativa. Atualização cancelada.")
                continue
            livros[indice]['quantidade'] = nova_quantidade
            print(f"Quantidade do livro '{livros[indice]['titulo']}' atualizada para {nova_quantidade}.")
        else:
            print("Número inválido.")

    elif opcao == "5":
        try:
            indice = int(input("Digite o número do livro para registrar o empréstimo: ")) - 1
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
        if 0 <= indice < len(livros):
            if livros[indice]['quantidade'] > 0:
                nome_usuario = input("Digite o nome do usuário que está emprestando o livro: ")
                try:
                    quantidade_livros = int(input("Digite a quantidade de livros a emprestar: "))
                except ValueError:
                    print("Por favor, insira um número válido para a quantidade.")
                    continue
                if quantidade_livros <= 0:
                    print("Quantidade deve ser maior que zero. Empréstimo cancelado.")
                    continue
                if quantidade_livros > livros[indice]['quantidade']:
                    print(f"Desculpe, apenas {livros[indice]['quantidade']} cópias disponíveis. Empréstimo cancelado.")
                    continue

                livros[indice]['quantidade'] -= quantidade_livros
                historico_emprestimos.append({
                    "titulo": livros[indice]['titulo'],
                    "autor": livros[indice]['autor'],
                    "usuario": nome_usuario,
                    "quantidade": quantidade_livros
                })
                print(f"Empréstimo registrado para '{livros[indice]['titulo']}' por {nome_usuario}.")
            else:
                print("Desculpe, este livro não está disponível no momento.")
        else:
            print("Número inválido.")
    elif opcao == "6":
        if not historico_emprestimos:
            print("Nenhum empréstimo registrado.")
        else:
            for idx, emprestimo in enumerate(historico_emprestimos):
                print(
                    f"{idx + 1} - Título: '{emprestimo['titulo']}' | "
                    f"Autor: {emprestimo['autor']} | "
                    f"Usuário: {emprestimo['usuario']} | "
                    f"Quantidade: {emprestimo['quantidade']}"
                )
    elif opcao == "0":
        print("Saindo do Gerenciador de Livros. Até mais!")
        break