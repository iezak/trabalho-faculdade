# Vinicius Medeiros Iezak
# Curso: Raciocínio Computacional

class MeuApp:
    def __init__(self) -> None:
        # Inicialização da classe
        self.opcao = 0
        self.listaDeEstudantes = list()

    def MenuPrincipal(self):
        # Menu principal do aplicativo
        while True:
            print("---- MENU PRINCIPAL ----")
            print("")
            print("(1) Gerenciar estudantes.")
            print("(2) Gerenciar professores.")
            print("(3) Gerenciar disciplinas.")
            print("(4) Gerenciar turmas.")
            print("(5) Gerenciar Matriculas.")
            print("(9) Sair.")

            self.opcao = input("Informe a opção desejada: ")
            if self.opcao.isdigit():
                self.opcao = int(self.opcao)
                self.EscolhaOperacao()
            else:
                print(f"A opção {self.opcao} é inválida, tente novamente")

    def EscolhaOperacao(self):
        # Método para escolha da operação a ser realizada
        if self.opcao == 1:
            self.MenuEstudantes()
        elif self.opcao == 2:
            self.MenuProfessores()
        elif self.opcao == 3:
            self.MenuDisciplinas()
        elif self.opcao == 4:
            self.MenuTurmas()
        elif self.opcao == 5:
            self.MenuMatriculas()
        elif self.opcao == 9:
            quit()
        else:
            print(f"A opção {self.opcao} é inválida, tente novamente")

    def MenuEstudantes(self):
        # Menu para gerenciamento de estudantes
        while True:
            print('***** [Estudantes] Menu de operações *****')
            print("")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.")
            self.opcao = (input("Informe a ação desejada: "))
            if self.opcao.isdigit():
                self.opcao = int(self.opcao)
                self.Opcao()
            else:
                print("Opção invalida, entre com um mumero ")

    def MenuProfessores(self):
        # Menu para gerenciamento de professores
        print("EM DESENVOLVIMENTO")
        self.MenuPrincipal()

    def MenuDisciplinas(self):
        # Menu para gerenciamento de disciplinas
        print("EM DESENVOLVIMENTO")
        self.MenuPrincipal()

    def MenuTurmas(self):
        # Menu para gerenciamento de turmas
        print("EM DESENVOLVIMENTO")
        self.MenuPrincipal()

    def MenuMatriculas(self):
        # Menu para gerenciamento de matrículas
        print("EM DESENVOLVIMENTO")
        self.MenuPrincipal()

    def Opcao(self):
        # Método para execução das opções escolhidas
        if self.opcao == 1:
            self.incluirEstudantes()
        if self.opcao == 2:
            self.listarEstudntes()
        elif self.opcao in [3, 4]:
            print("EM DESENVOLVIMENTO")
        elif self.opcao == 9:
            self.MenuPrincipal()
        else:
            print(f"A opção {self.opcao} é inválida, tente novamente \n")

    def incluirEstudantes(self):
    # Método para incluir estudantes na lista
        print("\n===== INCLUSÃO =====\n")
        while True:
            nomeEstudante = input("Informe o nome do estudante: ")
            if nomeEstudante.replace(" ", "").isalpha():
                self.listaDeEstudantes.append(nomeEstudante)
                input("Pressione ENTER para continuar\n\n")
                break
            else:
                print("Insira um nome válido")

    def listarEstudntes(self):
        # Método para listar estudantes cadastrados
        print("\n===== LISTAGEM =====\n")
        if self.listaDeEstudantes:
            for i, estudante in enumerate(self.listaDeEstudantes, 1):
                print(f"{i}. {estudante}")
            input("Precione ENTER para continuar\n\n")
        else:
            print("Não há estudantes cadastrados.")

app = MeuApp()
app.MenuPrincipal()