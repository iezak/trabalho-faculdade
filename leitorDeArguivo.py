import json  # Importando o módulo json para manipulação de arquivos JSON

class GravadorJson:
        
    def escreve_json(self, estudante):
        # Método para escrever um estudante no arquivo JSON
        # Obtém a lista de estudantes do arquivo JSON
        estudantes = self.listar_json()
        
        # Adiciona o novo estudante à lista de estudantes
        estudantes.append(estudante)
        
        # Escreve a lista atualizada de estudantes no arquivo JSON
        with open("estudante.json", 'w', encoding='utf-8') as w:
            json.dump(estudantes, w)  # Salva a lista de estudantes no arquivo JSON

    def listar_json(self):
        # Método para listar os estudantes do arquivo JSON
        try:
            with open("estudante.json", "r", encoding='utf-8') as r:
                return json.load(r)  # Retorna a lista de estudantes do arquivo JSON
        except FileNotFoundError:
            return[]  # Retorna uma lista vazia se o arquivo não for encontrado