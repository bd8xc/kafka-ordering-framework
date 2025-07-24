--

# Kafka Ordering Framework

The **Kafka Ordering Framework** is a real-time food ordering simulation built using **Apache Kafka**, **ClickHouse**, and **Python**. This project showcases how modern stream processing systems can manage, process, and analyze takeaway food orders at scale.

---

## Overview

This system models the lifecycle of food orders through multiple services, simulating the architecture of a real-world ordering platform:

* A **Kafka Producer** streams structured order data.
* A **Consumer Service** processes incoming orders.
* A **Transaction Service** simulates order confirmations.
* A **ClickHouse Database** stores order data for high-performance analytics.
* An **Analytics Module** generates visual insights and trends.

---

## Project Structure

```
kafka_order_system/
├── data/                  # Datasets containing order and product details
├── db/                    # ClickHouse configuration and ORM models
├── producer/              # Kafka producer scripts
├── services/              # Consumer, transaction, and analytics logic
├── requirement.txt        # Python dependencies
└── README.md              # Project documentation
```

---

## Technologies Used

| Technology              | Purpose                                |
| ----------------------- | -------------------------------------- |
| **Apache Kafka**        | Real-time data streaming and messaging |
| **ClickHouse**          | OLAP database optimized for analytics  |
| **Python 3.12**         | Service and pipeline development       |
| **Pandas**              | Data manipulation and preprocessing    |
| **Matplotlib, Seaborn** | Data visualization and plotting        |

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/bd8xc/kafka-ordering-framework.git
cd kafka_order_system
```

### 2. Install Dependencies

Ensure your Python environment is activated, then install the required packages:

```bash
pip install -r requirement.txt
```

### 3. Start Kafka and Zookeeper

Navigate to your Kafka installation directory and run:

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
```

### 4. Run the Kafka Producer

```bash
python producer/grouped_order_producer.py
```

### 5. Run Consumer and Transaction Services

```bash
python services/order_consumer.py
python services/transaction.py
```

### 6. Run the Analytics Module

```bash
python services/analytics.py
```

---

## Sample Analytics Output

Visualizations generated using Seaborn and Matplotlib include:

* Daily order volume
* Revenue distribution
* Top-selling menu items
* Orders with highest item quantity

---

## Data Sources

| File                              | Description                  |
| --------------------------------- | ---------------------------- |
| `restaurant-1-orders.csv`         | Simulated food order data    |
| `restaurant-1-products-price.csv` | Product catalog with pricing |

---

## Future Enhancements

* [ ] Integrate **Apache Flink** for advanced real-time stream processing
* [ ] Add an **Email Notification Service** for order confirmations

---

## Author

**Bikram Dutta**
Third-Year Computer Science Undergraduate
Focus Areas: Kafka • Python • Machine Learning
