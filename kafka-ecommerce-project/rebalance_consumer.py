from kafka import KafkaConsumer
import json
import time

consumer = KafkaConsumer(
    "ecommerce.orders",
    bootstrap_servers="localhost:9092",
    group_id="order-analytics",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Consumer Started...")
print("Waiting for partition assignment...")

time.sleep(5)

print("\nAssigned Partitions:")
print(consumer.assignment())

for message in consumer:
    print(message.value)