import os

from datetime import datetime

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Event:
    def __init__(
        self,
        event_id: int,
        name: str,
        start_datetime: datetime,
        end_datetime: datetime,
        full_location: str,
        description: str,
    ):
        self.event_id = event_id
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.full_location = full_location
        if "," in full_location:
            x = full_location.index(",")
            self.building_name = full_location[0:x]
        else:
            self.building_name = full_location
        self.description = description


db_uri = os.getenv("ATLAS_URI")
db_client = MongoClient(db_uri, server_api=ServerApi("1"))
db_cluster = db_client.Madhacks2023Cluster0
events_db = db_cluster.events
