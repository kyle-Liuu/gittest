from flask import Flask, request,jsonify
import os
import time
from datetime import datetime


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "index"

@app.route('/interface', methods=['POST', 'GET'])
def interface():
    request_params = request.get_json()
    print("interface()", datetime.now())
    print("\n")
    print(request_params)
    print("\n")

    ret = False
    msg = "error"

    ret = True
    msg = "successful"

    response_data = {
        "code": 1000 if ret else 0,
        "msg": msg
    }
    return jsonify(response_data)

if __name__ == '__main__':
    # app.debug = True

    # 接收报警接口的数据上传
    # http://127.0.0.1:8072/interface
    app.run(host='0.0.0.0', port=8072, debug=False)