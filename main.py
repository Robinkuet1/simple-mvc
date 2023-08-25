from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data (you can replace this with a database)
learning_times = []
grades = []

@app.route('/')
def index():
    average_grade = calculate_average_grade()
    return render_template('home.html', learning_times=learning_times, grades=grades, average_grade=average_grade)

@app.route('/add_learning_time', methods=['POST'])
def add_learning_time():
    learning_time = int(request.form['learning_time'])
    learning_times.append(learning_time)
    return index()

@app.route('/add_grade', methods=['POST'])
def add_grade():
    grade = int(request.form['grade'])
    grades.append(grade)
    return index()

def calculate_average_grade():
    if not grades:
        return 0
    return sum(grades) / len(grades)

if __name__ == '__main__':
    app.run(debug=True)
