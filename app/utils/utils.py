from app.objects.user import User


def compare_users_by_rating(user: User):
    return -user.rating
