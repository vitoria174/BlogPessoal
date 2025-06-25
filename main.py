import json

class Usuario:
      def __init__(self, caminho_json):
            self.caminho_json = caminho_json
      
      def open(self):
            with open(self.caminho_json,'r') as file:
                  dados = json.load(file)
                  return dados
                  
      def read_all(self):
            artigos = self.open()
            for artigos in artigos:
                  print(artigos)
                  
a=Usuario('arquivo.json')
