from src.storage.db_handler import DBHandler
from src.subscription.manager import SubscriptionManager

def main():
    db_handler = DBHandler("GitHubSentinel/subscriptions.db")
    subscription_manager = SubscriptionManager(db_handler)

    # Load default subscriptions
    subscription_manager.load_default_subscriptions()

    # List current subscriptions
    print("Loaded subscriptions:")
    for repo in subscription_manager.list_subscriptions():
        print(f"- {repo}")

if __name__ == "__main__":
    main()
