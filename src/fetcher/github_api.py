import requests

class GitHubAPIClient:
    def __init__(self, token):
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"token {token}"}

    def fetch_repo_updates(self, repo):
        """Fetch updates for a specific repository."""
        url = f"{self.base_url}/repos/{repo}/events"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_latest_release(self, repo):
        """Fetch the latest release of a repository."""
        url = f"{self.base_url}/repos/{repo}/releases/latest"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
