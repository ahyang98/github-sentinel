from src.storage.db_handler import DBHandler
from src.subscription.manager import SubscriptionManager
from src.fetcher.github_api import GitHubAPIClient
from src.report.generator import ReportGenerator
from src.notifier.email_notifier import EmailNotifier
from src.scheduler.task_scheduler import TaskScheduler

def fetch_and_notify():
    db_handler = DBHandler("GitHubSentinel/subscriptions.db")
    subscription_manager = SubscriptionManager(db_handler)

    # Initialize API client, report generator, and notifier
    api_client = GitHubAPIClient(token="YOUR_GITHUB_TOKEN")
    report_generator = ReportGenerator()
    email_notifier = EmailNotifier(smtp_server="smtp.example.com", port=587, username="user@example.com", password="password")

    updates = []
    for repo in subscription_manager.list_subscriptions():
        try:
            latest_release = api_client.fetch_latest_release(repo)
            updates.append(f"{repo}: {latest_release['name']} - {latest_release['html_url']}")
        except Exception as e:
            updates.append(f"Failed to fetch updates for {repo}: {e}")

    report_content = report_generator.generate_markdown_report(updates)
    report_generator.save_report(report_content, "GitHubSentinel/report.md")

    email_notifier.send_email("recipient@example.com", "GitHub Sentinel Report", report_content)

    print("Update fetched, report generated, and notification sent.")

def main():
    task_scheduler = TaskScheduler()
    task_scheduler.add_task(fetch_and_notify, interval=24)  # Run daily
    task_scheduler.start()

    print("Scheduler started. Press Ctrl+C to exit.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        task_scheduler.stop()

if __name__ == "__main__":
    main()
