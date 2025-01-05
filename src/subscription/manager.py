class SubscriptionManager:
    def __init__(self, storage):
        self.storage = storage

    def add_subscription(self, repo_url):
        """Add a new repository subscription."""
        self.storage.save_subscription(repo_url)

    def remove_subscription(self, repo_url):
        """Remove an existing repository subscription."""
        self.storage.delete_subscription(repo_url)

    def list_subscriptions(self):
        """List all subscribed repositories."""
        return self.storage.get_subscriptions()
