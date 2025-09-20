from flask import Flask, jsonify, request
app = Flask(__name__)

# In-memory storage for users
users = [
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Jane Doe", "age": 25}
]

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users})

@app.route('/')
def home():
    return "<h2>Welcome! Visit <a href='/users'>/users</a> to see all users.</h2>"

# GET a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# POST a new user
@app.route('/users', methods=['POST'])
def create_user():
    new_user = {
        "id": len(users) + 1,
        "name": request.json['name'],
        "age": request.json['age']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT (update) a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    user['name'] = request.json.get('name', user['name'])
    user['age'] = request.json.get('age', user['age'])
    return jsonify(user)

# DELETE a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    print("Server running at http://localhost:5000")
    app.run(debug=True)