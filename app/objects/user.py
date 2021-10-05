from datetime import datetime, timezone

from app.objects.entity_manager import EntityManager
from app.objects.word import Word
from collections import defaultdict

from app.utils.constants import DATE_FORMAT


class User:
    def __init__(self, name):
        self.guessed_words_by_cat = defaultdict(list)
        self.guessed_words = dict()
        self.name = name
        self.rating = 0
        self.id = -1

    def get_rating(self):
        return self.rating

    def add_guessed_word(self, word):
        guessed_word = Word(word.word, word.score, word.category)
        if word.word not in self.guessed_words:
            self.guessed_words[word.word] = guessed_word
            self.rating += word.score
            if word.category != "":
                self.guessed_words_by_cat[word.category].append(guessed_word)
            cur_date = datetime.now(timezone.utc).strftime(DATE_FORMAT)
            if self.rating >= EntityManager.users.top_user_rating:
                EntityManager.users.set_top_user_rating(self.rating)
                EntityManager.users.storage.add(cur_date, self)

    def get_words(self, category):
        if category != "":
            return self.guessed_words_by_cat[category]
        return self.guessed_words
