from .ch_config import client
from datetime import datetime

def create_orders_table():
    client.command("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id UInt32,
            order_date String,
            total_cost Float32,
            status String,
            transaction_id String,
            processed_at String
        ) ENGINE = MergeTree()
        ORDER BY order_id
    """)

def create_order_items_table():
    client.command("""
        CREATE TABLE IF NOT EXISTS order_items (
            order_id UInt32,
            item_name String,
            quantity UInt32,
            product_price Float32,
            subtotal Float32
        ) ENGINE = MergeTree()
        ORDER BY order_id
    """)

def insert_order(order_data):
    query = f"""
        INSERT INTO orders
            (order_id, order_date, total_cost, status, transaction_id, processed_at)
        VALUES
            ({order_data['order_id']},
             '{order_data['order_date']}',
             {order_data['total_cost']},
             '{order_data['status']}',
             '{order_data['transaction_id']}',
             '{order_data['processed_at']}')
    """
    client.command(query)

def insert_order_items(order_data):
    values = []
    for item in order_data['items']:
        values.append(
            f"({order_data['order_id']},"
            f"'{item['item_name']}',"
            f"{item['quantity']},"
            f"{item['product_price']},"
            f"{item['subtotal']})"
        )
    query = f"""
        INSERT INTO order_items
            (order_id, item_name, quantity, product_price, subtotal)
        VALUES
            {','.join(values)}
    """
    client.command(query)
