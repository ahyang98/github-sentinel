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
        """Save a new subscription."""
        query = "INSERT INTO subscriptions (repo_url) VALUES (?)"
        self.conn.execute(query, (repo_url,))
        self.conn.commit()

    def delete_subscription(self, repo_url):
        """Delete a subscription."""
        query = "DELETE FROM subscriptions WHERE repo_url = ?"
        self.conn.execute(query, (repo_url,))
        self.conn.commit()

    def get_subscriptions(self):
        """Retrieve all subscriptions."""
        query = "SELECT repo_url FROM subscriptions"
        return [row[0] for row in self.conn.execute(query)]
