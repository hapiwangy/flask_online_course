# 這裡面會存放使用者可以go into的page(login、home之類的)
from unicodedata import category
from flask import Blueprint, jsonify, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
# 裡面會存放一些URL、view之類的東東
# 首先要建立藍圖，讓我們的view可比不用全部都塞在一起(可在不同file)
views = Blueprint('views', __name__)
# 以上的views的部分都是可以自訂的，不用一釘叫做views

@views.route('/', methods=['GET','POST']) 
@login_required
# 表示現在要定義哪個page，後面擺分頁的網址
# 當輸入以上的route的後，home裡面的東西就會進行
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is tpp short', category = "error")
        else:
            new_note = Note(data=note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('ADD Note', category = "success")
    return render_template("home.html", user = current_user)
    # 當我們定義完views之類的東西的時候
    # 要回到init來register他們

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
