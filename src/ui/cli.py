import sys

class CLI:
    def __init__(self, subscription_manager, fetch_and_notify_callback):
        self.manager = subscription_manager
        self.fetch_and_notify_callback = fetch_and_notify_callback

    def display_help(self):
        """Display help for the CLI commands."""
        help_message = """
Usage: github-sentinel <command> [options]

Commands:
  add <repo_url>       Add a new repository to the subscription list
  remove <repo_url>    Remove a repository from the subscription list
  list                 List all subscribed repositories
  fetch                Fetch updates for subscribed repositories
  report               Generate a report of the latest updates
  exit                 Exit the tool
  help                 Show this help message

Examples:
  github-sentinel add https://github.com/langchain-ai/langchain
  github-sentinel fetch
  github-sentinel list
"""
        print(help_message)

    def handle_command(self, command, *args):
        """Handle the command and its options."""
        if command == "add":
            if len(args) != 1:
                print("Error: 'add' command requires a repository URL.")
            else:
                repo_url = args[0]
                self.manager.add_subscription(repo_url)
                print(f"Added subscription for {repo_url}")
        elif command == "remove":
            if len(args) != 1:
                print("Error: 'remove' command requires a repository URL.")
            else:
                repo_url = args[0]
                self.manager.remove_subscription(repo_url)
                print(f"Removed subscription for {repo_url}")
        elif command == "list":
            self.list_subscriptions()
        elif command == "fetch":
            self.fetch_and_notify_callback()
            print("Updates fetched and report generated.")
        elif command == "report":
            self.generate_report()
        elif command == "help":
            self.display_help()
        elif command == "exit":
            print("Exiting GitHub Sentinel.")
            sys.exit(0)
        else:
            print(f"Error: Unknown command '{command}'. Use 'help' for available commands.")

    def list_subscriptions(self):
        """List all current subscriptions."""
        print("Subscribed Repositories:")
        subscriptions = self.manager.list_subscriptions()
        if not subscriptions:
            print("No subscriptions found.")
        for repo in subscriptions:
            print(f"- {repo}")

    def generate_report(self):
        """Generate a report of the latest updates."""
        print("Generating the report of the latest updates...")
        self.fetch_and_notify_callback()
        print("Report generated successfully.")