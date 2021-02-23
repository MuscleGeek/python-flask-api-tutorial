from flask import Flask, jsonify, request,json
app = Flask(__name__)

todos = [{"label":"My first task","done":False}]

@app.route('/todos', methods=['GET'])
def hello_world():

    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    json_text = jsonify(todos)
    return json_text 

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)


# request_body = request.data
#     decoded_object = json.loads(request_body)
#     todos.append(decoded_object)
#     json_text = jsonify(todos)
#     return json_text 

# @app.route('/todos', methods=['POST'])
# def add_new_todo():
#     decode_object = request.get_json()
#     todos.append(decode_object) 
#     print("Incoming request with the following body", decode_object)
#     return jsonify(todos), 200