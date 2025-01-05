import markdown

class ReportGenerator:
    def generate_markdown_report(self, updates):
        """Generate a Markdown report from updates."""
        content = "# Repository Updates\n\n"
        for update in updates:
            content += f"- {update}\n"
        return markdown.markdown(content)

    def save_report(self, content, file_path):
        """Save the report to a file."""
        with open(file_path, "w") as file:
            file.write(content)
