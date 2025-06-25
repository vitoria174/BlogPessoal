class Admin:
      
      def __init__(self, login = 'admin', senha = 'admin123'):
            self.login = login
            self.senha = senha
      
      def autenticacao(self, login, senha):
            if self.login == login and self.senha == senha:
                  print(f'Bem vindo {self.login}')
            else:
                  print(f'Login ou Senha incorreta')
            
        