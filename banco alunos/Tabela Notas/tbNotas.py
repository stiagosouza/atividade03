import sqlite3
from modeloAlunos import Notas
from tbAlunos import aluno1,aluno2,aluno3,aluno4

from tbDisciplina import Historia, Matematica,Geografia
banco = sqlite3.connect('provas alunos.db')
banco.execute("PRAGMA forengn_keys=on") 
cursor = banco.cursor()

#Inserção de dados em tabela Notas
Insert = '''INSERT INTO Notas(disciplina, nota,aluno) VALUES (;disciplina, :nota1, :nota,:aluno);''' 

AlunoNota1 = Notas (Historia.id,8.5,aluno1.id),
(Matematica.id, 5.5,aluno1.id),
(Geografia.id, 7.5,aluno1.id)

AlunoNota2 = Notas(Historia.id,8.5,aluno2.id),
(Matematica.id, 5.5,aluno2.id),
(Geografia.id, 7.5,aluno2.id)

AlunoNota3 = Notas(Historia.id,8.5,aluno3.id),
(Matematica.id, 5.5,aluno3.id),
(Geografia.id, 7.5,aluno3.id)

AlunoNota4 = Notas(Historia.id,8.5,aluno4.id),
(Matematica.id, 5.5,aluno4.id),
(Geografia.id, 7.5,aluno4.id)

cursor.execute(Insert, vars(AlunoNota1))
cursor.execute(Insert, vars(AlunoNota2))
cursor.execute(Insert, vars(AlunoNota3))
cursor.execute(Insert, vars(AlunoNota4))

banco.commit()
cursor.close()
banco.close()

