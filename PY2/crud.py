from classeConexao import Conexao
from time import sleep
import os

# print('teste')
# sleep(3) #aguarda 3seg
# os.system('cls') #limpa a tela
# print('TESTE2')
# sleep(3)
# os.system(3)
valores = []
campos = []




def MontaCampos():
     global campos
     campos = []
     op = 0
     while op != 2:
         campos.append (input('Informe o nome do campo: '))
         op = int(input('Deseja informar mais algum campo? [1- Sim | 2- Não]: '))

     global valores
     valores = []
     for x in range(0,len(campos)):
         valores.append(input('Informe o valor para "' + campos[x] + '": '))

#      print(campos)
#      print(valores)

# MontaCampos()

def MontaMenu():
    op = 0
    while ( op != 5 ):
       print('+-----------------------------+')
       print('|1- Cadastrar      2- Alterar |')
       print('|3- Excluir     4- Visualizar |')
       print('          5- Sair             |')
       print('+-----------------------------+')
       op = int(input('Opção desejada: '))
       if  op == 1 :
           print('Irá cadastrar as informações ')
           tabela = input('Nome da tabela para cadastrar: ')
           campos = []
           valores = []
           MontaCampos()
           conexao.cadastra_dados(tabela,campos,valores)
           sleep(3)
           os.system('cls')
       elif  op == 2 :
          print('Irá alterar os dados')
          sleep(3)
          os.system('cls')
       elif  op == 3 :
          print('Irá excluir os dados ')
          sleep(3)
          os.system('cls')
       elif  op == 4  :
          print('Irá visualizar as informações')
          sleep(3)
          os.system('cls')
       elif  op == 5  :
           print('Obrigado')
           sleep(3)
           break
       else:
          print('Opção inválida')
          sleep(3)
          os.system('cls')

conexao = Conexao('localhost','escola','root','')
sleep(2)
if conexao.existeUsuario():
   sleep(3)
   os.system('cls')
   MontaMenu()


    

# conexao = Conexao('localhost','escola','root','')
# valores = [5,'F']
# campos = ['id_cad_aluno','sexo_cad_aluno']
# conexao.altera_dados('cad_alunos',campos,valores, 'id_cad_aluno = 3 and nome_cad_aluno = "Fabiana"')
# # conexao.retorna_dados('cad_alunos')
# tabela = ['Mayara','f']
# clausula = ['nome_cad_vendedor','sexo_cad_vendedor']
#conexao.exclui_dados('cad_vendedores', 'id_cad_vendedor >= 1')
# conexao.retorna_dados('cad_professores')
# conexao.exclui_dados('nome_cad_vendedor','sexo_cad_vendedor')
# conexao.retorna_dados('cad_alunos')
#conexao.altera_dados('cad_alunos','nome_cad_aluno','Fabiana','id_cad_aluno = 3')
# conexao.retorna_dados('cad_alunos')
#campos = 'nome_cad_vendedor','sexo_cad_vendedor'
#conexao.retorna_total_registros('cad_vendedores', 'id_cad_vendedor >1')