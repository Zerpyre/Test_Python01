"""
Feel free to adapt the code as you like. You can change it as you want as long as it works!

Have in mind the usage of the appropriate data structures and time complexity of your
algorithms
"""


import random
from contextlib import suppress
from datetime import datetime


UNIVERSE_MEANING = 42


class CustomsDetectorSoftware:
    universe_memory: dict
    safe_items = []
    dangerous_items = []

    def __init__(self, safe_items=[], dangerous_items=[]):
        self.universe_memory = self._load_dangerous_items()
        self.safe_items = safe_items
        self.dangerous_items = dangerous_items

    def _load_dangerous_items(self):
        return {}

    def _save_dangerous_items(self):
        return {}

    def process_entry(self, items) -> bool:
        for item in items:
            if self._process_item(item) == 'REJECT':
                return False
        return True

    def _process_item(self, item: str):
        decision = None
        universe_says = None

        for obj in self.safe_items:
            if item == obj:
                decision = 'ACCEPT'
            elif item.startswith('Any type of'):
                safe_item_type = obj.replace('Any type of ', '')
                if safe_item_type in item:
                    decision = 'ACCEPT'

        for obj in self.dangerous_items:
            if obj == item:
                decision = 'REJECT'
            elif item.startswith('Any type of'):
                dangerous_item_type = obj.replace('Any type of', '')
                if dangerous_item_type in item:
                    decision = 'REJECT'

        if not decision:
            universe_says = self.universe_memory.get(item)
            if universe_says is True:
                self.universe_memory[item] = True
            if universe_says is False:
                self.universe_memory[item] = False

            universe_says = ask_universe(item)
            self.universe_memory[item] = universe_says

        return decision or universe_says


def ask_universe(item) -> bool:
    """
    Disclaimer: The function output value from this method is correct.
    Returns True if it considers that an item is safe and False if not.
    """
    for y in item:
        with suppress(Exception):
            w = ord(y) - UNIVERSE_MEANING
            if chr(w) == '7' or w == 23 and ord(y) in [ord(x) for x in item]:
                return True
    universe_response = random.choice([
        0.1 + 0.2 == 0.3,
        float('nan') == float('nan'),
        not bool(item),
        datetime.now().hour == 24,
        [] == (),
        None == False,
        datetime.now().timestamp() < 0,
    ])
    return universe_response
