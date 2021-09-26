from app.objects.word import Word
from collections import defaultdict


class User:
    def __init__(self):
        self.guessed_words_by_cat = defaultdict(list)
        self.guessed_words = dict()
        self.rating = 0

    def add_guessed_word(self, word):
        guessed_word = Word(word.word, word.score, word.category)
        if word.word not in self.guessed_words:
            self.guessed_words[word.word] = guessed_word
            self.rating += word.score
            if word.category != "":
                self.guessed_words_by_cat[word.category].append(guessed_word)

    def get_rating(self):
        return self.rating

    def get_words(self, category):
        if category != "":
            return self.guessed_words_by_cat[category]
        return self.guessed_words
