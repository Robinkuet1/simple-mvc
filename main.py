from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# model
tasks = []
users = []


# view
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, users=users)


@app.route("/users")
def view_users():
    return render_template("user.html", users=users)


# controller
@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    user = request.form.get("user")
    new_task = {'id': len(tasks) + 1, 'title': title, 'completed': False, "user": user}
    tasks.append(new_task)
    return redirect(url_for('index'))


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get("user")
    users.append({"name":name})
    return redirect(url_for('index'))


@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            break
    return redirect(url_for('index'))

@app.route('/remove/<int:task_id>')
def remove_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            break
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
