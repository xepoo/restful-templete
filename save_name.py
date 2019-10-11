
from flask import Flask, abort, request, jsonify

app = Flask(__name__)

# 测试数据暂时存放
tasks = []

@app.route('/add_name/', methods=['POST'])
def add_name():
    if not request.json or 'id' not in request.json or 'name' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'name': request.json['name']
    }
    tasks.append(task)
    return jsonify({'result': 'success'})

if __name__ == "__main__":
    app.run(debug=True)