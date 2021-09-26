from fastapi import FastAPI

from app.models.word_model import GameWord
from app.objects.all_users import AllUsers
from app.objects.all_words import AllWords
from app.objects.user import User

app = FastAPI()
users = AllUsers()
hat = AllWords()


@app.get("/")
async def root():
    return {"message": "Welcome to the 'Hat' game!"}


# add new user
@app.get("/add_user")
async def add_user():
    users.add_user(User())
    return "Added a user with id:" + str(len(users.users) - 1)


# guessed words of user with user_id
@app.get("/users/{user_id}/guessed_words")
async def get_guessed_words(user_id: int, category):
    return users.get_user(user_id).get_words(category)


# guess the word
@app.post("/game/playground/{user_id}/guess_word")
async def guess_word(user_id: int, word):
    users.get_user(user_id).add_guessed_word(word)
    return "Added a word with score:" + str(word.score)


# add word to the hat
@app.post("/game/words/add")
async def add_new_word(word):
    hat.add_word(word)
    return "Added a word with score:" + str(word.score)


# show word
@app.post("/game/playground/")
async def show_word():
    return hat.get_next_word()


# view rating of all users
@app.post("/game/rating")
async def show_rating():
    return users.get_rating()
