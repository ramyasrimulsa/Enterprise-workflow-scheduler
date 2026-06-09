from models import Task
from storage import JSONStorageManager

class TodoEngine:
    def __init__(self):
        self.storage = JSONStorageManager()

    def get_all_tasks(self):
        """Retrieves items and sorts them chronologically by date and 24-hour time."""
        raw_data = self.storage.load_raw_data()
        all_tasks = [Task.from_dict(item) for item in raw_data]
        
        # Sorts tasks sequentially by their date/time string value
        all_tasks.sort(key=lambda task: task.schedule_time)
        return all_tasks

    def add_task(self, title, description, schedule_time):
        """Saves a new item into the sorted timeline arrays."""
        tasks = self.get_all_tasks()
        next_id = len(tasks) + 1
        
        new_task = Task(next_id, title, description, schedule_time)
        tasks.append(new_task)
        
        self.storage.save_raw_data([t.to_dict() for t in tasks])

    def update_status(self, task_id, new_status):
        """Finds an explicit task ID element and re-saves its status value."""
        tasks = self.get_all_tasks()
        for task in tasks:
            if task.id == task_id:
                task.status = new_status
                self.storage.save_raw_data([t.to_dict() for t in tasks])
                return True
        return False

    def delete_task(self, task_id):
        """Removes a task node and cleans the remaining IDs to avoid counting gaps."""
        tasks = self.get_all_tasks()
        filtered = [t for t in tasks if t.id != task_id]
        
        if len(tasks) == len(filtered):
            return False
            
        # Re-indexing step to keep ID values neat (1, 2, 3...)
        for index, task in enumerate(filtered, start=1):
            task.id = index
            
        self.storage.save_raw_data([t.to_dict() for t in filtered])
        return True

    def get_analytics(self):
        """Calculates daily schedule status percentages and shapes a progress bar."""
        tasks = self.get_all_tasks()
        total = len(tasks)
        if total == 0:
            return None
            
        pending = sum(1 for t in tasks if t.status == "Pending")
        in_progress = sum(1 for t in tasks if t.status == "In Progress")
        completed = sum(1 for t in tasks if t.status == "Completed")
        
        percentage = int((completed / total) * 100)
        bar_blocks = percentage // 5
        progress_bar = "█" * bar_blocks + "░" * (20 - bar_blocks)
        
        return {
            "total": total, "pending": pending, "progress": in_progress,
            "completed": completed, "percent": percentage, "bar": progress_bar
        }
