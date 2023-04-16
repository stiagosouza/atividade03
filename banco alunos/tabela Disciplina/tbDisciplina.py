import sqlite3
from modeloAlunos import Disciplinas

banco = sqlite3.connect('provas alunos.db')
banco.execute("PRAGMA forengn_keys=on") 

cursor = banco.cursor()

#Inserção de dados em tabela Disciplina
Insert = '''INSERT INTO Disciplinas(id,nome, professor) VALUES (:id,:nome, :professor);''' 

Historia = Disciplinas(None,"Historia","Tiago")
cursor.execute(Insert, vars(Historia))
Historia.id= cursor.lastrowid

Matematica = Disciplinas(None,"Matematica","Debora")
cursor.execute(Insert, vars(Matematica))
Matematica.id= cursor.lastrowid

Geografia = Disciplinas(None,"Geografia","Layla")
cursor.execute(Insert, vars(Geografia))
Geografia.id= cursor.lastrowid

Portugues = Disciplinas(None,"Portugues","Lucas")
cursor.execute(Insert, vars(Portugues))
Portugues.id= cursor.lastrowid

banco.commit()
cursor.close()
banco.close()

