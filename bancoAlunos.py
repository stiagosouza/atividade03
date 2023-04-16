# Enviar toda a atividade de registro de notas: Retorne o nome dos alunos e suas notas e Retorne o nome dos alunos e suas
# respectivas disciplinas!

import sqlite3
from modeloAlunos import Alunos,Disciplinas,Notas

banco = sqlite3.connect('provas alunos.db')
banco.execute("PRAGMA forengn_keys=on") 
cursor = banco.cursor()

# cursor.execute('''CREATE TABLE Alunos (
#                 cpf INTEGER PRIMARY KEY,
#                 nome TEXT NOT NULL,
#                 nascimento DATE NOT NULL);''')

# cursor.execute('''CREATE TABLE Disciplinas (
#                 id INTEGER AUTO INCREMENT PRIMARY KEY,
#                 nome TEXT NOT NULL,
#                 professor TEXT NOT NULL);''')

# cursor.execute('''CREATE TABLE Notas (
#                 id INTEGER AUTO INCREMENT PRIMARY KEY,
#                 disciplina TEXT NOT NULL,
#                 nota REAL NOT NULL,
#                 aluno TEXT  NOT NULL,
#                 FOREIGN KEY(aluno) REFERENCES Aluno(id),
#                 FOREIGN KEY(disciplina) REFERENCES Disciplina(id));''')

#Inserção de dados em tabela Alunos
comand = '''INSERT INTO Alunos(cpf, nome, nascimento) VALUES (:cpf, :nome, :nascimento);''' 

aluno1 = Alunos(97716012371,"Carlos","2005-05-25")
aluno2 = Alunos(18465243344,"Marcelo","2007-01-20")
aluno3 = Alunos(60242054307,"Matheus","2004-08-15")
aluno4 = Alunos(37142193310,"Leonardo","2000-11-10")

# cursor.execute(comand, vars(aluno1))
# cursor.execute(comand, vars(aluno2))
# cursor.execute(comand, vars(aluno3))
# cursor.execute(comand, vars(aluno4))


#Inserção de dados em tabela Disciplina
Insert = '''INSERT INTO Disciplinas(id,nome, professor) VALUES (:id,:nome, :professor);''' 

Historia = Disciplinas(None,"Historia","Tiago")
Matematica = Disciplinas(None,"Matematica","Debora")
Geografia = Disciplinas(None,"Geografia","Layla")

# cursor.execute(Insert, vars(Historia))
# cursor.execute(Insert, vars(Matematica))
# cursor.execute(Insert, vars(Geografia))

#Inserção de dados em tabela Notas
Insert = '''INSERT INTO Notas(disciplina, nota,aluno) VALUES (;disciplina, :nota,:aluno);''' 

AlunoNota1 = Notas (Historia,8.5,aluno1)
(Matematica, 5.5,aluno1)
(Geografia, 7.5,aluno1)

AlunoNota2 = Notas(Historia,8.5,aluno2)
(Matematica, 5.5,aluno2)
(Geografia, 7.5,aluno2)

AlunoNota3 = Notas(Historia,8.5,aluno3)
(Matematica, 5.5,aluno3)
(Geografia, 7.5,aluno3)

AlunoNota4 = Notas(Historia,8.5,aluno4)
(Matematica, 5.5,aluno4)
(Geografia, 7.5,aluno4)

# cursor.execute(Insert, vars(AlunoNota1))
# cursor.execute(Insert, vars(AlunoNota2))
# cursor.execute(Insert, vars(AlunoNota3))
# cursor.execute(Insert, vars(AlunoNota4))

banco.commit()
cursor.close()
banco.close()

