from fastapi import FastAPI

from app.models.hat_model import GameWord, Action

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the 'Hat' game!"}


# the word
@app.get("/game/playground/{word}")
async def get_word(word):
    return {"word": word}


# skip / guess the word
@app.post("/game/playground")
async def do_action(action: Action):
    return action


# to add your own words before the game
@app.post("/game/add_words")
async def add_word(word: GameWord):
    return word
