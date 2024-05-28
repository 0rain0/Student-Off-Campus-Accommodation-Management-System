from flask import Flask, jsonify,request
from flask_cors import CORS
import json
import connect

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)


# sanity check route
@app.route('/')
def index():
    return jsonify({"message": "Hello, this is a CORS-enabled Flask application!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_data()
    data = json.loads(data)
    print(sum)
    connection = connect.connect_to_db()
    if connection is not None:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user WHERE username = %s AND password = %s"
            cursor.execute(sql, (data['username'], data['password']))
            result = cursor.fetchone()
            if result is not None:
                return jsonify({"login": 'success'})
            else:
                return jsonify({"login": 'fail'})
    else:
        return jsonify({"login": 'sql connection fail'})

if __name__ == '__main__':
    app.run(debug=True)
