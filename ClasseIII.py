from abc import ABC, abstractclassmethod, abstractmethod

class ClasseAbstrata(ABC):
    valor = ''
    def __init__(self,valor):
        self.valor = valor
    
    @abstractmethod
    def metodoAbstrato(self):
        pass

class A(ClasseAbstrata):
    def metodoAbstrato(self):
        print('Eu sou um metodo abstrato')

obj = A('teste')
obj.metodoAbstrato()