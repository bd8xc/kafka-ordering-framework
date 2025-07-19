from json import dumps
from time import sleep
from kafka import KafkaProducer

ORDER_KAFKA_TOPIC="order_details"

order_limit=15

producer= KafkaProducer(bootstrap_servers=['localhost:9092'],
                        value_serializer= lambda x:dumps(x).encode('utf-8'),
                        acks='all',
                        linger_ms=5,
                        retries=3
                        )

for i in range(order_limit):
    data={
        "order_id": i,
        "user_id": f"tom_{i}",
        "total_cost": i*2
    }
    producer.send(
        ORDER_KAFKA_TOPIC,
        value=data
    )
    print("order in progress: {}".format(data))


    