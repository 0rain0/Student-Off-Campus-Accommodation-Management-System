from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import traceback
import connect

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

def convert_to_dict(tuples_list):
    keys = ["id", "department", "class", "grade", "teacher", "number"]
    dict_list = [dict(zip(keys, row)) for row in tuples_list]
    return dict_list

def generate_new_cid(cursor):
    cursor.execute("SELECT cid FROM CLASS ORDER BY cid DESC LIMIT 1")
    result = cursor.fetchone()[0]
    if result:
        last_cid = result
        new_cid_num = int(last_cid[1:]) + 1
        print(new_cid_num)
        new_cid = f"c{new_cid_num:03}"
        print(new_cid)
    else:
        new_cid = "c001"
    return new_cid

@app.route('/')
def index():
    return jsonify({"message": "Hello, this is a CORS-enabled Flask application!"})


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        print("Received data:", data)  # 打印接收到的數據
        connection = connect.connect.connect_to_db()
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
                if department:
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

@app.route('/receive_form',methods = ['GET','POST'])
def receive_form():
    user = request.form
    print(user)

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
                    SA_13 = {SA_13},
                    EN_01 = {EN_01},
                    EN_02 = {EN_02},
                    EN_03 = {EN_03},
                    EN_04 = {EN_04},
                    VI_01 = {VI_01},
                    VI_02 = {VI_02},
                    Result = {Result},
                    DI_01 = {DI_01},
                    DI_02 = {DI_02},
                    DI_03 = {DI_03},
                    DI_04 = {DI_04},
                    DI_05 = {DI_05},
                    EN_03_Des = '{EN_03_Des}',
                    EN_04_Des = '{EN_04_Des}',
                    VI_01_Des = '{VI_01_Des}',
                    RE_Des = '{RE_Des}',
                    RE_Memo = '{RE_Memo}',
                    DI_05_Des = '{DI_05_Des}'
                WHERE SID = '{SID}'
            """

        sql = sql.replace("'None'", "Null").replace("None", "Null")
        connect.update(sql)
        return redirect("http://localhost:5174/Successform")
    else:
        #未存在訪視紀錄，新增表單
        #需要有學號在資料庫內才能新增
        sql = f"""
                    insert into visit_form (State,DG,SID,S_Name,S_Tel,T_Name,
                                            V_Time,L_Name,L_Tel,R_Addr,RoommateN,
                                            RoommateP,RA,RentType,RoomType,Price,
                                            Deposit,recommend,SA_01,SA_02,SA_03,
                                            SA_04,SA_05,SA_06,SA_07,SA_08,SA_09,
                                            SA_10,SA_11,SA_12,SA_13,EN_01,EN_02,
                                            EN_03,EN_04,VI_01,VI_02,Result,DI_01,
                                            DI_02,DI_03,DI_04,DI_05,EN_03_Des,
                                            EN_04_Des,VI_01_Des,RE_Des,RE_Memo,
                                            DI_05_Des)
                    values (1,'{DG}','{SID}','{S_Name}','{S_Tel}','{T_Name}',
                            '{visit}','{L_Name}','{L_Tel}','{R_Addr}','{RoommateN}',
                            '{RoommateP}',{RA},{RentType},{RoomType},{Price},
                            {Deposit},{Recommend},{SA_01},{SA_02},{SA_03},{SA_04},
                            {SA_05},{SA_06},{SA_07},{SA_08},{SA_09},{SA_10},{SA_11},
                            {SA_12},{SA_13},{EN_01},{EN_02},{EN_03},{EN_04},{VI_01},
                            {VI_02},{Result},{DI_01},{DI_02},{DI_03},{DI_04},{DI_05},
                            '{EN_03_Des}','{EN_04_Des}','{VI_01_Des}','{RE_Des}',
                            '{RE_Memo}','{DI_05_Des}')
                """

        sql = sql.replace("'None'", "Null").replace("None", "Null")
        connect.update(sql)
        return redirect("http://localhost:5174/Successform")

if __name__ == '__main__':
    app.run(debug=True)
