from flask import Flask, render_template,request
from classes.usuario import Usuario


app = Flask(__name__)
artigo = Usuario()

@app.route('/')
def home():
      
      return render_template('home.html',titulo = 'Blog Pessoal', lista_artigos = artigo.read_all())

@app.route('/artigo/<int:id>')
def read_id(id):
      return render_template('post_id.html', titulo = 'Postagem', postagem = artigo.read_id(id))

@app.route('/admin')
def login():
      login = request.get([form = ])

app.run(debug=True)