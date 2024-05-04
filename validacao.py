# Importa a classe GravadorJson do módulo leitorDeArguivo
from leitorDeArguivo import GravadorJson

# Instancia um objeto GravadorJson para lidar com operações de leitura e escrita de JSON
arquivo = GravadorJson()

# Obtém a lista de estudantes do arquivo JSON


# Função para validar o nome do estudante
def validar_nome(nome, entidade, nome_original=None):
    """Valida o nome da entidade.
    
    Verifica se o nome é válido e se não está duplicado na lista de entidades.
    
    Args:
        nome (str): Nome da entidade a ser validado.
        entidade (str): Tipo de entidade a ser validada.
        nome_original (str, optional): Nome original da entidade. Usado para atualização de dados.
        
    Raises:
        ValueError: Se o nome for vazio, não for composto apenas por letras ou já estiver cadastrado.
    """
    pessoas = arquivo.listar_json(entidade)

    if nome == nome_original:
        return

    if not nome:
        raise ValueError("O nome não pode ser vazio.")

    if not nome.replace(" ", "").isalpha():
        raise ValueError("O nome deve conter apenas letras.")

    for pessoa in pessoas:
        if pessoa['nome'] == nome:
            raise ValueError("Este nome já está cadastrado.")

# Função para validar o código do estudante
def validar_codigo(codigo, entidade):
    """Valida o código da entidade.
    
    Verifica se o código é válido e se não está duplicado na lista de entidades.
    
    Args:
        codigo (str): Código da entidade a ser validado.
        entidade (str): Tipo de entidade a ser validada.
        
    Raises:
        ValueError: Se o código for vazio, não for um número inteiro ou já estiver cadastrado.
    """
    pessoas = arquivo.listar_json(entidade)
    
    if not codigo:
        raise ValueError("O código não pode ser vazio.")
    
    if not codigo.isdigit():
        raise ValueError("O código deve ser um número inteiro.")
    
    for pessoa in pessoas:
        if pessoa['codigo'] == codigo:
            raise ValueError("Este código já está cadastrado.")

# Função para validar o CPF do estudante
def validar_cpf(cpf, entidade, cpf_original=None):
    """Valida o CPF da entidade.
    
    Verifica se o CPF é válido e se não está duplicado na lista de entidades.
    
    Args:
        cpf (str): CPF da entidade a ser validado.
        entidade (str): Tipo de entidade a ser validada.
        cpf_original (str, optional): CPF original da entidade. Usado para atualização de dados.
        
    Raises:
        ValueError: Se o CPF for vazio, não for um número inteiro, não tiver 11 dígitos ou já estiver cadastrado.
    """
    pessoas = arquivo.listar_json(entidade)
    
    if cpf == cpf_original:
        return

    if not cpf:
        raise ValueError("O CPF não pode ser vazio.")
    
    if not cpf.isdigit():
        raise ValueError("O CPF deve ser um número inteiro.")
    
    if len(cpf) != 11:
        raise ValueError("O CPF deve ter 11 dígitos.")
    
    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            raise ValueError("Este CPF já está cadastrado.")
        
def valida_professor(codigo):
    """Valida o código do professor.
    
    Verifica se o código do professor é um número inteiro válido e se está cadastrado na lista de professores.
    
    Args:
        codigo (str): Código do professor a ser validado.
        
    Raises:
        ValueError: Se o código não for um número inteiro ou não estiver cadastrado na lista de professores.
        IndexError: Se não for encontrado um professor cadastrado com o código fornecido.
    """
    professores = arquivo.listar_json('professor')
    
    if not codigo.isdigit():
        raise ValueError("O código deve ser um número inteiro.")
    
    for professor in professores:
        if codigo == professor['codigo']:
            return
        
    raise IndexError(f"Não foi encontrado um professor cadastrado com o código {codigo}")
    
def valida_disciplina(codigo):
    """Valida o código da disciplina.
    
    Verifica se o código da disciplina é um número inteiro válido e se está cadastrado na lista de disciplinas.
    
    Args:
        codigo (str): Código da disciplina a ser validado.
        
    Raises:
        ValueError: Se o código não for um número inteiro ou não estiver cadastrado na lista de disciplinas.
        IndexError: Se não for encontrada uma disciplina cadastrada com o código fornecido.
    """
    disciplinas = arquivo.listar_json('disciplina')
    
    if not codigo.isdigit():
        raise ValueError("O código deve ser um número inteiro.")
    
    for disciplina in disciplinas:
        if codigo == disciplina['codigo']:
            return
    raise IndexError(f"Não foi encontrada uma disciplina cadastrada com o código {codigo}")

def valida_turma(codigo):
    """Valida o código da turma.
    
    Verifica se o código da turma é um número inteiro válido e se está cadastrado na lista de turmas.
    
    Args:
        codigo (str): Código da turma a ser validado.
        
    Raises:
        ValueError: Se o código não for um número inteiro ou não estiver cadastrado na lista de turmas.
        IndexError: Se não for encontrada uma turma cadastrada com o código fornecido.
    """
    turmas = arquivo.listar_json('turma')
    
    if not codigo.isdigit():
        raise ValueError("O código deve ser um número inteiro.")
    
    for turma in turmas:
        if codigo == turma['codigo']:
            return
    raise IndexError(f"Não foi encontrada uma turma cadastrada com o código {codigo}")

def valida_estudante(codigo):
    """Valida o código do estudante.
    
    Verifica se o código do estudante é um número inteiro válido e se está cadastrado na lista de estudantes.
    
    Args:
        codigo (str): Código do estudante a ser validado.
        
    Raises:
        ValueError: Se o código não for um número inteiro ou não estiver cadastrado na lista de estudantes.
        IndexError: Se não for encontrado um estudante cadastrado com o código fornecido.
    """
    estudantes = arquivo.listar_json('estudante')
    
    if not codigo.isdigit():
        raise ValueError("O código deve ser um número inteiro.")
    
    for estudante in estudantes:
        if codigo == estudante['codigo']:
            return
    raise IndexError(f"Não foi encontrado um estudante cadastrado com o código {codigo}")
