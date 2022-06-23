# 這裡面會存放使用者可以go into的page(login、home之類的)
from flask import Blueprint, render_template
# 裡面會存放一些URL、view之類的東東
# 首先要建立藍圖，讓我們的view可比不用全部都塞在一起(可在不同file)
views = Blueprint('views', __name__)
# 以上的views的部分都是可以自訂的，不用一釘叫做views

@views.route('/') 
# 表示現在要定義哪個page，後面擺分頁的網址
# 當輸入以上的route的後，home裡面的東西就會進行
def home():
    return render_template("home.html")
    # 當我們定義完views之類的東西的時候
    # 要回到init來register他們
