class Conta():

    saldo = 0
    numero = ''



    def __init__(self,numero):
        if ( len(str(numero)) != 5):
            print('Tamanho exigido para o número da conta é 5 caracteres. \n'+
            'Tamanho passado: '+ str(len(str(numero))))
            return
        self.numero = numero

    def sacar(self, valor):
        if ( valor > self.saldo):
            return 'Saldo insuficiente'
        if (self.__class__.__name__ == 'Corrente'):
          self.saldo -= valor + 10
        else:
            self.saldo -= valor
        return 'Saque efetuado com sucesso'
   
    def depositar(self, valor):
        self.saldo =+ valor
        return 'Depósito efetuado com sucesso'

    def verSaldo(self):
        return f'Saldo Atual: {self.saldo}'

class Corrente(Conta):
    def metodoCorrente(self):
        print(f'método usado na class {__class__.__name__}')

class Poupanca(Conta):
     pass
    
