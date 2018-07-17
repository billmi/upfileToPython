# -*- coding:utf-8 -*-
import datetime
import os

__authro__ = 'Bill'

from flask import Flask
from flask import request
from flask import jsonify
from flask_script import Manager, Server
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.debug = True

manager = Manager(app)
manager.add_command('runServ', Server(host='127.0.0.1', port=3000))

SUCC_CODE = 1
ERROR_CODE = 0

VALI_KEY = "cc123456"


def get_file_dir():
    return os.path.dirname(os.path.abspath(__file__)) + "\\"


def response_message(data=[], message='Success !', code=SUCC_CODE):
    nowDatetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    resInfo = {'code': None, 'data': None, 'msg': None, 'timestamp': nowDatetime}
    resInfo['data'] = data
    resInfo['msg'] = message
    resInfo['code'] = code
    return jsonify(resInfo)


@app.route('/upload', methods=['POST'])
def upload():
    message = "上传成功!"
    key = request.form.get('key', '').strip()
    if key == '' or key != VALI_KEY:
        message = "秘钥错误!"
        return response_message([], message, ERROR_CODE)
    f = request.files['file']
    if not f:
        message = "上传失败!"
        return response_message([], message, ERROR_CODE)
    fname = secure_filename(f.filename)
    f.save(os.path.join("./", fname))
    return response_message([], message)


if __name__ == "__main__":
    manager.run()
