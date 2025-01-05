from src.subscription.manager import SubscriptionManager
from src.fetcher.github_api import GitHubAPIClient
from src.notifier.email_notifier import EmailNotifier
from src.report.generator import ReportGenerator
from src.scheduler.task_scheduler import TaskScheduler
from src.storage.db_handler import DBHandler
from src.ui.cli import CLI
import os

if __name__ == "__main__":
    # Initialize components
    db_handler = DBHandler()
    subscription_manager = SubscriptionManager(db_handler)
    github_client = GitHubAPIClient(os.getenv("GITHUB_TOKEN", "your_token_here"))
    email_notifier = EmailNotifier(
        smtp_server=os.getenv("SMTP_SERVER", "smtp.example.com"),
        port=int(os.getenv("SMTP_PORT", 587)),
        username=os.getenv("SMTP_USER", "user@example.com"),
        password=os.getenv("SMTP_PASSWORD", "your_password")
    )
    report_generator = ReportGenerator()
    scheduler = TaskScheduler()

    # Choose interface to start
    interface = input("Choose interface to start (cli/web): ")
    if interface == "cli":
        cli = CLI(subscription_manager)
        cli.display_menu()
    elif interface == "web":
        from src.ui.web import app
        app.run(debug=True)
    else:
        print("Invalid choice. Exiting...")
