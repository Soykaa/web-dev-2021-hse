from objects.user import User


def compare_users_by_rating(user1: User, user2: User):
    if user1.rating < user2.rating:
        return -1
    elif user1.rating > user2.rating:
        return 1
    else:
        return 0
