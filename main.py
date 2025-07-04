from flask import Flask, render_template,request,redirect,flash
from classes.usuario import Usuario
from classes.admin import Admin
from classes.modelo import Artigo


app = Flask(__name__)
app.secret_key='minha_palavra_secreta'
acesso = Usuario()
admin = Admin()
artigo = Artigo()

@app.route('/')
@app.route('/home')
def home():
      
      return render_template('home.html',titulo = 'Blog Pessoal', lista_artigos = acesso.read_all())

@app.route('/artigo/<int:id>')
def read_id(id):
      return render_template('post_id.html', titulo = 'Postagem', postagem = acesso.read_id(id))

@app.route('/login')
def login():
      return render_template('login.html')

@app.route('/autenticacao', methods = ['POST',])
def autenticacao():
      login = request.form['login']
      senha = request.form['password']
      
      if admin.autenticacao(login, senha):
            return render_template('admin.html', titulo = 'Aba Admin', ler = artigo.read())
      
      else:
            flash('login ou senha incorreta')
            return redirect('/login')
      
@app.route('/new')
def new():
      return render_template('new_article.html', titulo= 'Novo Artigo')

@app.route('/publicar', methods = ['POST',])
def publicar():
      titulo = request.form['titulo']
      descricao = request.form['descricao']
      
      artigo.create(titulo, descricao)
      return redirect('/autenticacao')
      
app.run(debug=True)