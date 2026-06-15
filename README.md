# ⏳ Enterprise Workflow Scheduler

A lightweight, student-friendly Python web application built with **Flask** to schedule, track, and manage core backend workflows or tasks. This application helps developers organize recurring operations, monitor system statuses, and track task lifecycles in real time.

🔗 **[Live Demo on Hugging Face Spaces](https://huggingface.co)**

---

## 🏗️ System Architecture

The application follows a modular architecture pattern that separates the user interface, backend routing, business rules, and storage mechanisms.

### 🔄 Data Flow Diagram
Below is the structural layout showing how data travels through the application files:

![System Architecture Diagram](assets/system_architecture.png) 
*(Note: Replace 'architecture_blocks.png' with your actual architecture image filename after uploading it to your repo)*

1. **User Browser**: The client interface where you interact with tasks and view analytics dashboards.
2. **templates/**: Houses the visual HTML/Jinja2 files that render the front-end forms and task status cards.
3. **app.py**: The central network routing hub and application controller handling web requests.
4. **todo_logic.py**: The core application brain containing business logic, calculations, and rules.
5. **storage.py**: The data persistence abstraction module acting as a virtual filing cabinet to save records.
6. **models.py**: Defines the baseline task object template structures (IDs, dates, statuses).

---

## 🖥️ Application UI Preview

The dashboard features a live **Metrics Overview** tracker, an **Add New Task** configuration manager, and an interactive **Task Registry** with status control buttons.

![Application Interface Screenshot](ui_screenshot.png)
*(Note: Replace 'ui_screenshot.png' with your actual dashboard screenshot filename after uploading it to your repo)*

---

## 🚀 Getting Started Locally

Follow these quick steps to get a development environment up and running on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com
cd Enterprise-workflow-scheduler
```

### 2. Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Fire Up the Server
```bash
python app.py
```
Once initialized, navigate your local browser environment to **`http://127.0.0.1:5000`**.

---

## 🛠️ Features
* 📊 **Live Metrics Tracker**: Displays real-time calculations for Pending, In Progress, and Completed workflows.
* 🕒 **Time-Based Scheduling**: Configure custom operational execution dates and timestamps.
* ⚡ **State Control**: Quickly toggle tasks between active, running, or done states using simple dashboard controllers.
