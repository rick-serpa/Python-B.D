import mysql.connector

class Conexao():
    def __init__(self,host,banco,usuario,senha):
        self.host = host
        self.database = banco
        self.user = usuario
        self.password = senha
        #parametros --> host | database | user | password
        self.conn = mysql.connector.connect(host=self.host,database=self.database,user=self.user,password=self.password)
        if self.conn.is_connected():
            print('conexão efetuada com sucesso') 
        else:
            print('Falha na conexão ao banco/servidor')

    def retorna_dados(self, tabela, clausula = ''):
        if self.conn.is_connected():
            cursor = self.conn.cursor()
            if clausula != '' :    
                cursor.execute('SELECT * FROM ' + tabela + ' WHERE ' + clausula)
            else:
                cursor.execute('SELECT * FROM ' + tabela)
            linha = cursor.fetchall()
            if ( cursor.rowcount == 0 ):
               print ('Não foram encontrador registros com a selação atual')
            else: 
                print('Resultado da consulta')
                for reg in linha:
                    if reg[2] == 'f':
                       print(str(reg[0]) + ' | ' + reg[1] + ' | Feminino ') 
                    else:
                        if reg[2] == 'm':
                            print(str(reg[0]) + ' | ' + reg[1] + ' | Masculino ') 
                        else:
                            print(str(reg[0]) + ' | ' + reg[1] + ' | Sexo indefinidp ') 
                            

                print('Total de Registros: ' + str(cursor.rowcount))

    def cadastra_dados(self,tabela,campos,valores):
        if self.conn.is_connected():
            cursor = self.conn.cursor()
            try:
                cursor.execute('INSERT INTO' + tabela + ' (' + campos + ') VALUES ("' + valores[0] + '", "' + valores[1] + '")') 
                self.conn.commit()
                print('Registro cadastrado com sucesso')
            except:
                self.conn.rollback
                print('Erro ao cadastrar')


