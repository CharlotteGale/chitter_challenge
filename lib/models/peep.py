class Peep:
    def __init__(self, id, author, peep, time_posted):
        self.id = id
        self.author = author
        self.peep = peep
        self.time_posted = time_posted

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Peep({self.id}, {self.author}, {self.peep}, {self.time_posted})" 
    
    @property
    def formatted_time(self):
        """Returns time in HH:MM format"""
        return self.time_posted.strftime('%H:%M')