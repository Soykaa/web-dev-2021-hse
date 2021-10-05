from collections import deque
from datetime import datetime


class WinnersStorage:
    def __init__(self):
        self.storage = {}
        self.win_dates = deque()
        self.num_of_records = 366

    def add(self, date_string, winner):
        date_object = datetime.strptime(date_string, "%Y-%m-%d").date()

        # date was mentioned
        if date_object in self.storage:
            self.storage[date_object] = winner
            return

        # keep records in storage no longer than a year
        if len(self.storage) == 366:
            odd_date = self.win_dates.popleft()
            self.storage.pop(odd_date)
        self.win_dates.append(date_object)
        self.storage[date_object] = winner

    def get(self, date_object):
        if date_object not in self.storage:
            return None
        return self.storage[date_object]
