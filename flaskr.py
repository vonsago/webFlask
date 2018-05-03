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
import csv
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from werkzeug import secure_filename

UPLOAD_FOLDER = '/Users/vassagovon/myProject/venv3/webapp/static/image'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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
    pass

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


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
    entry = [dict(title='第{}个学生'.format(str(row[0])), name = row[2], number = row[1], score = row[3], image=row[4]) for row in cur.fetchall()]
    db.close()
    return render_template('show_student.html', entries=entry)

@app.route('/show_detail')
def show_detail():
    db = connect_db()
    cur = db.cursor()
    cur.execute('select * from shop')
    entry = [dict(name = row[0],message = row[1],num=row[2], key1=row[3],key2=row[4],classname=row[5],picname='../static/image/'+row[6]) for row in cur.fetchall()]
    db.close()
    return render_template('show_detail.html', entries=entry)  

@app.route('/add', methods=['POST','GET'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    error = None
    db = connect_db()
    cur = db.cursor()
    sql='insert into student_info(s_num,s_name, s_score, s_image)VALUES(%s,%s,%s,%s)'
    if request.method == 'POST':
        if request.form['classname'] == 'yes':
            file = request.files['csvfile']
            filename = ''
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                picname = filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with open(app.config['UPLOAD_FOLDER']+'/'+filename) as f:
                f_csv = csv.reader(f)
                headers = next(f_csv)
                for row in f_csv:
                    cur.execute(sql,(row[1],row[2],row[3],row[4]))
                db.commit()
                db.close()
            flash('Students were successfully added')
        else:
            try:
                picname = ''
                #update file
                file = request.files['file']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    picname = filename
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                cur.execute(sql,(request.form['number'],request.form['name'],request.form['score'],picname))
                db.commit()
                db.close()
                flash('New Student was successfully added')
            except Exception as e:
                error = e
                flash(e)
    return render_template('add_new.html')

@app.route('/delete_info', methods=['GET','POST'])
def delete_info():
    if request.method == 'POST':
        db = connect_db()
        cur = db.cursor()
        sql = 'delete from student_info where s_num = {}'
        cur.execute(sql.format(request.form['number']))
        db.commit()
        db.close()
        flash('Delete successfully')
        return redirect(url_for('find_info'))
    return render_template('delete_info.html')

@app.route('/update_info', methods=['GET','POST'])
def update_info():
    dic = {'1':'计算机','2':'英语','3':'数理系','4':'体育','5':'艺术','6':'机械'}
    if request.method == 'POST':
        name = request.form['bookname']
        content = request.form['bookcontent']
        key1 = request.form['key1']
        key2 = request.form['key2']
        num = request.form['booknum']
        classname = request.values.getlist('classname')[0]
        classname = dic[ classname ]
        picname = ''
        #update file
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            picname = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        sql='insert into student_detail(name,message,num,key1,key2,classname,picture)VALUES(%s,%s,%s,%s,%s,%s,%s)'
        #sql = "update student_info set s_name='{0}',s_score='{1}' where s_num='{2}' "
        db = connect_db()
        cur = db.cursor()
        cur.execute(sql,(name,content,key1,key2,classname,picname))
        db.commit()
        db.close()
        flash('Update successfully') 
        return redirect(url_for('show_detail'))
    return render_template('update_info.html')  

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

@app.route('/find_info',methods = ['GET','POST'])
def find_info():
    if request.method == 'POST':
        db = connect_db()
        cur = db.cursor()

        if request.form['classname']=='yes':
            csvFile = open("/Users/vassagovon/Downloads/students.csv", "w")
            fileheader = ['编号','学号','名字','分数','照片']
            dict_writer = csv.DictWriter(csvFile, fileheader)
            dict_writer.writerow(dict(zip(fileheader, fileheader)))
            cur.execute('select * from student_info')
            for row in cur.fetchall():
                dict_writer.writerow(dict(zip(fileheader, row)))
            flash('导出成功')
            return render_template('find_student.html', entries=['get'])
        sql = 'select * from student_info where s_name = "{}" and s_num="{}"'
        sql1 = 'select * from student_info where s_name = "{}"'
        sql2 = 'select * from student_info where s_num = "{}"'

        name = request.form['name']
        number = request.form['number']
        if name == '' and number == '':
            db.close()
            flash('请输入搜索关键词')
            return render_template('find_student.html',entries=['get'])
        try:
            if name != '' and number != '':
                cur.execute(sql.format(name,number))
            elif name !='':
                cur.execute(sql1.format(name))
            elif number != '':
                cur.execute(sql2.format(number))
            entry = [dict(num=row[0],snum=row[1],name=row[2],score=row[3],image='../static/image/'+row[4]) for row in cur.fetchall()]
            flash('查询成功')
            return render_template('find_student.html', entries=entry)
        except Exception as e:
            flash('查询失败'+str(e))
    return render_template('find_student.html',entries=['get'])


@app.route('/find_class')
def find_class():
    flash('hold on....')
    return render_template('class.html')
    pass

if __name__ == '__main__':
    app.debug = True
    app.run()

