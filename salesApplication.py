class SalesApplication:
    def __init__(self):
        # Initialize an empty list to store sales data (product, amount)
        self.sales_data = []

    def add_sale(self, product, amount):
        # Add a sale to the sales data
        self.sales_data.append((product, amount))

    def calculate_total_sales(self):
        # Calculate the total sales across all products
        total_sales = sum(amount for _, amount in self.sales_data)
        return total_sales

# Example usage:
if __name__ == "__main__":
    app = SalesApplication()

    # Add some sales data (product, amount)
    app.add_sale("Product A", 100)
    app.add_sale("Product B", 150)
    app.add_sale("Product A", 50)  # Additional sale for Product A

    # Calculate and print the total sales
    total_sales_amount = app.calculate_total_sales()
    print(f"Total sales amount: ${total_sales_amount:.2f}")
