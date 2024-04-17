import pandas as pd
from sqlalchemy import create_engine
import os


def main():
    """ 
    Reads a CSV file containing sales data, connects to a PostgreSQL database, and transfers the data into a table.
    """    
    file_path = os.path.join("data", "processed", "sales_data_cleaned.csv")
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Connect to the PostgreSQL database
    engine = create_engine("postgresql://postgres:password@localhost/my_database")

    # Store the data into a table
    df.to_sql("sales_data", engine, if_exists="replace", index=False)

    print("Data transfer complete.")


if __name__ == "__main__":
    main()
