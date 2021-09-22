from typing import Optional
from pydantic import BaseModel


class GameWord(BaseModel):
    word: str
    score: Optional[int] = None
    category: Optional[str] = None


class Action(BaseModel):
    action: int
