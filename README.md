### GitHub Sentinel: Your Intelligent GitHub Update Companion

**GitHub Sentinel** is an open-source AI-driven agent, designed specifically for developers and project managers to streamline the process of tracking updates from GitHub repositories. By automating subscription management, update retrieval, notifications, and report generation, GitHub Sentinel ensures you stay informed about repository changes in a timely and efficient manner. 

---

### Features

- **Subscription Management**: Add, remove, and list GitHub repository subscriptions easily.
- **Automated Update Retrieval**: Periodically fetch the latest updates from your subscribed repositories.
- **Notification System**: Stay informed through customizable notifications (e.g., email).
- **Comprehensive Reports**: Generate Markdown reports for quick sharing and review.
- **Multiple Interfaces**: Access via CLI or web interface, catering to your workflow preferences.
- **Customizable Scheduling**: Flexible task scheduling to retrieve updates daily, weekly, or at intervals of your choice.

---

### Benefits

1. **Enhanced Collaboration**: Keeps all team members updated on project changes, improving efficiency and communication.
2. **Improved Workflow**: Automates repetitive tasks, allowing developers and managers to focus on more strategic activities.
3. **Scalability**: Handles multiple repositories, making it suitable for individual projects or large-scale enterprise needs.
4. **Transparency**: Detailed and accessible reporting ensures that no critical updates are overlooked.
5. **Ease of Use**: Offers an intuitive CLI for quick operations and a web-based interface for broader accessibility.

---

### Getting Started

#### Prerequisites
1. Python 3.8 or higher installed on your system.
2. SQLite for lightweight database management.
3. Required Python packages listed in the `requirements.txt` file.

#### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/GitHubSentinel.git
   cd GitHubSentinel
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### Configuration
1. Set up environment variables for GitHub API Token and SMTP settings:
   ```bash
   export GITHUB_TOKEN=your_github_personal_access_token
   export SMTP_SERVER=smtp.example.com
   export SMTP_PORT=587
   export SMTP_USER=your_email@example.com
   export SMTP_PASSWORD=your_email_password
   ```

#### Usage
1. Start the application:
   ```bash
   python src/main.py
   ```
2. Choose your preferred interface:
   - **CLI**: Interact directly with the system through command-line menus.
   - **Web**: Access the system through a Flask-powered web interface.

#### Running Tests
1. Run unit tests:
   ```bash
   pytest tests/
   ```

---

### License
GitHub Sentinel is released under the MIT License. See `LICENSE` for details.

---

This project is an ongoing effort. Contributions are welcome! For feature suggestions, bug reports, or pull requests, visit the [GitHub repository](https://github.com/your-username/GitHubSentinel). Stay connected, stay updated, and let GitHub Sentinel take the hassle out of repository tracking!