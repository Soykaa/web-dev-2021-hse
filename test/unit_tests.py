import pytest

from fastapi import HTTPException

from app.objects.all_users import AllUsers
from app.objects.all_words import AllWords
from app.objects.category import Category
from app.objects.user import User
from app.objects.word import Word


def test_guessed_word_adding_with_cat():
    test_user = User()
    word = Word("tree", 100, "nature")
    test_user.add_guessed_word(word)
    assert (test_user.guessed_words_by_cat["nature"][0].word == "tree")
    assert (len(test_user.guessed_words) == 1)
    assert (test_user.guessed_words[word.word].word == "tree")


def test_guessed_word_adding_without_cat():
    test_user = User()
    test_string = "nothing"
    word = Word("tree", 100, "")
    test_user.add_guessed_word(word)
    if not test_user.guessed_words_by_cat:
        test_string = "empty"
    assert (test_user.guessed_words[word.word].word == "tree")
    assert (len(test_user.guessed_words) == 1)
    assert (test_string == "empty")


def test_guessed_word_adding_with_cat_twice():
    test_user = User()
    word = Word("tree", 100, "nature")
    word2 = Word("tree", 100, "nature")
    test_user.add_guessed_word(word)
    test_user.add_guessed_word(word2)
    assert (test_user.guessed_words_by_cat["nature"][0].word == "tree")
    assert (len(test_user.guessed_words) == 1)
    assert (test_user.guessed_words[word.word].word == "tree")
    word3 = Word("bear", 150, "nature")
    word4 = Word("fox", 150, "nature")
    test_user.add_guessed_word(word3)
    assert (test_user.guessed_words.get(word4) is None)


def test_rating_after_init():
    test_user = User()
    assert (test_user.get_rating() == 0)


def test_rating_after_changing():
    test_user = User()
    test_user.rating += 100
    assert (test_user.get_rating() == 100)


def test_words_after_init():
    test_user = User()
    assert (test_user.get_words(Category("")) == [])


def test_words_without_category():
    test_user = User()
    word1 = Word("school", 100, "")
    word2 = Word("bird", 100, "")
    word3 = Word("summary", 100, "")
    test_user.guessed_words[word1.word] = word1
    test_user.guessed_words[word2.word] = word2
    test_user.guessed_words[word3.word] = word3
    expected = [word1.word, word2.word, word3.word]
    actual = list(test_user.get_words("").keys())
    assert (actual == expected)


def test_words_with_category():
    test_user = User()
    word1 = Word("school", 100, "study")
    word2 = Word("bird", 100, "animals")
    word3 = Word("pencil", 100, "study")
    test_user.add_guessed_word(word1)
    test_user.add_guessed_word(word2)
    test_user.add_guessed_word(word3)
    expected1 = [word1.word, word2.word, word3.word]
    actual1 = list(test_user.get_words("").keys())
    expected2 = [word1.word, word3.word]
    actual2 = [w.word for w in list(test_user.get_words("study"))]
    assert (actual2 == expected2)
    assert (actual1 == expected1)


def test_adding_user_zero_users():
    test_users = AllUsers()
    assert (len(test_users.users) == 0)


def test_adding_user_three_users():
    test_users = AllUsers()
    user1 = User()
    user2 = User()
    user3 = User()
    test_users.add_user(user1)
    test_users.add_user(user2)
    test_users.add_user(user3)
    assert (len(test_users.users) == 3)


def test_num_of_users_zero_users():
    test_users = AllUsers()
    assert (test_users.num_of_users() == 0)


def test_adding_user_two_users():
    test_users = AllUsers()
    user1 = User()
    user2 = User()
    test_users.add_user(user1)
    test_users.add_user(user2)
    assert (test_users.num_of_users() == 2)


def test_get_user_no_such_id_too_big():
    with pytest.raises(HTTPException):
        test_users = AllUsers()
        user1 = User()
        test_users.add_user(user1)
        test_users.get_user(10)


def test_get_user_no_such_id_neg():
    with pytest.raises(HTTPException):
        test_users = AllUsers()
        user1 = User()
        test_users.add_user(user1)
        test_users.get_user(-2)


def test_get_user_such_id_exists():
    test_users = AllUsers()
    user1 = User()
    user2 = User()
    user3 = User()
    test_users.add_user(user1)
    test_users.add_user(user2)
    test_users.add_user(user3)
    assert (test_users.get_user(2).id == 2)


def test_get_global_rating():
    test_users = AllUsers()
    user1 = User()
    user1.rating = 200
    user2 = User()
    user2.rating = 100
    user3 = User()
    user3.rating = 200
    user4 = User()
    user4.rating = 300
    test_users.add_user(user1)
    test_users.add_user(user2)
    test_users.add_user(user3)
    test_users.add_user(user4)
    tmp = test_users.get_rating()
    assert ([u.id for u in tmp] == [3, 0, 2, 1])


def test_word_adding_with_cat():
    test_hat = AllWords()
    word = Word("tree", 100, "nature")
    test_hat.add_word(word)
    assert (len(test_hat.words) == 1)
    assert (test_hat.words[0].word == "tree")


def test_word_adding_without_cat():
    test_hat = AllWords()
    word = Word("tree", 100, "")
    test_hat.add_word(word)
    assert (len(test_hat.words) == 1)
    assert (test_hat.words[0].word == "tree")


def test_show_next_word():
    test_hat = AllWords()
    word1 = Word("school", 100, "study")
    word2 = Word("bird", 100, "animals")
    word3 = Word("pencil", 100, "study")
    test_hat.add_word(word1)
    test_hat.add_word(word2)
    test_hat.add_word(word3)
    next_word = test_hat.get_next_word()
    assert(next_word.word == "school")
    assert(len(test_hat.words) == 2)
    next_word = test_hat.get_next_word()
    assert (next_word.word == "bird")
    assert (len(test_hat.words) == 1)
    next_word = test_hat.get_next_word()
    assert (next_word.word == "pencil")
    assert (len(test_hat.words) == 0)
    next_word = test_hat.get_next_word()
    assert (next_word.word == "")
    assert (len(test_hat.words) == 0)


if __name__ == '__main__':
    pytest.main()
