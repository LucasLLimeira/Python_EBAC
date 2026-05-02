num1, num2, num3 = map(int, input("Digite três números separados por espaço: ").split())

minha_lista = []

minha_lista.append(num1)
minha_lista.append(num2)
minha_lista.append(num3)
minha_lista.sort()
print(f"A mediana é: {minha_lista[1]}")