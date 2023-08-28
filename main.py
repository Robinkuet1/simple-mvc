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

@app.route('/remove_user/<string:name>')
def remove_user(name):
    for user in users:
        if user['name'] == name:
            users.remove(user)
            break
    return redirect(url_for('view_users'))


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get("user")
    users.append({"name":name})
    return redirect(url_for('view_users'))


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

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task_to_edit = next((task for task in tasks if task['id'] == task_id), None)

    if request.method == 'POST':
        new_title = request.form.get('title')
        new_user = request.form.get('user')
        for task in tasks:
            if task['id'] == task_id:
                task['title'] = new_title
                task['user'] = new_user
                break
        return redirect(url_for('index'))
    
    return render_template('index.html', tasks=tasks, users=users, task_to_edit=task_to_edit)



if __name__ == '__main__':
    app.run(debug=True)