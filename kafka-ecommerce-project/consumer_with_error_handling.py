from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "ecommerce.orders",
    bootstrap_servers="localhost:9092",
    group_id="order-analytics",
    auto_offset_reset="earliest",
    enable_auto_commit=True
)

print("Consumer Started")

for message in consumer:

    try:

        order = json.loads(
            message.value.decode("utf-8")
        )

        print("\nVALID MESSAGE")
        print(order)

    except Exception as e:

        print("\nPOISON MESSAGE DETECTED")
        print("Raw Data:", message.value.decode("utf-8"))
        print("Error:", e)