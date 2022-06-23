from flask import Blueprint, render_template
# 做的事情跟view依樣，只是改成auth
auth = Blueprint('auth', __name__)

@auth.route('/login')
# 跟render_template一起船的參數就可以用在前面的那個html裡面
def login():
    return render_template("login.html", text="testing")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")