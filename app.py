from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global variables to store tasks
tasks = []
task_id_counter = 1

# Home page - display tasks
@app.route('/')
def index():
    filter_status = request.args.get('status')
    filter_priority = request.args.get('priority')

    filtered_tasks = tasks

    # Filter tasks by status if filter_status is provided
    if filter_status:
        filtered_tasks = [task for task in filtered_tasks if task['status'] == filter_status]

    # Filter tasks by priority if filter_priority is provided
    if filter_priority:
        filtered_tasks = [task for task in filtered_tasks if task['priority'] == filter_priority]

    return render_template('index.html', tasks=filtered_tasks, filter_status=filter_status, filter_priority=filter_priority)

# Create task page
@app.route('/create', methods=['GET', 'POST'])
def create_task():
    global task_id_counter
    if request.method == 'POST':
        description = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']
        task = {
            'id': task_id_counter,
            'description': description,
            'due_date': due_date,
            'priority': priority,
            'status': 'pending'
        }
        tasks.append(task)
        task_id_counter += 1
        return redirect(url_for('index'))
    return render_template('create_task.html')

# Update task page
@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if request.method == 'POST':
        task['description'] = request.form['description']
        task['due_date'] = request.form['due_date']
        task['priority'] = request.form['priority']
        task['status'] = request.form['status']
        return redirect(url_for('index'))
    return render_template('update_task.html', task=task)

# Delete task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

# Mark task as completed
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['status'] = 'completed'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
