import json
from collections import defaultdict
from kafka import KafkaConsumer, KafkaProducer

RATE_PER_RIDE = 5

driver_stats = defaultdict(int)

consumer = KafkaConsumer(
    "ride.completed",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="driver-earnings",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Driver Earnings Consumer Started")

for message in consumer:

    ride = message.value

    driver_id = ride["driver_id"]

    driver_stats[driver_id] += 1

    earnings = driver_stats[driver_id] * RATE_PER_RIDE

    summary = {
        "driver_id": driver_id,
        "completed_rides": driver_stats[driver_id],
        "earnings": earnings
    }

    producer.send(
        "driver.earnings",
        value=summary
    )

    print(summary)