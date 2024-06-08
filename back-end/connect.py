import pymysql

db_settings = {
    "host": "http://127.0.0.1:5051/",
    "user": "root",
    "password": "rainmysql314043",
    "db": "test",
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
