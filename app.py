from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to create a database and table
def create_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS dictionary
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, key TEXT, value TEXT)''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def index():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM dictionary")
    data = c.fetchall()
    conn.close()
    items = [{'id': row[0], 'key': row[1], 'value': row[2]} for row in data]
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    key = request.form['key']
    value = request.form['value']
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO dictionary (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete(item_id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DELETE FROM dictionary WHERE id=?", (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)