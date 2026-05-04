lista = map(int, input("Digite os números separados por espaço: ").split())

dicionario = {}

for numero in lista:
    if numero in dicionario:
        dicionario[numero] += 1
    else:
        dicionario[numero] = 1

unicos = [numero for numero, contagem in dicionario.items() if contagem == 1]

print("Números únicos:", unicos)