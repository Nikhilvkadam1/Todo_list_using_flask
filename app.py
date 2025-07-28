from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# -------------------- Models --------------------
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Todo {self.id} - {self.task}>'

# -------------------- Routes --------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_content = request.form["task"].strip()
        task_desc = request.form.get("description", "").strip()

        if task_content:
            new_task = Todo(task=task_content, description=task_desc)
            db.session.add(new_task)
            db.session.commit()
        return redirect("/")

    tasks = Todo.query.order_by(Todo.date_created.desc()).all()
    return render_template("index.html", tasks=tasks)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    todo = Todo.query.get_or_404(id)

    if request.method == "POST":
        task = request.form['task']
        description = request.form['description']
        todo.task = task
        todo.description = description
        db.session.commit()  # No need to use db.session.add(todo) again
        return redirect('/')  # Redirect to avoid form resubmission

    return render_template('update.html', todo=todo)


@app.route("/delete/<int:id>")
def delete(id):
    task = Todo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")

@app.route("/complete/<int:id>")
def complete(id):
    task = Todo.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect("/")

@app.route("/show")
def show_query():
    all_todos = Todo.query.all()
    print("\n📋 All Todos:")
    for todo in all_todos:
        print(todo)
    return "✅ Printed all todos in the terminal."

# -------------------- Main --------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("✅ Database recreated successfully.")
    app.run(port=8000, debug=True)
