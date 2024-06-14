import pymysql
from dotenv import load_dotenv
import os

# 載入 .env 檔案
load_dotenv()

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

def test_db_connection():
    # 連接到資料庫
    conn = connect_to_db()
    if conn is not None:
        try:
            # 建立Cursor物件
            cursor = conn.cursor()
            # 執行簡單的查詢
            cursor.execute("SELECT * FROM account WHERE ID = 'a1103306' AND Password = '12345'")
            # 取得結果
            result = cursor.fetchone()
            if result:
                print("資料庫連線測試成功，查詢結果：", result)
            else:
                print("資料庫連線測試失敗")
        except Exception as ex:
            print("查詢失敗：", ex)
        finally:
            # 關閉Cursor和Connection
            cursor.close()
            conn.close()
    else:
        print("無法連接到資料庫")

# 執行測試
test_db_connection()
