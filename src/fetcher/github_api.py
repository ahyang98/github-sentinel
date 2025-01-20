from datetime import datetime
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
    
    def fetch_issues(self, repo, start_date:str=None, end_date:str=None):
        """Fetch all issues from a repository."""
        url = f"{self.base_url}/repos/{repo}/issues"
        params = {'state': 'closed'}
        if start_date:
            params['since'] = datetime.strptime(start_date, "%Y-%m-%d").isoformat()
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        if end_date:
            issues = response.json()
            issues = [issue for issue in issues if issue['closed_at'] <= datetime.strptime(end_date, "%Y-%m-%d").isoformat()]
            return issues
        return response.json()

    def fetch_pull_requests(self, repo, start_date:str=None, end_date:str=None):
        """Fetch all pull requests from a repository."""
        url = f"{self.base_url}/repos/{repo}/pulls"
        params = {'state': 'closed'}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        prs = response.json()
        if start_date:            
            prs = [pr for pr in prs if pr['closed_at'] >= datetime.strptime(start_date, "%Y-%m-%d").isoformat()]
        if end_date:
            prs = [pr for pr in prs if pr['closed_at'] <= datetime.strptime(end_date, "%Y-%m-%d").isoformat()]
        return prs
    
    def fetch_commits(self, repo, start_date:str=None, end_date:str=None):
        """Fetch all commits from a repository."""
        url = f"{self.base_url}/repos/{repo}/commits"
        params = {'state': 'closed'}
        if start_date:
            params['since'] = datetime.strptime(start_date, "%Y-%m-%d").isoformat()
        if end_date:
            params['until'] = datetime.strptime(end_date, "%Y-%m-%d").isoformat()
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    
    
