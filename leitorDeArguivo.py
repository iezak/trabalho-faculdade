import json  # Importando o módulo json para manipulação de arquivos JSON

class GravadorJson:
        
    def escreve_a_json(self, entidade, nomeArquivo):
        """Escreve uma nova entidade no arquivo JSON.
        
        Adiciona a nova entidade à lista de entidades existente e escreve no arquivo JSON.
        
        Args:
            entidade (dict): Dados da entidade a ser escrita no arquivo.
            nomeArquivo (str): Nome do arquivo JSON onde a entidade será escrita.
        """
        # Obtém a lista de entidades do arquivo JSON
        listaEntidade = self.listar_json(nomeArquivo)
        
        # Adiciona a nova entidade à lista de entidades
        listaEntidade.append(entidade)
        
        # Escreve a lista atualizada de entidades no arquivo JSON
        with open(nomeArquivo+".json", 'w', encoding='utf-8') as w:
            json.dump(listaEntidade, w)  # Salva a lista de entidades no arquivo JSON
            
    def escreve_w_json(self, entidades, nomeArquivo):
        """Escreve a lista de entidades no arquivo JSON.
        
        Substitui o conteúdo do arquivo pelo conteúdo da lista de entidades.
        
        Args:
            entidades (list): Lista de entidades a ser escrita no arquivo.
            nomeArquivo (str): Nome do arquivo JSON onde as entidades serão escritas.
        """
        with open(nomeArquivo+".json", 'w', encoding='utf-8') as w:
            json.dump(entidades, w)

    def listar_json(self, nomeArquivo):
        """Lista as entidades do arquivo JSON.
        
        Lê o conteúdo do arquivo JSON e retorna a lista de entidades.
        
        Args:
            nomeArquivo (str): Nome do arquivo JSON a ser lido.
        
        Returns:
            list: Lista de entidades do arquivo JSON.
        """
        try:
            with open(nomeArquivo+".json", "r", encoding='utf-8') as r:
                return json.load(r)  # Retorna a lista de entidades do arquivo JSON
        except FileNotFoundError:
            return[]  # Retorna uma lista vazia se o arquivo não for encontrado
        except json.decoder.JSONDecodeError:
            return []
