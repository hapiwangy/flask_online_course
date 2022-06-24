from flask import Blueprint, render_template, request, flash
# 做的事情跟view依樣，只是改成auth
auth = Blueprint('auth', __name__)

# 加入methods代表可以接受的http request
# 不加入的話點選button會出現error
@auth.route('/login', methods =['GET', 'POST'])
# 跟render_template一起船的參數就可以用在前面的那個html裡面
def login():
    # 代表會接收某種形式的資料
    # data = request.form
    # print(data)
    return render_template("login.html", text="testing", boolean = True)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods =['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # 如果出錯的處理
        if len(email) < 4:
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
            flash("Account establish success", category="success")
    return render_template("sign_up.html")