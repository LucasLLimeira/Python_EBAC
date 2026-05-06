while True:

    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

    print("Escolha a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
    while opcao < 1 or opcao > 4:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    operacoes = {
        1: ("adição", lambda x, y: x + y),
        2: ("subtração", lambda x, y: x - y),
        3: ("multiplicação", lambda x, y: x * y),
        4: ("divisão", lambda x, y: x / y)
    }

    if opcao == 4 and numero2 == 0:
        while numero2 == 0:
            print("Erro: Divisão por zero não é permitida. Por favor, digite um número diferente de zero.")
            try:
                numero2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")
    operacao_nome, operacao_funcao = operacoes[opcao]
    resultado = operacao_funcao(numero1, numero2)

    print(f"O resultado da {operacao_nome} é: {resultado}")

    print("Deseja realizar outra operação? (s/n)")
    resposta = input().lower()
    if resposta != 's':
        print("Encerrando a calculadora. Até mais!")
        break
    else:
        print("Reiniciando a calculadora...")

