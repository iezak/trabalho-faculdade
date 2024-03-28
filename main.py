class MeuApp:   
    def __init__(self) -> None:
        self.opcao = 0
               
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
        while True:
            print("***** [Professores] Menu de operações *****")
            print("")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.")
            self.opcao = int(input("Informe a ação desejada: "))
            self.Opcao()
        
    def MenuDisciplinas(self):
        while True:   
            print("***** [Disciplinas] Menu de operações *****")
            print("")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.")
            self.opcao = int(input("Informe a ação desejada: "))
            self.Opcao()
        
    def MenuTurmas(self):
        while True:    
            print("***** [Turmas] Menu de operações *****")
            print("")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.")
            self.opcao = int(input("Informe a ação desejada: "))
            self.Opcao()
        
    def MenuMatriculas(self):
        while True:    
            print("***** [Matriculas] Menu de operações *****")
            print("")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(9) Voltar ao menu principal.")
            self.opcao = int(input("Informe a ação desejada: "))
            self.Opcao()
        
    def Opcao(self):
        if self.opcao in [1, 2, 3, 4]:
            print(f"A opção {self.opcao} é válida \n")
        elif self.opcao == 9:
            self.MenuPrincipal()
        else:
            print(f"A opção {self.opcao} é inválida, tente novamente \n")

app = MeuApp()
app.MenuPrincipal()
