import smtplib
from email.mime.text import MIMEText
import json

class EmailNotifier:
    def __init__(self, config_path="src/config/config.json"):
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
            self.smtp_server = config["smtp_server"]
            self.port = config["smtp_port"]
            self.username = config["smtp_username"]
            self.password = config["smtp_password"]

    def send_email(self, to_address, subject, content):
        """Send an email notification."""
        msg = MIMEText(content)
        msg["Subject"] = subject
        msg["From"] = self.username
        msg["To"] = to_address

        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(self.username, to_address, msg.as_string())
