from openai import OpenAI
import json
import os

class LLMClient:
    def __init__(self, config):
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
            base_url="https://api.openai.com/v1"
        )

    def generate_report_from_issues_prs_commits(self, issues, prs, commits):
        """Generate a formal daily report using GPT-4 with issues, PRs, and commits."""
        prompt = ""
        
        for issue in issues:
            prompt += f"- {issue['title']} (#{issue['number']}) - {issue['user']['login']}\n"
            prompt += f"  {issue['html_url']}\n"
        
        prompt += "\nPull Requests:\n"
        
        for pr in prs:
            prompt += f"- {pr['title']} (#{pr['number']}) - {pr['user']['login']}\n"
            prompt += f"  {pr['html_url']}\n"
        
        prompt += "\nCommits:\n"
        
        for commit in commits:
            prompt += f"- {commit['commit']['message']} - {commit['commit']['author']['name']}\n"
            prompt += f"  {commit['html_url']}\n"

        return self.generate_summary(prompt)
    
    def generate_summary(self, content):
        """Generate a summary of a given text."""
        prompt = f"以下是项目的最新进展，根据功能合并同类项，形成一份简报，至少包含：1）新增功能；2）主要改进；3）修复问题；:\n\n{content}"
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="gpt-3.5-turbo",
            )
            # Extract the generated text from the response
            print(response)
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error while generating summary: {e}")
            raise