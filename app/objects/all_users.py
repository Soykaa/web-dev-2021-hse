from app.utils.utils import compare_users_by_rating as compare


class AllUsers:
    def __init__(self):
        self.users = list()

    def num_of_users(self):
        return len(self.users)

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, user_id):
        return self.users[user_id]

    def get_rating(self):
        return self.users.sort(key=compare)
