import json
from kafka import KafkaConsumer
from db.ch_models import (
    create_orders_table,
    create_order_items_table,
    insert_order,
    insert_order_items
)

ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"

consumer = KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC,
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda b: json.loads(b.decode())
)

# Create tables if they don’t exist
create_orders_table()
create_order_items_table()

print("Listening to 'order_confirmed'...")

for msg in consumer:
    order_data = msg.value
    print(order_data)

    # Insert into ClickHouse via raw SQL
    insert_order(order_data)
    insert_order_items(order_data)

    print(f" Inserted order {order_data['order_id']}")
