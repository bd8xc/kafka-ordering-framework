import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from clickhouse_driver import Client

# Setup ClickHouse client
client = Client(host='localhost')

def fetch_df(query: str, columns: list) -> pd.DataFrame:
    data = client.execute(query)
    return pd.DataFrame(data, columns=columns)

def plot_top_items(n=10):
    query = f'''
        SELECT item_name, SUM(quantity) AS total_sold
        FROM order_items
        GROUP BY item_name
        ORDER BY total_sold DESC
        LIMIT {n}
    '''
    df = fetch_df(query, ["Item", "Total Sold"])
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Total Sold", y="Item", data=df, palette="viridis")
    plt.title(f"Top {n} Selling Items")
    plt.xlabel("Units Sold")
    plt.ylabel("Item")
    plt.tight_layout()
    plt.show()

def plot_busiest_hours():
    query = '''
        SELECT toHour(toDateTime(processed_at)) AS Hour, COUNT(*) AS `Order Count`
        FROM orders
        GROUP BY Hour
        ORDER BY Hour
    '''
    df = fetch_df(query, ["Hour", "Order Count"])
    plt.figure(figsize=(10, 6))
    sns.lineplot(x="Hour", y="Order Count", data=df, marker='o', color="coral")
    plt.title("Orders by Hour of the Day")
    plt.xlabel("Hour (24h)")
    plt.ylabel("Number of Orders")
    plt.xticks(range(0, 24))
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_daily_sales():
    query = '''
        SELECT toDate(toDateTime(processed_at)) AS Date, SUM(total_cost) AS Sales
        FROM orders
        GROUP BY Date
        ORDER BY Date
    '''
    df = fetch_df(query, ["Date", "Sales"])
    df["Date"] = pd.to_datetime(df["Date"])
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Date", y="Sales", data=df, marker="o", color="teal")
    plt.title("Daily Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def run_visual_analytics():
    print("📈 Generating Visual Analytics...\n")
    plot_top_items()
    plot_busiest_hours()
    plot_daily_sales()
    print("\n✅ Done.")

if __name__ == "__main__":
    run_visual_analytics()
