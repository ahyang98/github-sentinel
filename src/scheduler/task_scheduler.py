from apscheduler.schedulers.background import BackgroundScheduler

class TaskScheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def add_task(self, func, interval):
        """Add a periodic task."""
        self.scheduler.add_job(func, 'interval', hours=interval)

    def start(self):
        """Start the scheduler."""
        self.scheduler.start()

    def stop(self):
        """Stop the scheduler."""
        self.scheduler.shutdown()
