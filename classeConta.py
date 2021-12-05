# Implementar os métodos que serão abstratos na classe Conta.
from abc import ABC, abstractmethod

class Conta(ABC):
    saldo = 0
    numero = ''

    def __init__(self,numero):
        if ( len(str(numero)) != 5):
            print(f'Tamanho exigido para o número da conta é 5 caracretes. \n Tamanho passado: {numero}')
            print(self.__class__.__name__)
            return
        if ( self.__class__.__name__ == 'Salario' ):
            self.saldo = 1000
        self.numero = numero
    
    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        if ( self.__class__.__name__ != 'Salario' ):
            self.saldo += valor
            return 'Depósito efetuado com sucesso.'
        return 'Não é possível efetuar depósito através desta conta.'

    @abstractmethod
    def verSaldo(self):
        pass
    
    def transferir(self,destino,valor):
        if ( len(str(destino)) != 5):
            return 'A conta destino deverá ter 5 caracteres!'
        if ( str(destino) == str(self.numero) ):
            return 'A conta destino deve ser diferente da conta atual.'
        if ( self.__class__.__name__ != 'Salario' ):
            if ( valor > self.saldo ):
                return 'Saldo insuficiente!'
        if ( self.__class__.__name__ == 'Salario' ):
            return 'Não é possível transferir via conta salário.'
        self.saldo -= valor
        return 'Transferência efetuada com sucesso.'

class Corrente(Conta):    
    def metodoCorrente(self):
        print(f'método usado na classe {__class__.__name__}')
    
    def verSaldo(self):
        return f'Saldo atual: Conta {self.__class__.__name__} : {self.saldo}'
    
    def sacar(self, valor):
        if ( valor > self.saldo ):
            return 'Saldo insuficiente!'
        self.saldo -= valor + 10
        return 'Saque efetuado com sucesso.'

class Poupanca(Conta):
    def verSaldo(self):
        return f'Saldo atual: Conta {self.__class__.__name__} : {self.saldo}'
    
    def sacar(self, valor):
        if ( valor > self.saldo ):
            return 'Saldo insuficiente!'
        self.saldo -= valor
        return 'Saque efetuado com sucesso.'

class Salario(Conta):
    def verSaldo(self):
        return f'Saldo atual: Conta {self.__class__.__name__} : {self.saldo}'
    
    def sacar(self, valor):
        if ( valor > self.saldo ):
            return 'Saldo insuficiente!'
        self.saldo -= valor
        return 'Saque efetuado com sucesso.'