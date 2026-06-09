import os
from flask import Flask, render_template, request, jsonify
from todo_logic import TodoEngine

app = Flask(__name__)
engine = TodoEngine()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Returns chronologically sorted task objects as JSON array."""
    tasks = engine.get_all_tasks()
    return jsonify([t.to_dict() for t in tasks])

@app.route('/api/tasks', methods=['POST'])
def add_task():
    """Accepts form structures to seamlessly populate new workflow matrices."""
    data = request.json
    title = data.get('title', '').strip()
    description = data.get('description', '').strip()
    date_val = data.get('date', '').strip()   # Format: YYYY-MM-DD
    time_val = data.get('time', '').strip()   # Format: HH:MM

    if not title or not date_val or not time_val:
        return jsonify({"success": False, "error": "Missing required fields"}), 400

    schedule_time = f"{date_val} {time_val}"
    
    try:
        engine.add_task(title, description, schedule_time)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/tasks/<int:task_id>/status', methods=['PATCH'])
def update_status(task_id):
    """Updates status cleanly via targeted status adjustments."""
    data = request.json
    new_status = data.get('status') # Expected: 'In Progress' or 'Completed'
    
    success = engine.update_status(task_id, new_status)
    if success:
        return jsonify({"success": True})
    return jsonify({"success": False, "error": "Task not found"}), 404

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Drops task node and requests automated array matrix re-indexing."""
    success = engine.delete_task(task_id)
    if success:
        return jsonify({"success": True})
    return jsonify({"success": False, "error": "Task not found"}), 404

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    """Pulls structural data arrays straight out of analytical tracking metrics."""
    stats = engine.get_analytics()
    if not stats:
        return jsonify({
            "total": 0, "pending": 0, "progress": 0,
            "completed": 0, "percent": 0, "bar": "░" * 20
        })
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
