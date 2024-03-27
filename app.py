import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host="localhost",
                            database=os.environ['POSTGRES_DB'],
                            user=os.environ['USERNAME_DB'],
                            password=os.environ['PASSWORD_DB'])
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Jokes;')
    jokes = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', jokes=jokes)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        jokeText = request.form['jokeText']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO jokes (title, author, jokeText)'
                    'VALUES (%s, %s, %s)',
                    (title, author, jokeText))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')
