class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade=27):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    Anderson = Pessoa(nome='Anderson')
    Elias = Pessoa(Anderson, nome='Elias')
    print(Pessoa.cumprimentar(Elias))
    print(id(Elias))
    print(Elias.cumprimentar())
    print(Elias.nome)
    print(Elias.idade)
    for filho in Elias.filhos:
        print(filho.nome)
    Elias.sobrenome = 'Silva'
    del Elias.filhos
    print(Elias.__dict__)
    print(Anderson.__dict__)
