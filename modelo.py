import os
import json
import datetime

arquivo_json = "arquivo.json" #arquivo json que sera criado

#classe onde o administrador criar, atualizara e deletarar os artigos.
class Artigo():
      def __init__(self):
            self.artigo = arquivo_json
            self.dados = []
      
      #metodo para ler o arquivo json
      def load(self):
            if os.path.exists(self.artigo):
                  with open(self.artigo, 'r') as file:
                       self.dados =  json.load(file)
            else:
                  self.dados = []
                  self.save()
      
      #metodo para salvar artigos no json
      def save(self):
            with open(self.artigo, 'w') as file:
                  json.dump(self.dados, file, indent=4)
      
      #Função para criar artigos          
      def create(self):
            titulo = str(input('Titulo: '))
            descricao = str(input('Descricao: '))
            
            dado = {
                  'id':len(self.dados)+1,
                  'Titulo':titulo,
                  'Descricao':descricao,
                  'Data':str(datetime.date.today())
            }
            
            self.dados.append(dado)
            self.save()
      
      #Leitura dos artigos  
      def read(self):
            for i in self.dados:
                  print(i)
                  
      #metodo de atualizacao dos artigos
      def update(self):
            update_id = int(input('Digite o id que deseja atualizar: '))
            
            for indice, chave in enumerate(self.dados):
                  if chave['id'] == update_id:
                        chave['Titulo'] = str(input('Titulo novo: '))
                        chave['Descricao'] = str(input('Descricao: '))
                        chave['Data'] = str(datetime.date.today())
                        self.save()
                        
      def delete(self):
            delete_id = int(input('Id que deseja deletar: '))
            
            for indice, id_chave in enumerate(self.dados):
                  if delete_id == id_chave['id']:
                       del self.dados[indice]
                       self.save()
                        
