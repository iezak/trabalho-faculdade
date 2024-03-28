class MeuApp:   
    def __init__(self) -> None:
        self.opcao = 0
        self.listaDeEstudantes = list()
               
    def MenuPrincipal(self):
        while True:    
            print("---- MENU PRINCIPAL ----")
            print("")
            print("(1) Gerenciar estudantes.")
            print("(2) Gerenciar professores.")
            print("(3) Gerenciar disciplinas.")
            print("(4) Gerenciar turmas.")
            print("(5) Gerenciar Matriculas.")
            print("(9) Sair.")
            
            self.opcao = int(input("Informe a opção desejada: "))
            self.EscolhaOperacao()
        
    def EscolhaOperacao(self):
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
        while True:    
            print('***** [Estudantes] Menu de operações *****')
            print("")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.")  
            self.opcao = int(input("Informe a ação desejada: "))
            self.Opcao()
        
        
    def MenuProfessores(self):
        print("EM DESENVOLVIMENTO")
        self.MenuPrincipal()
        
    def MenuDisciplinas(self):
        print("EM DESENVOLVIMENTO")
        self.MenuPrincipal()
        
    def MenuTurmas(self):   
        print("EM DESENVOLVIMENTO")
        self.MenuPrincipal()
        
    def MenuMatriculas(self):
        print("EM DESENVOLVIMENTO")
        self.MenuPrincipal()
        
    def Opcao(self):
        if self.opcao == 1:
            self.incluirEstudantes()
        if self.opcao == 2:
            self.listarEstudntes()
        elif self.opcao in [3,4]:
            print("EM DESENVOLVIMENTO")
        elif self.opcao == 9:
            self.MenuPrincipal()
        else:
            print(f"A opção {self.opcao} é inválida, tente novamente \n")
            
    def incluirEstudantes(self):
        print("\n===== INCLUSÃO =====\n")
        nomeEstudante = input("Informe o nome do estudante: ")
        self.listaDeEstudantes.append(nomeEstudante)
        input("Precione ENTER para continuar\n\n")
        print(self.listaDeEstudantes)
        
    def listarEstudntes(self):
        print("\n===== LISTAGEM =====\n")
        if self.listaDeEstudantes:
            for i, estudante in enumerate(self.listaDeEstudantes, 1):
                print(f"{i}. {estudante}")
            input("Precione ENTER para continuar\n\n")
        else:
            print("Não há estudantes cadastrados.")
        
app = MeuApp()
app.MenuPrincipal()
