from graphene import ObjectType, Date, Field

from app.models.record_model import StorageRecord
from app.models.winner_model import Winner
from app.objects.entity_manager import EntityManager


class Query(ObjectType):
    record_by_date = Field(StorageRecord, date=Date(required=True))

    def resolve_record_by_date(self, date):
        storage_record = EntityManager.users.storage.get(date)
        return StorageRecord(winner=Winner(storage_record.id, storage_record.rating, storage_record.name),
                             win_date=date)
