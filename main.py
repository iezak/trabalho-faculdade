# Vinicius Medeiros Iezak
# Curso: Raciocínio Computacional

# Importação da classe estudanteClass do arquivo estudante.py
from estudante import estudanteClass

# Definição da classe MeuApp
class MeuApp:
    def __init__(self) -> None:
        # Inicialização da classe
        self.opcao = 0
        self.estudanteClass = estudanteClass()  # Instância da classe estudanteClass

    def MenuPrincipal(self):
        # Menu principal do aplicativo
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
            self.MenuEstudantes()  # Chamando o menu de operações dos estudantes
        elif self.opcao == 2:
            self.MenuProfessores()  # Chamando o menu de operações dos professores
        elif self.opcao == 3:
            self.MenuDisciplinas()  # Chamando o menu de operações das disciplinas
        elif self.opcao == 4:
            self.MenuTurmas()  # Chamando o menu de operações das turmas
        elif self.opcao == 5:
            self.MenuMatriculas()  # Chamando o menu de operações das matrículas
        elif self.opcao == 9:
            quit()  # Encerrando o programa
        else:
            print(f"A opção {self.opcao} é inválida, tente novamente")  # Tratando opção inválida

    def MenuEstudantes(self):
        # Menu para gerenciamento de estudantes
        while True:
            print('***** [Estudantes] Menu de operações *****')
            print("")
            # Opções do menu de estudantes
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.")
            self.opcao = (input("Informe a ação desejada: "))
            try:
                self.opcao = int(self.opcao)  # Convertendo a opção para um número inteiro
                self.Opcao()  # Chamando o método para execução da opção escolhida
            except ValueError:
                print(f"A opção {self.opcao} é inválida, tente novamente")  # Tratando erro de conversão

    # Os métodos MenuProfessores, MenuDisciplinas, MenuTurmas e MenuMatriculas
    # têm uma estrutura semelhante ao MenuEstudantes e não foram comentados individualmente.

    def Opcao(self):
        # Método para execução das opções escolhidas
        if self.opcao == 1:
            self.estudanteClass.incluirEstudantes()  # Chamando o método para inclusão de estudantes
        elif self.opcao == 2:
            self.estudanteClass.listarEstudantes()  # Chamando o método para listagem de estudantes
        elif self.opcao == 3:
            self.estudanteClass.EditarEstudante()  # Chamando o método para edição de estudantes
        elif self.opcao == 4:
            self.estudanteClass.ExcluirEstudante()  # Chamando o método para exclusão de estudantes
        elif self.opcao == 9:
            self.MenuPrincipal()  # Voltando ao menu principal
        else:
            print(f"A opção {self.opcao} é inválida, tente novamente \n")  # Tratando opção inválida

# Instanciação da classe e início do aplicativo
app = MeuApp()
app.MenuPrincipal()