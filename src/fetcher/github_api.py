import os
import requests

class GitHubAPIClient:
    def __init__(self, config):
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"token {os.environ.get("GITHUB_TOKEN")}"}

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
    
    def fetch_issues(self, repo):
        """Fetch all issues from a repository."""
        url = f"{self.base_url}/repos/{repo}/issues?state=open"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_pull_requests(self, repo):
        """Fetch all pull requests from a repository."""
        url = f"{self.base_url}/repos/{repo}/pulls?state=open"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def fetch_commits(self, repo):
        """Fetch all commits from a repository."""
        url = f"{self.base_url}/repos/{repo}/commits"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    
