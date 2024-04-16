import pandas as pd

def process_data(data):
    # Calculate total profit for each transaction
    data['TotalProfit'] = data['Quantity'] * (data['SalePrice'] - data['PurchasePrice'])
    
    # Calculate total profit for each product
    product_profit = data.groupby('Product')['TotalProfit'].sum().reset_index()
    
    # Identify the top 2 selling products based on total quantity
    top_products = data.groupby('Product')['Quantity'].sum().nlargest(2).reset_index()
    
    return product_profit, top_products

# Example usage
data = pd.DataFrame({
    'TransactionID': [1, 2, 3, 4, 5],
    'Product': ['A', 'B', 'A', 'B', 'C'],
    'Quantity': [10, 20, 15, 25, 30],
    'SalePrice': [100, 200, 150, 250, 300],
    'PurchasePrice': [50, 100, 75, 125, 150]
})

product_profit, top_products = process_data(data)

print("Product Profit:")
print(product_profit)

print("\nTop Selling Products:")
print(top_products)
