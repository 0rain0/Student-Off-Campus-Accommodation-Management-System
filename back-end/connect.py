import pymysql

db_settings = {
    "host": "localhost",
    "user": "你的帳號",
    "password": "你的密碼",
    "db": "你的資料庫名稱",
}

def connect_to_db():
    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)
        print("連線成功")
        return conn
    except Exception as ex:  # 出現意外時印出
        print(ex)
        return None
