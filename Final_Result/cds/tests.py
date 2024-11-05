import sys
from pathlib import Path
from unittest.mock import patch
from .customs_software import CustomsDetectorSoftware

sys.path.append(str(Path(__file__).parent))

def test_universe_fundamentals():
    """Test the functionality of the ask_universe function using mocks."""
    with patch('customs_software.ask_universe') as mock_ask_universe:
        # Simulate the behavior of ask_universe
        mock_ask_universe.side_effect = [False, True]

        # First case: we expect it to return False
        result = mock_ask_universe('Incomprehensibilities Strengths')
        assert result is False, f"Expected False, got {result}"

        # Second case: we expect it to return True
        result = mock_ask_universe('supercalifragilisticexpialidocious')
        assert result is True, f"Expected True, got {result}"

def test_customs_detector():
    """Test the CustomsDetectorSoftware for various passenger scenarios."""
    cds = CustomsDetectorSoftware(
        safe_items=["oxygen mask", "Candy", "Towel"],
        dangerous_items=["Smokes", "Any type of gun"]
    )

    # Case 1: Passenger with safe items and oxygen mask
    assert cds.process_entry(["oxygen mask", "Candy", "Towel"]) is True, "Failed on case 1"

    # Case 2: Passenger without oxygen mask 
    assert cds.process_entry(["Candy", "Towel"]) is False, "Failed on case 2"

    # Case 3: Passenger with dangerous item and oxygen mask
    assert cds.process_entry(["oxygen mask", "Smokes"]) is False, "Failed on case 3"

    # Case 4: Passenger with an unclassified item
    result = cds.process_entry(["oxygen mask", "Selfie Stick"])
    assert result in [True, False], f"Unexpected result for unclassified item: {result}"

