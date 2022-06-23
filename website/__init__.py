# 此INIT代表會自動跑在WEBSITE這個folder裡面的東東
from flask import Flask


def create_app():
    app = Flask(__name__)
    # 每個flask都 app要有
    # use for encrypt or secure cookie
    # just use random string(不要share)
    app.config['SECRET_KEY'] = 'alskdjf;laksdjf;aks'

    # 定義完views之類的東西之後要用的地方
    from .views import views
    from .auth import auth

    # register那些定義完的東西
    # url_prefix代表說如果要進入底的目錄的前墜
    # 例如if auth的url_prefix = /he，假如我想進入auth，route值為"hi"，則我的網址需要是/he/hi
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix = '/')
    
    return app

    