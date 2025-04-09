from flask import Flask, render_template, request, redirect, url_for
import os
import datetime

app = Flask(__name__)

# Create the directory to store task text files
if not os.path.exists('data/tasks'):
    os.makedirs('data/tasks')

@app.route('/')
def index():
    tasks = []
    for filename in os.listdir('data/tasks'):
        with open(os.path.join('data/tasks', filename), 'r') as file:
            task = file.read().split('\n')
            tasks.append(task)
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_description = request.form['task_description']
    customer = request.form['customer']
    next_step_owner = request.form['next_step_owner']
    status = request.form['status']
    information = request.form['information']
    links = request.form['links']
    creation_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    update_date = creation_date
    completion_date = ''
    task_link = str(datetime.datetime.now().timestamp()).replace('.', '')

    task_data = [
        task_description,
        customer,
        next_step_owner,
        status,
        information,
        links,
        creation_date,
        update_date,
        completion_date,
        task_link
    ]

    with open(f'data/tasks/{task_link}.txt', 'w') as file:
        file.write('\n'.join(task_data))

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
