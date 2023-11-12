import base64
import functions_framework

from common import *


# triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def run_scrape_events(cloud_event):
    message = base64.b64decode(cloud_event.data["message"]["data"]).decode()
    if message == "scrape events":
        print("running scrape events")
        event_data = scrape_event_data()
        publish_to_db(event_data)


def scrape_event_data() -> [Event]:
    return [
        Event(
            0,
            "test event",
            datetime.strptime("2023-11-11_20:00:00", "%Y-%m-%d_%H:%M:%S"),
            datetime.strptime("2023-11-11_22:00:00", "%Y-%m-%d_%H:%M:%S"),
            "Weeks Hall",
            "Weeks Hall",
            "",
        )
    ]


def publish_to_db(event_data: [Event]):
    # clear all events in the db
    events_db.delete_many({})

    # convert the event data from array of classes to array of dictionaries (required by insert_many)
    doc = []
    for e in event_data:
        doc.append(e.__dict__)

    events_db.insert_many(doc)