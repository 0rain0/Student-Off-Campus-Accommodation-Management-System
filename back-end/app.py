from flask import Flask, jsonify, request
from flask_cors import CORS
import traceback
import connect

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

def convert_to_dict(tuples_list):
    keys = ["id", "department", "grade", "class", "teacher", "number"]
    dict_list = [dict(zip(keys, row)) for row in tuples_list]
    return dict_list

@app.route('/')
def index():
    return jsonify({"message": "Hello, this is a CORS-enabled Flask application!"})


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        print("Received data:", data)  # 打印接收到的數據
        connection = connect.connect_to_db()
        if connection is not None:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM ACCOUNT WHERE ID = %s AND PassWord = %s"
                cursor.execute(sql, (data['username'], data['password']))
                result = cursor.fetchone()
                if result is not None:
                    if result[2] == 1:
                        return jsonify({"login": 'success_1'})
                    else:
                        return jsonify({"login": 'success_2'})
                else:
                    return jsonify({"login": 'fail'})
        else:
            return jsonify({"login": 'sql connection fail'})
    except Exception as ex:
        print(f"Error: {ex}")
        traceback.print_exc()  # 打印完整的堆棧追踪
        return jsonify({"login": 'error', "message": str(ex)})
    
    
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        
        # 註冊進資料庫
        connection = connect.connect_to_db()
        if connection is not None:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `landlord` (`name`, `e-mail`, `password`) VALUES (%s, %s, %s);"
                
                re = cursor.execute(sql, (name, email, password))
                connection.commit()
                
                if re > 0:
                    return jsonify({"register": 'success'})
                else:
                    return jsonify({"register": 'fail'})
                
        else:
            return jsonify({"register": 'sql connection fail'})
    except Exception as ex:
        print(f"Error: {ex}")
        traceback.print_exc()  # 打印完整的堆棧追踪
        return jsonify({"register": 'error', "message": str(ex)})
    
    
def get_class_data():
    try:
        connection = connect.connect_to_db()
        if connection is not None:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM CLASS"
                cursor.execute(sql)
                result = cursor.fetchall()
                
                class_ids = [data[0] for data in result]
                numbers = []
                for id in class_ids:
                    sql = "SELECT count(*) FROM STUDENT WHERE CLASS = %s"
                    cursor.execute(sql, (id,))
                    count_result = cursor.fetchone()
                    count = count_result[0] if count_result else 0
                    numbers.append(count)
                
                modified_result = [tup + (numbers[i],) for i, tup in enumerate(result)]
                return convert_to_dict(modified_result)            
        else:
            return jsonify({"ClassManage": 'sql connection fail'})
    except Exception as ex:
        print(f"Error: {ex}")
        traceback.print_exc()  # 打印完整的堆棧追踪
        return jsonify({"ClassManage": 'error', "message": str(ex)})
    

