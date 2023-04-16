import sqlite3
from modeloAlunos import Alunos

banco = sqlite3.connect('provas alunos.db')
banco.execute("PRAGMA forengn_keys=on") 
cursor = banco.cursor()

#Inserção de dados em tabela Alunos
comand = '''INSERT INTO Alunos(cpf, nome, nascimento) VALUES (:cpf, :nome, :nascimento);''' 

aluno1 = Alunos(97716012371,"Carlos","2005-05-25")
cursor.execute(comand, vars(aluno1))
aluno1.id= cursor.lastrowid

aluno2 = Alunos(18465243344,"Marcelo","2007-01-20")
cursor.execute(comand, vars(aluno2))
aluno2.id= cursor.lastrowid

aluno3 = Alunos(60242054307,"Matheus","2004-08-15")
cursor.execute(comand, vars(aluno3))
aluno3.id= cursor.lastrowid

aluno4 = Alunos(37142193310,"Leonardo","2000-11-10")
cursor.execute(comand, vars(aluno4))
aluno4.id= cursor.lastrowid

banco.commit()
cursor.close()
banco.close()
