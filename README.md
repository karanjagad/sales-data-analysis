# Sales Data Analysis Project

This project involves cleaning, analyzing, and storing sales transaction data. The data is initially provided in a CSV file, `sales_data.csv`, and is processed using Python and stored in a PostgreSQL database.

## Project Structure

The project has the following structure:

- `data_analysis.ipynb`: A Jupyter notebook for cleaning the dataset and analyzing the relation between Sale Price and Quantity for some products.
- `src/transfer_sales_data.py`: A Python script to transfer the cleaned data from `sales_data_cleaned.csv` to a PostgreSQL database.
- `src/app.py`: This is the main Python script for the application to fetch data from the database and perform the analysis.
- `docker-compose.yml`: A Docker Compose file to run a PostgreSQL server.

## Getting Started

1. Create a Python virtual environment and activate it:

    For Windows:
    ```
    python -m venv env
    env\Scripts\activate
    ```

    For Unix or MacOS:
    ```
    python3 -m venv env
    source env/bin/activate
    ```

2. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

3. Run the Jupyter notebook `data_analysis.ipynb` to clean the dataset and perform the initial analysis. This will generate a cleaned CSV file, `sales_data_cleaned.csv`.

4. Start the PostgreSQL server with Docker Compose:

    ```
    docker-compose up -d
    ```

5. Run the Python script to transfer the cleaned data to the PostgreSQL database:

    ```
    python src/transfer_sales_data.py
    ```

6. You can then connect to the PostgreSQL server to query the data:

    ```
    docker-compose exec postgres psql -U postgres -d my_database
    ```
   Execute the following command to check the data in the postgre server
     ```  
    SELECT * FROM sales_data LIMIT 5;
     ```

7. Run the main Python script to process the data and get the desired results:
  
      ```
      python src/app.py
      ```


## Notes / Tasks

# Data Engineering Challenge

## Problem Statement

Imagine you are working with a large dataset in a CSV file that contains information about sales transactions for the last month.
Pricing team has provided `sales_data.csv` CSV file that contains all the information.
Each row in the CSV file represents a single transaction, and the columns include information such as 
"TransactionID," "ProductID," "Quantity,", "SalePrice" and "PurchasePrice"

Your task is to:
### 1) Clean and Analyse the Dataset

* Create a Jupyter Notebook `data_analysis.ipynb` where you clean the dataset and analyze the relation between Sale Price and Quantity for some products.

* Save the cleaned dataset into `sales_data_cleaned.csv`.

### 2) Store Data into Database

* Prepare a docker compose file to run PostgreSQL.

* Implement a Python script `transfer_sales_data.py` to read `sales_data_cleaned.csv` and store the data into a table in the PostgreSQL database.

### 3) Implement Process Data Python Function

Implement a Python function (`process_data`) which performs the following transformations on the data:
* Calculate the total profit for each transaction by multiplying the "Quantity" and ("SalePrice" - "PurchasePrice") columns.
* Calculate the total profit for each product.
* Identify the top 2 selling products based on the **total quantity**.

The Python function `process_data() -> tuple[dict[int, float], dict[int, float], list[int]]`
that reads the data from database and returns a tuple containing:

* A dictionary where the keys are transaction IDs, and values are the total profit for each transaction.
* A dictionary where the keys are product IDs, and values are the total profit for each product.
* The product IDs of the 2 top-selling products.

#### Example

Consider the following data in the database
```
transaction_id,product_id,quantity,sale_price,purchase_price
1,101,3,30.0,15.0
2,101,1,40.0,15.0
3,102,2,25.0,15.0
4,102,5,20.0,15.0
5,103,6,20.0,10.0
```
The function `process_data('sales_data.csv')` should return:
```
({
  1: 45.0,
  2: 25.0,
  3: 20.0,
  4: 25.0,
  5: 60.0
},{
  101: 70.0,
  102: 45.0,
  103: 60.0
},
[102, 103])
```

Ensure the function reads data from the PostgreSQL database and returns the desired results.

Please round floating results to 2 decimal places.

## Requirements

* Well structured code: Maintainable, Extensible and Readable.

* All three tasks are runnable locally on an isolated environment (e.g. Python virtual env or Docker container). We might ask you to change some part of your code in the interview. 

* The app.py should contain the implementation of the process_data function and any other necessary code.

* Include a requirements.txt file listing the Python packages needed for the application.

* Write necessary notes for each step of your solution in the README.md file.

* Prepare your solution with your favorite IDE and send your git repo as a zip file to us.


