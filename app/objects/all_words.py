from collections import deque

from app.objects.word import Word


class AllWords:
    def __init__(self):
        self.words = deque()

    def add_word(self, word):
        self.words.append(word)

    def get_next_word(self):
        word = Word("", 0, "")
        if len(self.words) > 0:
            word = self.words.popleft()
        return word
