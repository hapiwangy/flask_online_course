# 此INIT代表會自動跑在WEBSITE這個folder裡面的東東
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager

# 先設定一個db
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    # 每個flask都 app要有
    # use for encrypt or secure cookie
    # just use random string(不要share)
    app.config['SECRET_KEY'] = 'alskdjf;laksdjf;aks'
    # 告訴FLASK DB要存在哪裡
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # 告訴app我們要用這個db
    db.init_app(app)




    # 定義完views之類的東西之後要用的地方
    from .views import views
    from .auth import auth

    # register那些定義完的東西
    # url_prefix代表說如果要進入底的目錄的前墜
    # 例如if auth的url_prefix = /he，假如我想進入auth，route值為"hi"，則我的網址需要是/he/hi
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix = '/')
    
    # 等到設定完db model之後
    # 作後要把他create出來
    # 我們要檢查我們是否已經把db create出來了
    
    from .models import User, Note
    create_database(app)
    
    #　如果沒有登入的話要顯示的頁面
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # 告訴flask我們要找誰(by id)
        return User.query.get(int(id))
    return app
# 檢查database是否存在
# 否的話就創造一個
# 是的話就不用重新創造
def create_database(app):
    # 檢查website底下是否有database的path存在
    # 沒有的話就要創建
    if not path.exists('website/' + DB_NAME):
        # App代表要在哪個app製作database
        db.create_all(app=app)
        print("create Database")
    