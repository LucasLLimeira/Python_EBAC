class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("O animal emitiu um som genérico.")

class Cachorro(Animal):
    
    def emitir_som(self):
        print("O cachorro latiu!")

class Gato(Animal):
    
    def emitir_som(self):
        print("O gato miou!")
    
Dobby = Cachorro("Dobby", 3)
Mia = Gato("Mia", 2)

Dobby.emitir_som()
Mia.emitir_som()