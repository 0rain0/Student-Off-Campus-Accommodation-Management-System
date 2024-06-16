from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import traceback
import connect
from flask import make_response

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)


def convert_to_dict(tuples_list):
    keys = ["id", "department", "grade", "class", "teacher", "number"]
    dict_list = [dict(zip(keys, row)) for row in tuples_list]
    return dict_list


def generate_new_cid(cursor):
    print("hi")
    try:
        cursor.execute("SELECT cid FROM CLASS ORDER BY cid DESC LIMIT 1")
        result = cursor.fetchone()[0]
        print("result: ", result)
        if result:
            last_cid = result
            new_cid_num = int(last_cid[1:]) + 1
            print(new_cid_num)
            new_cid = f"c{new_cid_num:04}"
            print(new_cid)
        else:
            new_cid = "c0001"
        return new_cid
    except:
        return "c0001"

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
                    usertype = result[2]
                    if usertype == 1:
                        return jsonify({"login": 'success_1', "usertype": '1'})
                    elif usertype == 2:
                        return jsonify({"login": 'success_2', "usertype": '2'})
                    elif usertype == 3:
                        return jsonify({"login": 'success_2', "usertype": '3'})
                    elif usertype == 4:
                        return jsonify({"login": 'success_2', "usertype": '4'})
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
        tel = data.get('tel')
        account = data.get('account')

        # 註冊進資料庫
        connection = connect.connect_to_db()
        if connection is not None:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `account` (`ID`, `Password`, `UserType`) VALUES (%s, %s, '2');"
                
                re = cursor.execute(sql, (account, password,))
                connection.commit()

                sql = "INSERT INTO `landlord` (`LID`, `Name`, `Tel`, `Email`) VALUES (%s, %s, %s, %s);"
                re = cursor.execute(sql, (account, name, tel, email))
                connection.commit()

                if re > 0:
                    return jsonify({"register": 'success'})
                else:
                    # 創建失敗，把account刪除，避免帳號創建成功，landlord寫入失敗的情況
                    sql = "DELETE FROM account WHERE `account`.`ID` = %s"
                    re = cursor.execute(sql, (id,))
                    connection.commit()
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
                    cursor.execute("SELECT tid FROM TEACHER WHERE name = %s", (teacher))
                    teacher = cursor.fetchone()[0]
                    
                    sql = "SELECT CID FROM CLASS WHERE Department = %s AND Grade = %s AND section = %s AND tid = %s"
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

