print("Calculadora")
print("Escolha a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite a opção desejada: "))

if opcao < 1 or opcao > 4:
    print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
    exit()

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == 1:
    resultado = num1 + num2
    print(f"O resultado da adição é: {resultado}")
elif opcao == 2:
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif opcao == 3:
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif opcao == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")

