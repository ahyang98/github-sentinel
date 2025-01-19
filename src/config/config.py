import json

class Config:
    def __init__(self, config_path="config/config.json"):
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
        self.github_token = config.get("github_token")
        self.smtp_server = config.get("smtp_server")
        self.smtp_port = config.get("smtp_port")
        self.smtp_username = config.get("smtp_username")
        self.smtp_password = config.get("smtp_password")
        self.fetch_interval = config.get("fetch_interval", 24)
        self.db_path = config.get("db_path", "GitHubSentinel/subscriptions.db")
        self.openai_api_key = config.get("openai_api_key")
