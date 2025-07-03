class Admin:
      
      def __init__(self, login = 'admin', senha = 'admin123'):
            self.login = login
            self.senha = senha
      
      def autenticacao(self, login, senha):
            if self.login == login and self.senha == senha:
                  return True
            else:
                  return False
            
        