from operator import methodcaller
from flask import Blueprint, render_template, request, flash, redirect, url_for
# 把資料存放在database裡面會用到
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
# hash function沒有inverse
# 對於相同的inpt，每次hash會得到相同的結果
# 做的事情跟view依樣，只是改成auth
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__)

# 加入methods代表可以接受的http request
# 不加入的話點選button會出現error
@auth.route('/login', methods =['GET', 'POST'])
# 跟render_template一起船的參數就可以用在前面的那個html裡面
def login():
    # 代表會接收某種形式的資料
    # data = request.form
    # print(data)
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        # 找尋db裡面特定column的資料
        # 下面這個敘述代表找到和輸入的email相同的那個的第一筆資料
        user = User.query.filter_by(email = email).first()
        if user:
            # 有了找到某一個entry之後，就可以用.來access他的特定資料了
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                # 只要不重啟伺服器、使用者登出等等，就會一直保持是目前的這個使用者
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("error password", category="error")
        else:
            flash("email not exist", category = "error")

    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required
# login required確保要先登入才能會看到logout的資訊
def logout():
    logout_user()
    # 登出之後回到登入頁面
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods =['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # 檢查是否存在該user(by email)
        user = User.query.filter_by(email = email).first()
        if user:
            flash("email already been used", category="error")
        # 如果出錯的處理
        elif len(email) < 4:
            # 如果要flash訊息的話需要使用的東東
            # category可以自定名稱，大多是用來做分類的(可以上色之類的)
            flash("Email must be greater than four characters", category="error")

        elif len(firstName) < 2:
            flash("FirstName must be greater than three characters", category="error")
        elif password1 != password2:
            flash("passwords not match", category="error")
        elif len(password1) < 7:
            flash("password must be at least seven words", category="error")
        else:
            # add to database
            # sha256可以換成其他的hash function
            new_user = User(email = email, firstName = firstName, password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account establish success", category="success")
            # url_for的參數放blueprint name + function name   
            return redirect(url_for('views.home'))
    return render_template("sign_up.html", user = current_user)