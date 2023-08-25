from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# model
tasks = []


# view
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


# controller
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    new_task = {'id': len(tasks) + 1, 'title': title, 'completed': False}
    tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