@app.route('/api/classes', methods=['GET'])
def get_classes():
    try:
        data = get_class_data()
        return jsonify({"data": data, "status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    

@app.route('/api/classes/delete', methods=['POST'])
def delete_class():
    data = request.get_json()
    if data.get('_method') == 'DELETE':
        department = data.get('department')
        grade = data.get('grade')
        class_name = data.get('class')
        teacher = data.get('teacher')
        
        print(department, grade, class_name, teacher)
        
        connection = connect.connect_to_db()
        if connection is not None:
            with connection.cursor() as cursor:
                try:
                    sql = "SELECT CID FROM CLASS WHERE Department = %s AND Grade = %s AND Class = %s AND Teacher = %s"
                    cursor.execute(sql, (department, grade, class_name, teacher))
                    target_cid = cursor.fetchone()
                    
                    # 先將所有該班級學生的CLASS欄位設為 NULL
                    sql_update_students = "UPDATE STUDENT SET class = NULL WHERE class = %s"
                    cursor.execute(sql_update_students, (target_cid,))
                    connection.commit()
                    
                    # 再刪除該班級
                    sql = "DELETE FROM CLASS WHERE CID = %s"
                    cursor.execute(sql, (target_cid,))
                    connection.commit()
                    
                    return jsonify({"status": "success"})
                except Exception as ex:
                    print(ex)
                    return jsonify({"status": "fail", "message": str(ex)})
        else:
            return jsonify({"status": "fail", "message": "sql connection fail"})
    return jsonify({"status": "fail", "message": "Invalid method"})

def convert_account_to_dict(tuples_list):
    keys = ["account", "password", "permission", "name", "phone", "email"]
    dict_list = [dict(zip(keys, row)) for row in tuples_list]
    return dict_list

def get_accounts_data():
    try:
        connection = connect.connect_to_db()
        if connection is not None:
            with connection.cursor() as cursor:
                all_accounts_data = []  # 建立一個列表來存儲所有帳號相關的資訊
                
                # 遍歷不同的 UserType
                for user_type in range(1, 5):
                    # 從 'account' 表中獲取相關資訊
                    sql = "SELECT ID, Password FROM account WHERE UserType = %s"
                    cursor.execute(sql, (user_type,))
                    account_result = cursor.fetchall()
                    # 根據 UserType 找到對應的表，獲取其他資訊
                    if user_type == 1:  # administrator
                        for row in account_result:
                            account_id, account_password = row
                            sql = "SELECT Name, Email FROM administrator WHERE AID = %s"
                            cursor.execute(sql, (account_id,))
                            admin_data = cursor.fetchone()
                            if admin_data:
                                admin_data = list(admin_data)
                                admin_data.insert(1, "")
                                account_info = [account_id, account_password, "管理員"] + admin_data
                                all_accounts_data.append(account_info)
                    elif user_type == 2:  # landlord
                        for row in account_result:
                            account_id, account_password = row
                            sql = "SELECT Name, Tel, Email FROM landlord WHERE LID = %s"
                            cursor.execute(sql, (account_id,))
                            landlord_data = cursor.fetchone()
                            if landlord_data:
                                account_info = [account_id, account_password, "房東"] + list(landlord_data)
                                all_accounts_data.append(account_info)
                    elif user_type == 3:  # student
                        for row in account_result:
                            account_id, account_password = row
                            sql = "SELECT Name, Tel, Email FROM student WHERE SID = %s"
                            cursor.execute(sql, (account_id,))
                            student_data = cursor.fetchone()
                            if student_data:
                                account_info = [account_id, account_password, "學生"] + list(student_data)
                                all_accounts_data.append(account_info)
                    elif user_type == 4:  # teacher
                        for row in account_result:
                            account_id, account_password = row
                            sql = "SELECT Name, Tel, Email FROM teacher WHERE TID = %s"
                            cursor.execute(sql, (account_id,))
                            teacher_data = cursor.fetchone()
                            if teacher_data:
                                account_info = [account_id, account_password, "老師"] + list(teacher_data)
                                all_accounts_data.append(account_info)
                return convert_account_to_dict(all_accounts_data)  # 返回整合後的列表           
        else:
            return [{"AccountManage": 'sql connection fail'}]
    except Exception as ex:
        print(f"Error: {ex}")
        traceback.print_exc()  # 打印完整的堆棧追踪
        return [{"AccountManage": 'error', "message": str(ex)}]
    finally:
        # 关闭数据库连接
        connection.close()


@app.route('/api/accounts', methods=['GET'])
def get_accounts():
    try:
        data = get_accounts_data()
        return jsonify({"data": data, "status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
@app.route('/api/account/delete', methods=['POST'])
def delete_account():
    data = request.get_json()
    if data.get('_method') == 'DELETE':
        account = data.get('account')
        permission = data.get('permission')
        
        connection = connect.connect_to_db()
        if connection is not None:
            with connection.cursor() as cursor:
                try:
                    #if permission == "管理員":
                    #    return jsonify({"status": "fail", "message": "無法刪除管理員"})
                    # 刪除該帳號
                    sql = "DELETE FROM ACCOUNT WHERE ID = %s"
                    cursor.execute(sql, (account))
                    connection.commit()
                    
                    return jsonify({"status": "success"})
                except Exception as ex:
                    print(ex)
                    return jsonify({"status": "fail", "message": str(ex)})
                finally:
                # 关闭数据库连接
                    connection.close()
        else:
            return jsonify({"status": "fail", "message": "sql connection fail"})
    return jsonify({"status": "fail", "message": "Invalid method"})

@app.route('/api/account/update', methods=['POST'])
def update_account():
    data = request.get_json()
    if data.get('_method') == 'UPDATE':
        permission_mapping = {
            "管理員": 1,
            "房東": 2,
            "學生": 3,
            "老師": 4
        }
        account = data.get('account')
        password = data.get('password')
        permission = data.get('permission')
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')
        if permission not in permission_mapping:
            return jsonify({"status": "fail", "message": "未知的權限: '"+permission + "'，合法的權限(管理員, 房東, 學生, 老師)"})
        connection = connect.connect_to_db()
        if connection is not None:
            with connection.cursor() as cursor:
                try:
                    if permission == "管理員":
                        if account == "" or password == "" or permission == "" or name == "" or email == "":
                            return jsonify({"status": "fail", "message": "請輸入空欄位(除了電話)"})
                        sql = "UPDATE ACCOUNT SET Password = %s, UserType = %s WHERE ID = %s"
                        cursor.execute(sql, (password, permission_mapping.get(permission), account))
                        sql = "UPDATE administrator SET Name = %s, Email = %s WHERE AID = %s"
                        cursor.execute(sql, (name, email, account))
                        connection.commit()
                        return jsonify({"status": "success", "message": "編輯成功(管理員無電話欄位)"})
                    elif permission == "房東":
                        if account == "" or password == "" or permission == "" or name == "" or phone == "" or email == "":
                            return jsonify({"status": "fail", "message": "請輸入空欄位(除了電話)"})
                        sql = "UPDATE ACCOUNT SET Password = %s, UserType = %s WHERE ID = %s"
                        cursor.execute(sql, (password, permission_mapping.get(permission), account))
                        sql = "UPDATE landlord SET Name = %s, Tel = %s, Email = %s WHERE LID = %s"
                        cursor.execute(sql, (name, phone, email, account))
                        connection.commit()
                    elif permission == "學生":
                        if account == "" or password == "" or permission == "" or name == "" or phone == "" or email == "":
                            return jsonify({"status": "fail", "message": "請輸入空欄位(除了電話)"})
                        sql = "UPDATE ACCOUNT SET Password = %s, UserType = %s WHERE ID = %s"
                        cursor.execute(sql, (password, permission_mapping.get(permission), account))
                        sql = "UPDATE student SET Name = %s, Tel = %s, Email = %s WHERE SID = %s"
                        cursor.execute(sql, (name, phone, email, account))
                        connection.commit()
                    elif permission == "老師":
                        if account == "" or password == "" or permission == "" or name == "" or phone == "" or email == "":
                            return jsonify({"status": "fail", "message": "請輸入空欄位(除了電話)"})
                        sql = "UPDATE ACCOUNT SET Password = %s, UserType = %s WHERE ID = %s"
                        cursor.execute(sql, (password, permission_mapping.get(permission), account))
                        sql = "UPDATE teacher SET Name = %s, Tel = %s, Email = %s WHERE TID = %s"
                        cursor.execute(sql, (name, phone, email, account))
                        connection.commit()
                    return jsonify({"status": "success", "message": "編輯成功"})
                except Exception as ex:
                    print(ex)
                    return jsonify({"status": "fail", "message": str(ex)})
                finally:
                # 关闭数据库连接
                    connection.close()
        else:
            return jsonify({"status": "fail", "message": "sql connection fail"})
    return jsonify({"status": "fail", "message": "Invalid method"})

@app.route('/api/accounts/new', methods=['POST'])
def new_accounts():
    data = request.get_json()
    permission_mapping = {
        "管理員": 1,
        "房東": 2,
        "學生": 3,
        "老師": 4
    }
    account = data.get('account')
    password = data.get('password')
    permission = data.get('permission')
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')
    Teacher = data.get('Teacher') # 學生需要
    Class = data.get('Class') # 學生需要
    if account == '':
        return jsonify({"status": "fail", "message": "請輸入帳號!"})
    elif password == '':
        return jsonify({"status": "fail", "message": "請輸入密碼!"})
    elif permission not in permission_mapping:
        return jsonify({"status": "fail", "message": "請選擇權限!"})
    elif name == '':
        return jsonify({"status": "fail", "message": "請輸入姓名!"})
    elif permission != "管理員" and phone == '':
        return jsonify({"status": "fail", "message": "請輸入電話!"})
    elif email == '':
        return jsonify({"status": "fail", "message": "請輸入電子信箱!"})
    elif permission == "學生":
        if Teacher == '':
            return jsonify({"status": "fail", "message": "請輸入老師!"})
        elif Class == '':
            return jsonify({"status": "fail", "message": "請輸入班級!"})
        
    connection = connect.connect_to_db()
    if connection is not None:
        with connection.cursor() as cursor:
            try:
                print("Test")
                cursor.execute("SELECT * FROM account WHERE ID = %s", (account,))
                existing_account = cursor.fetchone()
                if existing_account:
                    return jsonify({"status": "fail", "message": "帳號已存在!"})
                
                if permission == "管理員":
                    insert_query = "INSERT INTO account (ID, Password, UserType) VALUES (%s, %s, %s)"
                    cursor.execute(insert_query, (account, password, "1"))
                    insert_query = "INSERT INTO administrator (AID, Name, Email) VALUES (%s, %s, %s)"
                    cursor.execute(insert_query, (account, name, email))
                    connection.commit()
                elif permission == "房東":
                    insert_query = "INSERT INTO account (ID, Password, UserType) VALUES (%s, %s, %s)"
                    cursor.execute(insert_query, (account, password, "2"))
                    insert_query = "INSERT INTO landlord (LID, Name, Tel, Email) VALUES (%s, %s, %s, %s)"
                    cursor.execute(insert_query, (account, name, phone, email))
                    connection.commit()
                elif permission == "學生":
                    cursor.execute("SELECT * FROM teacher WHERE TID = %s", (Teacher,))
                    existing_account = cursor.fetchone()
                    if not existing_account:
                        return jsonify({"status": "fail", "message": "老師ID不存在!"})
                    
                    cursor.execute("SELECT * FROM class WHERE CID = %s", (Class,))
                    existing_account = cursor.fetchone()
                    if not existing_account:
                        return jsonify({"status": "fail", "message": "班級ID不存在!"})
                    
                    insert_query = "INSERT INTO account (ID, Password, UserType) VALUES (%s, %s, %s)"
                    cursor.execute(insert_query, (account, password, "3"))
                    insert_query = "INSERT INTO student (SID, Name, Tel, Email, TEACHER, CLASS) VALUES (%s, %s, %s, %s, %s, %s)"
                    cursor.execute(insert_query, (account, name, phone, email, Teacher, Class))
                    connection.commit()
                elif permission == "老師":
                    insert_query = "INSERT INTO account (ID, Password, UserType) VALUES (%s, %s, %s)"
                    cursor.execute(insert_query, (account, password, "4"))
                    insert_query = "INSERT INTO teacher (TID, Name, Tel, Email) VALUES (%s, %s, %s, %s)"
                    cursor.execute(insert_query, (account, name, phone, email))
                    connection.commit()
                return jsonify({"status": "success", "message": "新增成功"})
            except Exception as ex:
                print(ex)
                return jsonify({"status": "fail", "message": str(ex)})
            finally:
                # 关闭数据库连接
                connection.close()
    else:
        return jsonify({"status": "fail", "message": "sql connection fail"})

@app.route('/api/accounts/bulk_add', methods=['POST'])
def bulk_add_accounts():
    permission_mapping = {
        "管理員": 1,
        "房東": 2,
        "學生": 3,
        "老師": 4
    }
    data = request.get_json()
    file_content = data.get('fileContent')
    
    if not file_content:
        return jsonify({"status": "fail", "message": "No file content"})
    
    try:
        reader = file_content
        original_rows = reader.split('\n')
        rows = [row.replace(" ", "") for row in original_rows if row.strip()]
        
        connection = connect.connect_to_db()
        if connection is not None:
            with connection.cursor() as cursor:
                for row in rows:
                    columns = row.split(',')
                    if len(columns) >= 6:
                        if columns[2] not in permission_mapping:
                            return jsonify({"status": "fail", "message": "未知的權限: " + columns[2]})
                        elif columns[2] == "管理員":
                            if columns[0] == "" or columns[1] == "" or columns[2] == "" or columns[3] == "" or columns[5] == "":
                                return jsonify({"status": "fail", "message": "資料格式錯誤: " + str(columns)})
                            insert_query = "INSERT INTO account (ID, Password, UserType) VALUES (%s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[1], "1"))
                            insert_query = "INSERT INTO administrator (AID, Name, Email) VALUES (%s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[3], columns[5]))
                        elif columns[2] == "房東":
                            if columns[0] == "" or columns[1] == "" or columns[2] == "" or columns[3] == "" or columns[4] == "" or columns[5] == "":
                                return jsonify({"status": "fail", "message": "資料格式錯誤: " + str(columns)})
                            insert_query = "INSERT INTO account (ID, Password, UserType) VALUES (%s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[1], "2"))
                            insert_query = "INSERT INTO landlord (LID, Name, Tel, Email) VALUES (%s, %s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[3], columns[4], columns[5]))
                        elif columns[2] == "學生":
                            if len(columns) < 8:
                                return jsonify({"status": "fail", "message": "學生欄位錯誤!"})
                            if columns[0] == "" or columns[1] == "" or columns[2] == "" or columns[3] == "" or columns[4] == "" or columns[5] == "" or columns[6] == "" or columns[7] == "":
                                return jsonify({"status": "fail", "message": "資料格式錯誤: " + str(columns)})
                            
                            cursor.execute("SELECT * FROM teacher WHERE TID = %s", (columns[6],))
                            existing_account = cursor.fetchone()
                            if not existing_account:
                                return jsonify({"status": "fail", "message": "老師ID不存在: " + columns[6]})
                            
                            cursor.execute("SELECT * FROM class WHERE CID = %s", (columns[7],))
                            existing_account = cursor.fetchone()
                            if not existing_account:
                                return jsonify({"status": "fail", "message": "班級ID不存在: " + columns[7]})
                            
                            insert_query = "INSERT INTO account (ID, Password, UserType) VALUES (%s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[1], "3"))
                            insert_query = "INSERT INTO student (SID, Name, Tel, Email, TEACHER, CLASS) VALUES (%s, %s, %s, %s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[3], columns[4], columns[5], columns[6], columns[7]))
                        elif columns[2] == "老師":
                            if columns[0] == "" or columns[1] == "" or columns[2] == "" or columns[3] == "" or columns[4] == "" or columns[5] == "":
                                return jsonify({"status": "fail", "message": "資料格式錯誤: " + str(columns)})
                            insert_query = "INSERT INTO account (ID, Password, UserType) VALUES (%s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[1], "4"))
                            insert_query = "INSERT INTO teacher (TID, Name, Tel, Email) VALUES (%s, %s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[3], columns[4], columns[5]))

                    else:return jsonify({"status": "fail", "message": "檔案格式錯誤"})
            connection.commit()
            return jsonify({"status": "success", "message": "批量新增成功"})
        else:
            return jsonify({"status": "fail", "message": "SQL connection fail"})
    except Exception as e:
        print(e)
        return jsonify({"status": "fail", "message": "Failed to process file"})
    finally:
        # 关闭数据库连接
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
