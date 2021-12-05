import random


class Humano():
    _nome = 'Nome do Humano' 
    idade = 0

    @property
    def Nome(cls):
        return cls._nome

    def defineNome(self, nome):
        self.nome = nome
    
    @classmethod
    def obtemNome(cls):
        return cls.nome
    
    @classmethod
    def alteraNome(cls,nome):
        cls.nome = nome

    @staticmethod
    def defineId():
        r = random.randint(10,50)
        return r

print(Humano.defineId())
h = Humano()
print(h.defineId())