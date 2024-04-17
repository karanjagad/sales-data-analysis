import psycopg2
from collections import defaultdict


def connect_to_database():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="my_database", user="postgres", password="password", host="localhost"
    )
    return conn


def fetch_data(conn):
    # Fetch data from the database
    cur = conn.cursor()
    cur.execute(
        """SELECT transaction_id , product_id , quantity ,sale_price , purchase_price FROM sales_data;"""
    )
    rows = cur.fetchall()
    cur.close()
    return rows


def analyze_sales_data(rows):
    transaction_profit = {}
    product_profit = defaultdict(float)
    product_quantity = defaultdict(int)

    for row in rows:
        transaction_id, product_id, quantity, sale_price, purchase_price = row
        total_profit = round(quantity * (sale_price - purchase_price), 2)
        transaction_profit[transaction_id] = total_profit
        product_profit[product_id] += total_profit
        product_quantity[product_id] += quantity

    top_products = sorted(product_quantity, key=product_quantity.get, reverse=True)[:2]
    
    return transaction_profit, dict(product_profit), top_products


def process_data():
    conn = connect_to_database()
    rows = fetch_data(conn)
    conn.close()

    transaction_profit, product_profit, top_products = analyze_sales_data(rows)

    return transaction_profit, product_profit, top_products


def main():
    transaction_profit, product_profit, top_products = process_data()
    result = (transaction_profit, product_profit, top_products)
    print(result)
    return result    
    
if __name__ == "__main__":
    main()
