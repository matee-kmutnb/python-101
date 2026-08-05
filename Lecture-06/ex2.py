inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]


def update_inventory(inventory, item_name, quantity_sold):
    """Reduce the quantity of a specified item after a sale.

    Returns True if the item was found and updated, False otherwise.
    Quantity will not go below 0.
    """
    for item in inventory:
        if item[0].lower() == item_name.lower():
            item[1] -= quantity_sold
            if item[1] < 0:
                item[1] = 0
            return True
    return False


def calculate_total_value(inventory):
    """Calculate the total value of all items in stock."""
    total = 0.0
    for name, qty, price in inventory:
        total += qty * price
    return total


def find_most_expensive(inventory):
    """Return the name of the most expensive item by unit price."""
    if not inventory:
        return None
    max_item = max(inventory, key=lambda x: x[2])
    return max_item[0]


def add_item(inventory, item_name, quantity, price):
    """Add a new item or update an existing one (set quantity and price)."""
    for item in inventory:
        if item[0].lower() == item_name.lower():
            item[1] = quantity
            item[2] = price
            return "updated"
    inventory.append([item_name, quantity, price])
    return "added"


if __name__ == "__main__":
    # Actions from the exercise
    update_inventory(inventory, "Banana", 20)  # sell 20 bananas
    print("After selling 20 Bananas:")
    print(inventory)

    total = calculate_total_value(inventory)
    print(f"Total inventory value: ${total:.2f}")

    most_exp = find_most_expensive(inventory)
    print("Most expensive item:", most_exp)

    # Add Eggs with 30 units at $0.25, then update to 50 units at $0.30
    add_item(inventory, "Eggs", 30, 0.25)
    print("After adding Eggs (30 , $0.25):")
    print(inventory)

    add_item(inventory, "Eggs", 50, 0.30)
    print("After updating Eggs (50 , $0.30):")
    print(inventory)

    print(f"Final total inventory value: ${calculate_total_value(inventory):.2f}")