# MVC/controllers/suit_controller.py
from MVC.models.suit_model import SuitModel

class SuitController:
    """
    Controller class that coordinates between the Model and the View.
    
    Handles user input, validates suit codes, checks durability,
    and updates suit data (including repairs) as needed.
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # Dictionary to keep track of repair counts per suit type
        self.repair_counts = {
            "ชุดทรงพลัง": 0,
            "ชุดลอบเร้น": 0,
            "ชุดปกปิดตัวตน": 0
        }

    def run(self):
        """
        Main loop of the program.
        
        Prompts the user for a suit code and processes the input accordingly.
        """
        while True:
            user_input = self.view.get_user_input("Enter suit code (6 digits, first digit not 0) or 'q' to quit: ")
            if user_input.lower() == 'q':
                self.view.display_message("Exiting program. Goodbye!")
                break

            # Validate suit code format
            if not (user_input.isdigit() and len(user_input) == 6 and user_input[0] != '0'):
                self.view.display_error("Invalid suit code format (must be 6 digits with first digit not 0)")
                continue

            # Check if the suit code exists in the model
            if user_input not in self.model.suits:
                self.view.display_error("Suit code not found in the database")
                continue

            suit = self.model.suits[user_input]
            self.view.display_suit_info(suit)

            # Check suit durability criteria
            if self.model.check_durability(suit):
                self.view.display_message("This suit meets the durability criteria and is usable.\n")
            else:
                self.view.display_message("This suit does not meet the durability criteria.")
                self.view.display_repair_option()
                choice = self.view.get_user_input("Your choice: ")
                if choice.lower() == 'r':
                    original_durability = suit.durability
                    suit.repair(25)
                    self.model.update_suit(suit)
                    self.repair_counts[suit.suit_type] += 1
                    self.view.display_message(
                        f"Suit repaired! Durability increased from {original_durability} to {suit.durability}\n"
                    )
                else:
                    self.view.display_message("Repair cancelled.\n")

            # Display repair statistics
            self.view.display_repair_counts(self.repair_counts)
