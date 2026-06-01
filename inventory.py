# This program demonstrates OOP with CSV file handling
# using Product and Inventory classes


import csv


class Product:

    def __init__(self, name, price, quantity):

        self.name = name
        self.price = price
        self.quantity = quantity


    def __str__(self):

        return (
            f"{self.name} | Price: {self.price} | "
            f"Quantity: {self.quantity}"
        )



class Inventory:

    def __init__(self):

        self.products = []


    def add_product(self, product):

        self.products.append(product)


    def total_value(self) -> float:

        total = 0

        for product in self.products:

            total += product.price * product.quantity

        return total


    def find_product(self, name: str):

        for product in self.products:

            if product.name.lower() == name.lower():

                return product

        return None


    def save_to_csv(self, filename):

        with open(filename, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["name", "price", "quantity"])

            for product in self.products:

                writer.writerow([
                    product.name,
                    product.price,
                    product.quantity
                ])


    def load_from_csv(self, filename):

        with open(filename, "r") as file:

            reader = csv.DictReader(file)

            self.products = []

            for row in reader:

                product = Product(
                    row["name"],
                    float(row["price"]),
                    int(row["quantity"])
                )

                self.products.append(product)



inventory = Inventory()


p1 = Product("Laptop", 50000, 2)

p2 = Product("Mouse", 700, 5)

p3 = Product("Keyboard", 1500, 3)


inventory.add_product(p1)

inventory.add_product(p2)

inventory.add_product(p3)


print("Inventory Products:\n")

for product in inventory.products:

    print(product)


print("\nTotal Inventory Value:")

print(inventory.total_value())


print("\nSearching for Mouse:")

found = inventory.find_product("mouse")

print(found)


inventory.save_to_csv("inventory.csv")

print("\nProducts saved to inventory.csv")


new_inventory = Inventory()

new_inventory.load_from_csv("inventory.csv")


print("\nLoaded Products:\n")

for product in new_inventory.products:

    print(product)


# @staticmethod does not use self or class variables.
# load_from_csv could also be a class method if it
# returned a new Inventory object directly.