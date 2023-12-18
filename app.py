from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id" : 1, "title" : "Task 1", "description" : "Description for Task 1"},
    {"id" : 2, "title" : "Task 2", "description" : "Description for Task 2"},
    {"id" : 3, "title" : "Task 3", "description" : "Description for Task 3"},
    {"id" : 4, "title" : "Task 4", "description" : "Description for Task 4"}
]

# Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


# Get a task by id
@app.route("/task/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        return jsonify(task)
    else:
        return jsonify({"error":"Task not found"}), 404



# Create a new task
@app.route("/task", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = {"id": len(tasks) + 1, "title": data["title"], "description": data["description"]}
    tasks.append(new_task)
    return jsonify(new_task), 201


# Update a task
@app.route("/task/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        data = request.get_json()
        task.update(data)
        return jsonify(task)
    else:
        return jsonify({"error": "Task not found"}), 404
    
# Delete a task
@app.route("/task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)