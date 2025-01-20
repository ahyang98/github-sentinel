import datetime
import os
import markdown
from llm.llm_client import LLMClient
from fetcher.github_api import GitHubAPIClient

class ReportGenerator:
    def __init__(self, llm_client: LLMClient=None, github_client: GitHubAPIClient=None):
        self.llm_client = llm_client
        self.github_client = github_client

    def generate_markdown_report(self, updates):
        """Generate a Markdown report from updates."""
        content = "# Repository Updates\n\n"
        for update in updates:
            content += f"- {update}\n"
        return markdown.markdown(content)

    def save_report(self, content, file_path):
        """Save the report to a file."""
        # Ensure the directory exists
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(file_path, "w") as file:
            file.write(content)
    
    def save_daily_report(self, report_content, repo):
        """Save the daily report to a file."""
        # Ensure the directory exists
        # Save the report
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        report_file = f"GitHubSentinel/reports/{repo}_{date_str}_report.md"
        with open(report_file, "w") as file:
            file.write(f"# {repo} Daily Report - {date_str}\n\n")
            file.write(report_content)
    
    def export_daily_progress(self, repo, updates, filename):
        with open(filename, "w") as file:
            file.write(f"# Daily Progress for {repo}\n\n")
            file.write("## Issues\n")
            for issue in updates["issues"]:
                file.write(f"- {issue['title']} (#{issue['number']})\n")

            file.write("\n## Pull Requests\n")
            for pr in updates["pull_requests"]:
                file.write(f"- {pr['title']} (#{pr['number']})\n")

            file.write("\n## Commits\n")
            for commit in updates["commits"]:
                file.write(f"- {commit['commit']['message']} ({commit['sha'][:7]})\n")
    
    def fetch_and_generate_report(self, repo):                
        issues = self.github_client.fetch_issues(repo)
        prs = self.github_client.fetch_pull_requests(repo)
        commits = self.github_client.fetch_commits(repo)

        # Save issues, PRs, and commits to markdown
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        markdown_file = f"GitHubSentinel/reports/{repo}_{date_str}_progress.md"
        directory = os.path.dirname(markdown_file)
        if directory and not os.path.exists(directory):
            os.makedirs(directory) 
        
        with open(markdown_file, "w", encoding="utf-8") as file:
            file.write(f"# {repo} Daily Progress - {date_str}\n\n")
            file.write("## Issues\n")
            for issue in issues:
                file.write(f"- {issue['title']} (#{issue['number']}) - {issue['user']['login']}\n")
                file.write(f"  {issue['html_url']}\n")
            file.write("\n## Pull Requests\n")
            for pr in prs:
                file.write(f"- {pr['title']} (#{pr['number']}) - {pr['user']['login']}\n")
                file.write(f"  {pr['html_url']}\n")
            file.write("\n## Commits\n")
            for commit in commits:
                file.write(f"- {commit['commit']['message']} - {commit['commit']['author']['name']}\n")
                file.write(f"  {commit['html_url']}\n")

        # Call GPT-4 to generate report
        report_content = self.llm_client.generate_report_from_issues_prs_commits(issues, prs, commits)
        report_file = f"GitHubSentinel/reports/{repo}_{date_str}_report.md"
        with open(report_file, "w", encoding="utf-8") as file:
            file.write(f"# {repo} Daily Report - {date_str}\n\n")
            file.write(report_content)
    
    def generate_daily_report(self, file_path:str):
        all_content = []        
        with open(file_path, "r", encoding="utf-8") as f:
            all_content.append(f.read())

        combined_content = "\n\n".join(all_content)
        prompt = f"""
You are an AI assistant tasked with summarizing daily progress reports. Below is the content of all reports for {datetime.date}:

{combined_content}

Please generate a summary in formal Markdown format, including separate sections for issues, pull requests, and commits.
"""
        # Use GPT-4 API to generate the summary
        summary = self.llm_client.generate_summary(prompt)
        report_file = f"{file_path.split('.')[0]}_report.md"
        with open(report_file, "w", encoding="utf-8") as file:
            # file.write(f"# {repo} Daily Report - {date_str}\n\n")
            file.write(summary)
        return summary

    def generate_range_report(self, repo:str, start_date:str, end_date:str):
        issues = self.github_client.fetch_issues(repo, start_date, end_date)
        prs = self.github_client.fetch_pull_requests(repo, start_date, end_date)
        commits = self.github_client.fetch_commits(repo, start_date, end_date)
        # Save issues, PRs, and commits to markdown        
        markdown_file = f"GitHubSentinel/reports/{repo}_{start_date}_{end_date}_progress.md"
        directory = os.path.dirname(markdown_file)
        if directory and not os.path.exists(directory):
            os.makedirs(directory) 
        
        with open(markdown_file, "w", encoding="utf-8") as file:
            file.write(f"# {repo} Progress - {start_date}~{end_date}\n\n")
            file.write("## Issues\n")
            for issue in issues:
                file.write(f"- {issue['title']} (#{issue['number']}) - {issue['user']['login']}\n")
                file.write(f"  {issue['html_url']}\n")
            file.write("\n## Pull Requests\n")
            for pr in prs:
                file.write(f"- {pr['title']} (#{pr['number']}) - {pr['user']['login']}\n")
                file.write(f"  {pr['html_url']}\n")
            file.write("\n## Commits\n")
            for commit in commits:
                file.write(f"- {commit['commit']['message']} - {commit['commit']['author']['name']}\n")
                file.write(f"  {commit['html_url']}\n")

        # Call GPT-4 to generate report
        report_content = self.llm_client.generate_report_from_issues_prs_commits(issues, prs, commits)
        report_file = f"GitHubSentinel/reports/{repo}_{start_date}_{end_date}_report.md"
        with open(report_file, "w", encoding="utf-8") as file:
            file.write(f"# {repo} Report - {repo}_{start_date}_{end_date}_\n\n")
            file.write(report_content)
