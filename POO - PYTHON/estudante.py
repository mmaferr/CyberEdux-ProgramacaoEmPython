class Estudante():
    def __init__(self) -> None:
        self.nome = None
        self.email = None
        self.semestre = 1

    def avancar_semestre(self):
        self.semestre += 1

class EstudanteDeGraduacao(Estudante):
    def __init__(self) -> None:
        super().__init__()
        self.curso = None
        self.modalidade = None

    def exibir(self):
        print('Nome: ', self.nome)
        print('Curso: ', self.curso)
        print('Modalidade: ', self.modalidade)

if __name__ == '__main__':
    aluno = EstudanteDeGraduacao()
    print(isinstance(aluno, Estudante))
    print(isinstance(aluno, Exception))
    print(isinstance(aluno, Estudante))
