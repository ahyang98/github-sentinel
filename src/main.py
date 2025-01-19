from config.config import Config
from storage.db_handler import DBHandler
from subscription.manager import SubscriptionManager
from fetcher.github_api import GitHubAPIClient
from notifier.email_notifier import EmailNotifier
from scheduler.task_scheduler import TaskScheduler
from report.generator import ReportGenerator
from ui.cli import CLI
from llm.llm_client import LLMClient


def main():
    global subscription_manager, github_client, email_notifier, report_generator, scheduler

    # Load configuration
    config = Config()

    # Initialize components
    db_handler = DBHandler()
    subscription_manager = SubscriptionManager(db_handler)
    llm_client = LLMClient(config)
    github_client = GitHubAPIClient(config)
    email_notifier = EmailNotifier(config)
    report_generator = ReportGenerator(llm_client, github_client)
    scheduler = TaskScheduler(config)

    # Load default subscriptions
    subscription_manager.load_default_subscriptions()

    # Start the scheduler (this is a non-blocking call)
    scheduler.start()

    # Initialize CLI
    cli = CLI(github_client, subscription_manager, report_generator)

    # cli.fetch_updates()

    scheduler.add_task(cli.fetch_updates)

    print("Welcome to GitHub Sentinel! Type 'help' for available commands.")
    cli.print_help()

    # Start interactive loop
    while True:
        # Get user input
        user_input = input("> ").strip()

        if user_input in ['exit', 'quit']:
            break

        if not user_input:
            continue

        # Parse command and arguments        
            # Handle the command
        cli.run(user_input)


if __name__ == "__main__":
    main()
