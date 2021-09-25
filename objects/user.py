from models.word_model import GameWord
from objects.word import Word


class User:
    def __init__(self):
        self.guessed_words = dict()
        self.rating = 0

    def add_guessed_word(self, word: GameWord):
        self.guessed_words[word.word] = Word(word.word, word.score, word.category)
        self.rating += word.score

    def get_guessed_word(self, word):
        return self.guessed_words[word]

    def get_rating(self):
        return self.rating
