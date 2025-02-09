# MVC/views/suit_view.py
class SuitView:
    """
    View class for interacting with the user.
    
    Provides methods to display messages, errors, suit information, and repair options.
    """
    def display_message(self, message):
        print(message)

    def display_error(self, error_message):
        print("Error: " + error_message)

    def get_user_input(self, prompt):
        return input(prompt)

    def display_suit_info(self, suit):
        print(f"\n=== Suit Information ===")
        print(f"Suit Code   : {suit.code}")
        print(f"Suit Type   : {suit.suit_type}")
        print(f"Durability  : {suit.durability}")
        print("========================\n")

    def display_repair_option(self):
        print("Press 'r' to repair the suit (increase durability by 25, max 100) or any other key to cancel.")

    def display_repair_counts(self, repair_counts):
        print("\n=== Repair Statistics ===")
        for suit_type, count in repair_counts.items():
            print(f"{suit_type}: Repaired {count} times")
        print("========================\n")
