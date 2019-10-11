
from flask import Flask, abort, request, jsonify

app = Flask(__name__)

# 测试数据暂时存放
names = []

@app.route('/add_name/', methods=['POST'])
def add_name():
    if not request.json or 'id' not in request.json or 'name' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'name': request.json['name']
    }
    names.append(task)
    return jsonify({'result': 'success'})

@app.route('/get_name/', methods=['GET'])
def get_name():
    print(request.args.to_dict().keys())
    print(request.args.to_dict())
    if not request.args.to_dict() or 'id' not in request.args.to_dict():
        # 没有指定id则返回全部
        return jsonify(names)
    else:
        task_id = request.args['id']
        print(task_id)
        task = list(filter(lambda t: t['id'] == task_id, names))
        print(task)
        if task:
            return jsonify(task)
        else:
            return jsonify({'result': 'not found'})


if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(debug=True)