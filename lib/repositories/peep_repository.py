from lib.models.peep import Peep

class PeepRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM peeps ' \
            'ORDER BY time_posted DESC;'
        )

        return [
            Peep(row['id'], row['author'], row['peep'], row['time_posted'])
            for row in rows
        ]