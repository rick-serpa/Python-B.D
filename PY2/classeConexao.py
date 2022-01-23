from tkinter import INSERT
from unittest import result
from xmlrpc.client import Boolean, boolean
import mysql.connector

class Conexao():
    

    def __init__(self,host,banco,usuario,senha):
        self.host = host
        self.database = banco
        self.user = usuario
        self.password = senha
        self._MSG_MENSAGEM_CLAUSULA_DELETE = 'Necessário informar o registro que deseja excluir'
        self._MSG_MENSAGEM_CLAUSULA_UPDATE = 'Necessário informar o registro que deseja alterar'
        self._MSG_SUCESSO_EXLUIR = 'Registro excluído com sucesso.'
        self._MSG_SUCESSO_ALTERAR = 'Registro alterado com sucesso.'
        self._MSG_SUCESSO_INSERIR = 'Registro inserido com sucesso.'
        self._MSG_ERRO_EXCLUIR = 'Erro ao excluir o registro.'
        self._MSG_ERRO_ALTERAR = 'Erro ao alterar o registro.'
        self._MSG_ERRO_INSERIR = 'Erro ao inserir o registro.'
        # parametros -> host | database | user | password
        self.conn = mysql.connector.connect(host=self.host,database=self.database,user=self.user,password=self.password)
        if self.conn.is_connected():
            print('Conexão efetuada com sucesso')
        else:
            print('Falha na conexão ao banco/servidor')

    def retorna_total_registros(self,tabela,clausula = '1 = 1'):
        if self.conn.is_connected():
            cursor = self.conn.cursor()
            sql = 'SELECT COUNT(*) total FROM ' + tabela + ' WHERE ' + clausula
            cursor.execute(sql)
            linha = cursor.fetchall()
            if ( cursor.rowcount == 0):
                    print(self._MSG_REGISTRO_INEXISTENTE)
                    return False
            return True

    def retorna_dados(self,tabela,clausula = ''):
        if self.conn.is_connected():
            cursor = self.conn.cursor()
            if clausula != '' :
                cursor.execute('SELECT * FROM ' + tabela + ' WHERE ' + clausula)
            else:
                cursor.execute('SELECT * FROM ' + tabela)
            linha = cursor.fetchall()
            if ( cursor.rowcount == 0 ):
                print('Não foram encontrados registros com a seleção atual. [Tabela = ' + tabela + ']')
            else:
                print('Resultado da consulta [Tabela = ' + tabela + ']')
                for reg in linha:
                    if reg[2] == 'f':
                        print(str(reg[0]) + ' | ' + reg[1] + ' | Feminino')
                    else:
                        if reg[2] == 'm':
                            print(str(reg[0]) + ' | ' + reg[1] + ' | Masculino')
                        else:
                            print(str(reg[0]) + ' | ' + reg[1] + ' | Sexo Inválido')
                print('Total de Registros: ' + str(cursor.rowcount))
    
    def cadastra_dados(self,tabela,campos,valores,EhCadastroLogin = False):
        sql = 'INSERT INTO ' + tabela + '('
        sqlC = ''
        for x in range(0,len(campos)):
            sqlC += campos[x] + ', '
        sqlC = sqlC[:-2]
        sql += sqlC + ') VALUES ('
        sqlV = ''
        for x in range(0,len(valores)):
            if (type(valores[x]) is int) or (type(valores[x]) is float):
                sqlV += str(valores[x]) + ', '
            else:
                sqlV += '"' + str(valores[x]) + '", '
        sqlV = sqlV[:-2]
        sql += sqlV + ')'
        # print(sql)
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
            print(self._MSG_SUCESSO_INSERIR)
        except:
            self.conn.rollback()
            print(self._MSG_ERRO_INSERIR)

            
            #print(sql)
        # sql = 'INSERT INTO' + tabela + '(' + campos + ') VALUES ("' + valores[0] + '", "' + valores[1] + '")'
        # print(sql)
        #if self.conn.is_connected():
            #cursor = self.conn.cursor()
           # try:
            #    cursor.execute('INSERT INTO ' + tabela + ' (' + campos + ') VALUES ("' + valores[0] + '", "' + valores[1] + '")')
            #    self.conn.commit()
            #    print(self._MSG_SUCESSO_INSERIR)
           # except:
           #     self.conn.rollback()
           #     print(self._MSG_ERRO_INSERIR)
    
    def exclui_dados(self,tabela,clausula):
        if self.conn.is_connected():
            if self.retorna_total_registros(tabela,clausula):
                try:
                     cursor = self.conn.cursor()
                     cursor.execute('DELETE FROM ' + tabela + ' WHERE ' + clausula)
                     self.conn.commit()
                     print(self._MSG_SUCESSO_EXLUIR)
                except:
                     self.conn.rollback()
                     print(self._MSG_ERRO_EXCLUIR)
    
    def altera_dados(self,tabela,campos,valores,clausula):
        if self.conn.is_connected():
            sql = ''
            if self.retorna_total_registros(tabela,clausula):
                sql = 'UPDATE ' + tabela
                sqlC = ''
                for x in range(0,len(campos)):
                    if (type(valores[x]) is int) or (type(valores[x]) is float):
                        sqlC += ' SET ' + campos[x] + ' = ' + str(valores[x])
                    else:
                        sqlC += ' SET ' + campos[x] + ' = ' + str(valores[x]) + '"'
                    sql += sqlC + ' WHERE ' + clausula
            print(sql)
        return
        if clausula == '':
            print(self._MSG_MENSAGEM_CLAUSULA_ALTERAR)
        if self.conn.is_connected():
            try:
                cursor = self.conn.cursor()
                cursor.execute('UPDATE ' + tabela + ' SET ' + campos + ' = "' + valores + '" WHERE ' + clausula)
                self.conn.commit()
                print(self._MSG_SUCESSO_ALTERAR)
            except:
                self.conn.rollback()
                print(self._MSG_ERRO_ALTERAR)



# op = 0
# while ( op != 3 ):
#    os.system('cls')
#    print('+-----------------------------+')
#    print('|1- Cadastrar       2- Listar |')
#    print('|         3- Sair             |')
#    print('+-----------------------------+')
#    op = int(input('Opção desejada: '))
#    if ( op == 1 ):
#        print('Irá cadastrar as informações')
#        sleep(3)
#    if ( op == 2 ):
#        print('Irá listar os dados')
#        sleep(3)

def existeUsuario(self):
    if self.conn.is_connected():
     cursor = self.conn.cursor()
    cursor.execute('SELECT * FROM cad_usuarios')
    linha=cursor.fetchall()
    if (cursor.rowcount == 0):
        print('Necessarios cadastrar usuario')
    campos = ['login_cad_usuario','senha_cad_usuario','nome_cad_usuario']
    valores = []
    for x in range(0,len(campos)):
        if(type(campos[x]) is int) or (type(campos[x]) is float):
            valores.append(int(input)('Informe o valor para o campo "' +str(campos[x] + '": ')))
        else:
            valores.append(input('Informeo valor para o campo: "' + campos[x] + '": '))
        self.cadastra_dados('cad_usuarios')
