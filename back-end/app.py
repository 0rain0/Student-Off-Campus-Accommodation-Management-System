from flask import Flask, jsonify, request, redirect
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
        connection = connect.connect.connect_to_db()
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
