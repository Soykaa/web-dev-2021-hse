import pytest

from app.objects.all_users import AllUsers
from app.objects.all_words import AllWords
from app.objects.user import User
from app.objects.word import Word


def test_guess_word():
    hat = AllWords()
    users = AllUsers()
    users.add_user(User("Sarah"))
    user = users.get_user(0)
    # add word to the hat
    hat.add_word(Word("flower", 100, "summer"))
    # guess the current word
    user.add_guessed_word(hat.get_next_word())
    assert (user.rating == 100)
    assert (list(user.guessed_words.keys()) == ["flower"])
    assert (list(user.guessed_words_by_cat.keys()) == ["summer"])


def test_guess_word_and_change_pos_in_rating():
    hat = AllWords()
    users = AllUsers()
    users.add_user(User("Jane"))
    users.add_user(User("Kate"))
    user1 = users.get_user(0)
    user2 = users.get_user(0)
    # add word to the hat
    hat.add_word(Word("flower", 500, "summer"))
    hat.add_word(Word("sun", 100, "summer"))
    # guess the current word
    user1.add_guessed_word(hat.get_next_word())
    user2.add_guessed_word(hat.get_next_word())
    # rating
    tmp = users.get_rating()
    assert (len(tmp) == 2)
    assert ([u.id for u in tmp] == [0, 1])


def test_guess_and_get_words():
    hat = AllWords()
    users = AllUsers()
    users.add_user(User("John"))
    user1 = users.get_user(0)
    # add word to the hat
    hat.add_word(Word("flower", 500, "spring"))
    hat.add_word(Word("sun", 100, "summer"))
    hat.add_word(Word("sea", 100, "summer"))
    # guess the words
    user1.add_guessed_word(hat.get_next_word())
    user1.add_guessed_word(hat.get_next_word())
    user1.add_guessed_word(hat.get_next_word())
    # words
    assert(list(user1.get_words("").keys()) == ["flower", "sun", "sea"])
    assert([w.word for w in user1.get_words("spring")] == ["flower"])


if __name__ == '__main__':
    pytest.main()
