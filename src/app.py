from flask import Flask, jsonify, request, json


app = Flask(__name__)

todos = [{"label":"My first task","done":False}]

@app.route('/todos', methods=['GET'])
def get_todo():

    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    # request_body = request.data
    decoded = json.loads(request.data)
    print(decoded)
    todos.insert(0, decoded)
    print("Incoming request with the following body", decoded)
    return jsonify(todos), 200

@app.route('/todos/<int:fid>', methods=['DELETE'])
def del_todos(fid):
    if fid < len(todos):
        todos.pop(fid)
    else:
        raise Exception("ID not found", status_code=404)

    return jsonify(todos), 200

@app.route('/todos/<int:fid>', methods=['DELETE'])
def delete_todo(fid):
    if fid < len(todos):
        todos.remove(fid)
        print("This is the position to delete: ", fid)
    else:
        raise Exception("unable to do it")

    return jsonify(todos), 200



# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

# @app.route('/todos', methods=['POST'])
# def add_new_todo():
#     decode_object = request.get_json()
#     todos.append(decode_object) 
#     print("Incoming request with the following body", decode_object)
#     return jsonify(todos), 200
