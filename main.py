from src.config.config import Config
from src.storage.db_handler import DBHandler
from src.subscription.manager import SubscriptionManager
from src.fetcher.github_api import GitHubAPIClient
from src.notifier.email_notifier import EmailNotifier
from src.scheduler.task_scheduler import TaskScheduler
from src.report.generator import ReportGenerator
from src.ui.cli import CLI


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
    global subscription_manager, github_client, email_notifier, report_generator, scheduler

    # Load configuration
    config = Config()

    # Initialize components
    db_handler = DBHandler()
    subscription_manager = SubscriptionManager(db_handler)
    github_client = GitHubAPIClient(config)
    email_notifier = EmailNotifier(config)
    report_generator = ReportGenerator()
    scheduler = TaskScheduler(config)

    # Load default subscriptions
    subscription_manager.load_default_subscriptions()

    # **立即获取更新**：在程序启动时立即获取一次仓库更新
    fetch_and_notify()

    # Start the scheduler (this is a non-blocking call)
    scheduler.start()

    # Initialize CLI
    cli = CLI(subscription_manager, fetch_and_notify)

    print("Welcome to GitHub Sentinel! Type 'help' for available commands.")

    # Start interactive loop
    while True:
        # Get user input
        user_input = input("> ").strip()

        # Parse command and arguments
        if user_input:
            parts = user_input.split()
            command = parts[0]
            args = parts[1:]
            # Handle the command
            cli.handle_command(command, *args)


if __name__ == "__main__":
    main()
