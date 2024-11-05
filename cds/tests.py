from pathlib import Path

from cds.customs_software import ask_universe

CURRENT_DIRECTORY = Path(__file__).parent
PASSENGER_MANIFEST = CURRENT_DIRECTORY.joinpath('../passenger_manifest.csv').resolve(strict=True)


def test_universe_fundamentals():
    """
    If this test fails: Please contact your test provider!
    """
    assert ask_universe('supercalifragilisticexpialidocious')
    assert not ask_universe('Incomprehensibilities Strengths')
