from graphene import ObjectType, Date, Field

from app.models.graphql.record_model import StorageRecord
from app.models.graphql.winner_model import Winner
from app.objects.entity_manager import EntityManager


class Query(ObjectType):
    record_by_date = Field(StorageRecord, date=Date(required=True))

    def resolve_record_by_date(self, info, date):
        storage_record: Winner = EntityManager.users.storage.get(date)

        if storage_record is not None:
            return StorageRecord(winner=Winner(storage_record.id, storage_record.rating, storage_record.name),
                                 win_date=date)
        return None
