from flask import Flask, render_template
from classes.usuario import Usuario


app = Flask(__name__)

@app.route('/')
def home():
      artigo = Usuario()
      return render_template('home.html',titulo = 'Blog Pessoal', lista_artigos = artigo.read_all())


app.run(debug=True)