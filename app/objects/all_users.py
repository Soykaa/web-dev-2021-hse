from fastapi import HTTPException

from app.objects.storage import WinnersStorage
from app.utils.utils import compare_users_by_rating


class AllUsers:
    def __init__(self):
        self.users = list()
        self.top_user_rating = 0
        self.top_user_id = -1
        self.storage = WinnersStorage()

    def num_of_users(self):
        return len(self.users)

    def add_user(self, user):
        user.id = len(self.users)
        self.users.append(user)

    def get_user(self, user_id):
        if user_id > self.num_of_users() or user_id < 0:
            raise HTTPException(status_code=404, detail="User not found")
        return self.users[user_id]

    def get_rating(self):
        return sorted(self.users, key=compare_users_by_rating)

    def set_top_user_rating(self, rating):
        self.top_user_rating = rating
