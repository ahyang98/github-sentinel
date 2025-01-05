class CLI:
    def __init__(self, subscription_manager):
        self.manager = subscription_manager

    def display_menu(self):
        """Display the command-line interface menu."""
        while True:
            print("1. Add Subscription")
            print("2. Remove Subscription")
            print("3. List Subscriptions")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                repo = input("Enter repository URL: ")
                self.manager.add_subscription(repo)
            elif choice == "2":
                repo = input("Enter repository URL to remove: ")
                self.manager.remove_subscription(repo)
            elif choice == "3":
                print("Subscribed Repositories:")
                for repo in self.manager.list_subscriptions():
                    print(repo)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
