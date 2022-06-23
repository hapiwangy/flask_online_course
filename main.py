# import 剛剛建立好的˙package
# 並使用內含的function來製作一個app
from distutils.log import debug
from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug = True)
# 到這裡可以run 一下code，可以發現自己的網站網址
# 但是會顯示not found之類的錯誤訊息(因為還沒新增)
