import csv
import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

with open("ride_events.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        producer.send("ride.events", value=row)
        print("Published:", row)

producer.flush()
producer.close()

print("\nRide events published successfully.")