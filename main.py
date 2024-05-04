# Vinicius Medeiros Iezak
# Curso: Raciocínio Computacional

# Importação da classe estudanteClass do arquivo estudante.py
from editor import Editor

# Definição da classe MeuApp
class MeuApp:
    def __init__(self) -> None:
        # Inicialização da classe
        self.opcao = 0
        self.entidade = ""

    # Menu principal do aplicativo
    def MenuPrincipal(self):
        while True:
            print("---- MENU PRINCIPAL ----")
            print("")
            # Opções do menu principal
            print("(1) Gerenciar estudantes.")
            print("(2) Gerenciar professores.")
            print("(3) Gerenciar disciplinas.")
            print("(4) Gerenciar turmas.")
            print("(5) Gerenciar Matriculas.")
            print("(9) Sair.")

            # Solicitar opção ao usuário
            self.opcao = input("Informe a opção desejada: ")
            try:
                self.opcao = int(self.opcao)  # Convertendo a opção para um número inteiro
                self.EscolhaOperacao()  # Chamando o método para escolha da operação
            except ValueError:
                print(f"Eroo: A opção {self.opcao} é inválida, tente novamente")  # Tratando erro de conversão

    def EscolhaOperacao(self):
        # Método para escolha da operação a ser realizada
        if self.opcao == 1:
            self.entidade = "estudante"
            self.MenuSecundario()  # Chamando o menu de operações dos estudantes
        elif self.opcao == 2:
            self.entidade = "professor"
            self.MenuSecundario()  # Chamando o menu de operações dos professores
        elif self.opcao == 3:
            self.entidade = "disciplina"
            self.MenuSecundario()  # Chamando o menu de operações das disciplinas
        elif self.opcao == 4:
            self.entidade = "turma"
            self.MenuSecundario()  # Chamando o menu de operações das turmas
        elif self.opcao == 5:
            self.entidade = "matricula"
            self.MenuSecundario()  # Chamando o menu de operações das matrículas
        elif self.opcao == 9:
            quit()  # Encerrando o programa
        else:
            print(f"A opção {self.opcao} é inválida, tente novamente")  # Tratando opção inválida

    def MenuSecundario(self):
        # Menu para gerenciamento de estudantes
        while True:
            print(F'\n***** [{self.entidade}] Menu de operações *****\n')
            # Opções do menu de estudantes
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.")
            self.opcao_secundaria = (input("Informe a ação desejada: "))
            try:
                opcao_secundaria = int(self.opcao_secundaria)  # Convertendo a opção para um número inteiro
                self.Opcao(opcao_secundaria)  # Chamando o método para execução da opção escolhida
            except ValueError:
                print(f"A opção {self.opcao_secundaria} é inválida, tente novamente")  # Tratando erro de conversão

    def Opcao(self, opcao_secundaria):
        editor = Editor()
        # Método para execução das opções escolhidas
        if opcao_secundaria == 1:
            if self.entidade == 'professor' or self.entidade == 'estudante':
                editor.incluirPessoa(self.entidade)  # Chamando o método para inclusão de estudantes
            if self.entidade == 'disciplina':
                editor.incluirDiciplina(self.entidade)
            if self.entidade == 'turma':
                editor.incluirTurma(self.entidade)
            if self.entidade == 'matricula':
                editor.incluirMatricula(self.entidade)
                
        elif opcao_secundaria == 2:
            if self.entidade == 'estudante' or self.entidade == 'professor':
                editor.listarPessoa(self.entidade)  # Chamando o método para inclusão de estudantes
            if self.entidade == 'disciplina':
                editor.listarDiciplinas(self.entidade)
            if self.entidade == 'turma':
                editor.listarTurmas(self.entidade)
            if self.entidade == 'matricula':
                editor.listarMatriculas(self.entidade)
                print()
        elif opcao_secundaria == 3:
            if self.entidade == 'estudante' or self.entidade == 'professor':
                editor.editarPessoa(self.entidade)  # Chamando o método para inclusão de estudantes
            if self.entidade == 'disciplina':
                editor.editarDiciplina(self.entidade)
            if self.entidade == 'turma':
                editor.editarTurma(self.entidade)
            if self.entidade == 'matricula':
                editor.editarMatricula(self.entidade)
                print()
        elif opcao_secundaria == 4:
            if self.entidade == 'estudante' or self.entidade == 'professor':
                editor.excluirPessoa(self.entidade)  # Chamando o método para inclusão de estudantes
            if self.entidade == 'disciplina':
                editor.excluirDiciplina(self.entidade)
            if self.entidade == 'turma':
                editor.excluirTurma(self.entidade)
            if self.entidade == 'matricula':
                editor.excluirMatricula(self.entidade)
                print()
        elif opcao_secundaria == 9:
            self.MenuPrincipal()  # Voltando ao menu principal
        else:
            print(f"A opção {opcao_secundaria} é inválida, tente novamente \n")  # Tratando opção inválida

# Instanciação da classe e início do aplicativo
app = MeuApp()
app.MenuPrincipal()

