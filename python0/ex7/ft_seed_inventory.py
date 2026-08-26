def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit != "area" and unit != "grams" and unit != "packets":
        print("Unknown unit type")
        return
    print(seed_type.lower().capitalize(), "seeds:", end=" ")
    if unit == "packets":
        print(quantity, "packets available")
    elif unit == "grams":
        print(quantity, "grams total")
    else:
        print("covers", quantity, "square meters")
