import json
from kafka import KafkaConsumer

latest_stats = {}

consumer = KafkaConsumer(
    "driver.earnings",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="top-drivers",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Loading Driver Statistics...")

for message in consumer:

    data = message.value

    latest_stats[data["driver_id"]] = data

try:
    sorted_drivers = sorted(
        latest_stats.values(),
        key=lambda x: x["completed_rides"],
        reverse=True
    )

    print("\nTOP 5 DRIVERS\n")

    for index, driver in enumerate(sorted_drivers[:5], start=1):

        print(
            f"{index}. "
            f"{driver['driver_id']} | "
            f"Rides: {driver['completed_rides']} | "
            f"Earnings: ${driver['earnings']}"
        )

except KeyboardInterrupt:
    pass