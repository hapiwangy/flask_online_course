# 此INIT代表會自動跑在WEBSITE這個folder裡面的東東
from flask import Flask


def creat_app():
    app = Flask(__name__)
    # 每個flask都 app要有
    # use for encrypt or secure cookie
    # just use random string(不要share)
    app.config['SECRET_KEY'] = 'alskdjf;laksdjf;aks'
    return app

    