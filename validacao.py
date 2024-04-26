# Importa a classe GravadorJson do módulo leitorDeArguivo
from leitorDeArguivo import GravadorJson

# Instancia um objeto GravadorJson para lidar com operações de leitura e escrita de JSON
arquivo = GravadorJson()

# Obtém a lista de estudantes do arquivo JSON
estudantes = arquivo.listar_json()

# Função para validar o nome do estudante
def validar_nome(nome):
    try:
        # Verifica se o nome contém apenas letras e espaços
        if not nome.replace(" ", "").isalpha():
            raise ValueError("O nome deve conter apenas letras.")
        
        # Verifica se o nome já está presente na lista de estudantes
        for estudante in estudantes:
            if estudante['nome'] == nome:
                raise ValueError("Este nome já está cadastrado.")
        
        # Retorna True se a validação for bem-sucedida, junto com None para indicar a ausência de erros
        return True, None
    
    except ValueError as e:
        # Retorna False em caso de erro, junto com a mensagem de erro convertida para string
        return False, str(e)

# Função para validar o código do estudante
def validar_codigo(codigo):
    try:
        # Verifica se o código é composto apenas por dígitos
        if not codigo.isdigit():
            raise ValueError("O código deve ser um número inteiro.")
        
        # Verifica se o código já está presente na lista de estudantes
        for estudante in estudantes:
            if estudante['codigo'] == codigo:
                raise ValueError("Este código já está cadastrado.")
            
        # Retorna True se a validação for bem-sucedida, junto com None para indicar a ausência de erros
        return True, None
    
    except ValueError as e:
        # Retorna False em caso de erro, junto com a mensagem de erro convertida para string
        return False, str(e)

# Função para validar o CPF do estudante
def validar_cpf(cpf):
    try:
        # Verifica se o CPF é composto apenas por dígitos
        if not cpf.isdigit():
            raise ValueError("O CPF deve ser um número inteiro.")
        
        # Verifica se o CPF já está presente na lista de estudantes
        for estudante in estudantes:
            if estudante['cpf'] == cpf:
                raise ValueError("Este CPF já está cadastrado.")
            
        # Retorna True se a validação for bem-sucedida, junto com None para indicar a ausência de erros
        return True, None
    
    except ValueError as e:
        # Retorna False em caso de erro, junto com a mensagem de erro convertida para string
        return False, str(e)