from flask import Flask, jsonify
from flask import request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

from push import enviar_push


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mmyrzeixfbekwd:1ca12c40d966184e080e29060717d33255a473227a7ce27ffa267cd62d077bb6@ec2-75-101-131-79.compute-1.amazonaws.com:5432/d37tphbbo7344p'

db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = "persons"
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(255), unique=True)
  key = db.Column(db.String(255), unique=True)

  def __init__(self, nome, key):
    self.nome = nome  
    self.key = key  

@app.route("/", methods=['GET', 'POST'])
def hello():
  if request.method == 'POST':
    keys = request.form.getlist('cbox')
    text = request.form.get('tarea')
    titulo = request.form.get('input')

    print(keys)
    print(titulo)
    print(text)

    enviar_push(keys, titulo, text)
    
    return redirect('/')
  else:
    lp = Person.query.all()

    return render_template('main.html', pessoas=lp)

@app.route("/adicionar", methods=['POST'])
def add_pessoa():
  p = Person(request.json['nome'], request.json['key'])
  db.session.add(p)
  db.session.commit()

  return jsonify({'status': 'ok'}), 201

@app.route("/remover/<nome>")
def remove_pessoa(nome):
  p = Person.query.filter_by(nome=nome).first()
  db.session.delete(p)
  db.session.commit()

  return redirect('/')
if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
