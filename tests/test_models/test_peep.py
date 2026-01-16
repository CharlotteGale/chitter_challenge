from lib.models.peep import Peep

def test_peep_constructs():
    test_peep = Peep(None, 'Charlotte', 'This is a test peep', None)

    assert test_peep.author == 'Charlotte'
    assert test_peep.peep == 'This is a test peep'

def test_peep_equalises():
    test_peep_1 = Peep(None, 'Charlotte', 'This is a test peep', None)
    test_peep_2 = Peep(None, 'Charlotte', 'This is a test peep', None)

    assert test_peep_1 == test_peep_2

def test_peep_stringifies():
    test_peep = Peep(None, 'Charlotte', 'This is a test peep', None)

    assert str(test_peep) == 'Peep(None, Charlotte, This is a test peep, None)'

