import queue
from collections import deque

from app.models.word_model import GameWord


class AllWords:
    def __init__(self):
        self.words = deque()

    def add_word(self, word: GameWord):
        self.words.append(word)

    def get_next_word(self):
        word = self.words.popleft()
        return word
