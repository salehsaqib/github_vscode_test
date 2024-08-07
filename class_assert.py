class Item:
    def __init__(self, name, price, quantity=0):
        # Run Validation to the received Argumants
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("phone", 30000, 1)
item2 = Item("Laptop", 100000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())


