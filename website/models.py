# we need db model for user and notes
# import 那個SQLALchemy物件而非其他的不知道甚麼咚咚
from . import db
# 可以繼承的東東，方便我們使用
# 如果做其他用途就不會import 了
from flask_login import UserMixin
from sqlalchemy.sql import func

# 針對每個可能進來的咚咚和他們資料的特性建立不同的class

# database model類似一種藍圖，用來表示說你的database裡面可能會存放的資料是甚麼行事
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    # 讓sqlalchemy自己幫我們決定時間，我們不用自己處裡
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    # associate不同的note with different user
    # 透過foreign key
    # one to many data model
    # 使用db.Foreignkey來強制只要創建此物件就要輸入特定的東東
    # user.id代表使用的key為user的id attribute
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin):
    # 需要使用primary key來區分不同user確有某些相同資料的情況
    id = db.Column(db.Integer, primary_key = True)
    # 設定為string的時候要限制長度
    # 設定unique代表任何重複的email是不被允許的
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    # 告訴sqlalchemy說，每次只要建立一個note，就要和正確的user建立連結
    # 這裡使用的是那個class的名稱
    notes = db.relationship('Note')