# Classe Veículo
class Veiculo():
    # Atributos da classe
    marca = ''
    modelo = ''
    ano = 0
    cor = ''
    ligado = False
    marcha = 0
    velocidade = 0

    # Método construtor
    def __init__(self,marca, pModelo, pAno, pCor, pMarcha = 0):
        self.marca = marca
        self.modelo = pModelo
        self.ano = pAno
        self.cor = pCor
        self.marcha = pMarcha

    # Métodos da classe
    def ligar(self): # Utilizando Self indica que o método é do objeto (instância) e não da classe.
        if ( not ( self.ligado )):
            print('Ligou o carro')
            self.ligado = True
        else:
            print('O carro já está ligado')
        
    def getModelo(self):
        return self.modelo
    
    def setMarcha(self, marcha):
        self.marcha = marcha
    
    def getMarcha(self):
        return self.marcha

    def desligar(self):
        if ( not ( self.ligado )):
            print('O carro já está desligado')
            self.ligado = False
        else:
            print('Desligou o carro')

    def subirMarcha(self):
        if ( self.marcha < 5 ):
            self.marcha += 1
            print(f'{self.marcha}')
        else:
            print('Já está na marcha 5')

    def descerMarcha(self):
        if ( self.marcha > 0 ):
            self.marcha -= 1
            print(f'{self.marcha}')
        else:
            print('Já está na marcha 0')

    def acelerar(self):        
        # A cada acelerada, irá incrementar 10km/h.
        # Ao chegar em 20km/h, o carro deve AUTOMATICAMENTE subir para marcha 2
        # Ao chegar em 40km/h, o carro deve AUTOMATICAMENTE subir para a marcha 3
        # Ao chegar em 50km/h, o carro deve AUTOMATICAMENTE subir para a marcha 4
        # Ao chegar em 60km/h ou mais, o carro já deve estar na marcha 5
        if ( not ( self.ligado )):
            print('Necessário ligar o carro')
        else:
            self.velocidade += 10
            if ( self.velocidade < 20 ):
                self.marcha = 1
            elif( self.velocidade < 40 ):
                self.marcha = 2
            elif ( self.velocidade < 50 ):
                self.marcha = 3
            elif ( self.velocidade < 60 ):
                self.marcha = 4
            else:
                self.marcha = 5
            print(f'Velocidade: {self.velocidade} | Marcha: {self.marcha}')
    
    def obemMarcha(self):
        # return 'Marcha atual: ' + str(self.marcha)
        return f'Marcha atual: {self.marcha}. Veículo {self.modelo}'