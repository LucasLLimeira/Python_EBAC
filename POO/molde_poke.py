class pokemon:
    def __init__(self, nome, tipo, hp, ataque, altura, peso, nivel):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.ataque = ataque
        self.altura = altura
        self.peso = peso
        self.nivel = nivel
    
    def mostrar_nome(self):
        print(f"O nome do pokemon é: {self.nome}")

    def mostrar_status(self):
        print(f"Tipo: {self.tipo}")
        print(f"HP: {self.hp}")
        print(f"Ataque: {self.ataque}")
        print(f"Altura: {self.altura} cm")
        print(f"Peso: {self.peso} kg")
        print(f"Nível: {self.nivel}")

Pikachu = pokemon("Pikachu", "Elétrico", 100, "Choque do trovão", 0.4, 6.0, 5)

Charmander = pokemon("Charmander", "Fogo", 80, "Lança-chamas", 0.6, 8.5, 5)

Pikachu.mostrar_nome()
Charmander.mostrar_nome()
