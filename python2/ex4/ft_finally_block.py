class GardenError(Exception):

    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:

    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: {plant_name}")


def test_watering_system() -> None:

    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for plant in valid_plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught Planterror: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing water systems")
    print()
    print("Testing invalid plants")
    print("Opening watering system")
    invalid_plants = ["Tomato", "lettuce", "carrots"]
    try:
        for plant in invalid_plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught Planterror: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing water systems")
        print()
        print("Cleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===")
    print()
    test_watering_system()


if __name__ == "__main__":
    main()
