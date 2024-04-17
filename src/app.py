import psycopg2
from collections import defaultdict


def connect_to_database():
    """
    Connects to the PostgreSQL database.

    Returns:
        conn (psycopg2.extensions.connection): The connection object to the database.
    """
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="my_database", user="postgres", password="password", host="localhost"
    )
    return conn


def fetch_data(conn):
    """
    Fetches data from the database.

    Args:
        conn: The database connection object.

    Returns:
        A list of tuples representing the fetched data.
    """
    cur = conn.cursor()
    cur.execute(
        """SELECT transaction_id , product_id , quantity ,sale_price , purchase_price FROM sales_data;"""
    )
    rows = cur.fetchall()
    cur.close()
    return rows


def analyze_sales_data(rows):
    """
    Analyzes sales data and calculates transaction profit, product profit, and top products.

    Parameters:
    - rows (list): A list of rows containing transaction data.

    Returns:
    - transaction_profit (dict): A dictionary mapping transaction IDs to their respective total profits.
    - product_profit (dict): A dictionary mapping product IDs to their respective total profits.
    - top_products (list): A list of the top two product IDs based on quantity sold.
    """
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


def main():
    """
    This is the main function of the application.
    It connects to the database, fetches data, analyzes the sales data,
    and returns the result.

    Returns:
        tuple: A tuple containing the transaction profit, product profit, and top products.
    """
    conn = connect_to_database()
    rows = fetch_data(conn)
    conn.close()
    transaction_profit, product_profit, top_products = analyze_sales_data(rows)
    result = (transaction_profit, product_profit, top_products)
    print(result)
    return result


if __name__ == "__main__":
    main()
