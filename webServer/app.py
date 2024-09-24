from flask import Flask, request, url_for, render_template, redirect, session, flash
from markupsafe import escape
from hashlib import sha256
import secrets
import random
import string
from modules.db import db_handler
from werkzeug.middleware.proxy_fix import ProxyFix

database = db_handler()          # Sets up communication with database server.

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

app.secret_key = secrets.token_hex()

@app.route("/")
def index():
    return render_template('index.html.jinja')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        credentials = database.qury(f"SELECT password, salt FROM users WHERE \
                username='{escape(request.form['username'])}'")
       
        if credentials == []:   # This triggers if the user dosent exists in the database.
            flash("Login Failed", 'error')
            return render_template('login.html.jinja')
        else:
            password_hash = credentials[0]['password']
            salt = credentials[0]['salt']
            
            pass_from_user = bytes(salt + escape(request.form['password']), 'utf-8')
            pass_from_user_hex = sha256(pass_from_user).hexdigest()

            if password_hash == pass_from_user_hex:  # This triggers when login is completed.
                session['username'] = escape(request.form['username'])
                return redirect(url_for('dashboard'))
            
        flash("Login failed", "error")
        return render_template('login.html.jinja')
    else:
        return render_template('login.html.jinja')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username = escape(request.form['username'])
        user_exists = database.qury(f"SELECT COUNT(1) FROM users WHERE username = '{username}'")[0]['COUNT(1)'] 

        if user_exists:
            flash("Registration failed", 'error')
            return render_template('register.html.jinja')
        else:
            password = escape(request.form['password'])
            if len(password) < 8:
                flash("Password must be 8 characters or more")
                return render_template('register.html.jinja')
            else:
                salt = ''.join(random.choices(string.ascii_letters +
                             string.digits, k=32))
                password = sha256(bytes(salt + password, 'utf-8')).hexdigest()
                database.insert(f"INSERT INTO users (username, salt, password, is_admin) VALUES ('{username}', '{salt}', '{password}', 0)")
                flash('User created sucessfully!')
                return redirect(url_for('login'))

    else:
        return render_template('register.html.jinja')


@app.route("/dashboard")
def dashboard():

    if 'username' in session:
        return render_template('dashboard.html.jinja', user=session['username'])
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out')
    return redirect(url_for('index'))

@app.route('/db')
def db():
    
    data_dump = database.qury('SELECT * FROM users') + database.qury('SELECT * FROM products')
    return data_dump

@app.route('/products')
def products():
    
    products = database.qury('SELECT * FROM products')

    return render_template('item_grid.html.jinja', products=products)

@app.route('/course/AI_and_Productivity')
def ai_and_productivity():
    if 'username' in session:
        return render_template('course/ai_and_productivity.html.jinja')
    else:
        return redirect(url_for('login'))

@app.route('/course/Problem_Solving')
def problem_solving():
    if 'username' in session:
        return render_template('course/problem_solving.html.jinja')
    else:
        return redirect(url_for('login'))

