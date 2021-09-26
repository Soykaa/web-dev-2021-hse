import unittest

from app.objects.category import Category
from app.objects.user import User
from app.objects.word import Word


class UserTestCase(unittest.TestCase):
    def test_word_adding_with_cat(self):
        test_user = User()
        word = Word('tree', 100, 'nature')
        test_user.add_guessed_word(word)
        self.assertEqual('tree', test_user.guessed_words_by_cat['nature'][0].word)
        self.assertEqual(1, len(test_user.guessed_words))
        self.assertEqual('tree', test_user.guessed_words[word.word].word)

    def test_word_adding_without_cat(self):
        test_user = User()
        test_string = "nothing"
        word = Word('tree', 100, "")
        test_user.add_guessed_word(word)
        if not test_user.guessed_words_by_cat:
            test_string = "empty"
        self.assertEqual('tree', test_user.guessed_words[word.word].word)
        self.assertEqual(1, len(test_user.guessed_words))
        self.assertEqual("empty", test_string)

    def test_word_adding_with_cat_twice(self):
        test_user = User()
        word = Word('tree', 100, 'nature')
        word2 = Word('tree', 100, 'nature')
        test_user.add_guessed_word(word)
        test_user.add_guessed_word(word2)
        self.assertEqual('tree', test_user.guessed_words_by_cat['nature'][0].word)
        self.assertEqual(1, len(test_user.guessed_words))
        self.assertEqual('tree', test_user.guessed_words[word.word].word)
        word3 = Word('bear', 150, 'nature')
        word4 = Word('fox', 150, 'nature')
        test_user.add_guessed_word(word3)
        self.assertEqual(None, test_user.guessed_words.get(word4))

    def test_rating_after_init(self):
        test_user = User()
        self.assertEqual(0, test_user.get_rating())

    def test_rating_same_words(self):
        test_user = User()
        test_user.add_guessed_word(Word('tree', 100, 'nature'))
        test_user.add_guessed_word(Word('tree', 100, 'nature'))
        self.assertEqual(100, test_user.get_rating())

    def test_rating_different_words(self):
        test_user = User()
        test_user.add_guessed_word(Word('tree', 100, 'nature'))
        test_user.add_guessed_word(Word('bear', 200, 'nature'))
        self.assertEqual(300, test_user.get_rating())

    def test_words_after_init(self):
        test_user = User()
        self.assertEqual([], test_user.get_words(Category('')))

    def test_words_without_category(self):
        test_user = User()
        word1 = Word('school', 100, "")
        word2 = Word('bird', 100, "")
        word3 = Word('summary', 100, "")
        test_user.add_guessed_word(word1)
        test_user.add_guessed_word(word2)
        test_user.add_guessed_word(word3)
        expected = [word1.word, word2.word, word3.word]
        actual = list(test_user.get_words("").keys())
        self.assertEqual(expected, actual)

    def test_words_with_category(self):
        test_user = User()
        word1 = Word('school', 100, "study")
        word2 = Word('bird', 100, "animals")
        word3 = Word('pencil', 100, "study")
        test_user.add_guessed_word(word1)
        test_user.add_guessed_word(word2)
        test_user.add_guessed_word(word3)
        expected1 = [word1.word, word2.word, word3.word]
        actual1 = list(test_user.get_words("").keys())
        expected2 = [word1.word, word3.word]
        actual2 = [Word.get_word(w) for w in list(test_user.get_words("study"))]
        self.assertEqual(expected2, actual2)
        self.assertEqual(expected1, actual1)


if __name__ == '__main__':
    unittest.main()
