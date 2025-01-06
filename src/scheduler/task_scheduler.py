from apscheduler.schedulers.background import BackgroundScheduler
import json

class TaskScheduler:
    def __init__(self, config_path="src/config/config.json"):
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
            self.interval = config["fetch_interval"]
        self.scheduler = BackgroundScheduler()

    def add_task(self, func):
        """Add a periodic task."""
        self.scheduler.add_job(func, 'interval', hours=self.interval)

    def start(self):
        """Start the scheduler."""
        self.scheduler.start()

    def stop(self):
        """Stop the scheduler."""
        self.scheduler.shutdown()
