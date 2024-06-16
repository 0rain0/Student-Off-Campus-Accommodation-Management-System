import pymysql
from dotenv import load_dotenv
import os
# 資料庫設定
db_settings = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "db": os.getenv("DB_NAME"),
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
