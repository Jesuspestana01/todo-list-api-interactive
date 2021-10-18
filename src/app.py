from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [{"label": "My first taks", "done": False}]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    new_todo = json.loads(request.data)
    todos.append(new_todo)
    response = jsonify(todos)
    print("Incoming request with the following body", new_todo)
    return response, 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    response = jsonify(todos)
    print("This is the position to delete: ",position)
    return response, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)