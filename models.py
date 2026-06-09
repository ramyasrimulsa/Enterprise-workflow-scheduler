class Task:
    def __init__(self, task_id, title, description, schedule_time, status="Pending"):
        self.id = int(task_id)
        self.title = str(title).strip()
        self.description = str(description).strip()
        self.schedule_time = str(schedule_time).strip()  # Format: YYYY-MM-DD HH:MM (24-hour)
        self.status = str(status).strip()

    def to_dict(self):
        """Converts object details into a dictionary for JSON writing."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "schedule_time": self.schedule_time,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Task object from dictionary data loaded from JSON."""
        return cls(data["id"], data["title"], data["description"], data["schedule_time"], data["status"])
