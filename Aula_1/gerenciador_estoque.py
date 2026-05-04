estoque = {}
_proximo_indice = 1


def _resolver_nome(entrada):
    entrada = entrada.strip()
    if entrada.isdigit():
        indice = int(entrada)
        for nome, info in estoque.items():
            if info["indice"] == indice:
                return nome
        return None
    return entrada if entrada in estoque else None


def _listar_indices():
    if not estoque:
        print("Nenhum produto cadastrado.")
        return False
    for nome, info in sorted(estoque.items(), key=lambda item: item[1]["indice"]):
        print(f"  [{info['indice']}] {nome}")
    return True


def adicionar_produto(nome, quantidade, preco):
    global _proximo_indice
    estoque[nome] = {"indice": _proximo_indice, "quantidade": quantidade, "preco": preco}
    _proximo_indice += 1
    return f"Produto '{nome}' adicionado com sucesso!"


def listar_produtos():
    if not estoque:
        return "Nenhum produto cadastrado."
    else:
        for nome, info in sorted(estoque.items(), key=lambda item: item[1]["indice"]):
            print(f"  [{info['indice']}] {nome} - Quantidade: {info['quantidade']}, Preço: R${info['preco']:.2f}")


def remover_produto():
    print("\nProdutos disponíveis:")
    if not _listar_indices():
        return
    entrada = input("Digite o nome ou índice do produto a remover: ").strip()
    nome = _resolver_nome(entrada)
    if nome:
        del estoque[nome]
        print(f"Produto '{nome}' removido com sucesso!")
    else:
        print("Erro: Produto não encontrado.")


def atualizar_quantidade():
    print("\nProdutos disponíveis:")
    if not _listar_indices():
        return
    entrada = input("Digite o nome ou índice do produto: ").strip()
    nome = _resolver_nome(entrada)
    if nome:
        quantidade = int(input("Digite a nova quantidade: "))
        estoque[nome]["quantidade"] = quantidade
        print(f"Quantidade do produto '{nome}' atualizada para {quantidade}.")
    else:
        print("Erro: Produto não encontrado.")


def exibir_menu():
    return (
        "\nMenu:"
        "\n1 - Adicionar produto"
        "\n2 - Listar produtos"
        "\n3 - Remover produto"
        "\n4 - Atualizar quantidade"
        "\n5 - Sair"
    )


def main():
    while True:
        print(exibir_menu())
        opcao = int(input("Escolha uma opção: ").strip())

        if opcao == 1:
            nome = input("Digite o nome do produto: ").strip()
            quantidade = int(input("Digite a quantidade: "))
            preco = float(input("Digite o preço: "))
            print(adicionar_produto(nome, quantidade, preco))
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            remover_produto()
        elif opcao == 4:
            atualizar_quantidade()
        elif opcao == 5:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()