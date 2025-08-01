import json 
from kafka import KafkaConsumer

ORDER_CONFIRMED_KAFKA_TOPIC="order_confirmed"

consumer=KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC,
    bootstrap_servers="localhost:9092"
)


email_sent_so_far=set()
print("email sever listining")

while True:
    for message in consumer:
        consumed_message=json.loads(message.value.decode())
        customer_email=consumed_message["customer_email"]

        print(f"sending email to {customer_email}")

        email_sent_so_far.add(customer_email)
        print(f"so far sent email to {len(email_sent_so_far)} unique emails")
