#classe veiculo

class veiculo():

    #atributos da classe
    marca = ''
    modelo = ''
    ano = 0
    cor = ''
    marca = ''
    ligado = False
    marcha = 0
    acel = 0

    

    
#Método construtor
    def __init__(self,marca,pModelo,pAno,pCor,pMarcha = 0):
      self.marca = marca
      self.modelo = pModelo
      self.ano = pAno
      self.cor = pCor
      self.marcha = pMarcha

    
    def ligar(self):
        if ( not ( self.ligado )):
            print('Ligou o carro')
            self.ligado = True
        else:
            print('O carro já esta ligado')

    def getModelo(self):
        return self.modelo

    def setMarcha(self, marcha):
        self.marcha = marcha

    def getMarcha(self):
        return self.marcha

    def desligar(self):
        if ( not ( self.ligado)):
          print('O carro já esta desligado')
          self.ligado = False
        else:
            print('Desligou o carro')
    def subirMarcha(self):
        if ( self.marcha < 5 ):
          self.marcha += 1
          print(self.marcha)
        else:
            print('Já esta na marcha 5')


    def descerMarcha(self):
        if ( self.marcha > 0 ):
           self.marcha -= 1 
           print(self.marcha)
        else:
            print('já esta na marcha 0')

    def acelerar(self):
        if ( self.acel > 10, 20, 40, 50, 60):
            self.acel += 10
            print(self.acel)
        if ( self.acel ==10):
            print('Marcha 1')
        else:
          if ( self.acel <= 20): 
            print('Subiu para marcha 2')
          else:
            if (self.acel <= 40):
             print('Subiu para a marcha 3')
            else:
             if (self.acel <= 50):
              print('Subiu para a marcha 4')
             else:
              if (self.acel <= 60):
                print('Subiu para a marcha 5')
            
    def obemMarcha(self):
       #return 'Marcha atual: ' + str(self.marcha)
       return f'Marcha atual: {self.marcha}. Veículo {self.modelo}'
    
    
       
