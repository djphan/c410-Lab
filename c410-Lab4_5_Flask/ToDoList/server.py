# Follows the tutorial in Flask
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

# Create Application
app = Flask(__name__)
app.config.from_object(__name__)
db = 'todolist.db'
conn = None

# Connection Methods
def connect():
    global conn
    if conn is None:
        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
    return conn

@app.teardown_appcontext
def closeConnect(exception):
    global conn
    if conn is not None:
        conn.close()
        conn = None

# DB Query Methods
def query_db(query, args=(), one=False):
    cur = connect().cursor()
    cur.execute(query, args)
    r = cur.fetchall()
    cur.close()
    return (r[0] if r else None) if one else r
    
# Task add
def add_task(catagory, priority, description):
    query_db ("insert into todolist(category, priority, description) values(?, ?, ?)", 
                (catagory, priority, description), one=True)
    connect().commit();

"""
def print_tasks():
    tasks = query_db('select * from todolist')
    for task in tasks:
        print ('Tasks: %s' % tasks['category'])
    print ("%d total tasks" %len(tasks))
"""
 
"""   
def remove_task(task):
    query_db("delete from todolist where rowid=?",rowid, one=True)
    connect().commit();
"""


"""
@app.route('/')
def welcome():
    #text = '<title>Dan Flask ToDo List Application</title>'
    text = '<h1> Dan Flask ToDo List Application </h1>'
    return text
"""

# Add redirection to tasks
@app.route('/')
def index():
    return redirect(url_for('tasks'))


@app.route('/tasks/delete',methods=["POST"])
def delete():
    rowid = request.form['id']  
    remove_task(rowid)
    return redirect(url_for('tasks'))

@app.route('/tasks',methods=["GET","POST"])
def tasks(name=None):
    # Post
    if request.method == "POST":
        category = request.form['category']
        priority = request.form['priority']
        description = request.form['description']

        add_task(category, priority, description)
        return redirect(url_for('tasks'))

    # Get 
    elif request.method == "GET":
       tasks = query_db("select * from todolist order by priority DESC")
       return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    app.debug = True
    app.run()
