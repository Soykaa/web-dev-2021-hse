from pydantic import BaseModel


class GameWord(BaseModel):
    word: str
    score: int
    category: str
