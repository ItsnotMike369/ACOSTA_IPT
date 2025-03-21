class Item:
    def __init__(self, item_id: int, name: str, description: str, price: float):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("ID must be a positive integer.")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        try:
            if item_id in self.items:
                raise ValueError("Item with this ID already exists.")
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def read_items(self):
        if not self.items:
            print("No items found.")
        else:
            for item in self.items.values():
                print(item)

    def update_item(self, item_id, name=None, description=None, price=None):
        try:
            if item_id not in self.items:
                raise ValueError("Item not found.")

            item = self.items[item_id]
            if name:
                if not name.strip():
                    raise ValueError("Name cannot be empty.")
                item.name = name
            if description is not None:
                item.description = description
            if price is not None:
                if price < 0:
                    raise ValueError("Price cannot be negative.")
                item.price = price

            print("Item updated successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_item(self, item_id):
        try:
            if item_id not in self.items:
                raise ValueError("Item not found.")
            del self.items[item_id]
            print("Item deleted successfully!")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    manager = ItemManager()
    while True:
        print("\nItem Management System")
        print("1. Create Item")
        print("2. Read Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                item_id = int(input("Enter ID: "))
                name = input("Enter name: ")
                description = input("Enter description: ")
                price = float(input("Enter price: "))
                manager.create_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input. Please enter correct values.")
        elif choice == '2':
            manager.read_items()
        elif choice == '3':
            try:
                item_id = int(input("Enter ID to update: "))
                name = input("Enter new name (or press Enter to skip): ") or None
                description = input("Enter new description (or press Enter to skip): ") or None
                price = input("Enter new price (or press Enter to skip): ")
                price = float(price) if price else None
                manager.update_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input. Please enter correct values.")
        elif choice == '4':
            try:
                item_id = int(input("Enter ID to delete: "))
                manager.delete_item(item_id)
            except ValueError:
                print("Invalid input. Please enter correct values.")
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
