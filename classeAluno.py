class Aluno():

    def __init__(self):
        self.nome = "Pinguim"
        self.rg = 1234567891011
        self.curso = "missanga"

    def printa(self):
        print("nome = ",self.nome)
        print("rg = ",self.rg)
        print("curso = ",self.curso)



Aluno = Aluno()
Aluno.printa()           