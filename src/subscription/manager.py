import json
import os

class SubscriptionManager:
    def __init__(self, storage, config_path="config/subscriptions.json"):
        self.storage = storage
        self.config_path = config_path

    def add_subscription(self, repo_url):
        """Add a new repository subscription."""
        self.storage.save_subscription(repo_url)

    def remove_subscription(self, repo_url):
        """Remove an existing repository subscription."""
        self.storage.delete_subscription(repo_url)

    def list_subscriptions(self):
        """List all subscribed repositories."""
        return self.storage.get_subscriptions()

    def load_default_subscriptions(self):
        """Load default subscriptions from the JSON configuration."""
        if not os.path.exists(self.config_path):
            print(f"Config file not found: {self.config_path}")
            return
        with open(self.config_path, "r") as file:
            data = json.load(file)
            for subscription in data.get("default_subscriptions", []):
                self.add_subscription(subscription["repo_name"])
