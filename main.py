# Vinicius Medeiros Iezak
# Curso: Raciocínio Computacional

class MeuApp:
    def __init__(self) -> None:
        # Inicialização da classe
        self.opcao = 0
        self.estudantes = {}  # Dicionário para armazenar os estudantes

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
            # Opções do menu de estudantes
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
                print("Opção invalida, entre com um número ")

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
        elif self.opcao == 2:
            self.listarEstudantes()
        elif self.opcao == 3:
            self.EditarEstudante()
        elif self.opcao == 4:
            self.ExcluirEstudante()
        elif self.opcao == 9:
            self.MenuPrincipal()
        else:
            print(f"A opção {self.opcao} é inválida, tente novamente \n")
            
    def validar_dados_estudante(self, nome, cpf, codigo=None):
        if not (nome.replace(" ", "").isalpha() and cpf.isdigit()):
            print("Erro na digitação, tente novamente.")
            return False
        if codigo is not None and not codigo.isdigit():
            print("Código deve ser um número inteiro.")
            return False
        if codigo is not None and codigo in self.estudantes:
            print(f"Codigo({codigo} já cadastrado.)")
            return False
        if cpf in [dados['cpf'] for dados in self.estudantes.values()]:
            print(f"CPF({cpf} já cadastrado.)")
            return False
        return True

    def incluirEstudantes(self):
        # Método para incluir estudantes na lista
        print("\n===== INCLUSÃO =====\n")
        while True:
            codigoEstudante = input("Insira o codigo do estudante: ")
            nomeEstudante = input("Insira o nome do estudante: ")
            cpfEstudante = input("Insira o CPF do estudante: ")
            
            if self.validar_dados_estudante(nomeEstudante, codigoEstudante, cpfEstudante):
            
                self.estudantes[codigoEstudante] = {'nome': nomeEstudante, 'cpf': cpfEstudante}
                if input("Gostaria de cadastrar mais um estudante (s/n)") == "n":
                    break
            
    def listarEstudantes(self):
        # Método para listar estudantes cadastrados
        print("\n===== LISTAGEM =====\n")
        if self.estudantes:
            for codigo, dados in self.estudantes.items():
                print(f"Código: {codigo}, Nome: {dados['nome']}, CPF: {dados['cpf']}")
            input("Precione ENTER para continuar\n\n")
        else:
            print("Não há estudantes cadastrados.")
    
    def ExcluirEstudante(self):
        # Método para excluir um estudante
        print("\n===== EXCLUSÃO =====\n")
        while True:
            codigo = input("Insira o código do estudante para a exclusão: ")
            if codigo in self.estudantes:
                self.estudantes.pop(codigo)
                input("Precione ENTER para continuar\n\n")
                break
            else:
                print(f"Estudante com código {codigo} não encontrado.")
                print("Não há estudantes cadastrados.")
    
    def EditarEstudante(self):
    # Método para editar os detalhes de um estudante
        print("\n===== EDIÇÃO =====\n")
        while True:
            codigo = input("Insira o código do estudante para a edição: ")
            estudante = self.estudantes.get(codigo)
            if estudante:
                print("Digite os novos dados do estudante.")
                novoNome = input(f"Novo nome ({estudante['nome']}): ").strip() or estudante['nome']
                novoCpf = input(f"Novo cpf ({estudante['cpf']}): ").strip() or estudante['cpf']
                
                if self.validar_dados_estudante(novoNome, novoCpf):
                    # Atualiza os dados do estudante
                    estudante['nome'] = novoNome
                    estudante['cpf'] = novoCpf
                    print(f"Dados do estudante com código {codigo} atualizados com sucesso.")
                    break
            else:
                print("Estudante não encontrado. Verifique se digitou corretamente o código.")
                
                
# Instanciação da classe e início do aplicativo
app = MeuApp()
app.MenuPrincipal()