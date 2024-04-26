from leitorDeArguivo import GravadorJson  # Importando a classe GravadorJson do arquivo leitorDeArguivo.py
from validacao import *  # Importando todas as funções do arquivo validacao.py

class estudanteClass:
    def __init__(self) -> None:
        self.arquivo = GravadorJson()  # Instanciando a classe GravadorJson

    def incluirEstudantes(self):
        # Método para incluir estudantes na lista
        print("\n===== INCLUSÃO =====\n")
        while True:
            try:
                # Solicitação do código do estudante
                codigoEstudante = input("Insira o código do estudante: ")
                # Validação do código
                validacao_codigo, erro_codigo = validar_codigo(codigoEstudante)
                if not validacao_codigo:
                    raise ValueError(erro_codigo)

                # Solicitação do nome do estudante
                nomeEstudante = input("Insira o nome do estudante: ")
                # Validação do nome
                validacao_nome, erro_nome = validar_nome(nomeEstudante)
                if not validacao_nome:
                    raise ValueError(erro_nome)

                # Solicitação do CPF do estudante
                cpfEstudante = input("Insira o CPF do estudante: ")
                # Validação do CPF
                validacao_cpf, erro_cpf = validar_cpf(cpfEstudante)
                if not validacao_cpf:
                    raise ValueError(erro_cpf)

                # Criação do dicionário representando o estudante
                estudante = {"codigo": codigoEstudante, "nome": nomeEstudante,  "cpf": cpfEstudante}

                # Chamada do método para escrever o estudante no arquivo JSON
                self.arquivo.escreve_json(estudante)

                # Verificação se o usuário deseja cadastrar mais um estudante
                if input("Gostaria de cadastrar mais um estudante, pressione 'n' para parar: ") == "n":
                    break

            except ValueError as e:
                print("Erro:", e)

    def listarEstudantes(self):
        # Método para listar estudantes cadastrados
        print("\n===== LISTAGEM =====\n")
        try:
            # Chamada do método para listar os estudantes do arquivo JSON
            estudantes = self.arquivo.listar_json()
            if estudantes:
                # Impressão dos estudantes
                for estudante in estudantes:
                    print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")
                input("Pressione ENTER para continuar\n\n")
            else:
                print("Não há estudantes cadastrados.")
        except Exception as e:
            print("Erro ao listar estudantes")