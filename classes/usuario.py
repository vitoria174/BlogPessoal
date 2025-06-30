import json

class Usuario:
      def __init__(self):
            self.caminho_json = 'dados/arquivo.json'
      
      def open(self):
            with open(self.caminho_json,'r') as file:
                  dados = json.load(file)
                  return dados
                  
      def read_all(self):
            return self.open()
      
      def read_id(self):
            artigos = self.open()
            artigo_id = int(input('Id do artigo: '))
            
            for indice_artigo, chave_artigo in enumerate(artigos):
                  if chave_artigo['id'] == artigo_id:
                        return chave_artigo
                  
