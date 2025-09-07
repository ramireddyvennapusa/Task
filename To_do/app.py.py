from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API (replace with your key)
genai.configure(api_key="AIzaSyBQiGk4ebXGGSqqdgZdYzQlBsOs4PBthtE")
model = genai.GenerativeModel("gemini-1.5-flash")

tasks = {}
task_id = 1

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    global task_id
    data = request.get_json()
    task = {"id": task_id, "title": data.get("title", ""), "done": False}
    tasks[task_id] = task
    task_id += 1
    return jsonify(task)

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    if id not in tasks:
        return jsonify({"error": "Task not found"}), 404
    data = request.get_json()
    tasks[id]["title"] = data.get("title", tasks[id]["title"])
    tasks[id]["done"] = data.get("done", tasks[id]["done"])
    return jsonify(tasks[id])

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    if id not in tasks:
        return jsonify({"error": "Task not found"}), 404
    removed = tasks.pop(id)
    return jsonify(removed)

@app.route("/tasks/ai", methods=["POST"])
def ai_generate_task():
    data = request.get_json()
    prompt = data.get("prompt", "Suggest a task")
    try:
        response = model.generate_content(prompt)
        return jsonify({"ai_task": response.text})
    except:
        return jsonify({"error": "AI feature not available"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)

