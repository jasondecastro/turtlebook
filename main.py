from flask import Flask, request, render_template, redirect, url_for
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from werkzeug.security import generate_password_hash as gph
import hashlib, datetime, pymysql, sqlalchemy, re
from config import *
#-------------------------------------------------------------------------------
application = Flask(__name__, template_folder="templates/"+config['website']['template'])
conn = pymysql.connect(host=config['sql']['host'], user=config['sql']['username'],
                       passwd=config['sql']['password'], db=config['sql']['database'], charset='utf8')
cursor = conn.cursor()
#-------------------------------------------------------------------------------

class User():
    id = cursor.execute("SELECT * FROM users WHERE id = '%r'" % id)
    username = cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
    password = cursor.execute("SELECT * FROM users WHERE pwd = '%s'" % password)
    email = cursor.execute("SELECT * FROM users WHERE email = '%s'" % email)

#-------------------------------------------------------------------------------
class Index(Form):
    pass

@application.route('/')
@application.route('/index', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

#-------------------------------------------------------------------------------

class Login(Form):
    login_user = TextField('Username', [validators.Required()])
    login_pass = PasswordField('Password', [validators.Required()])

@application.route('/login', methods=('GET', 'POST'))
def login():
    l_form = Login(request.form, prefix="login-form")
    if request.method == 'POST' and l_form.validate():
        check_login = cursor.execute("SELECT * FROM users WHERE username = '%s' AND pwd = '%s'"
        % (l_form.login_user.data, hashlib.sha1(l_form.login_pass.data).hexdigest()))
        if check_login == True:
            conn.commit()
            #usr_obj = User(l_form.login.user.data)
            return redirect(url_for('home'))

    return render_template('login.html', lform=l_form)
#-------------------------------------------------------------------------------

class Register(Form):
    username = TextField('Username', [validators.Length(min=1, max = 12)])
    password = PasswordField('Password', [
        validators.Required(),
        #validators.EqualTo('confirm_password', message='Passwords do not match')
    ])
    #confirm_password = PasswordField('Confirm Password')
    email = TextField('Email', [validators.Length(min=6, max=35)])

"""def check_email(email_person_submitted):
    if re.match(r"\b[\w.-]+@[\w.-]+.\w{2,4}\b", email_person_submitted):
        pass
    else:
        redirect(url_for('index'))"""

@application.route('/register', methods=('GET','POST'))
def register():
    r_form = Register(request.form, prefix="register-form")
    if request.method == 'POST' and r_form.validate():
        check_reg = cursor.execute("SELECT * FROM users WHERE username = '%s' OR email = '%s'"
        % (r_form.username.data, r_form.email.data))

        if check_reg == False:
            cursor.execute("INSERT into users (username, pwd, email) VALUES ('%s','%s','%s')"
            % (r_form.username.data, hashlib.sha1(r_form.password.data).hexdigest(), r_form.email.data))
            conn.commit()
            return redirect(url_for('login'))
    return render_template('register.html', rform=r_form)

#-------------------------------------------------------------------------------

class Home(Form):
    pass

@application.route('/home', methods=['GET'])
def home():
    form = Home(request.form)
    #username = cursor.execute("")
    return render_template('home.html')

if __name__ == '__main__':
    application.run(debug=True)
