from lib.models.peep import Peep
from datetime import datetime

def test_peep_constructs():
    test_peep = Peep(None, 'Charlotte', 'This is a test peep', datetime(2025, 1, 15, 16, 26, 0))

    assert test_peep.author == 'Charlotte'
    assert test_peep.peep == 'This is a test peep'

def test_peep_equalises():
    test_peep_1 = Peep(None, 'Charlotte', 'This is a test peep', datetime(2025, 1, 15, 16, 26, 0))
    test_peep_2 = Peep(None, 'Charlotte', 'This is a test peep', datetime(2025, 1, 15, 16, 26, 0))

    assert test_peep_1 == test_peep_2

def test_peep_stringifies():
    test_peep = Peep(None, 'Charlotte', 'This is a test peep', datetime(2025, 1, 15, 16, 26, 0))

    assert str(test_peep) == 'Peep(None, Charlotte, This is a test peep, 2025-01-15 16:26:00)'

