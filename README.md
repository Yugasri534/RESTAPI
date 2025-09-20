Perfect! Let’s break down **what your code does, step by step**, so it’s clear and ready for your internship submission.

---

## 1️ **Flask App Initialization**

```python
from flask import Flask, jsonify, request
app = Flask(__name__)
```

* **`Flask(__name__)`**: Creates a Flask web app instance.
* **`jsonify`**: Converts Python data (dict/list) to JSON responses.
* **`request`**: Lets you access incoming data (like POST or PUT JSON).

---

## 2️**In-Memory Data**

```python
users = [
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Jane Doe", "age": 25}
]
```

* Stores user data **temporarily in memory**.
* No database needed — simple for testing API concepts.
* Each user has an `id`, `name`, and `age`.

---

## 3️ **Routes (Endpoints)**

### a) Home route

```python
@app.route('/')
def home():
    return "<h2>Welcome! Visit <a href='/users'>/users</a> to see all users.</h2>"
```

* When visiting `http://localhost:5000/`, shows a simple HTML page with a link to `/users`.

---

### b) GET all users

```python
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users})
```

* **HTTP GET** on `/users` returns all users as JSON.
* Example output:

```json
{
  "users": [
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Jane Doe", "age": 25}
  ]
}
```

---

### c) GET user by ID

```python
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)
```

* `<int:user_id>` in the route captures the user ID from the URL.
* Finds the user in the list; if not found, returns **404 error**.

---

### d) POST (create) a user

```python
@app.route('/users', methods=['POST'])
def create_user():
    new_user = {
        "id": len(users) + 1,
        "name": request.json['name'],
        "age": request.json['age']
    }
    users.append(new_user)
    return jsonify(new_user), 201
```

* **HTTP POST** allows clients to send JSON to create a new user.
* Example JSON body:

```json
{
  "name": "Alice",
  "age": 28
}
```

* Assigns a new `id` automatically.
* Returns **201 Created** with the new user.

---

### e) PUT (update) a user

```python
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    user['name'] = request.json.get('name', user['name'])
    user['age'] = request.json.get('age', user['age'])
    return jsonify(user)
```

* Updates a user by ID using **HTTP PUT**.
* `request.json.get('field', user['field'])` allows partial updates (only the fields provided are changed).

---

### f) DELETE a user

```python
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted"})
```

* Deletes a user by filtering them out of the `users` list.
* Returns a simple JSON message confirming deletion.

---

## 4️ **Run the server**

```python
if __name__ == '__main__':
    print("Server running at http://localhost:5000")
    app.run(debug=True)
```

* `debug=True` enables **hot reload** and shows detailed errors.
* Running this file starts the server at `http://localhost:5000.
