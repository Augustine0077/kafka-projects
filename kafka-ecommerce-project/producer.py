
import csv
import json
from kafka import KafkaProducer

TOPIC_NAME = "ecommerce.orders"

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    key_serializer=lambda k: str(k).encode("utf-8"),
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

with open("orders.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("Headers:", reader.fieldnames)
    for row in reader:
        order_id = row["order_id"]

        producer.send(
            TOPIC_NAME,
            key=order_id,
            value=row
        )

        print(f"Published Order ID: {order_id}")

producer.flush()
producer.close()

print("\nAll orders successfully published to Kafka!")