#學生編輯表單
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
                            return jsonify({"status": "fail", "message": "請輸入空欄位"})
                        sql = "UPDATE ACCOUNT SET Password = %s, UserType = %s WHERE ID = %s"
                        cursor.execute(sql, (password, permission_mapping.get(permission), account))
                        sql = "UPDATE administrator SET Name = %s, Email = %s WHERE AID = %s"
                        cursor.execute(sql, (name, email, account))
                        connection.commit()
                        return jsonify({"status": "success", "message": "編輯成功(管理員無電話欄位)"})
                    elif permission == "房東":
                        if account == "" or password == "" or permission == "" or name == "" or phone == "" or email == "":
                            return jsonify({"status": "fail", "message": "請輸入空欄位"})
                        sql = "UPDATE ACCOUNT SET Password = %s, UserType = %s WHERE ID = %s"
                        cursor.execute(sql, (password, permission_mapping.get(permission), account))
                        sql = "UPDATE landlord SET Name = %s, Tel = %s, Email = %s WHERE LID = %s"
                        cursor.execute(sql, (name, phone, email, account))
                        connection.commit()
                    elif permission == "學生":
                        if account == "" or password == "" or permission == "" or name == "" or phone == "" or email == "":
                            return jsonify({"status": "fail", "message": "請輸入空欄位"})
                        sql = "UPDATE ACCOUNT SET Password = %s, UserType = %s WHERE ID = %s"
                        cursor.execute(sql, (password, permission_mapping.get(permission), account))
                        sql = "UPDATE student SET Name = %s, Tel = %s, Email = %s WHERE SID = %s"
                        cursor.execute(sql, (name, phone, email, account))
                        connection.commit()
                    elif permission == "老師":
                        if account == "" or password == "" or permission == "" or name == "" or phone == "" or email == "":
                            return jsonify({"status": "fail", "message": "請輸入空欄位"})
                        sql = "UPDATE ACCOUNT SET Password = %s, UserType = %s WHERE ID = %s"
                        cursor.execute(sql, (password, permission_mapping.get(permission), account))
                        sql = "UPDATE teacher SET Name = %s, Tel = %s, Email = %s WHERE TID = %s"
                        cursor.execute(sql, (name, phone, email, account))
                        connection.commit()
                    return jsonify({"status": "success", "message": "編輯成功"})
                except Exception as ex:
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
    # 通用資料
    account = data.get('account')
    password = data.get('password')
    permission = data.get('permission')
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')

    # 學生
    Grade = data.get('Grade')
    Gender = data.get('Gender')
    Address = data.get('Address')
    HomeTel = data.get('HomeTel')
    ContactName = data.get('ContactName')
    ConTel = data.get('ConTel')

    # 老師
    Rank = data.get('Rank')
    OfficeAddr = data.get('OfficeAddr')
    OfficeTel = data.get('OfficeTel')
    
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
        if Grade == '':
            return jsonify({"status": "fail", "message": "請選擇年級!"})
        elif Gender == '':
            return jsonify({"status": "fail", "message": "請選擇性別!"})
        elif Address == '':
            return jsonify({"status": "fail", "message": "請輸入家中地址!"})
        elif HomeTel == '':
            return jsonify({"status": "fail", "message": "請輸入家中電話!"})
        elif ContactName == '':
            return jsonify({"status": "fail", "message": "請輸入聯絡人姓名!"})
        elif ConTel == '':
            return jsonify({"status": "fail", "message": "請輸入聯絡人電話!"})
    elif permission == "老師":
        if Rank == '':
            return jsonify({"status": "fail", "message": "請選擇職級!"})
        elif OfficeAddr == '':
            return jsonify({"status": "fail", "message": "請輸入辦公室位址!"})
        elif OfficeTel == '':
            return jsonify({"status": "fail", "message": "請輸入辦公室電話!"})

    connection = connect.connect_to_db()
    if connection is not None:
        with connection.cursor() as cursor:
            try:
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
                    insert_query = "INSERT INTO account (ID, Password, UserType) VALUES (%s, %s, %s)"
                    cursor.execute(insert_query, (account, password, "3"))
                    insert_query = "INSERT INTO student (SID, Name, Grade, Gender, CLASS, Tel, Email, Address, HomeTel, ContactName, ConTel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(insert_query, (account, name, int(Grade), int(Gender), None, phone, email, Address, HomeTel, ContactName, ConTel))
                    connection.commit()
                elif permission == "老師":
                    insert_query = "INSERT INTO account (ID, Password, UserType) VALUES (%s, %s, %s)"
                    cursor.execute(insert_query, (account, password, "4"))
                    insert_query = "INSERT INTO teacher (TID, Name, Rank, Tel, Email, OfficeAddr, OfficeTel) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(insert_query, (account, name, Rank, phone, email, OfficeAddr, OfficeTel))
                    connection.commit()
                return jsonify({"status": "success", "message": "新增成功"})
            except Exception as ex:
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
                    if len(columns) >= 5:
                        if columns[2] not in permission_mapping:
                            return jsonify({"status": "fail", "message": "未知的權限稱謂: " + columns[2]})
                        elif columns[2] == "管理員":
                            if columns[0] == "" or columns[1] == "" or columns[2] == "" or columns[3] == "" or columns[4] == "":
                                return jsonify({"status": "fail", "message": "管理員資料有空: " + str(columns)})
                            insert_query = "INSERT INTO account (ID, Password, UserType) VALUES (%s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[1], "1"))
                            insert_query = "INSERT INTO administrator (AID, Name, Email) VALUES (%s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[3], columns[4]))
                        elif columns[2] == "房東":
                            if len(columns) < 6:
                                return jsonify({"status": "fail", "message": "房東欄位有缺: " + str(columns)})
                            if columns[0] == "" or columns[1] == "" or columns[2] == "" or columns[3] == "" or columns[4] == "" or columns[5] == "":
                                return jsonify({"status": "fail", "message": "房東資料有空: " + str(columns)})
                            insert_query = "INSERT INTO account (ID, Password, UserType) VALUES (%s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[1], "2"))
                            insert_query = "INSERT INTO landlord (LID, Name, Tel, Email) VALUES (%s, %s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[3], columns[5], columns[4]))
                        elif columns[2] == "學生":
                            if len(columns) < 12:
                                return jsonify({"status": "fail", "message": "學生欄位有缺: " + str(columns)})
                            
                            if columns[0] == "" or columns[1] == "" or columns[2] == "" or columns[3] == "" or columns[4] == "" or columns[5] == "" or columns[6] == "" or columns[7] == "" or columns[8] == "" or columns[9] == "" or columns[10] == "" or columns[11] == "":
                                return jsonify({"status": "fail", "message": "學生資料有空: " + str(columns)})
                            
                            grade_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                            if columns[6] not in grade_list:
                                return jsonify({"status": "fail", "message": "學生年級錯誤: " + str(columns) + "\n錯誤的年級: " + columns[6]})
                            
                            gender_mapping = {"男": "0", "女": "1", "其他": "2"}
                            if columns[7] not in gender_mapping:
                                return jsonify({
                                    "status": "fail", 
                                    "message": f"學生性別錯誤: {columns}\n錯誤的性別: {columns[7]}"
                                })
                            columns[7] = gender_mapping[columns[7]]

                            insert_query = "INSERT INTO account (ID, Password, UserType) VALUES (%s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[1], "3"))
                            insert_query = "INSERT INTO student (SID, Name, Grade, Gender, CLASS, Tel, Email, Address, HomeTel, ContactName, ConTel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[3], columns[6], columns[7], None, columns[5], columns[4], columns[8], columns[9], columns[10], columns[11]))
                        elif columns[2] == "老師":
                            if len(columns) < 9:
                                return jsonify({"status": "fail", "message": "老師欄位有缺: " + str(columns)})
                            
                            if columns[0] == "" or columns[1] == "" or columns[2] == "" or columns[3] == "" or columns[4] == "" or columns[5] == "" or columns[6] == "" or columns[7] == "" or columns[8] == "":
                                return jsonify({"status": "fail", "message": "老師資料有空: " + str(columns)})
                            
                            rank_mapping = {"教授": "0", "副教授": "1", "助理教授": "2"}
                            if columns[6] not in rank_mapping:
                                return jsonify({
                                    "status": "fail", 
                                    "message": f"老師職級錯誤: {columns}\n錯誤的職級: {columns[6]}"
                                })
                            columns[6] = rank_mapping[columns[6]]

                            insert_query = "INSERT INTO account (ID, Password, UserType) VALUES (%s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[1], "4"))
                            insert_query = "INSERT INTO teacher (TID, Name, Rank, Tel, Email, OfficeAddr, OfficeTel) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                            cursor.execute(insert_query, (columns[0], columns[3], columns[6], columns[5], columns[4], columns[7], columns[8]))
                    else:
                        return jsonify({"status": "fail", "message": "資料格式錯誤"})
            connection.commit()
            return jsonify({"status": "success", "message": "批量新增成功"})
        else:
            return jsonify({"status": "fail", "message": "SQL connection fail"})
    except Exception as e:
        return jsonify({"status": "fail", "message": str(e)})
    finally:
        # 关闭数据库连接
        connection.close()

