import sqlite3

class DBHandler:
    def __init__(self, db_path="subscriptions.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        """Create the subscriptions table if it doesn't exist."""
        query = """
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            repo_url TEXT UNIQUE
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def save_subscription(self, repo_url):
        """Save a new subscription, avoiding duplicates."""
        # Check if the repo_url already exists
        query = "SELECT COUNT(*) FROM subscriptions WHERE repo_url = ?"
        cursor = self.conn.execute(query, (repo_url,))
        count = cursor.fetchone()[0]

        if count == 0:
            # If repo_url does not exist, insert it
            query = "INSERT INTO subscriptions (repo_url) VALUES (?)"
            self.conn.execute(query, (repo_url,))
            self.conn.commit()
            print(f"Subscription to {repo_url} added successfully.")
        else:
            print(f"Repository {repo_url} is already subscribed.")

    def delete_subscription(self, repo_url):
        """Delete a subscription."""
        query = "DELETE FROM subscriptions WHERE repo_url = ?"
        self.conn.execute(query, (repo_url,))
        self.conn.commit()

    def get_subscriptions(self):
        """Retrieve all subscriptions."""
        query = "SELECT repo_url FROM subscriptions"
        return [row[0] for row in self.conn.execute(query)]
