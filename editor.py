from leitorDeArguivo import GravadorJson  # Importando a classe GravadorJson do arquivo leitorDeArguivo.py
from validacao import *  # Importando todas as funções do arquivo validacao.py

class Editor:
    def __init__(self,) -> None:
        """Construtor da classe Editor.
        
        Inicializa a instância com um objeto da classe `GravadorJson`.
        """
        self.arquivo = GravadorJson()

    def incluirPessoa(self, entidade):
        """Inclui uma nova pessoa na lista.
        
        Args:
            entidade (str): Tipo de entidade a ser cadastrada ("estudante" ou "professor").
            
        Return: none
        """
        print("\n===== INCLUSÃO DE PESSOA =====\n")
        while True:
            try:
                # Validação do código da pessoa
                codigoPesoa = input(f"Insira o código do {entidade}: ")
                validar_codigo(codigoPesoa, entidade)
        
                # Validação do nome da pessoa
                nomePessoa = input(f"Insira o nome do {entidade}: ")
                validar_nome(nomePessoa, entidade)
                
                # Validação do CPF da pessoa
                cpf = input(f"Insira o CPF do {entidade}: ")
                validar_cpf(cpf, entidade)
        
                # Criação do dicionário com os dados da pessoa
                pessoa = {"codigo": codigoPesoa, "nome": nomePessoa,  "cpf": cpf}
                
                # Gravação da pessoa no arquivo JSON
                self.arquivo.escreve_a_json(pessoa, entidade)
                
                # Verificação se o usuário deseja cadastrar mais pessoas
                if input(f"Gostaria de cadastrar mais um {entidade}, pressione 'n' para parar: ") == "n":
                    break

            except ValueError as e:
                # Tratamento de exceções de validação
                print("Erro:", e)
                break

    def listarPessoa(self, entidade):
        """Lista todas as pessoas cadastradas.

        Args:
            entidade (str): Tipo de entidade a ser listada ("estudante" ou "professor").
            
        Return:
            None
        """
        print("\n===== LISTAGEM =====\n")
        try:
            # Leitura da lista de pessoas do arquivo JSON
            pessoas = self.arquivo.listar_json(entidade)
            if pessoas:
                # Impressão dos dados de cada pessoa
                for pessoa in pessoas:
                    print(f"Código: {pessoa['codigo']}, Nome: {pessoa['nome']}, CPF: {pessoa['cpf']}")
                input("Pressione ENTER para continuar\n\n")
            else:
                # Mensagem de aviso caso não existam pessoas cadastradas
                print(f"Não há {entidade} cadastrados.")
        except Exception as e:
             # Tratamento de exceções durante a leitura do arquivo
            print(f"Erro ao listar {entidade}")
            
    def editarPessoa(self, entidade):
        """Edita os dados de uma pessoa cadastrada.

        Args:
            entidade (str): Tipo de entidade a ser editada ("estudante" ou "professor").
            
        Return:
            None        
        """
        print("\n===== EDIÇÃO =====\n")
        
        # Leitura da lista de pessoas do arquivo JSON
        pessoas = self.arquivo.listar_json(entidade)
        if pessoas:
            # Solicitação do código da pessoa a ser editada
            codigoPessoa = input(f"Insira o código do {entidade} que deseja editar: ")
            for pessoa in pessoas:
                if pessoa['codigo'] == codigoPessoa:
                    # Impressão dos dados atuais da pessoa
                    print("Dados atuais:")
                    print(f"Nome: {pessoa['nome']}")
                    print(f"CPF: {pessoa['cpf']}\n")
                    try:
                        # Validação do novo nome da pessoa
                        novoNome = input(f"Insira o novo nome do {entidade}: ")
                        validar_nome(novoNome, entidade, pessoa['nome'])
                        
                        # Validação do novo CPF da pessoa
                        novoCpf = input(f"Insira o novo CPF do {entidade}: ")
                        validar_cpf(novoCpf, entidade, pessoa['cpf'])
                        
                        # Atualização dos dados da pessoa no dicionário
                        pessoa["nome"] = novoNome
                        pessoa["cpf"] = novoCpf
                        
                        # Atualização do conteúdo do arquivo JSON
                        self.arquivo.escreve_w_json(pessoas, entidade)
                        print(f"{entidade} atualizado com sucesso!")
                        
                        return
                    except ValueError as e:
                        # Tratamento de exceções de validação
                        print(e)
            # Mensagem de aviso caso o código da pessoa não seja encontrado
            print(f"não foi encontrado {entidade} com este codigo")
        # Mensagem de aviso caso não existam pessoas cadastradas
        else: print(f"Não há {entidade} cadastrados.")
                    
    def excluirPessoa(self, entidade):
        """Exclui uma pessoa cadastrada.

        Args:
            entidade (str): Tipo de entidade a ser excluída ("estudante" ou "professor").
            
        Return:
            None
        """
        print("\n===== EXCLUSÃO =====\n")        
        # Leitura da lista de pessoas do arquivo JSON
        pessoas = self.arquivo.listar_json(entidade)
        if pessoas:
            # Solicitação do código da pessoa a ser excluída
            codigoPessoa = input(f"Insira o código do {entidade} que deseja excluir: ")
            for pessoa in pessoas:
                if pessoa['codigo'] == codigoPessoa:
                    # Impressão dos dados atuais da pessoa
                    print("Dados atuais:")
                    print(f"Nome: {pessoa['nome']}")
                    print(f"CPF: {pessoa['cpf']}\n")
                    if input("Tem certesa (s).") == "s":
                        # Removendo a pessoa da lista
                        pessoas.remove(pessoa)

                        # Atualização do conteúdo do arquivo JSON
                        self.arquivo.escreve_w_json(pessoas, entidade)
                        return
                    else:
                        print("Processo cancelado")
                        return
            # Mensagem de aviso caso o código da pessoa não seja encontrado
            print(f"não foi encontrado {entidade} com este codigo")              
        else: print(f"Não há {entidade} cadastrados.")
                    
    def incluirDiciplina(self, entidade):
        """Inclui uma nova disciplina na lista.
        
        Args:
            entidade (str): Tipo de entidade a ser cadastrada ("disciplina").
            
        Return: none
        """
        print("\n===== INCLUSÃO DE DISCIPLINA =====\n")
        while True:
            try:
                # Validação do código da disciplina
                codigoDiciplina = input(f"Insira o código da {entidade}: ")
                validar_codigo(codigoDiciplina, entidade)
                
                # Validação do nome da disciplina
                nomeDiciplina = input(f"Insira o nome da {entidade}: ")
                validar_nome(nomeDiciplina, entidade)
                
                # Criação do dicionário com os dados da disciplina
                disciplina = {'codigo': codigoDiciplina, 'nome': nomeDiciplina}
                
                # Gravação da disciplina no arquivo JSON
                self.arquivo.escreve_a_json(disciplina, entidade)
                
                # Verificação se o usuário deseja cadastrar mais disciplinas
                if input(f"Gostaria de cadastrar mais uma {entidade}, pressione 'n' para parar: ") == "n":
                    break
            except ValueError as e:
                print('Erro:', e)
                
    def listarDiciplinas(self, entidade):
        """Lista todas as disciplinas cadastradas.

        Args:
            entidade (str): Tipo de entidade a ser listada ("disciplina").
            
        Return:
            None
        """
        print("\n===== LISTAGEM =====\n")
        try:
            # Leitura da lista de disciplinas do arquivo JSON
            disciplinas = self.arquivo.listar_json(entidade)
            if disciplinas:
                # Impressão dos dados de cada disciplina
                for disciplina in disciplinas:
                    print(f"Código: {disciplina['codigo']}, Nome: {disciplina['nome']}")
                input("Pressione ENTER para continuar\n\n")
            else:
                # Mensagem de aviso caso não existam disciplinas cadastradas
                print(f"Não há {entidade} cadastradas.")
        except Exception as e:
            # Tratamento de exceções durante a leitura do arquivo
            print(f"Erro ao listar {entidade}")
            
    def editarDiciplina(self, entidade):
        """Edita os dados de uma disciplina cadastrada.

        Args:
            entidade (str): Tipo de entidade a ser editada ("disciplina").
            
        Return:
            None        
        """
        print("\n===== EDIÇÃO =====\n")
        
        # Leitura da lista de disciplinas do arquivo JSON
        disciplinas = self.arquivo.listar_json(entidade)
        if disciplinas:
            # Solicitação do código da disciplina a ser editada
            codigoDiciplina = input(f"Insira o código da {entidade} que deseja editar: ")
            for disciplina in disciplinas:
                if disciplina['codigo'] == codigoDiciplina:
                    # Impressão dos dados atuais da disciplina
                    print("Dados atuais:")
                    print(f"Nome: {disciplina['nome']}")
                    try:
                        # Validação do novo nome da disciplina
                        novoNome = input(f"Insira o novo nome da {entidade}: ")
                        validar_nome(novoNome, entidade, disciplina['nome'])
                        
                        # Atualização do nome da disciplina no dicionário
                        disciplina["nome"] = novoNome
                        
                        # Atualização do conteúdo do arquivo JSON
                        self.arquivo.escreve_w_json(disciplinas, entidade)
                        print(f"{entidade} atualizada com sucesso!")
                        return
                    except ValueError as e:
                        # Tratamento de exceções de validação
                        print(e)
            # Mensagem de aviso caso o código da disciplina não seja encontrado
            print(f"Não foi encontrado {entidade} com este código")
        # Mensagem de aviso caso não existam disciplinas cadastradas
        else:
            print(f"Não há {entidade} cadastradas.")
        
    def excluirDiciplina(self, entidade):
        """Exclui uma disciplina cadastrada.

        Args:
            entidade (str): Tipo de entidade a ser excluída ("disciplina").
            
        Return:
            None
        """
        print("\n===== EXCLUSÃO =====\n")
        
        # Leitura da lista de disciplinas do arquivo JSON
        disciplinas = self.arquivo.listar_json(entidade)
        if disciplinas:
            # Solicitação do código da disciplina a ser excluída
            codigoDiciplina = input(f"Insira o código da {entidade} que deseja excluir: ")
            for disciplina in disciplinas:
                if disciplina['codigo'] == codigoDiciplina:
                    # Impressão dos dados atuais da disciplina
                    print("Dados atuais:")
                    print(f"Nome: {disciplina['nome']}")
                    if input("Tem certeza (s/n)? ") == "s":
                        # Remoção da disciplina da lista
                        disciplinas.remove(disciplina)

                        # Atualização do conteúdo do arquivo JSON
                        self.arquivo.escreve_w_json(disciplinas, entidade)
                        return
                    else:
                        print("Processo cancelado")
                        return
            # Mensagem de aviso caso o código da disciplina não seja encontrado
            print(f"Não foi encontrado {entidade} com este código")              
        # Mensagem de aviso caso não existam disciplinas cadastradas
        else:
            print(f"Não há {entidade} cadastradas.")
        
    def incluirTurma(self, entidade):
        """Inclui uma nova turma na lista.
        
        Args:
            entidade (str): Tipo de entidade a ser cadastrada ("turma").
            
        Return: none
        """
        print("\n===== INCLUSÃO DE TURMA =====\n")
        while True:
            try:
                # Validação do código da turma
                codigoTurma = input(f"Insira o código da {entidade}: ")
                validar_codigo(codigoTurma, entidade)
                
                # Validação do código do professor
                codigoProfessorTurma = input("Insira o código do professor: ")
                valida_professor(codigoProfessorTurma)
                
                # Validação do código da disciplina
                codigoDisciplinaTurma = input("Insira o código da disciplina: ")
                valida_disciplina(codigoDisciplinaTurma)
                
                # Criação do dicionário com os dados da turma
                turma = {'codigo': codigoTurma, 'codigoProfessor': codigoProfessorTurma, 'codigoDisciplina': codigoDisciplinaTurma}
                
                # Gravação da turma no arquivo JSON
                self.arquivo.escreve_a_json(turma, entidade)
                
                # Verificação se o usuário deseja cadastrar mais turmas
                if input(f"Gostaria de cadastrar mais uma {entidade}, pressione 'n' para parar: ") == "n":
                    break
            except ValueError as e:
                # Tratamento de exceções de validação
                print('Erro:', e)
                break
            except IndexError as e:
                # Tratamento de exceções de índice
                print('Erro:', e)
                break
            
    def listarTurmas(self, entidade):
        """Lista todas as turmas cadastradas.

        Args:
            entidade (str): Tipo de entidade a ser listada ("turma").
            
        Return:
            None
        """
        print("\n===== LISTAGEM =====\n")
        try:
            # Leitura da lista de turmas do arquivo JSON
            turmas = self.arquivo.listar_json(entidade)
            if turmas:
                # Impressão dos dados de cada turma
                for turma in turmas:
                    print(f"Código: {turma['codigo']}, Código professor: {turma['codigoProfessor']}, Código disciplina: {turma['codigoDisciplina']}")
                input("Pressione ENTER para continuar\n\n")
            else:
                # Mensagem de aviso caso não existam turmas cadastradas
                print(f"Não há {entidade} cadastradas.")
        except Exception as e:
            # Tratamento de exceções durante a leitura do arquivo
            print(f"Erro ao listar {entidade}")
            
    def editarTurma(self, entidade):
        """Edita os dados de uma turma cadastrada.

        Args:
            entidade (str): Tipo de entidade a ser editada ("turma").
            
        Return:
            None        
        """
        print("\n===== EDIÇÃO =====\n")
        turmas = self.arquivo.listar_json(entidade)
        
        if turmas:
            codigoTurma = input(f"Insira o código da {entidade} que deseja editar: ")
            for turma in turmas:
                if turma['codigo'] == codigoTurma:
                    # Impressão dos dados atuais da turma
                    print("Dados atuais:")
                    print(f"Código: {turma['codigo']}")
                    print(f"Código professor: {turma['codigoProfessor']}")
                    print(f"Código disciplina: {turma['codigoDisciplina']}")
                    try:
                        # Validação do novo código do professor
                        codigoProfessor = input(f"Insira o código do novo Professor: ")
                        valida_professor(codigoProfessor)
                        
                        # Validação do novo código da disciplina
                        codigoDisciplina = input(f"Insira o código da nova disciplina: ")
                        valida_disciplina(codigoDisciplina)
                        
                        # Atualização dos códigos da turma no dicionário
                        turma["codigoProfessor"] = codigoProfessor
                        turma["codigoDisciplina"] = codigoDisciplina
                        
                        # Atualização do conteúdo do arquivo JSON
                        self.arquivo.escreve_w_json(turmas, entidade)
                        print(f"{entidade} atualizada com sucesso!")
                        return
                    except ValueError as e:
                        # Tratamento de exceções de validação
                        print(e)
            # Mensagem de aviso caso o código da turma não seja encontrado
            print(f"Não foi encontrado {entidade} com este código")
        # Mensagem de aviso caso não existam turmas cadastradas
        else:
            print(f"Não há {entidade} cadastradas.")
        
    def excluirTurma(self, entidade):
        """Exclui uma turma cadastrada.

        Args:
            entidade (str): Tipo de entidade a ser excluída ("turma").
            
        Return:
            None
        """
        print("\n===== EXCLUSÃO =====\n")
        turmas = self.arquivo.listar_json(entidade)
        if turmas:
            codigoTurma = input(f"Insira o código da {entidade} que deseja excluir: ")
            for turma in turmas:
                if turma['codigo'] == codigoTurma:
                    # Impressão dos dados atuais da turma
                    print("Dados atuais:")
                    print(f"Código: {turma['codigo']}")
                    print(f"Código professor: {turma['codigoProfessor']}")
                    print(f"Código disciplina: {turma['codigoDisciplina']}")
                    if input("Tem certeza (s/n)? ") == "s":
                        # Remoção da turma da lista
                        turmas.remove(turma)

                        # Atualização do conteúdo do arquivo JSON
                        self.arquivo.escreve_w_json(turmas, entidade)
                        return
                    else:
                        print("Processo cancelado")
                        return
            # Mensagem de aviso caso o código da turma não seja encontrado
            print(f"Não foi encontrado {entidade} com este código")              
        # Mensagem de aviso caso não existam turmas cadastradas
        else:
            print(f"Não há {entidade} cadastradas.")
        
    def incluirMatricula(self, entidade):
        """Inclui uma nova matrícula na lista.
        
        Args:
            entidade (str): Tipo de entidade a ser cadastrada ("matrícula").
            
        Return: none
        """
        print("\n===== INCLUSÃO DE MATRÍCULA =====\n")
        while True:
            try:
                # Validação do código da matrícula
                codigoMatricula = input(f"Insira o código da {entidade}: ")
                validar_codigo(codigoMatricula, entidade)
                
                # Validação do código da turma
                codigoTurmaMatricula = input(f"Insira o código da turma: ")
                valida_turma(codigoTurmaMatricula)
                
                # Validação do código do estudante
                codigoEstudanteTurma = input(f"Insira o código do estudante: ")
                valida_estudante(codigoEstudanteTurma)
                
                # Criação do dicionário com os dados da matrícula
                matricula = {'codigo': codigoMatricula, 'codigoTurma': codigoTurmaMatricula, 'codigoEstudante': codigoEstudanteTurma}
                
                # Gravação da matrícula no arquivo JSON
                self.arquivo.escreve_a_json(matricula, entidade)
                
                # Verificação se o usuário deseja cadastrar mais matrículas
                if input(f"Gostaria de cadastrar mais uma {entidade}, pressione 'n' para parar: ") == "n":
                    break
            except ValueError as e:
                # Tratamento de exceções de validação
                print('Erro:', e)
                break
            except IndexError as e:
                # Tratamento de exceções de índice
                print('Erro:', e)
                break
            
    def listarMatriculas(self, entidade):
        """Lista todas as matrículas cadastradas.

        Args:
            entidade (str): Tipo de entidade a ser listada ("matrícula").
            
        Return:
            None
        """
        print("\n===== LISTAGEM =====\n")
        try:
            # Leitura da lista de matrículas do arquivo JSON
            matriculas = self.arquivo.listar_json(entidade)
            if matriculas:
                # Impressão dos dados de cada matrícula
                for matricula in matriculas:
                    print(f"Código: {matricula['codigo']}, Código Turma: {matricula['codigoTurma']}, Código Estudante: {matricula['codigoEstudante']}")
                input("Pressione ENTER para continuar\n\n")
            else:
                # Mensagem de aviso caso não existam matrículas cadastradas
                print(f"Não há {entidade} cadastradas.")
        except Exception as e:
            # Tratamento de exceções durante a leitura do arquivo
            print(f"Erro ao listar {entidade}")
    
    def editarMatricula(self, entidade):
        """Edita os dados de uma matrícula cadastrada.

        Args:
            entidade (str): Tipo de entidade a ser editada ("matrícula").
            
        Return:
            None        
        """
        print("\n===== EDIÇÃO =====\n")
        matriculas = self.arquivo.listar_json(entidade)
        
        if matriculas:
            codigoMatricula = input(f"Insira o código da {entidade} que deseja editar: ")
            for matricula in matriculas:
                if matricula['codigo'] == codigoMatricula:
                    # Impressão dos dados atuais da matrícula
                    print("Dados atuais:")
                    print(f"Código: {matricula['codigo']}")
                    print(f"Código Turma:  {matricula['codigoTurma']}")
                    print(f"Código Estudante: {matricula['codigoEstudante']}")
                    try:
                        # Validação do novo código da turma
                        codigoTurma = input(f"Insira o código da nova turma: ")
                        valida_turma(codigoTurma)
                        
                        # Validação do novo código do estudante
                        codigoEstudante = input(f"Insira o código do novo estudante: ")
                        valida_estudante(codigoEstudante)
                        
                        # Atualização dos códigos da matrícula no dicionário
                        matricula["codigoTurma"] = codigoTurma
                        matricula["codigoEstudante"] = codigoEstudante
                        
                        # Atualização do conteúdo do arquivo JSON
                        self.arquivo.escreve_w_json(matriculas, entidade)
                        print(f"{entidade} atualizada com sucesso!")
                        return
                    except ValueError as e:
                        # Tratamento de exceções de validação
                        print(e)
            # Mensagem de aviso caso o código da matrícula não seja encontrado
            print(f"Não foi encontrado {entidade} com este código")
        # Mensagem de aviso caso não existam matrículas cadastradas
        else:
            print(f"Não há {entidade} cadastradas.")
        
    def excluirMatricula(self, entidade):
        """Exclui uma matrícula cadastrada.

        Args:
            entidade (str): Tipo de entidade a ser excluída ("matrícula").
            
        Return:
            None
        """
        print("\n===== EXCLUSÃO =====\n")
        matriculas = self.arquivo.listar_json(entidade)
        if matriculas:
            codigoMatricula = input(f"Insira o código da {entidade} que deseja excluir: ")
            for matricula in matriculas:
                if matricula['codigo'] == codigoMatricula:
                    # Impressão dos dados atuais da matrícula
                    print("Dados atuais:")
                    print(f"Código: {matricula['codigo']}")
                    print(f"Código Turma:  {matricula['codigoTurma']}")
                    print(f"Código Estudante: {matricula['codigoEstudante']}")
                    if input("Tem certeza (s/n)? ") == "s":
                        # Remoção da matrícula da lista
                        matriculas.remove(matricula)

                        # Atualização do conteúdo do arquivo JSON
                        self.arquivo.escreve_w_json(matriculas, entidade)
                        return
                    else:
                        print("Processo cancelado")
                        return
            # Mensagem de aviso caso o código da matrícula não seja encontrado
            print(f"Não foi encontrado {entidade} com este código")              
        # Mensagem de aviso caso não existam matrículas cadastradas
        else:
            print(f"Não há {entidade} cadastradas.")
                    