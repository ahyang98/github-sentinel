from src.storage.db_handler import DBHandler
from src.subscription.manager import SubscriptionManager
from src.fetcher.github_api import GitHubAPIClient
from src.notifier.email_notifier import EmailNotifier
from src.scheduler.task_scheduler import TaskScheduler
from src.report.generator import ReportGenerator
from src.ui.cli import CLI
import json


def fetch_and_notify():
    subscriptions = subscription_manager.list_subscriptions()
    updates = []

    for repo in subscriptions:
        latest_release = github_client.fetch_latest_release(repo)
        updates.append(f"Latest release for {repo}: {latest_release.get('tag_name', 'N/A')}")

    if updates:
        report = report_generator.generate_markdown_report(updates)
        report_generator.save_report(report, "GitHubSentinel/reports/latest_report.md")
        email_notifier.send_email(
            "recipient@example.com", "GitHub Updates", "\n".join(updates)
        )


def main():
    global subscription_manager, github_client, email_notifier, report_generator

    with open("src/config/config.json", "r") as config_file:
        config = json.load(config_file)

    db_handler = DBHandler(config["db_path"])
    subscription_manager = SubscriptionManager(db_handler)
    github_client = GitHubAPIClient(config_path="src/config/config.json")
    email_notifier = EmailNotifier(config_path="src/config/config.json")
    report_generator = ReportGenerator()

    # Load default subscriptions
    subscription_manager.load_default_subscriptions()

    # Initialize CLI and TaskScheduler
    cli = CLI(subscription_manager)
    scheduler = TaskScheduler(config_path="src/config/config.json")
    scheduler.add_task(fetch_and_notify)
    scheduler.start()

    # Launch CLI
    cli.display_menu()

if __name__ == "__main__":
    main()
