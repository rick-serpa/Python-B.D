import mysql.connector
#pede parametros = hosat, banco de dados, usuario, senha.
try:
    con = mysql.connector.connect(host='localhost',database='escola',user='root',password='')
#if con.is_connected():
    #print('Conexão efetuada com sucesso')
#else:
    #print('Erro na conexão com o banco de dados/servidor')

    if con.is_connected():
        print('Conexão efetuada com sucesso')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM cad_alunos')
        linha = cursor.fetchall()
        if cursor.rowcount == 0 :
            print('Não foi retornado registros com a consulta')
        else:
            for reg in linha:
                if reg[2] ==  'm' :
                    print(str(reg[0]) + ' ' + reg[1] + ' Masculino ') 
                else:
                    if reg[2] == 'f':
                        print(str(reg[0]) + ' ' + reg[1] + ' Feminino ') 
                    else:
                        print(str(reg[0]) + ' ' + reg[1] + ' Indefinido ')    
    else:
        print('Não está conectado')
except:
    print('Erro na conexão com o banco de dados/servidor')

