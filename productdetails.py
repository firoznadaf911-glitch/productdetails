class Product:
    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def display_details(self):
        print("--- Product Details ---")
        print(f"ID       : {self.product_id}")
        print(f"Name     : {self.name}")
        print(f"Category : {self.category}")
        print(f"Price    : ${self.price:.2f}")
        print(f"In Stock : {self.stock} units")
        print("-----------------------")

# Example Usage
if __name__ == "__main__":
    item = Product(101, "Wireless Mouse", "Electronics", 29.99, 45)
    item.display_details()