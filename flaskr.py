#!/usr/bin/env python
# coding=utf-8
'''
> File Name: flaskr.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 四  4/12 10:20:41 2018
'''

# all the imports
import os
import pymysql
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.secret_key = "super secret key"

base_ip = '127.0.0.1'
base_user = 'root'
base_pwd = 'fengyufei123'
base_db = 'admintest'


def connect_db():
    """Connects to the specific database."""
    db = pymysql.connect(host = base_ip,user = base_user,charset = 'utf8',passwd = base_pwd,db = base_db)
    return db

def insert_db():
    cur = connect_db()
    cur.execute('')

@app.route('/')
def show_entries():
    db = connect_db()
    cur = db.cursor()
    cur.execute('select name from user')
    entry = [dict(title='第{}个用户'.format(str(row[0]+1)), text=row[1][0]) for row in enumerate(cur.fetchall())]
    db.close()
    return render_template('show_entries.html', entries=entry)
@app.route('/show_student')
def show_student():
    db = connect_db()
    cur = db.cursor()
    cur.execute('select * from student_info')
    entry = [dict(title='第{}个学生'.format(str(row[0])), name = row[2], number = row[1], score = row[-1]) for row in cur.fetchall()]
    db.close()
    return render_template('show_student.html', entries=entry)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    error = None
    db = connect_db()
    cur = db.cursor()
    sql='insert into student_info(s_name,s_num, s_score)VALUES(%s,%s,%s)'
    if request.method == 'POST':
        try:
            cur.execute(sql,(request.form['name'],request.form['number'],request.form['score']))
            db.commit()
            db.close()
            flash('New entry was successfully posted')
        except Exception as e:
            error = e
            flash(e)
    return redirect(url_for('show_student'))

@app.route('/', methods=['POST'])
def delete_info():
    pass

@app.route('/', methods=['POST'])
def update_info():
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    db = connect_db()
    cur = db.cursor()
    cur.execute('select name,password from user')
    pas = dict(cur.fetchall())
    db.close()
    if request.method == 'POST':
        if pas.get(request.form['username']) == None :
            error = 'Invalid username'
        elif request.form['password'] != pas[request.form['username']]:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/signup', methods = ['GET','POST'])
def signup():
    error = None
    sql = """INSERT INTO user(
    name,password
    )
    VALUES (%s,%s)"""
    if request.method == 'POST':
        name = request.form['username']
        pas  = request.form['password']
        db = connect_db()
        cur = db.cursor()
        try:
            cur.execute(sql,(name,pas))
            db.commit()
            db.close()
            flash('New User successfully post')
        except Exception as e:
            error = e
            flash('New User post error'+str(e))
        return redirect(url_for('show_entries'))
    return render_template('signup.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.debug = True
    app.run()

