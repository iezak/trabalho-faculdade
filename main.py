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

    def incluirEstudantes(self):
        # Método para incluir estudantes na lista
        print("\n===== INCLUSÃO =====\n")
        while True:
            codigoEstudante = input("Insira o codigo do estudante: ")
            nomeEstudante = input("Insira o nome do estudante: ")
            cpfEstudante = input("Insira o CPF do estudante: ")
            
            # Verifica se o nome, código e CPF são válidos e únicos
            if nomeEstudante.replace(" ", "").isalpha() and codigoEstudante.isdigit() and cpfEstudante.isdigit():
                if codigoEstudante not in self.estudantes and cpfEstudante not in [dados['cpf'] for dados in self.estudantes.values()]:
                    self.estudantes[codigoEstudante] = {'nome': nomeEstudante, 'cpf': cpfEstudante}
                    if input("Gostaria de cadastrar mais um estudante (s/n)") == "n":
                        break
                else:
                    print("Código ou CPF já cadastrado")
            else:
                print("Erro de caracter, tente novamente.")

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
            if codigo.isdigit():
                if codigo in self.estudantes:
                    print("Digite os novos detalhes do estudante:")
                    novoNome = input("Novo nome (deixe em branco para manter o mesmo): ")
                    novoCPF = input("Novo CPF (deixe em branco para manter o mesmo): ")

                    # Se o novo CPF for diferente do CPF atual e já estiver associado a outro estudante, mostra um erro
                    if novoCPF.strip() == "":
                        novoCPF = self.estudantes[codigo]['cpf']
                    if novoNome.strip() == "":
                        novoNome = self.estudantes[codigo]['nome']
                    elif novoCPF != self.estudantes[codigo]['cpf'] and novoCPF in [dados['cpf'] for dados in self.estudantes.values() if dados['cpf'] != self.estudantes[codigo]['cpf']]:
                        print("Erro: O CPF fornecido já está associado a outro estudante.")
                        continue

                    # Atualiza os dados do estudante
                    self.estudantes[codigo]['nome'] = novoNome
                    self.estudantes[codigo]['cpf'] = novoCPF
                    print(f"Dados do estudante com código {codigo} atualizados com sucesso.")
                    break
                else:
                    print(f"Estudante com código {codigo} não encontrado.")
                    print("Não há estudantes cadastrados.")
                    break
            else:
                print("Erro: O código deve ser numérico.")

# Instanciação da classe e início do aplicativo
app = MeuApp()
app.MenuPrincipal()