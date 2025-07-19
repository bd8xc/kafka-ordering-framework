import json
from kafka import KafkaConsumer,KafkaProducer
from datetime import datetime
import uuid
import time
import random

#ORDER_KAFKA_TOPIC = "order_details" for testing
ORDER_KAFKA_TOPIC = "grouped-order-details"
ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"

consumer = KafkaConsumer(
    ORDER_KAFKA_TOPIC,
    bootstrap_servers="localhost:9092"
)

producer=KafkaProducer(
    bootstrap_servers="localhost:9092"
)
print("transaction portal listening...")


while True:
    for message in consumer:
        print("Ongoing transaction...")
        order_data = json.loads(message.value.decode())

        sleep_duration=random.uniform(0.5,1.5)
        time.sleep(sleep_duration)

        order_data["status"]= "confirmed"
        order_data["transaction_id"]=str(uuid.uuid4())
        order_data["processed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("transaction sucessful")
        print(order_data)
        producer.send(
            ORDER_CONFIRMED_KAFKA_TOPIC,
            value=json.dumps(order_data).encode("utf-8")
        )
