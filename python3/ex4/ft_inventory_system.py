import sys


def main() -> None:

    print("=== Inventory System Analysis ===")

    inventory = {}

    for arg in sys.argv[1:]:

        pair = arg.split(':')
        if len(pair) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        key = pair[0]

        try:
            val = int(pair[1])
        except ValueError as error:
            print(f"Quantity error for '{key}': {error}")
            continue

        if key in inventory or val <= 0:
            print(f"Redundant item '{key}' - discarding")
        else:
            inventory[key] = val

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total_items = sum(inventory.values())

    print(f"Total quantity of the {len(inventory)} items: {total_items}")

    for item in inventory:
        percent = round(inventory[item] / total_items * 100, 1)
        print(f"Item {item} represents {percent}%")

    max_value, min_value = 0, 0

    try:
        max_value = max(inventory.values())
        min_value = min(inventory.values())

    except ValueError:
        print("Inventory empty!")

    max_name = ''
    min_name = ''
    for item in inventory:
        if inventory[item] == max_value and max_name == '':
            max_name = item

        if inventory[item] == min_value and min_name == '':
            min_name = item

    if max_value != 0:
        print(f"Item most abundant: {max_name} with quantity {max_value}")

    if min_value != 0:
        print(f"Item least abundant: {min_name} with quantity {min_value}")

    inventory["magic_item"] = 1

    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