# 驗證編輯個人資料權限
@app.route('/EditLogin', methods=['POST'])
def Edit_login():
    try:
        data = request.get_json()
        if data['account'] == '':
            return jsonify({"status": 'fail', "message": "請輸入帳號"})
        elif data['password'] == '':
            return jsonify({"status": 'fail', "message": "請輸入密碼"})
        print("Received data:", data)  # 打印接收到的數據
        connection = connect.connect_to_db()
        if connection is not None:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM account WHERE ID = %s AND PassWord = %s"
                cursor.execute(sql, (data['account'], data['password']))
                result = cursor.fetchone()
                result2 = None
                if result is not None:
                    if result[2] == 1: # 管理員身分
                        sql = "SELECT * FROM administrator WHERE AID = %s"
                        cursor.execute(sql, (data['account']))
                        result2 = cursor.fetchone()
                    elif result[2] == 2: # 房東身分
                        sql = "SELECT * FROM landlord WHERE LID = %s"
                        cursor.execute(sql, (data['account']))
                        result2 = cursor.fetchone()
                    elif result[2] == 3: # 學生身分
                        sql = "SELECT * FROM student WHERE SID = %s"
                        cursor.execute(sql, (data['account']))
                        result2 = cursor.fetchone()
                    elif result[2] == 4: # 老師身分
                        sql = "SELECT * FROM teacher WHERE TID = %s"
                        cursor.execute(sql, (data['account']))
                        result2 = cursor.fetchone()
                    else:
                        return jsonify({"status": 'fail', "message": "驗證錯誤"})
                    
                    if result2 is not None:
                        return jsonify({"status": 'success', "message": "驗證成功", "result": result, "result2": result2})
                    else:
                        return jsonify({"status": 'fail', "message": "驗證錯誤"})
                else:
                    return jsonify({"status": 'fail', "message": "帳號或密碼錯誤"})
        else:
            return jsonify({"login": 'sql connection fail'})
    except Exception as ex:
        print(f"Error: {ex}")
        traceback.print_exc()  # 打印完整的堆棧追踪
        return jsonify({"login": 'error', "message": str(ex)})
    
# 編輯個人資料
@app.route('/SaveChanges', methods=['POST'])
def SaveChanges():
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
    phone = data.get('Tel')
    email = data.get('email')
    address = data.get('address')
    Grade = data.get('Grade')
    Gender = data.get('Gender')
    HomeTel = data.get('HomeTel')
    ContactName = data.get('ContactName')
    ConTel = data.get('ConTel')
    Rank = data.get('Rank')
    OfficeAddr = data.get('OfficeAddr')
    OfficeTel = data.get('OfficeTel')
    if permission not in permission_mapping:
        return jsonify({"status": "fail", "message": "未知的權限: '"+permission + "'，合法的權限(管理員, 房東, 學生, 老師)"})
    connection = connect.connect_to_db()
    if connection is not None:
        with connection.cursor() as cursor:
            try:
                if permission == "管理員":
                    if account == "" or password == "" or permission == "" or name == "" or email == "":
                        return jsonify({"status": "fail", "message": "請輸入空欄位"})
                    sql = "UPDATE ACCOUNT SET Password = %s, UserType = %s WHERE ID = %s"
                    cursor.execute(sql, (password, permission_mapping.get(permission), account))
                    sql = "UPDATE administrator SET Name = %s, Email = %s WHERE AID = %s"
                    cursor.execute(sql, (name, email, account))
                    connection.commit()
                    return jsonify({"status": "success", "message": "編輯成功(管理員無電話欄位)"})
                elif permission == "房東":
                    if account == "" or password == "" or permission == "" or name == "" or phone == "" or email == "":
                        return jsonify({"status": "fail", "message": "請輸入空欄位"})
                    sql = "UPDATE ACCOUNT SET Password = %s, UserType = %s WHERE ID = %s"
                    cursor.execute(sql, (password, permission_mapping.get(permission), account))
                    sql = "UPDATE landlord SET Name = %s, Tel = %s, Email = %s WHERE LID = %s"
                    cursor.execute(sql, (name, phone, email, account))
                    connection.commit()
                elif permission == "學生":
                    if account == "" or password == "" or permission == "" or name == "" or phone == "" or email == "" or address == "" or Grade == "" or Gender == "" or HomeTel == "" or ContactName == "" or ConTel == "":
                        return jsonify({"status": "fail", "message": "請輸入空欄位"})
                    sql = "UPDATE ACCOUNT SET Password = %s, UserType = %s WHERE ID = %s"
                    cursor.execute(sql, (password, permission_mapping.get(permission), account))
                    sql = "UPDATE student SET Name = %s, Grade = %s, Gender = %s, Tel = %s, Email = %s, Address = %s, HomeTel = %s, ContactName = %s, ConTel = %s WHERE SID = %s"
                    cursor.execute(sql, (name, Grade, Gender, phone, email, address, HomeTel, ContactName, ConTel, account))
                    connection.commit()
                elif permission == "老師":
                    if account == "" or password == "" or permission == "" or name == "" or phone == "" or email == "" or Rank == "" or OfficeAddr == "" or OfficeTel == "":
                        return jsonify({"status": "fail", "message": "請輸入空欄位"})
                    sql = "UPDATE ACCOUNT SET Password = %s, UserType = %s WHERE ID = %s"
                    cursor.execute(sql, (password, permission_mapping.get(permission), account))
                    sql = "UPDATE teacher SET Name = %s, Rank = %s, Tel = %s, Email = %s, OfficeAddr = %s, OfficeTel = %s WHERE TID = %s"
                    cursor.execute(sql, (name, Rank, phone, email, OfficeAddr, OfficeTel, account))
                    connection.commit()
                return jsonify({"status": "success", "message": "編輯成功"})
            except Exception as ex:
                return jsonify({"status": "fail", "message": str(ex)})
            finally:
            # 关闭数据库连接
                connection.close()
    else:
        return jsonify({"status": "fail", "message": "sql connection fail"})
