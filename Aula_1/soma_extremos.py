lista = map(int, input("Digite os números separados por espaço: ").split())

lista_ordenada = sorted(lista)
soma_extremos = lista_ordenada[0] + lista_ordenada[-1]
print("Soma dos extremos:", soma_extremos)