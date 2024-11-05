"""
Feel free to adapt the code as you like. You can change it as you want as long as it works!

Have in mind the usage of the appropriate data structures and time complexity of your
algorithms
"""

import random
from functools import lru_cache
from typing import List

UNIVERSE_MEANING = 42

class CustomsDetectorSoftware:
    def __init__(self, safe_items: List[str] = None, dangerous_items: List[str] = None):
        self.universe_cache = {}
        self.safe_items = safe_items if safe_items is not None else []
        self.dangerous_items = dangerous_items if dangerous_items is not None else []

    def process_entry(self, items: List[str]) -> bool:
        """Process a list of items for customs detection."""
        if not any(item.lower() == "oxygen mask" for item in items):
            return False

        for item in items:
            if self.process_item(item) == 'REJECT':
                return False
        return True

    def process_item(self, item: str) -> str:
        """Process a single item and determine if it's safe or dangerous."""
        # Check safe items
        for safe_item in self.safe_items:
            if item == safe_item or item.startswith(f'Any type of {safe_item}'):
                return 'ACCEPT'

        # Check dangerous items
        for dangerous_item in self.dangerous_items:
            if item == dangerous_item or item.startswith(f'Any type of {dangerous_item}'):
                return 'REJECT'

        # Check universe if not classified
        if item not in self.universe_cache:
            universe_decision = ask_universe(item)
            self.universe_cache[item] = universe_decision
        return self.universe_cache[item]


@lru_cache(maxsize=1000)
def ask_universe(item: str) -> bool:
    """Determine item classification based on a universe check."""
    return any(ord(char) % 2 == 0 for char in item) or random.choices([True, False], weights=[0.3, 0.7])[0]
