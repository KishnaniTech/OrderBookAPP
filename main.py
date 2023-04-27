from flask import Flask, render_template, request, redirect, url_for
from data import data

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form['search_term']
        search_type = request.form['search_type']
        results = perform_search(search_term, search_type)
        return render_template('index.html', data=data, results=results, search_term=search_term, search_type=search_type)
    return render_template('index.html', data=data)


@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        # Simulate adding a new entry
        new_entry = {
            'id': len(data) + 1,
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'order_number': request.form['order_number'],
        }
        data.append(new_entry)
        return redirect('/')
    return render_template('add_entry.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_entry(id):
    entry = next((item for item in data if item['id'] == id), None)
    if not entry:
        return 'Entry not found', 404

    if request.method == 'POST':
        # Simulate updating the entry
        entry['first_name'] = request.form['first_name']
        entry['last_name'] = request.form['last_name']
        entry['order_number'] = request.form['order_number']
        return redirect('/')
    return render_template('update_entry.html', entry=entry)

@app.route('/delete/<int:id>')
def delete_entry(id):
    entry = next((item for item in data if item['id'] == id), None)
    if not entry:
        return 'Entry not found', 404

    # Simulate deleting the entry
    data.remove(entry)
    return redirect('/')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search_term']
        search_type = request.form['search_type']
        results = perform_search(search_term, search_type)
        return render_template('search_results.html', results=results)
    return render_template('search.html')

def perform_search(search_term, search_type):
    if search_type == 'name':
        results = [entry for entry in data if search_term.lower() in (entry['first_name'].lower() + ' ' + entry['last_name'].lower())]
    elif search_type == 'order_number':
        results = [entry for entry in data if search_term.lower() == entry['order_number'].lower()]
    else:
        results = []
    return results




if __name__ == '__main__':
    app.run()
