from flask import Flask, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250))

    def __repr__(self) -> str:
        return '<Task %r>' % self.title


db.create_all()  # Création et initialisation de la BD


all_tasks = []


@app.route('/')
def index():
    # Obtenit toutes les taches dans la base de données de l'objet Task
    all_tasks = Task.query.all()
    return render_template('index.html', tasks=all_tasks)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        task_title = request.form['title']  # obtenir le titre du formulaire
        # obtenir la description du formulaire
        task_description = request.form['description']
        new_task = Task(title=task_title, description=task_description)
        db.session.add(new_task)  # Enregostrer une tache
        db.session.commit()  # Enregistrer une tache
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete')
def delete():
    task_id = request.args.get('id')
    delete_task = Task.query.filter_by(
        id=task_id).first()  # Obtenir une tâche par son ID
    db.session.delete(delete_task)  # Supprimer cette tâche
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    task_id = request.args.get('id')
    update_task = Task.query.get(task_id)
    if request.method == 'POST':
        update_task.title = request.form['title']
        update_task.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', task=update_task)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
