from classeConexao import Conexao

conexao = Conexao('localhost','escola','root','')
#conexao.retorna_dados('cad_alunos')
professores = ['jhonni','m']
conexao.cadastra_dados('cad_professores','nome_cad_professor, sexo_cad_professor',professores)
conexao.retorna_dados('cad_professores'),