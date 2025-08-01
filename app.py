from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  # Each task will be a dictionary: {"task": "Buy milk", "done": False}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_name = request.form['task']
        tasks.append({'task': task_name, 'done': False})
        return redirect('/')
    return render_template('index.html', tasks=tasks[::-1])

@app.route('/delete', methods=['POST'])
def delete():
    index = int(request.form['task_index'])
    tasks.pop(index)
    return redirect('/')

@app.route('/toggle', methods=['POST'])
def toggle():
    index = int(request.form['task_index'])
    tasks[index]['done'] = not tasks[index]['done']
    return redirect('/')

@app.route('/edit', methods=['POST'])
def edit():
    index = int(request.form['task_index'])
    new_task = request.form['new_task']
    tasks[index]['task'] = new_task
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
