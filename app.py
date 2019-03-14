from flask import Flask, jsonify
from flask import request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

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
    text = request.form.getlist('tarea')

    print(keys)
    print(text)
    
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

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
