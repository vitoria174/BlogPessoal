import os
import json

arquivo_json = "arquivo.json"
class Artigo():
      def __init__(self):
            self.artigo = arquivo_json
            self.dados = []
            
      def load(self):
            if os.path.exists(self.artigo):
                  with open(self.artigo, 'r') as file:
                       self.dados =  json.load(file)
            else:
                  self.dados = []
                  self.save()
      
      def save(self):
            with open(self.artigo, 'w') as file:
                  json.dump(self.dados, file, indent=4)
                  
      def create(self):
            dado = {
                  'chave1' : 'valor1'
            }
            self.dados.append(dado)
            self.save()
                        
a = Artigo()
a.load()
a.create()
a.create()
a.create()
a.load()