import argparse

class CLI:
    def __init__(self, github_client, subscription_manager, report_generator):
        self.github_client = github_client
        self.subscription_manager = subscription_manager
        self.report_generator = report_generator
        self.parser = self.create_parser()     

    def create_parser(self):
        parser = argparse.ArgumentParser(
            description='GitHub Sentinel Command Line Interface',
            formatter_class=argparse.RawTextHelpFormatter
        )
        subparsers = parser.add_subparsers(title='Commands', dest='command')

        parser_add = subparsers.add_parser('add', help='Add a subscription')
        parser_add.add_argument('repo', type=str, help='The repository to subscribe to (e.g., owner/repo)')
        parser_add.set_defaults(func=self.add_subscription)

        parser_remove = subparsers.add_parser('remove', help='Remove a subscription')
        parser_remove.add_argument('repo', type=str, help='The repository to unsubscribe from (e.g., owner/repo)')
        parser_remove.set_defaults(func=self.remove_subscription)

        parser_list = subparsers.add_parser('list', help='List all subscriptions')
        parser_list.set_defaults(func=self.list_subscriptions)

        parser_fetch = subparsers.add_parser('fetch', help='Fetch updates immediately')
        parser_fetch.set_defaults(func=self.fetch_updates)

        parser_export = subparsers.add_parser('export', help='Export daily progress')
        parser_export.add_argument('repo', type=str, help='The repository to export progress from (e.g., owner/repo)')
        parser_export.set_defaults(func=self.export_daily_progress)

        parser_generate = subparsers.add_parser('generate', help='Generate daily report from markdown file')
        parser_generate.add_argument('file', type=str, help='The markdown file to generate report from')
        parser_generate.set_defaults(func=self.generate_daily_report)

        # Generate report command
        generate_report_parser = subparsers.add_parser("generate-range", help="Generate a project report")
        generate_report_parser.add_argument('repo', type=str, help='The repository to export progress from (e.g., owner/repo)')
        generate_report_parser.add_argument("--start-date", type=str, help="Start date (YYYY-MM-DD)")
        generate_report_parser.add_argument("--end-date", type=str, help="End date (YYYY-MM-DD)")
        generate_report_parser.set_defaults(func=self.generate_range_report)

        parser_help = subparsers.add_parser('help', help='Show help message')
        parser_help.set_defaults(func=self.print_help)

        return parser

    def add_subscription(self, args):
        self.subscription_manager.add_subscription(args.repo)
        print(f"Added subscription for repository: {args.repo}")

    def remove_subscription(self, args):
        self.subscription_manager.remove_subscription(args.repo)
        print(f"Removed subscription for repository: {args.repo}")

    def list_subscriptions(self, args):
        subscriptions = self.subscription_manager.list_subscriptions()
        print("Current subscriptions:")
        for sub in subscriptions:
            print(f"  - {sub}")

    def fetch_updates(self, args=None):
        subscriptions = self.subscription_manager.list_subscriptions()        
        for sub in subscriptions:
            updates = self.github_client.fetch_repo_updates(sub)        
            for update in updates:
                print(update)

    def export_daily_progress(self, args):
        self.report_generator.fetch_and_generate_report(args.repo)
        print(f"Exported daily progress for repository: {args.repo}")

    def generate_daily_report(self, args):
        self.report_generator.generate_daily_report(args.file)
        print(f"Generated daily report from file: {args.file}")
    
    def generate_range_report(self, args):
        self.report_generator.generate_range_report(args.repo, args.start_date, args.end_date)
        print(f"Generated project repo {args.repo}  report from {args.start_date} to {args.end_date}")

    def print_help(self, args=None):
        self.parser.print_help()
    
    def run(self, input_str):
        try:
            args = self.parser.parse_args(input_str.split())
            if args.command:
                args.func(args)
        except SystemExit as e:
            print("Invalid command. Type 'help' to see the list of available commands.")