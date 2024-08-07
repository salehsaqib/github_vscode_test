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

item1 = Item("phone", 30000, 11)
item2 = Item("Laptop", 100000, 23)
item3 = Item("mobile", 2000, 13)

item4 = Item("chair", 30, 1)
item5 = Item("table", 100, 3)
item6 = Item("fan", 20, 13)

print(item2.calculate_total_price())
print(item3.calculate_total_price())

print(item4.calculate_total_price())
print(item5.calculate_total_price())
print(item6.calculate_total_price())



