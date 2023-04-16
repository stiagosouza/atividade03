

class Alunos:
    def __init__(self, cpf, nome, nascimento):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
       

class Disciplinas:
    def __init__(self,id, nome,professor):
        self.id = None
        self.nome = nome
        self.professor = professor

class Notas:
    def __init__(self,id, disciplina, nota, aluno):
        self.id = id
        self.disciplina = disciplina
        self.nota = nota
        self.aluno = aluno
      