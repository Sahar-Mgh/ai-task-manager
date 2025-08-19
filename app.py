from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# UPDATED: Now a list of dictionaries
tasks = [
    {'text': 'Buy groceries', 'done': False},
    {'text': 'Finish project report', 'done': True}, # Example of a completed task
    {'text': 'Go for a run', 'done': False}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_task_text = request.form.get('task')
        if new_task_text:
            # Add a new dictionary for the new task
            tasks.append({'text': new_task_text, 'done': False})
        return redirect(url_for('index'))
    
    return render_template('index.html', tasks=tasks)

# NEW: Route to handle marking a task as done
@app.route('/done/<int:task_id>')
def mark_as_done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)