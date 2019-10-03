from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    connection = sqlite3.connect('blog.db')

    return render_template('page.html', rows=rows, title='Min databaseblog')


@app.route('/artikel/<int:id>')
def artikel(id):
    # find en blogpost/artikel vha id
    connection = sqlite3.connect('data/blog.db')

    return render_template('page.html', row=row, title='TO DO: find på titel til faneblad eller ret template')


@app.route('/admin')
def admin():
    # TO DO: find alle blogposter i databasen

    return render_template('admin.html', rows=rows)


@app.route('/admin/create', methods=('POST',))
def create():
    if request.method == 'POST':
        title = request.form['title']
        # TO DO: Hent de andre postvariabler og opret ny række i tabel
        return redirect('/admin')


@app.route('/admin/update', methods=('POST',))
def update():
    # TO DO: hent posterne og opdater rækken i databasen
    return redirect('/admin')


@app.route('/admin/delete', methods=('POST',))
def delete():
    #TO DO: hent postet id og lav delete af denne række i database

    return redirect('/admin')

####################

# Hvis du har brugertabel kan du lave login
# husk at tjekke credentials på sider, der skal beskyttes
##

@app.route('/login', methods=('POST',))
def login():
    #TO DO: kontroller brugernavn og password og set session-variabel, fx session['userid']
    return redirect('/admin')


@app.route('/logud')
def logud():
    if 'userid' in session:
        session.pop('userid', None)
    return redirect('/')

########################


if __name__ == '__main__':
    #app.secret_key = "session kræver en secret key!"
    app.run()
