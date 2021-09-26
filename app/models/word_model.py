from pydantic import BaseModel


class GameWord(BaseModel):
    word: str
    score: int = 1
    category: str = ''

