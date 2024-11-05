"""
Disclaimer: There is no need to refactor this file, but you can modify it in order to integrate with your code
"""
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List

from customs_software import CustomsDetectorSoftware

CURRENT_DIRECTORY = Path(__file__).parent
ACCEPT_STATUS = "ACCEPT"

def read_storage(file_path: str) -> List[str]:
    """Read lines from a specified file and return them as a list."""
    try:
        with open(file_path) as file:
            return [line.strip() for line in file]
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

@dataclass
class Passenger:
    person_name: str
    items: List[str]
    approval_status: bool

def parse_passenger(values: List[str]) -> Passenger:
    """Parse passenger data from a list of strings."""
    person_name = values[0].strip()
    items = [item.strip() for item in values[1:-1]]
    approval_status = values[-1].strip() == ACCEPT_STATUS
    return Passenger(person_name, items, approval_status)

def check_passenger_status(approval_status: bool, passenger: Passenger):
    """Check and print the approval status of a passenger."""
    if approval_status != passenger.approval_status:
        expected_action = "ACCEPTED" if passenger.approval_status else "REJECTED"
        print(f'ERROR - "{passenger.person_name}" was not {expected_action}. Items: {passenger.items}')
    else:
        print(f'OK - "{passenger.person_name}"')

if __name__ == "__main__":
    STORAGE_PATH = CURRENT_DIRECTORY.joinpath("../storage").resolve(strict=True)
    PASSENGER_MANIFEST_FILE = CURRENT_DIRECTORY.joinpath("../passenger_manifest.csv").resolve(strict=True)

    # Initialize the CustomsDetectorSoftware with safe and dangerous items
    cds = CustomsDetectorSoftware(
        safe_items=read_storage(STORAGE_PATH.joinpath("safe.txt")),
        dangerous_items=read_storage(STORAGE_PATH.joinpath("dangerous.txt")),
    )

    # Read and process passenger manifest
    try:
        with open(PASSENGER_MANIFEST_FILE, newline="") as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                passenger = parse_passenger(row)
                approval_status = cds.process_entry(passenger.items)
                check_passenger_status(approval_status, passenger)
    except Exception as e:
        print(f"Error reading {PASSENGER_MANIFEST_FILE}: {e}")


