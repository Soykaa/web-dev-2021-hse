from collections import deque
from datetime import datetime

from graphene import Date

from app.utils.constants import WIN_RECORDS_LIMIT, DATE_FORMAT


class WinnersStorage:
    def __init__(self):
        self.storage = {}
        # test
        # self.storage["1996-03-15"] = Winner(1, 20, "Kate")
        self.win_dates = deque()

    def add(self, date_string, winner):
        date_object = datetime.strptime(date_string, DATE_FORMAT).date()

        # date was mentioned
        if date_object in self.storage:
            self.storage[date_object] = winner
            return

        # keep records in storage no longer than a year
        if len(self.storage) == WIN_RECORDS_LIMIT:
            odd_date = self.win_dates.popleft()
            self.storage.pop(odd_date)
        self.win_dates.append(date_object)
        self.storage[date_object] = winner

    def get(self, date: Date):
        date_str = str(date)
        if date_str not in self.storage:
            return None
        return self.storage[str(date_str)]
