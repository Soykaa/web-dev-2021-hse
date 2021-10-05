from graphene import Int, ObjectType, String


class Winner(ObjectType):
    id = Int(required=True)
    rating = String(required=True)
    name = String(required=True)