# Class編輯頁面用於獲取班級內student資訊
@app.route('/api/students', methods=['GET'])
def get_students():
    department = request.args.get('department')
    grade = request.args.get('grade')
    section = request.args.get('section')
    page = request.args.get('page', 1, type=int)

    page = request.args.get('page', 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page

    connection = connect.connect_to_db()
    if connection is not None:
        with connection.cursor() as cursor:
            try:
                if department:
                    cursor.execute("SELECT sid, name FROM STUDENT")
                    students = cursor.fetchall()
                    student_list = [{"sid": student[0], "name": student[1]} for student in students]

                    cursor.execute("SELECT COUNT(*) FROM STUDENT")
                    total = cursor.fetchone()[0]

                    cursor.execute("SELECT cid FROM CLASS WHERE department=%s and grade=%s and section=%s",
                                   (department, grade, section,))
                    cid = cursor.fetchone()[0]

                    cursor.execute("SELECT sid, name FROM STUDENT WHERE CLASS = %s LIMIT %s OFFSET %s",
                                   (cid, per_page, offset))
                    students = cursor.fetchall()

                    # 将数据转换为字典列表
                    student_selected = [{"sid": student[0], "name": student[1]} for student in students]
                    print(student_selected)

                    return jsonify({"status": "success", "student_all": student_list, "total": total,
                                    "student_selected": student_selected})

                else:
                    cursor.execute("SELECT sid, name FROM STUDENT")
                    students = cursor.fetchall()
                    student_list = [{"sid": student[0], "name": student[1]} for student in students]

                    cursor.execute("SELECT COUNT(*) FROM STUDENT")
                    total = cursor.fetchone()[0]

                    return jsonify({"status": "success", "student_all": student_list, "total": total})

            except Exception as ex:
                print(ex)
                return jsonify({"status": "fail", "message": str(ex)})
    else:
        return jsonify({"status": "fail", "message": "sql connection fail"})


# 用於回傳所有teacher資訊
@app.route('/api/teachers', methods=['GET'])
def get_teachers():
    connection = connect.connect_to_db()
    if connection is not None:
        with connection.cursor() as cursor:
            try:
                cursor.execute("SELECT tid, name FROM TEACHER")
                teachers = cursor.fetchall()
                teacher_list = [{"tid": teacher[0], "name": teacher[1]} for teacher in teachers]
                return jsonify({"status": "success", "data": teacher_list})
            except Exception as ex:
                print(ex)
                return jsonify({"status": "fail", "message": str(ex)})
    else:
        return jsonify({"status": "fail", "message": "sql connection fail"})


# 提交class修改
import re


@app.route('/api/classes/update', methods=['POST'])
def update_class():
    data = request.get_json()
    original_data = data.get('originalData')
    new_data = data.get('newData')
    selected_students = data.get('selectedStudents')

    original_department = original_data.get('department')
    original_grade = original_data.get('grade')
    original_section = original_data.get('section')
    original_teacher = original_data.get('teacher')

    new_department = new_data.get('department')
    new_grade = new_data.get('grade')
    new_section = new_data.get('section')
    new_teacher = new_data.get('teacher')

    connection = connect.connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                # 查找原班级CID
                cursor.execute(
                    "SELECT cid FROM CLASS WHERE department=%s AND grade=%s AND section=%s",
                    (original_department, original_grade, original_section)
                )
                cid = cursor.fetchone()
                if not cid:
                    return jsonify({"status": "fail", "message": "Class not found"})
                cid = cid[0]

                if str(original_teacher) == str(new_teacher):
                    cursor.execute("SELECT tid FROM CLASS WHERE cid=%s", (cid,))
                    new_teacher = cursor.fetchone()[0]
                    print(new_teacher)

                # 更新 CLASS 表
                cursor.execute(
                    "UPDATE CLASS SET department=%s, grade=%s, section=%s, tid=%s WHERE cid=%s",
                    (new_department, new_grade, new_section, new_teacher, cid)
                )

                # 清空該班級的所有學生
                cursor.execute(
                    "UPDATE STUDENT SET class=NULL WHERE class=%s", (cid,)
                )

                # 添加選中的學生到該班級
                for student in selected_students:
                    cursor.execute(
                        "UPDATE STUDENT SET class=%s WHERE sid=%s",
                        (cid, student['sid'])
                    )

                connection.commit()
                return jsonify({"status": "success"})
        except Exception as ex:
            connection.rollback()
            print(ex)
            return jsonify({"status": "fail", "message": str(ex)})
    else:
        return jsonify({"status": "fail", "message": "sql connection fail"})


# 提交AddNewClass的班級創建
@app.route('/api/classes/create', methods=['POST'])
def create_class():
    data = request.get_json()
    department = data.get('department')
    grade = data.get('grade')
    section = data.get('section')
    teacher = data.get('teacher')
    selected_students = data.get('selectedStudents')
    
    print(department, grade, section, teacher, selected_students)

    connection = connect.connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                # 生成新的 CID
                new_cid = generate_new_cid(cursor)
                print(new_cid)

                # 插入新的班级
                cursor.execute(
                    "INSERT INTO CLASS (cid, department, grade, section, tid) VALUES (%s, %s, %s, %s, %s)",
                    (new_cid, department, grade, section, teacher)
                )

                # 更新學生的班级信息
                for student in selected_students:
                    cursor.execute(
                        "UPDATE STUDENT SET class=%s WHERE sid=%s",
                        (new_cid, student['sid'])
                    )

                connection.commit()
                return jsonify({"status": "success"})
        except Exception as ex:
            connection.rollback()
            print(ex)
            return jsonify({"status": "fail", "message": str(ex)})
    else:
        return jsonify({"status": "fail", "message": "sql connection fail"})

#學生編輯表單
@app.route('/receive_form_s',methods = ['GET','POST'])
def receive_form_s():
    user = request.form
    print(user)

    #獲取表單參數
    SID = request.form.get("SID")
    DG = request.form.get("DG")
    S_Name = request.form.get("S_Name")
    S_Tel = request.form.get("S_Tel")
    T_Name = request.form.get("T_Name")
    year = request.form.get("year",'0000')
    month = request.form.get("month",'00')
    day = request.form.get("day",'00')
    hour = request.form.get("hour",'00')
    visit = year +"-"+ month +"-"+ day +" "+ hour +":00:00"
    L_Name = request.form.get("L_Name")
    L_Tel = request.form.get("L_Tel")
    R_Addr = request.form.get("R_Addr")
    RoommateN = request.form.get("RoommateN")
    RoommateP = request.form.get("RoommateP")
    RA = request.form.get("RA")
    RentType = request.form.get("RentType")
    RoomType = request.form.get("RoomType")
    Price = request.form.get("Price")
    Deposit = request.form.get("Deposit")
    Recommend = request.form.get("Recommend")
    SA_01 = request.form.get("SA_01")
    SA_02 = request.form.get("SA_02")
    SA_03 = request.form.get("SA_03")
    SA_04 = request.form.get("SA_04")
    SA_05 = request.form.get("SA_05")
    SA_06 = request.form.get("SA_06")
    SA_07 = request.form.get("SA_07")
    SA_08 = request.form.get("SA_08")
    SA_09 = request.form.get("SA_09")
    SA_10 = request.form.get("SA_10")
    SA_11 = request.form.get("SA_11")
    SA_12 = request.form.get("SA_12")
    SA_13 = request.form.get("SA_13")

    #確認該學號是否存在訪視紀錄
    sql = f"""
        select * from visit_form where SID= '{SID}'
        """
    datas = connect.query_data(sql)

    if(datas != ()):
        #已存在訪視紀錄，更新表單
        sql = f"""
                UPDATE visit_form
                SET DG = '{DG}',
                    S_Name = '{S_Name}',
                    S_Tel = '{S_Tel}',
                    T_Name = '{T_Name}',
                    V_Time = '{visit}',
                    L_Name = '{L_Name}',
                    L_Tel = '{L_Tel}',
                    R_Addr = '{R_Addr}',
                    RoommateN = '{RoommateN}',
                    RoommateP = '{RoommateP}',
                    RA = {RA},
                    RentType = {RentType},
                    RoomType = {RoomType},
                    Price = {Price},
                    Deposit = {Deposit},
                    recommend = {Recommend},
                    State = 1,
                    SA_01 = {SA_01},
                    SA_02 = {SA_02},
                    SA_03 = {SA_03},
                    SA_04 = {SA_04},
                    SA_05 = {SA_05},
                    SA_06 = {SA_06},
                    SA_07 = {SA_07},
                    SA_08 = {SA_08},
                    SA_09 = {SA_09},
                    SA_10 = {SA_10},
                    SA_11 = {SA_11},
                    SA_12 = {SA_12},
                    SA_13 = {SA_13}
                WHERE SID = '{SID}'
            """

        sql = sql.replace("'None'", "Null").replace("None", "Null")
        connect.update(sql)
        return redirect("http://localhost:5173/Successform")
    else:
        #未存在訪視紀錄，新增表單
        #需要有學號在資料庫內才能新增
        sql = f"""
                    insert into visit_form (State,DG,SID,S_Name,S_Tel,T_Name,
                                            V_Time,L_Name,L_Tel,R_Addr,RoommateN,
                                            RoommateP,RA,RentType,RoomType,Price,
                                            Deposit,recommend,SA_01,SA_02,SA_03,
                                            SA_04,SA_05,SA_06,SA_07,SA_08,SA_09,
                                            SA_10,SA_11,SA_12,SA_13)
                    values (1,'{DG}','{SID}','{S_Name}','{S_Tel}','{T_Name}',
                            '{visit}','{L_Name}','{L_Tel}','{R_Addr}','{RoommateN}',
                            '{RoommateP}',{RA},{RentType},{RoomType},{Price},
                            {Deposit},{Recommend},{SA_01},{SA_02},{SA_03},{SA_04},
                            {SA_05},{SA_06},{SA_07},{SA_08},{SA_09},{SA_10},{SA_11},
                            {SA_12},{SA_13})
                """

        sql = sql.replace("'None'", "Null").replace("None", "Null")
        connect.update(sql)
        return redirect("http://localhost:5173/Successform")


#老師編輯表單
@app.route('/receive_form_t', methods=['GET', 'POST'])
def receive_form_t():
    user = request.form
    print(user)

    # 獲取表單參數
    SID = request.form.get("SID")
    DG = request.form.get("DG")
    S_Name = request.form.get("S_Name")
    S_Tel = request.form.get("S_Tel")
    T_Name = request.form.get("T_Name")
    year = request.form.get("year", '0000')
    month = request.form.get("month", '00')
    day = request.form.get("day", '00')
    hour = request.form.get("hour", '00')
    visit = f"{year}-{month}-{day} {hour}:00:00"
    EN_01 = request.form.get("EN_01")
    EN_02 = request.form.get("EN_02")
    EN_03 = request.form.get("EN_03")
    EN_04 = request.form.get("EN_04")
    VI_01 = request.form.get("VI_01")
    VI_02 = request.form.get("VI_02")
    Result = request.form.get("Result")
    DI_01 = request.form.get("DI_01")
    DI_02 = request.form.get("DI_02")
    DI_03 = request.form.get("DI_03")
    DI_04 = request.form.get("DI_04")
    DI_05 = request.form.get("DI_05")
    EN_03_Des = request.form.get("EN_03_Des")
    EN_04_Des = request.form.get("EN_04_Des")
    VI_01_Des = request.form.get("VI_01_Des")
    RE_Des = request.form.get("RE_Des")
    RE_Memo = request.form.get("RE_Memo")
    DI_05_Des = request.form.get("DI_05_Des")

    # 確認該學號是否存在訪視紀錄
    sql = f"""
        SELECT * FROM visit_form WHERE SID = '{SID}'
    """
    datas = connect.query_data(sql)

    if datas:
        # 已存在訪視紀錄，更新表單
        sql = f"""
            UPDATE visit_form
            SET DG = '{DG}',
                S_Name = '{S_Name}',
                S_Tel = '{S_Tel}',
                T_Name = '{T_Name}',
                V_Time = '{visit}',
                State = 1,
                EN_01 = {EN_01 if EN_01 else 'NULL'},
                EN_02 = {EN_02 if EN_02 else 'NULL'},
                EN_03 = {EN_03 if EN_03 else 'NULL'},
                EN_04 = {EN_04 if EN_04 else 'NULL'},
                VI_01 = {VI_01 if VI_01 else 'NULL'},
                VI_02 = {VI_02 if VI_02 else 'NULL'},
                Result = {Result if Result else 'NULL'},
                DI_01 = {DI_01 if DI_01 else 'NULL'},
                DI_02 = {DI_02 if DI_02 else 'NULL'},
                DI_03 = {DI_03 if DI_03 else 'NULL'},
                DI_04 = {DI_04 if DI_04 else 'NULL'},
                DI_05 = {DI_05 if DI_05 else 'NULL'},
                EN_03_Des = {f"'{EN_03_Des}'" if EN_03_Des else 'NULL'},
                EN_04_Des = {f"'{EN_04_Des}'" if EN_04_Des else 'NULL'},
                VI_01_Des = {f"'{VI_01_Des}'" if VI_01_Des else 'NULL'},
                RE_Des = {f"'{RE_Des}'" if RE_Des else 'NULL'},
                RE_Memo = {f"'{RE_Memo}'" if RE_Memo else 'NULL'},
                DI_05_Des = {f"'{DI_05_Des}'" if DI_05_Des else 'NULL'}
            WHERE SID = '{SID}'
        """
        print("Generated SQL:", sql)  # 打印SQL語句
        sql = sql.replace("'None'", "NULL").replace("None", "NULL")
        connect.update(sql)
        return redirect("http://localhost:5173/Successform")
    else:
        # 未存在訪視紀錄，新增表單
        sql = f"""
            INSERT INTO visit_form
                (State, DG, SID, S_Name, S_Tel, T_Name, V_Time,
                EN_01, EN_02, EN_03, EN_04, VI_01, VI_02, Result,
                DI_01, DI_02, DI_03, DI_04, DI_05, EN_03_Des,
                EN_04_Des, VI_01_Des, RE_Des, RE_Memo, DI_05_Des)
            VALUES (1, '{DG}', '{SID}', '{S_Name}', '{S_Tel}', '{T_Name}', 
                    '{visit}', {EN_01 if EN_01 else 'NULL'}, {EN_02 if EN_02 else 'NULL'}, 
                    {EN_03 if EN_03 else 'NULL'}, {EN_04 if EN_04 else 'NULL'}, 
                    {VI_01 if VI_01 else 'NULL'}, {VI_02 if VI_02 else 'NULL'}, {Result if Result else 'NULL'}, 
                    {DI_01 if DI_01 else 'NULL'}, {DI_02 if DI_02 else 'NULL'}, {DI_03 if DI_03 else 'NULL'}, 
                    {DI_04 if DI_04 else 'NULL'}, {DI_05 if DI_05 else 'NULL'}, 
                    {f"'{EN_03_Des}'" if EN_03_Des else 'NULL'}, {f"'{EN_04_Des}'" if EN_04_Des else 'NULL'}, 
                    {f"'{VI_01_Des}'" if VI_01_Des else 'NULL'}, {f"'{RE_Des}'" if RE_Des else 'NULL'}, 
                    {f"'{RE_Memo}'" if RE_Memo else 'NULL'}, {f"'{DI_05_Des}'" if DI_05_Des else 'NULL'})
        """
        print("Generated SQL:", sql)  # 打印SQL語句
        sql = sql.replace("'None'", "NULL").replace("None", "NULL")
        connect.update(sql)
        return redirect("http://localhost:5173/Successform")

    
@app.route('/VSS/studentStatue', methods=['GET'])
def get_VSS_students():
    page = request.args.get('page', 1, type=int)
    pageSize = request.args.get('pageSize', 10, type=int)
    sid = request.args.get('SID', None)
    name = request.args.get('Name', None)
    cid = request.args.get('CID', None)
    offset = (page - 1) * pageSize

    connection = connect.connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                count_query = "SELECT COUNT(*) FROM student"
                select_query = "SELECT SID, Name, CLASS, Tel, Email FROM student"
                conditions = []
                params = []

                if sid:
                    conditions.append("SID LIKE %s")
                    params.append(f"%{sid}%")
                if name:
                    conditions.append("Name LIKE %s")
                    params.append(f"%{name}%")
                if cid:
                    conditions.append("CLASS LIKE %s")
                    params.append(f"%{cid}%")

                if conditions:
                    count_query += " WHERE " + " AND ".join(conditions)
                    select_query += " WHERE " + " AND ".join(conditions)

                select_query += " LIMIT %s OFFSET %s"
                params.extend([pageSize, offset])

                cursor.execute(count_query, params[:-2])
                total = cursor.fetchone()[0]

                cursor.execute(select_query, params)
                students = cursor.fetchall()

                student_list = []
                for student in students:
                    sid = student[0]
                    cursor.execute("SELECT 1 FROM visit_form WHERE SID = %s", (sid,))
                    visit_record = cursor.fetchone()
                    status = '已填寫' if visit_record else '未填寫'
                    student_info = {
                        "SID": student[0],
                        "Name": student[1],
                        "Phone": student[2],
                        "Email": student[3],
                        "Status": status
                    }
                    student_list.append(student_info)

                return jsonify({"students": student_list, "total": total, "status": "success"})
        except Exception as ex:
            print(ex)
            return jsonify({"status": "fail", "message": str(ex)})
        finally:
            connection.close()
    else:
        return jsonify({"status": "fail", "message": "sql connection fail"})


@app.route('/VSS/ClassStatue', methods=['GET'])
def get_VSS_classes():
    page = request.args.get('page', 1, type=int)
    pageSize = request.args.get('pageSize', 10, type=int)
    department = request.args.get('department', None)
    grade = request.args.get('grade', None)
    section = request.args.get('section', None)
    offset = (page - 1) * pageSize

    connection = connect.connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                count_query = "SELECT COUNT(*) FROM class"
                select_query = """SELECT class.CID, class.Department, class.Grade, class.Section, 
                                  class.TID, teacher.Name, COUNT(student.SID) AS StudentCount, 
                                  SUM(CASE WHEN visit_form.SID IS NOT NULL THEN 1 ELSE 0 END) AS VisitCount
                                  FROM class
                                  LEFT JOIN teacher ON class.TID = teacher.TID
                                  LEFT JOIN student ON class.CID = student.CLASS
                                  LEFT JOIN visit_form ON student.SID = visit_form.SID"""
                conditions = []
                params = []

                if department:
                    conditions.append("class.Department = %s")
                    params.append(department)
                if grade:
                    conditions.append("class.Grade = %s")
                    params.append(grade)
                if section:
                    conditions.append("class.Section = %s")
                    params.append(section)

                if conditions:
                    condition_str = " WHERE " + " AND ".join(conditions)
                else:
                    condition_str = ""

                count_query += condition_str
                select_query += condition_str + " GROUP BY class.CID, class.Department, class.Grade, class.Section, class.TID, teacher.Name"
                select_query += " LIMIT %s OFFSET %s"
                params.extend([pageSize, offset])

                cursor.execute(count_query, params[:-2])
                total = cursor.fetchone()[0]

                cursor.execute(select_query, params)
                classes = cursor.fetchall()

                class_list = [{'CID': cl[0], 'Department': cl[1], 'Grade': cl[2],
                               'Section': cl[3], 'TID': cl[4], 'teacherName': cl[5],
                               'CompleteRate': (cl[7] / cl[6] * 100) if cl[6] > 0 else 0}  # 轉換為百分比
                              for cl in classes]

                return jsonify({"classes": class_list, "total": total, "status": "success"})
        except Exception as ex:
            print(ex)
            return jsonify({"status": "fail", "message": str(ex)})
        finally:
            connection.close()
    else:
        return jsonify({"status": "fail", "message": "sql connection fail"})
    
@app.route('/VSS/CheckForm_S/<sid>', methods=['GET'])
def check_form_s(sid):
    connection = connect.connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM visit_form WHERE SID = %s", (sid,))
                form = cursor.fetchone()
                if form:
                    return jsonify({"status": "success", "form": form})
                else:
                    return jsonify({"status": "fail", "message": "No form found"})
        except Exception as ex:
            print(ex)
            return jsonify({"status": "fail", "message": str(ex)})
        finally:
            connection.close()
    else:
        return jsonify({"status": "fail", "message": "SQL connection failed"})
    
@app.route('/VSS/TIDtoCID', methods=['GET'])
def tid_to_cid():
    try:
        tid = request.args.get('TID')
        connection = connect.connect_to_db()
        if connection is not None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT CID FROM CLASS WHERE TID = %s", (tid,))
                cid = cursor.fetchone()
                if cid:
                    return jsonify({"cid": {"CID": cid[0], "status": "success"}})
                else:
                    return jsonify({"cid": {"CID": "", "status": "fail"}})
        else:
            return jsonify({"status": "sql connection fail"})
    except Exception as ex:
        print(ex)
        return jsonify({"status": "fail", "message": str(ex)})

@app.route('/VSS/CheckForm_query/<sid>', methods=['GET'])
def check_form_query(sid):
    connection = connect.connect_to_db()
    if connection is not None:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM visit_form WHERE SID = %s", (sid,))
                form = cursor.fetchone()
                if form:
                    return jsonify({"status": "success", "form": form})
                else:
                    return jsonify({"status": "fail", "message": "No form found"})
        except Exception as ex:
            print(ex)
            return jsonify({"status": "fail", "message": str(ex)})
        finally:
            connection.close()
    else:
        return jsonify({"status": "fail", "message": "SQL connection failed"})


@app.route('/api/ad/delete-review', methods=['POST'])
def delete_review():
    data = request.get_json()
    rid = data.get('RID')
    connection = connect.connect_to_db()
    if connection is not None:
        with connection.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM review WHERE RID = '"+rid + "'")
                connection.commit()
                return jsonify({"status": "success"})
            except Exception as ex:
                print(ex)
                return jsonify({"status": "fail", "message": str(ex)})
    else:
        return jsonify({"status": "fail", "message": "sql connection fail"})
    
@app.route('/api/ad/edit-review', methods=['POST'])
def edit_review():
    data = request.get_json()
    rid = data.get('RID')
    content = data.get('content')
    rate = data.get('rate')
    connection = connect.connect_to_db()
    if connection is not None:
        with connection.cursor() as cursor:
            try:
                cursor.execute("UPDATE review SET Content = '"+content + "', Rate = '"+str(rate) + "' WHERE RID = '"+rid + "'")
                connection.commit()
                return jsonify({"status": "success"})
            except Exception as ex:
                print(ex)
                return jsonify({"status": "fail", "message": str(ex)})
    else:
        return jsonify({"status": "fail", "message": "sql connection fail"})
    
@app.route('/api/ad/edit-comment', methods=['POST'])
def edit_comment():
    data = request.get_json()
    cid = data.get('CMID')
    content = data.get('content')
    print(cid, content)
    connection = connect.connect_to_db()
    if connection is not None:
        with connection.cursor() as cursor:
            try:
                cursor.execute("UPDATE comment SET Content = '"+content + "' WHERE CMID = '"+cid + "'")
                connection.commit()
                return jsonify({"status": "success"})
            except Exception as ex:
                print(ex)
                return jsonify({"status": "fail", "message": str(ex)})
    else:
        return jsonify({"status": "fail", "message": "sql connection fail"})

@app.route('/api/ad/delete-comment', methods=['POST'])
def delete_comment():
    data = request.get_json()
    cid = data.get('CMID')
    connection = connect.connect_to_db()
    if connection is not None:
        with connection.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM comment WHERE CMID = '"+cid + "'")
                connection.commit()
                return jsonify({"status": "success"})
            except Exception as ex:
                print(ex)
                return jsonify({"status": "fail", "message": str(ex)})
    else:
        return jsonify({"status": "fail", "message": "sql connection fail"})

@app.route('/api/ad/delete-AD', methods=['POST'])
def delete_AD():
    data = request.get_json()
    adid = data.get('ADID')
    connection = connect.connect_to_db()
    if connection is not None:
        with connection.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM advertisement WHERE ADID = '"+adid + "'")
                connection.commit()
                return jsonify({"status": "success"})
            except Exception as ex:
                print(ex)
                return jsonify({"status": "fail", "message": str(ex)})
    else:
        return jsonify({"status": "fail", "message": "sql connection fail"})


@app.route('/api/ad/delete-post', methods=['POST'])
def delete_post():
    data = request.get_json()
    pid = data.get('PID')
    connection = connect.connect_to_db()
    if connection is not None:
        with connection.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM post WHERE PID = '"+pid + "'")
                connection.commit()
                return jsonify({"status": "success"})
            except Exception as ex:
                print(ex)
                return jsonify({"status": "fail", "message": str(ex)})
    else:
        return jsonify({"status": "fail", "message": "sql connection fail"})

@app.route('/api/getUserType', methods=['POST'])
def getUserType():
    try:
        data = request.get_json()
        print("Received data:", data)  # 打印接收到的數據
        connection = connect.connect_to_db()
        if connection is not None:
            with connection.cursor() as cursor:
                sql = "SELECT UserType FROM ACCOUNT WHERE ID = %s"
                cursor.execute(sql, (data['userID'],))
                result = cursor.fetchone()
                if result is not None:
                    return jsonify({"status": "success", "data": result[0]})
                else:
                    return jsonify({"status": "fail", "message": "User not found"})
        else:
            return jsonify({"status": "fail", "message":  'sql connection fail'})
    except Exception as ex:
        print(f"Error: {ex}")
        traceback.print_exc()

if __name__ == '__main__':
    app.run(debug=True)
