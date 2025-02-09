# main.py
"""
Main entry point for the superhero suit program.
"""

from MVC.models.suit_model import SuitModel
from MVC.views.suit_view import SuitView
from MVC.controllers.suit_controller import SuitController

def main():
    csv_file = "suits.csv"  # CSV file to store suit data
    model = SuitModel(csv_file)
    view = SuitView()
    controller = SuitController(model, view)
    controller.run()

if __name__ == "__main__":
    main()
