from db.ch_models import create_orders_table, insert_order, fetch_recent_orders

# Step 1: Create the table (if not already exists)
create_orders_table()
print("✅ Table ensured.")

# Step 2: Insert a test order
insert_order(order_id=1, customer_id="user_123", customer_email="user@example.com", total_cost=199.99)
print("✅ Order inserted.")

# Step 3: Fetch recent orders
orders = fetch_recent_orders()
print("✅ Recent Orders:")
for order in orders:
    print(order)
