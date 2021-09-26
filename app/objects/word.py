class Word:
    def __init__(self, word, score, category):
        self.word = word
        self.score = score
        self.category = category

    def change_score(self, new_score):
        self.score = new_score

    def get_word(self):
        return self.word
