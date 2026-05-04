# Variável global de tarefas
tarefas = {}

def adicionar_tarefa(nome):
    nome = nome.strip()
    if nome in tarefas:
        return "Essa tarefa já existe."
    else:
        tarefas[nome] = False
        return f"Tarefa '{nome}' adicionada com sucesso!!"

def listar_tarefas(tarefas):
    if not tarefas:
        return "Nenhuma tarefa cadastrada."
    else:
        resultado = ["Tarefas:"]
        for nome, concluida in sorted(tarefas.items(), key=lambda item: item[0]):
            status = "✅ Concluída" if concluida else "❌ Não concluída"
            resultado.append(f"{nome}: {status}")
        return "\n".join(resultado)

def remover_tarefa(nome):
    nome = nome.strip()
    if nome in tarefas:
        del tarefas[nome]
        return f"Tarefa '{nome}' removida com sucesso!"
    else:
        return "Erro: Tarefa não encontrada."

def marcar_concluida(nome):
    nome = nome.strip()
    if nome in tarefas:
        tarefas[nome] = True
        return f"Tarefa '{nome}' marcada como concluída!"
    else:
        return "Erro: Tarefa não encontrada."

def exibir_menu():
    return (
        "\nMenu:"
        "\n1 - Adicionar tarefa"
        "\n2 - Listar tarefas"
        "\n3 - Remover tarefa"
        "\n4 - Marcar tarefa como concluída"
        "\n5 - Sair"
    )

def main():
    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Digite o nome da tarefa: ")
            print(adicionar_tarefa(nome))
        elif opcao == "2":
            print(listar_tarefas(tarefas))
        elif opcao == "3":
            nome = input("Digite o nome da tarefa a remover: ")
            print(remover_tarefa(nome))
        elif opcao == "4":
            nome = input("Digite o nome da tarefa a marcar como concluída: ")
            print(marcar_concluida(nome))
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()