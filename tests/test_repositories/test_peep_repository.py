from lib.repositories.peep_repository import PeepRepository
from lib.models.peep import Peep
from datetime import datetime

"""
When I call #all
I can get a list of Peep objects
reflecting seed data
"""
def test_get_all_records(db_connection):
    db_connection.execute(
        'INSERT INTO peeps (author, peep, time_posted) VALUES (%s, %s, %s)',
        ['test author_1', 'this is a test peep', datetime(2025, 1, 15, 15, 17, 0)]
    )
    db_connection.execute(
        'INSERT INTO peeps (author, peep, time_posted) VALUES (%s, %s, %s)',
        ['test author_2', 'this is another test peep', datetime(2025, 1, 15, 16, 26, 0)]
    )
    repo = PeepRepository(db_connection)

    assert repo.all() == [
        Peep(2, "test author_2", "this is another test peep", datetime(2025, 1, 15, 16, 26, 0)),
        Peep(1, "test author_1", "this is a test peep", datetime(2025, 1, 15, 15, 17, 0))
    ]

    peeps = repo.all()
    assert peeps[0].formatted_time == "16:26"
    assert peeps[1].formatted_time == "15:17"
    

