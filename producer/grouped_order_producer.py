import pandas as pd
from kafka import KafkaProducer
from json import dumps


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8'),
    acks='all',
    linger_ms=5,
    retries=3
)

orders_df = pd.read_csv("kafka_order_system/data/restaurant-1-orders.csv")
prices_df = pd.read_csv("kafka_order_system/data/restaurant-1-products-price.csv")
orders_df.columns = orders_df.columns.str.strip().str.lower()
prices_df.columns = prices_df.columns.str.strip().str.lower()
prices_df.rename(columns={"product price": "price_from_price_file"}, inplace=True)
orders_df = orders_df.merge(prices_df, on="item name", how="left")
orders_df["subtotal"] = orders_df["quantity"] * orders_df["price_from_price_file"]
grouped = orders_df.groupby("order number")



for order_id, group in grouped:
    order_date = group["order date"].iloc[0]
    items = []

    for x, row in group.iterrows():
        items.append({
            "item_name": row["item name"],
            "quantity": int(row["quantity"]),
            "product_price": float(row["price_from_price_file"]),
            "subtotal": float(row["subtotal"])
         })

    total_amount = sum(item["subtotal"] for item in items)
    print(order_id,order_date,items,total_amount)
    order_msg = {
        "order_id": int(order_id),
        "order_date": order_date,
        "items": items,
        "total_cost": total_amount
    }

    producer.send(
    "grouped-order-details",
    key=str(order_id).encode('utf-8'),
    value=order_msg
)

    print(f" Sent order {order_id} to Kafka")

producer.flush()
