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
      
      def read_id(self,id):
            artigos = self.open()
            lista =[]
            
            for a in  artigos:
                  if a['id'] == id:
                        titulo = a['Titulo']
                        descricao = a['Descricao']
                        data_criada = a['Data']
                        dict ={
                              'titulo':titulo,
                              'descricao':descricao,
                              'data':data_criada
                        }
                        lista.append(dict)
                        return lista
