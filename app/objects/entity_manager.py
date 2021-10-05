from app.objects.all_users import AllUsers
from app.objects.all_words import AllWords
from app.objects.storage import WinnersStorage


class EntityManager:
    users = AllUsers()
    hat = AllWords()
    storage = WinnersStorage()
