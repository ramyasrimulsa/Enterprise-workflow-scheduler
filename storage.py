import json
import os

class JSONStorageManager:
    _instance = None
    FILENAME = "tasks.json"

    def __new__(cls):
        """Implements Singleton Pattern: Ensures only one file stream channel exists."""
        if cls._instance is None:
            cls._instance = super(JSONStorageManager, cls).__new__(cls)
        return cls._instance

    def load_raw_data(self):
        """Safely reads records from the file system."""
        if not os.path.exists(self.FILENAME):
            return []
        try:
            with open(self.FILENAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []

    def save_raw_data(self, data_list):
        """Writes data updates smoothly onto the physical storage disk."""
        try:
            with open(self.FILENAME, "w", encoding="utf-8") as file:
                json.dump(data_list, file, indent=4)
                return True
        except IOError:
            return False
