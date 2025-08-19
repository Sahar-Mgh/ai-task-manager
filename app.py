from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# --- DATABASE CONFIGURATION ---
# Set the location of the database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Create the database instance
db = SQLAlchemy(app)

# --- DATABASE MODEL ---
# This class defines the structure of our 'task' table in the database
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# --- Create the database file and table(s) ---
# This needs to run once to create the tasks.db file
with app.app_context():
    db.create_all()

# --- ROUTES ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_task_text = request.form.get('task')
        if new_task_text:
            # Create a new Task object
            new_task = Task(text=new_task_text, done=False)
            # Add it to the database session and commit
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('index'))
    
    # Query the database for all tasks
    all_tasks = Task.query.all()
    return render_template('index.html', tasks=all_tasks)

@app.route('/done/<int:task_id>')
def mark_as_done(task_id):
    # Find the task by its ID (primary key)
    task = Task.query.get(task_id)
    if task:
        task.done = True
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)