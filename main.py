from fastapi import FastAPI, HTTPException

from models.word_model import GameWord
from objects.all_users import AllUsers
from objects.all_words import AllWords
from objects.user import User

app = FastAPI()
users = AllUsers()
hat = AllWords()


@app.get("/")
async def root():
    return {"message": "Welcome to the 'Hat' game!"}


@app.get("/add_user")
async def add_user():
    users.add_user(User())


# guessed words of user with user_id
@app.get("/users/{user_id}/words")
async def get_items_amount(user_id: int):
    if user_id >= users.num_of_users():
        raise HTTPException(status_code=404, detail="User not found")
    return users.get_user(user_id).get_words()


# guess the word
@app.post("/game/playground/{user_id}/words/add")
async def guess_word(user_id: int, word: GameWord):
    if user_id >= users.num_of_users():
        raise HTTPException(status_code=404, detail="User not found")
    users.get_user(user_id).add_guessed_word(word)
    return "Added a word with score:" + str(word.score)


# add word to the hat
@app.post("/game/words/add")
async def add_new_word(word: GameWord):
    hat.add_word(word)
    return "Added a word with score:" + str(word.score)


# show word
@app.get("game/playground/")
async def show_word():
    return hat.get_next_word()


# view rating of all users
@app.post("/game/rating")
async def add_new_word():
    return users.get_rating()
