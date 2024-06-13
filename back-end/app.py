from flask import Flask, jsonify, request
from flask_cors import CORS
import traceback
import connect

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

def convert_to_dict(tuples_list):
    keys = ["id", "department", "class", "grade", "teacher", "number"]
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
                sql = "SELECT * FROM account WHERE ID = %s AND PassWord = %s"
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
                data = convert_to_dict(modified_result)
                for d in data:
                    tid = d['teacher']
                    sql = "SELECT name FROM Teacher WHERE tid = %s"
                    cursor.execute(sql, (tid,))
                    result = cursor.fetchone()
                    d['teacher'] = result[0]
                return data          
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
                cursor.execute("SELECT sid, name FROM STUDENT")
                students = cursor.fetchall()
                student_list = [{"sid": student[0], "name": student[1]} for student in students]
                
                cursor.execute("SELECT COUNT(*) FROM STUDENT")
                total = cursor.fetchone()[0]
                
                cursor.execute("SELECT cid FROM CLASS WHERE department=%s and grade=%s and section=%s", (department, grade, section,))
                cid = cursor.fetchone()[0]
                
                cursor.execute("SELECT sid, name FROM STUDENT WHERE CLASS = %s LIMIT %s OFFSET %s", (cid, per_page, offset))
                students = cursor.fetchall()
                
                # 将数据转换为字典列表
                student_selected = [{"sid": student[0], "name": student[1]} for student in students]
                print(student_selected)
                
                return jsonify({"status": "success", "student_all": student_list, "total": total, "student_selected": student_selected})
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

                # 清空该班级的所有学生
                cursor.execute(
                    "UPDATE STUDENT SET class=NULL WHERE class=%s", (cid,)
                )

                # 添加选中的学生到该班级
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

    


if __name__ == '__main__':
    app.run(debug=True)
