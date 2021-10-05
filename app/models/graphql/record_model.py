from graphene import Field, ObjectType, Date

from app.models.graphql.winner_model import Winner


class StorageRecord(ObjectType):
    winner = Field(Winner, required=True)
    win_date = Date(required=True)
