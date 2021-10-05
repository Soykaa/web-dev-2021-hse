from app.models.query_model import Query
from app.objects.entity_manager import EntityManager
from app.objects.user import User

import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

app = FastAPI()

# graphene
app.add_route("/winners", GraphQLApp(schema=graphene.Schema(query=Query)))


# test
@app.get("/")
async def root():
    return {"message": "Welcome to the 'Hat' game!"}


# add new user
@app.get("/add_user")
async def add_user(name: str):
    EntityManager.users.add_user(User(name))
    return "Added a user with id:" + str(len(EntityManager.users.users) - 1)


# guessed words of user with user_id
@app.get("/users/{user_id}/guessed_words")
async def get_guessed_words(user_id: int, category):
    return EntityManager.users.get_user(user_id).get_words(category)


# guess the word
@app.post("/game/playground/{user_id}/guess_word")
async def guess_word(user_id: int, word):
    EntityManager.users.users.get_user(user_id).add_guessed_word(word)
    return "Added a word with score:" + str(word.score)


# add word to the hat
@app.post("/game/words/add")
async def add_new_word(word):
    EntityManager.hat.add_word(word)
    return "Added a word with score:" + str(word.score)


# show word
@app.post("/game/playground/")
async def show_word():
    return EntityManager.hat.get_next_word()


# view rating of all users
@app.post("/game/rating")
async def show_rating():
    return EntityManager.users.get_rating()
