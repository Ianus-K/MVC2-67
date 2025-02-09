# MVC/models/suit_model.py
import csv
import os
import random
from MVC.models.suit import Suit

class SuitModel:
    """
    Model class for managing superhero suit data.
    
    Loads suit data from a CSV file (or generates sample data if the file does not exist),
    checks durability criteria, and updates suit information.
    """
    def __init__(self, csv_file):
        self.csv_file = csv_file
        # Dictionary to store suits by code
        self.suits = {}
        self.load_data()

    def load_data(self):
        """
        Loads suit data from the CSV file.
        If the file does not exist, sample data will be generated.
        """
        if not os.path.exists(self.csv_file):
            self.generate_sample_data()
        with open(self.csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                code = row['code']
                suit_type = row['type']
                durability = int(row['durability'])
                suit = Suit(code, suit_type, durability)
                self.suits[code] = suit

    def generate_sample_data(self):
        """
        Generates sample suit data with at least 50 entries.
        Each suit type ("ชุดทรงพลัง", "ชุดลอบเร้น", "ชุดปกปิดตัวตน") has at least 10 entries.
        """
        suit_types = ["ชุดทรงพลัง", "ชุดลอบเร้น", "ชุดปกปิดตัวตน"]
        data = []

        # Generate at least 10 entries for each suit type
        for suit_type in suit_types:
            for _ in range(10):
                code = self.generate_code(existing_codes=[d['code'] for d in data])
                durability = random.randint(0, 100)
                data.append({'code': code, 'type': suit_type, 'durability': durability})

        # Add additional entries until total reaches 50
        additional = 50 - len(data)
        for _ in range(additional):
            suit_type = random.choice(suit_types)
            code = self.generate_code(existing_codes=[d['code'] for d in data])
            durability = random.randint(0, 100)
            data.append({'code': code, 'type': suit_type, 'durability': durability})

        # Write the generated data to the CSV file
        with open(self.csv_file, mode='w', newline='', encoding='utf-8') as f:
            fieldnames = ['code', 'type', 'durability']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    def generate_code(self, existing_codes):
        """
        Generates a unique 6-digit suit code (first digit not 0) that is not already in existing_codes.
        """
        while True:
            code = str(random.randint(100000, 999999))
            if code not in existing_codes:
                return code

    def check_durability(self, suit):
        """
        Checks suit durability based on suit type criteria.
        
        - ชุดทรงพลัง: durability must be >= 70
        - ชุดลอบเร้น: durability must be >= 50
        - ชุดปกปิดตัวตน: durability must not end with 3 or 7
        
        Returns:
            bool: True if the suit meets the durability criteria, False otherwise.
        """
        if suit.suit_type == "ชุดทรงพลัง":
            return suit.durability >= 70
        elif suit.suit_type == "ชุดลอบเร้น":
            return suit.durability >= 50
        elif suit.suit_type == "ชุดปกปิดตัวตน":
            last_digit = suit.durability % 10
            return last_digit not in (3, 7)
        else:
            return False

    def update_suit(self, suit):
        """
        Updates the suit information in the model and saves the data back to the CSV file.
        """
        self.suits[suit.code] = suit
        self.save_data()

    def save_data(self):
        """
        Saves all suit data to the CSV file.
        """
        with open(self.csv_file, mode='w', newline='', encoding='utf-8') as f:
            fieldnames = ['code', 'type', 'durability']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for suit in self.suits.values():
                writer.writerow({
                    'code': suit.code,
                    'type': suit.suit_type,
                    'durability': suit.durability
                })
