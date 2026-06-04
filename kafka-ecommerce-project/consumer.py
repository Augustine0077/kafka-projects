import json
from collections import defaultdict
from kafka import KafkaConsumer

user_order_count = defaultdict(int)

consumer = KafkaConsumer(
    "ecommerce.orders",
    bootstrap_servers="localhost:9092",
    group_id="order-analytics",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Consumer Started...\n")

for message in consumer:

    order = message.value

    print("Order Received:")
    print(order)

    user_id = order["user_id"]

    user_order_count[user_id] += 1

    print(
        f"Running Count -> User {user_id}: {user_order_count[user_id]} orders"
    )

    print("-" * 50)