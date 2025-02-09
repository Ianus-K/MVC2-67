# MVC/models/suit.py
"""
Suit class representing a superhero suit.

Attributes:
    code (str): Suit code (6-digit number, first digit is not 0).
    suit_type (str): Type of suit ("ชุดทรงพลัง", "ชุดลอบเร้น", "ชุดปกปิดตัวตน").
    durability (int): Durability value (0 - 100).
"""

class Suit:
    def __init__(self, code, suit_type, durability):
        self.code = code
        self.suit_type = suit_type
        self.durability = durability

    def repair(self, increment=25):
        """
        Repairs the suit by increasing its durability by the given increment (max 100).
        """
        self.durability = min(100, self.durability + increment)
