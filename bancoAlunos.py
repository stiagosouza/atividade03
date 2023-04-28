# Enviar toda a atividade de registro de notas: Retorne o nome dos alunos e suas notas e Retorne o nome dos alunos e suas
# respectivas disciplinas!

import sqlite3
from modeloAlunos import Alunos,Disciplinas,Notas

banco = sqlite3.connect('provas alunos.db')
banco.execute("PRAGMA forengn_keys=on") 
cursor = banco.cursor()

cursor.execute('''CREATE TABLE Alunos (
                  cpf INTEGER PRIMARY KEY,
                  nome TEXT NOT NULL,
                  nascimento DATE NOT NULL);''')

 cursor.execute('''CREATE TABLE Disciplinas (
                 id INTEGER AUTO INCREMENT PRIMARY KEY,
                 nome TEXT NOT NULL,
                 professor TEXT NOT NULL);''')

 cursor.execute('''CREATE TABLE Notas (
                 id INTEGER AUTO INCREMENT PRIMARY KEY,
                 disciplina TEXT NOT NULL,
                 nota REAL NOT NULL,
                 aluno TEXT  NOT NULL,
                 FOREIGN KEY(aluno) REFERENCES Aluno(id),
                 FOREIGN KEY(disciplina) REFERENCES Disciplina(id));''')


banco.commit()
cursor.close()
banco.close()

