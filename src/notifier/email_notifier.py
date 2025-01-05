import smtplib
from email.mime.text import MIMEText

class EmailNotifier:
    def __init__(self, smtp_server, port, username, password):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

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
