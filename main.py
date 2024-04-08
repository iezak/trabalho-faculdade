class MeuApp:   # Define a classe MeuApp.
    def __init__(self) -> None:  # Define o método de inicialização da classe.
        self.opcao = 0  # Inicializa a variável opcao como 0.
        self.listaDeEstudantes = list()  # Inicializa uma lista vazia para armazenar estudantes.
               
    def MenuPrincipal(self):  # Define o método MenuPrincipal.
        while True:    # Loop infinito para exibir o menu principal repetidamente.
            print("---- MENU PRINCIPAL ----")  # Imprime o título do menu principal.
            print("")
            print("(1) Gerenciar estudantes.")  # Opção para gerenciar estudantes.
            print("(2) Gerenciar professores.")  # Opção para gerenciar professores.
            print("(3) Gerenciar disciplinas.")  # Opção para gerenciar disciplinas.
            print("(4) Gerenciar turmas.")  # Opção para gerenciar turmas.
            print("(5) Gerenciar Matriculas.")  # Opção para gerenciar matrículas.
            print("(9) Sair.")  # Opção para sair do programa.
            
            self.opcao = input("Informe a opção desejada: ")  # Solicita a opção do usuário.
            if self.opcao.isdigit():
                self.opcao = int(self.opcao)
                self.EscolhaOperacao()  # Chama o método EscolhaOperacao.
            else:
                print("Opção invalida, entre com um mumero")
        
    def EscolhaOperacao(self):  # Define o método EscolhaOperacao.
        if self.opcao == 1:  # Se a opção selecionada for 1:
            self.MenuEstudantes()  # Chama o método MenuEstudantes.
        elif self.opcao == 2:  # Se a opção selecionada for 2:
            self.MenuProfessores()  # Chama o método MenuProfessores.
        elif self.opcao == 3:  # Se a opção selecionada for 3:
            self.MenuDisciplinas()  # Chama o método MenuDisciplinas.
        elif self.opcao == 4:  # Se a opção selecionada for 4:
            self.MenuTurmas()  # Chama o método MenuTurmas.
        elif self.opcao == 5:  # Se a opção selecionada for 5:
            self.MenuMatriculas()  # Chama o método MenuMatriculas.
        elif self.opcao == 9:  # Se a opção selecionada for 9:
            quit()  # Sai do programa.
        else:  # Se a opção não for válida:
            print(f"A opção {self.opcao} é inválida, tente novamente")  # Exibe uma mensagem de opção inválida.
        
    def MenuEstudantes(self):  # Define o método MenuEstudantes.
        while True:    # Loop infinito para exibir o menu de operações de estudantes repetidamente.
            print('***** [Estudantes] Menu de operações *****')  # Título do menu de operações de estudantes.
            print("")
            print("(1) Incluir.")  # Opção para incluir um estudante.
            print("(2) Listar.")  # Opção para listar os estudantes.
            print("(3) Atualizar.")  # Opção para atualizar os dados de um estudante.
            print("(4) Excluir.")  # Opção para excluir um estudante.
            print("(9) Voltar ao menu principal.")  # Opção para voltar ao menu principal.  
            self.opcao = (input("Informe a ação desejada: "))  # Solicita a opção do usuário.
            if self.opcao.isdigit():
                self.opcao = int(self.opcao)
                self.Opcao()  # Chama o método EscolhaOperacao.
            else:
                print("Opção invalida, entre com um mumero ")
        
        
    def MenuProfessores(self):  # Define o método MenuProfessores.
        print("EM DESENVOLVIMENTO")  # Exibe uma mensagem indicando que a funcionalidade está em desenvolvimento.
        self.MenuPrincipal()  # Retorna ao menu principal.
        
    def MenuDisciplinas(self):  # Define o método MenuDisciplinas.
        print("EM DESENVOLVIMENTO")  # Exibe uma mensagem indicando que a funcionalidade está em desenvolvimento.
        self.MenuPrincipal()  # Retorna ao menu principal.
        
    def MenuTurmas(self):   # Define o método MenuTurmas.
        print("EM DESENVOLVIMENTO")  # Exibe uma mensagem indicando que a funcionalidade está em desenvolvimento.
        self.MenuPrincipal()  # Retorna ao menu principal.
        
    def MenuMatriculas(self):  # Define o método MenuMatriculas.
        print("EM DESENVOLVIMENTO")  # Exibe uma mensagem indicando que a funcionalidade está em desenvolvimento.
        self.MenuPrincipal()  # Retorna ao menu principal.
        
    def Opcao(self):  # Define o método Opcao.
        if self.opcao == 1:  # Se a opção selecionada for 1:
            self.incluirEstudantes()  # Chama o método incluirEstudantes.
        if self.opcao == 2:  # Se a opção selecionada for 2:
            self.listarEstudntes()  # Chama o método listarEstudntes.
        elif self.opcao in [3,4]:  # Se a opção selecionada for 3 ou 4:
            print("EM DESENVOLVIMENTO")  # Exibe uma mensagem indicando que a funcionalidade está em desenvolvimento.
        elif self.opcao == 9:  # Se a opção selecionada for 9:
            self.MenuPrincipal()  # Retorna ao menu principal.
        else:  # Se a opção não for válida:
            print(f"A opção {self.opcao} é inválida, tente novamente \n")  # Exibe uma mensagem de opção inválida.
            
    def incluirEstudantes(self):  # Define o método incluirEstudantes.
        print("\n===== INCLUSÃO =====\n")  # Título da seção de inclusão.
        while True:
            nomeEstudante = str(input("Informe o nome do estudante: "))  # Solicita o nome do estudante.
            if nomeEstudante.isalpha() :
                self.listaDeEstudantes.append(nomeEstudante)  # Adiciona o estudante à lista de estudantes.
                input("Precione ENTER para continuar\n\n")  # Aguarda a entrada do usuário.
                break
            else : 
                print("Insira um nome válido")
                
    def listarEstudntes(self):  # Define o método listarEstudntes.
        print("\n===== LISTAGEM =====\n")  # Título da seção de listagem.
        if self.listaDeEstudantes:  # Se houver estudantes na lista:
            for i, estudante in enumerate(self.listaDeEstudantes, 1):  # Itera sobre a lista de estudantes.
                print(f"{i}. {estudante}")  # Exibe o número e o nome do estudante.
            input("Precione ENTER para continuar\n\n")  # Aguarda a entrada do usuário.
        else:  # Se não houver estudantes cadastrados:
            print("Não há estudantes cadastrados.")  # Exibe uma mensagem indicando a ausência de estudantes.
        
app = MeuApp()  # Instancia um objeto da classe MeuApp.
app.MenuPrincipal()  # Chama o método MenuPrincipal para iniciar o programa.
